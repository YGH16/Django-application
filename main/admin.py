from django.contrib import admin

from .models import Profile, Report, serviceUpdate, QuarterlyReport, SupportTicket, ClientAgreement

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "FirstName", "LastName", "clientid", "mobile_number")
    search_fields = ["user__first_name", "user__last_name", "user__username", "clientid", "mobile_number"]
    
class ClientAgreementAdmin(admin.ModelAdmin):
    list_display = ("user", "FirstName", "LastName", "agreement_name", "pdf")
    search_fields = ["user__first_name", "user__last_name", "user__username", "user__id"]

class ReportAdmin(admin.ModelAdmin):
    list_display = ("user", "FirstName", "LastName", "date", "pdf")
    search_fields = ["user__first_name", "user__last_name", "user__username", "user__id"]

class QuarterlyReportAdmin(admin.ModelAdmin):
    list_display = ("user", "FirstName", "name" , "LastName", "date", "pdf")
    search_fields = ["user__first_name", "user__last_name", "user__username", "user__id", "name"]

class SupportTicketAdmin(admin.ModelAdmin):
    list_display = ("email", "subject", "detail")


admin.site.register(Profile, ProfileAdmin)
admin.site.register(ClientAgreement, ClientAgreementAdmin)
admin.site.register(Report, ReportAdmin)
admin.site.register(QuarterlyReport, ReportAdmin)
admin.site.register(SupportTicket, SupportTicketAdmin)
admin.site.register(serviceUpdate)

admin.site.site_header = 'Blackwell Global Admin Panel'
admin.site.site_title = 'Blackwell Global'
