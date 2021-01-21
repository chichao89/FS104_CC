from django.contrib import admin

# Register your models here.
from .models import Contact, Account, Activity, ContactStatus , ContactSource,ActivityStatus


# Register your models here.
admin.site.register(Contact)
admin.site.register(Account)
admin.site.register(Activity)
admin.site.register(ContactStatus)
admin.site.register(ContactSource)
admin.site.register(ActivityStatus)
