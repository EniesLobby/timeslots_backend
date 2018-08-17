from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Interviewer, Candidate, TimeSlot_Candidate, TimeSlot_Interviewer
from .serializers import InterviewerSerializer, CandidateSerializer

START_DATE = '2018-08-20'
END_DATE = '2018-08-24'

# tests for views
class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_interviewer(first_name = "", last_name= "", email = ""):
        
        if first_name != "" and last_name != "" and email != "":
            Interviewer.objects.create(first_name = first_name, last_name = last_name, email = email)
    
    @staticmethod
    def create_candidate(first_name = "", last_name= "", email = ""):

        if first_name != "" and last_name != "" and email != "":
            Candidate.objects.create(first_name = first_name, last_name = last_name, email = email)
    
    @staticmethod
    def create_interviewer_timeslot(interviewer = "", start_date= "", end_date = ""):
        
        if interviewer != "" and start_date != "" and end_date != "":
            TimeSlot_Interviewer.objects.create(interviewer = interviewer, start_date = start_date, end_date = end_date)
    
    @staticmethod
    def create_candidate_timeslot(candidate = "", start_date= "", end_date = ""):
        
        if candidate != "" and start_date != "" and end_date != "":
            TimeSlot_Candidate.objects.create(candidate = candidate, start_date = start_date, end_date = end_date)


    def setUp(self):
        # add test data
        self.create_interviewer("Anton", "Ivanov", "an@gmail.com")
        self.create_interviewer("Peter", "Molodec", "pe@gmail.com")
        self.create_interviewer("Sergej", "Muller", "se@gmail.com")
        self.create_interviewer("Laura", "Peter", "la@gmail.com")

        self.create_candidate("Mike", "Trinogiy", "mi@gmail.com")
        self.create_candidate("Peter", "Jackson", "ajck@gmail.com")
        self.create_candidate("Ukrop", "Volosyans", "uik@gmail.com")
        self.create_candidate("Kat", "Man", "kat@gmail.com")


