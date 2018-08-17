import datetime

#Minimum duration of the interview
MIN_INTERVIEW_TIME = 1800 #minutes

# computes matches of timeslots for candidate as list of timeslots and interviewers as timeslots
# with given date range
# 4 situations:

# First Case:
# [               ] - first timerange
#    [          ]   - second timerange

# Second Case:
#    [          ]   - first timerange
# [               ] - second timerange

# Third Case:
#    [         ]  - firt timerange
# [          ]    - second timerange
# *with condition that intersection is more than MIN_INTERVIEW_TIME

# Fourth Case:
# [           ]     - firt timerange
#      [          ] - second timerange
# *with condition that intersection is more than MIN_INTERVIEW_TIME

class timeslot:
    def __init__(self, start_date = None, end_date = None, interviewer = None):
        self.start_date = start_date
        self.end_date = end_date
        self.interviewer = interviewer

class _timeslot_sm:
    def __init__(self, start_date = None, end_date = None):
        self.start_date = start_date
        self.end_date = end_date

def timeslots_computation(interviewers, candidate):

    timeslots = []

    for candidate_element in candidate:
        for interviewer_element in interviewers:
            if interviewer_element.start_date.date() == candidate_element.start_date.date():
                if candidate_element.end_date > interviewer_element.start_date:

                    first_timedate_start = candidate_element.start_date
                    first_timedate_end = candidate_element.end_date
                    second_timedate_start = interviewer_element.start_date
                    second_timedate_end = interviewer_element.end_date

                    #First case
                    if (first_timedate_start <= second_timedate_start and first_timedate_end > second_timedate_end):
                        timeslots.append(timeslot(second_timedate_start, second_timedate_end, interviewer_element.interviewer))

                    #Second case
                    if (first_timedate_start >= second_timedate_start and first_timedate_end <= second_timedate_end):
                        timeslots.append(timeslot(first_timedate_start, first_timedate_end, interviewer_element.interviewer))

                    #Third case
                    if (first_timedate_start > second_timedate_start and first_timedate_start < second_timedate_end and
                        first_timedate_end > second_timedate_end and
                        (second_timedate_end - first_timedate_start).seconds >= MIN_INTERVIEW_TIME):
                        timeslots.append(timeslot(first_timedate_start, second_timedate_end, interviewer_element.interviewer))

                    #Fourth case
                    if (first_timedate_end > second_timedate_start and first_timedate_end < second_timedate_end and
                        first_timedate_start < second_timedate_start and
                        (first_timedate_end - second_timedate_start).seconds >= MIN_INTERVIEW_TIME):
                        timeslots.append(timeslot(second_timedate_start, first_timedate_end, interviewer_element.interviewer))
        
    return timeslots

def timeslots_computation_sm(interviewers, candidate):
    timeslots_sm = []
    timeslots = []
    timeslots = timeslots_computation(interviewers, candidate)
    
    for i in range(0, len(timeslots)):
        for j in range(i, len(timeslots)):
            if(timeslots[i].interviewer.id != timeslots[j].interviewer.id ):

                first_timedate_start = timeslots[i].start_date
                first_timedate_end = timeslots[i].end_date
                second_timedate_start = timeslots[j].start_date
                second_timedate_end = timeslots[j].end_date

                if timeslots[i].start_date.date() == timeslots[j].start_date.date():                
                    if first_timedate_end > second_timedate_start:

                        #First case
                        if (first_timedate_start <= second_timedate_start and first_timedate_end > second_timedate_end):
                            timeslots_sm.append(_timeslot_sm(second_timedate_start, second_timedate_end))

                        #Second case
                        if (first_timedate_start >= second_timedate_start and first_timedate_end <= second_timedate_end):
                            timeslots_sm.append(_timeslot_sm(first_timedate_start, first_timedate_end))

                        #Third case
                        if (first_timedate_start > second_timedate_start and first_timedate_start < second_timedate_end and
                            first_timedate_end > second_timedate_end and
                            (second_timedate_end - first_timedate_start).seconds >= MIN_INTERVIEW_TIME):
                            timeslots_sm.append(_timeslot_sm(first_timedate_start, second_timedate_end))

                        #Fourth case
                        if (first_timedate_end > second_timedate_start and first_timedate_end < second_timedate_end and
                            first_timedate_start < second_timedate_start and
                            (first_timedate_end - second_timedate_start).seconds >= MIN_INTERVIEW_TIME):
                            timeslots_sm.append(_timeslot_sm(second_timedate_start, first_timedate_end))
                
    #returns only timeslots
    return timeslots_sm
