from django.contrib import admin

from .models import Risk,Risk_type,Controls,Risk_Owners,Control_Owners,Likelihood_rating,Res_Likelihood_rating,Impact_rating,control_status

admin.site.register(Risk)
admin.site.register(Risk_type)
admin.site.register(Controls)
admin.site.register(Risk_Owners)
admin.site.register(Control_Owners)
admin.site.register(Likelihood_rating)
admin.site.register(Res_Likelihood_rating)
admin.site.register(Impact_rating)
admin.site.register(control_status)