class GetAllInterviewersTest(BaseViewTest):

    def test_get_all_interviewers(self):

        # hit the API endpoint
        response = self.client.get(
            reverse("interviewers-all", kwargs={})
        )

        # fetch the data from db
        expected = Interviewer.objects.all()
        serialized = InterviewerSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class GetAllCandidatesTest(BaseViewTest):

    def test_get_all_candidates(self):

        # hit the API endpoint
        response = self.client.get(
            reverse("candidates-all", kwargs={})
        )
        # fetch the data from db
        expected = Candidate.objects.all()
        serialized = CandidateSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class AddInterviwewersAddCandidateAddTimeslotsCheckMatchesTests(APITestCase):
    def test_create_timeslots_and_check(self):

        base_url = 'http://127.0.0.1:8000/api/'
        interviewer_url = reverse("interviewers-all", kwargs={})
        candidate_url = reverse("candidates-all", kwargs={})

        data_interviewer_1 = []
        data_interviewer_2 = []
        data_candidate = []

        #Add interviewers timeslots
        interviewer_1 = {
            "first_name": "Peter",
            "last_name": "Parker",
            "email": "spider@gmail.com"
        }
        
        data_interviewer_1.append({
            "interviewer": "1",
            "start_date": "2018-08-20 09:00",
            "end_date": "2018-08-20 16:00"            
        })

        data_interviewer_1.append({
            "interviewer": "1",
            "start_date": "2018-08-21T09:10:00",
            "end_date": "2018-08-21T10:10:00" 
        })

        data_interviewer_1.append({
            "interviewer": "1",
            "start_date": "2018-08-21T13:30:00",
            "end_date": "2018-08-21T14:00:00" 
        })

        data_interviewer_1.append({
            "interviewer": "1",
            "start_date": "2018-08-21T15:00:00",
            "end_date": "2018-08-21T16:00:00" 
        })
        
        data_interviewer_1.append({
            "interviewer": "1",
            "start_date": "2018-08-22T09:30:00",
            "end_date": "2018-08-22T10:30:00"
        })

        data_interviewer_1.append({
            "interviewer": "1",
            "start_date": "2018-08-22T11:30:00",
            "end_date": "2018-08-22T12:30:00"
        })

        data_interviewer_1.append({
            "interviewer": "1",
            "start_date": "2018-08-22T14:30:00",
            "end_date": "2018-08-22T16:00:00"
        })

        data_interviewer_1.append({
            "interviewer": "1",
            "start_date": "2018-08-23T09:00:00",
            "end_date": "2018-08-23T16:00:00"
        })
        
        interviewer_2 = {
            "first_name": "Johnson",
            "last_name": "James",
            "email": "whereisphotospider@gmail.com"
        }

        data_interviewer_2.append({
            "interviewer": '2',
            "start_date": "2018-08-20T09:30:00",
            "end_date": "2018-08-20T10:30:00"
        })

        data_interviewer_2.append({
            "interviewer": '2',
            "start_date": "2018-08-20T11:30:00",
            "end_date": "2018-08-20T13:30:00"
        })

        data_interviewer_2.append({
            "interviewer": '2',
            "start_date": "2018-08-20T14:30:00",
            "end_date": "2018-08-20T15:30:00"
        })

        data_interviewer_2.append({
            "interviewer": '2',
            "start_date": "2018-08-21T09:30:00",
            "end_date": "2018-08-21T10:30:00"
        })

        data_interviewer_2.append({
            "interviewer": '2',
            "start_date": "2018-08-21T13:00:00",
            "end_date": "2018-08-21T14:00:00"
        })

        data_interviewer_2.append({
            "interviewer": '2',
            "start_date": "2018-08-23T09:00:00",
            "end_date": "2018-08-23T10:00:00"
        })

        data_interviewer_2.append({
            "interviewer": '2',
            "start_date": "2018-08-23T11:00:00",
            "end_date": "2018-08-23T12:00:00"
        })

        data_interviewer_2.append({
            "interviewer": '2',
            "start_date": "2018-08-23T13:00:00",
            "end_date": "2018-08-23T14:00:00"
        })

        candidate = {
            "first_name": "Tom",
            "last_name": "Hardy",
            "email": "tom@gmail.com"
        }

        data_candidate.append({
            "candidate": '1',
            "start_date": "2018-08-20T09:00:00",
            "end_date": "2018-08-20T12:00:00"
        })

        data_candidate.append({
            "candidate": '1',
            "start_date": "2018-08-20T13:15:00",
            "end_date": "2018-08-20T15:15:00"
        })

        data_candidate.append({
            "candidate": '1',
            "start_date": "2018-08-21T09:00:00",
            "end_date": "2018-08-21T11:00:00"
        })

        data_candidate.append({
            "candidate": '1',
            "start_date": "2018-08-21T12:00:00",
            "end_date": "2018-08-21T14:30:00"
        })

        data_candidate.append({
            "candidate": '1',
            "start_date": "2018-08-21T14:45:00",
            "end_date": "2018-08-21T16:00:00"
        })

        data_candidate.append({
            "candidate": '1',
            "start_date": "2018-08-22T10:00:00",
            "end_date": "2018-08-22T12:00:00"
        })

        data_candidate.append({
            "candidate": '1',
            "start_date": "2018-08-22T14:00:00",
            "end_date": "2018-08-22T16:00:00"
        })

        data_candidate.append({
            "candidate": '1',
            "start_date": "2018-08-23T09:00:00",
            "end_date": "2018-08-23T16:00:00"
        })


        #test interviwewers are added
        response = self.client.post(interviewer_url, interviewer_1, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.post(interviewer_url, interviewer_2, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        #test candidate is added
        response = self.client.post(candidate_url, candidate, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


        #check interviewers timeslots are added
        for data_el in data_interviewer_1:
            response = self.client.post(base_url + 'timeslots/interviewers/1', data_el, format='json')
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        for data_el in data_interviewer_2:
            response = self.client.post(base_url + 'timeslots/interviewers/2', data_el, format='json')
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        #check candidates timeslots are added
        for data_el in data_candidate:
            response = self.client.post(base_url + 'timeslots/candidates/1', data_el, format='json')
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        #check timeslots in that case = 15    
        response = self.client.get(base_url + 
        'timeslots/candidates/1/interviewers/?ids=1,2&start_date=' + START_DATE + '&end_date=' + END_DATE +'&smcheck=0')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 15)

        #check timeslots simultaneously for given interviewers = 6
        response = self.client.get(base_url + 
        'timeslots/candidates/1/interviewers/?ids=1,2&start_date=' + START_DATE + '&end_date=' + END_DATE +'&smcheck=1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 6)

        


