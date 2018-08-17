from django.contrib import admin
from .models import Candidate, Interviewer, TimeSlot_Candidate, TimeSlot_Interviewer

admin.site.register(Candidate)
admin.site.register(Interviewer)

admin.site.register(TimeSlot_Candidate)
admin.site.register(TimeSlot_Interviewer)