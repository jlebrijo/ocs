from site_manager.models import Quote,Freebie,User,Survey,Configuration
from django.contrib import admin

class QuoteAdmin(admin.ModelAdmin):
    list_display = ('pub_date', 'text')
    
admin.site.register(Quote,QuoteAdmin)

class FreebieAdmin(admin.ModelAdmin):
    list_display = ('pub_date', 'link')
    
admin.site.register(Freebie,FreebieAdmin)

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email')
    filter_horizontal = ('surveys',)
    
admin.site.register(User,UserAdmin)

class SurveyAdmin(admin.ModelAdmin):
    list_display = ('id', 'link', 'value','active')
    
admin.site.register(Survey, SurveyAdmin)

class ConfigurationAdmin(admin.ModelAdmin):
    list_display = ('key', 'value')
    
admin.site.register(Configuration,ConfigurationAdmin)



