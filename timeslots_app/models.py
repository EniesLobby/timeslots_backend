from django.db import models

class Interviewer(models.Model):
    #Interviewer's first name
    first_name = models.CharField(max_length = 255, null = False)

    #Interviewer's last name
    last_name = models.CharField(max_length = 255, null = False)

    #Interviewer's email
    email = models.CharField(max_length = 255, null = False)

    def __str__(self):
        return "{} - {} - {}".format(self.first_name, self.last_name, self.email)


class Candidate(models.Model):
    #Candidate's first name
    first_name = models.CharField(max_length = 255, null = False)

    #Candidate's last name
    last_name = models.CharField(max_length = 255, null = False)

    #Candidate's email
    email = models.CharField(max_length = 255, null = False)

    def __str__(self):
        return "{} - {} - {}".format(self.first_name, self.last_name, self.email)


class TimeSlot_Candidate(models.Model):
    #User's (Candidate or Interviewer) Id
    candidate  = models.ForeignKey(Candidate, on_delete = models.CASCADE)

    #User's start date (date + time) of the interview
    start_date  = models.DateTimeField()

    #User's end date (date + time) of the interview
    end_date  = models.DateTimeField()  


class TimeSlot_Interviewer(models.Model):
    #User's (Candidate or Interviewer) Id
    interviewer  = models.ForeignKey(Interviewer, on_delete = models.CASCADE)

    #User's start date (date + time) of the interview
    start_date  = models.DateTimeField()

    #User's end date (date + time) of the interview
    end_date  = models.DateTimeField()    