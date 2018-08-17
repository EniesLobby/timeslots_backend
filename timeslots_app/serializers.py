from rest_framework import serializers
from .models import Interviewer, Candidate, TimeSlot_Interviewer, TimeSlot_Candidate

class InterviewerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interviewer
        fields = ('id', 'first_name', 'last_name', 'email')

class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = ('id', 'first_name', 'last_name', 'email')

class CandidateTimeSlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeSlot_Candidate  
        fields = ('id', 'candidate', 'start_date', 'end_date')


class InterviewerTimeSlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeSlot_Interviewer
        fields = ('id', 'interviewer', 'start_date', 'end_date')

class MatchedTimeSlotsSerializer(serializers.Serializer):
    interviewer = InterviewerSerializer()
    start_date = serializers.DateTimeField()
    end_date = serializers.DateTimeField()

    class Meta:
        fields = ('interviewer', 'start_date', 'end_date')

class MatchedTimeSlotsSerializer_SM(serializers.Serializer):
    start_date = serializers.DateTimeField()
    end_date = serializers.DateTimeField()

    class Meta:
        fields = ('start_date', 'end_date')