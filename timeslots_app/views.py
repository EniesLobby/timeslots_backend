from django.shortcuts import render

from rest_framework import status, generics
from rest_framework.response import Response
from .models import Interviewer, Candidate, TimeSlot_Candidate, TimeSlot_Interviewer
from .serializers import *

from .tscompute import timeslots_computation, timeslots_computation_sm

class ListInterviewersView_list(generics.ListCreateAPIView):
    #Provides a GET and POST method handler for Interviewers
    queryset = Interviewer.objects.all()
    serializer_class = InterviewerSerializer

class ListInterviewersView_detail(generics.RetrieveUpdateDestroyAPIView):
    #Provides a DELETE and UPDATE method handler for Interviewers
    queryset = Interviewer.objects.all()
    serializer_class = InterviewerSerializer

class ListCandidatesView_list(generics.ListCreateAPIView):
    #Provides a GET and POST method handler for Candidates
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer

class ListCandidatesView_detail(generics.RetrieveUpdateDestroyAPIView):
    #Provides a DELETE and UPDATE method handler for Candidates
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer


#Timeslots List for give Candidate with GET and POST operations
class ListCandidateTimeSlotsView_list(generics.ListCreateAPIView):

    serializer_class = CandidateTimeSlotSerializer
    queryset = TimeSlot_Candidate.objects.all()

    def get_queryset(self):
        candidate = self.kwargs['pk']
        return TimeSlot_Candidate.objects.filter(candidate = candidate)
    
#Exact timeslot for exact Candidate with DELETE and UPDATE operations    
class ListCandidateTimeSlotsView_detail(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = CandidateTimeSlotSerializer
    queryset = TimeSlot_Candidate.objects.all()

    def get_queryset(self):
        timeslot = self.kwargs['pk']
        return TimeSlot_Candidate.objects.filter(id = timeslot)

#Timeslots List for given Interviewer with GET and POST operations
class ListInterviewerTimeSlotsView_list(generics.ListCreateAPIView):

    queryset = TimeSlot_Interviewer.objects.all()
    serializer_class = InterviewerTimeSlotSerializer

    def get_queryset(self):
        interviewer = self.kwargs['pk']
        return TimeSlot_Interviewer.objects.filter(interviewer = interviewer)

#Exact timeslot for exact Interviewer with DELETE and UPDATE operations
class ListInterviewerTimeSlotsView_detail(generics.RetrieveUpdateDestroyAPIView):

    queryset = TimeSlot_Interviewer.objects.all()
    serializer_class = InterviewerTimeSlotSerializer

#View timeslots available for a given candidate and given interviewers
class ListTimeSlots(generics.ListAPIView):
    
    def get_serializer_class(self):
        check_sm = self.request.query_params.get('smcheck', 0)
        if check_sm == '1':
            return MatchedTimeSlotsSerializer_SM      
        else:
            return MatchedTimeSlotsSerializer

    def get_queryset(self):
        candidate_id = self.kwargs['pk']
        
        # Get URL parameter as a string, if exists 
        string_ids = self.request.query_params.get('ids', None)
        start_date = self.request.query_params.get('start_date', None)
        end_date = self.request.query_params.get('end_date', None)
        interviewer_ids = [ int(x) for x in string_ids.split(',') ]
        check_sm = self.request.query_params.get('smcheck', 0)

        matched_timeslots = []

        # Get all objects for all parameter ids with given date
        interviewers_queryset = TimeSlot_Interviewer.objects.filter(
                                                            interviewer__in = interviewer_ids,
                                                            start_date__gte = start_date,
                                                            end_date__lte = end_date)
    
        # Get all timeslots for a given candidate_id with given date
        candidate_queryset =  TimeSlot_Candidate.objects.filter(
                                                            candidate = candidate_id,
                                                            start_date__gte = start_date,
                                                            end_date__lte = end_date)
        if check_sm == '0':
            matched_timeslots = timeslots_computation(interviewers_queryset, candidate_queryset)
        else:
            matched_timeslots = timeslots_computation_sm(interviewers_queryset, candidate_queryset)
       
        return matched_timeslots

    
              
