from django.urls import path, re_path
from django.conf.urls import include, url
from .views import *


urlpatterns = [
    path('interviewers/', ListInterviewersView_list.as_view(), name="interviewers-all"),
    path('candidates/', ListCandidatesView_list.as_view(), name="candidates-all"),
    
    re_path('^interviewers/(?P<pk>[0-9]+)$', ListInterviewersView_detail.as_view(), name="interviewer-detail"),
    re_path('^candidates/(?P<pk>[0-9]+)$', ListCandidatesView_detail.as_view(), name="candidate-detail"),

    re_path('^timeslots/candidates/(?P<pk>[0-9]+)$', ListCandidateTimeSlotsView_list.as_view(), name="interviewer-timeslots-all"),
    re_path('^timeslots/interviewers/(?P<pk>[0-9]+)$', ListInterviewerTimeSlotsView_list.as_view(), name="candidate-timelots-all"),

    re_path('^timeslots/(?P<pk>[0-9]+)/candidates/$', ListCandidateTimeSlotsView_detail.as_view(), name="interviewer-timeslots-detail"),
    re_path('^timeslots/(?P<pk>[0-9]+)/interviewers/$', ListInterviewerTimeSlotsView_detail.as_view(), name="candidate-timeslots-detail"),

    re_path('^timeslots/candidates/(?P<pk>[0-9]+)/interviewers/$', ListTimeSlots.as_view(), name="showtimeslots")
]