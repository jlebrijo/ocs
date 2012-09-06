from django.shortcuts import render_to_response
from django.template import RequestContext
from site_manager.models import Configuration
from site_manager.models import User
from site_manager.models import Survey
from recaptcha.client import captcha
from django.http import HttpResponse
import logging
logger = logging.getLogger(__name__)
import pdb

def home(request):
    return render_to_response('ocs/landing.html', context_instance=RequestContext(request))

def validate(request):
    password = request.POST['password']
    true_pass = Configuration.objects.filter(key='password')[0].value
    if password == true_pass:
        return render_to_response('ocs/presurvey.html', context_instance=RequestContext(request))
    else:
        return render_to_response('ocs/loginerror.html')

def authenticate(request):
    # Look for the user:
    user = User.objects.filter(email=request.POST.get('email'))[0]
    # talk to the reCAPTCHA service
    response = captcha.submit(
            request.POST.get('recaptcha_challenge_field'),
            request.POST.get('recaptcha_response_field'),
            '6Lc3qdUSAAAAALmjFhHJzhBhWqgyQhuslvnqYRny',
            request.META['REMOTE_ADDR'],)
        
    # see if the user correctly entered CAPTCHA information
    # and handle it accordingly.
    if response.is_valid and user:
        # Search for the first survey undone
        ids_surveys_done = user.surveys.all().values_list('id', flat=True)
        if ids_surveys_done:
            first_survey_not_done = Survey.objects.exclude(id__in=ids_surveys_done).filter(active=True)[0]
        else:
            first_survey_not_done = Survey.objects.filter(active=True)[0]
        return render_to_response('ocs/survey.html', {'user': user, 'survey': first_survey_not_done})
    else:
        return render_to_response('ocs/presurvey.html', context_instance=RequestContext(request))
    
def survey_done(request):
    user_id = request.GET.get('user_id')
    survey_id = request.GET.get('survey_id')
    logger.info("user_id="+str(user_id)+"& survey_id="+str(survey_id))
    try:
        user = User.objects.get(pk=user_id)
        survey = Survey.objects.get(pk=survey_id)
    except (User.DoesNotExist, Survey.DoesNotExist):
        return HttpResponse(status=404) # Not Found
    else:
        logger.info("user="+user.name+"& survey="+survey.link)
        user.surveys.add(survey)
        user.save()
        return HttpResponse(status=201) # Created