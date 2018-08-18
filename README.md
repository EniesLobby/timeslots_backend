# Timeslots backend
## Overview
Simple restful backend for timeslots management between interviewers and candidates  

## Installation
git clone https://github.com/EniesLobby/timeslots_backend  
cd timeslots_backend  
python manage.py runserver  
  
https://github.com/ottoyiu/django-cors-headers - corsheaders should be also installed for the cross domain access  
  
By default localhost:4200 is allowed  


## API

<b>Interviewer/candidate create and view a list</b>
[o] api/interviewers/ - GET, POST  
[o] api/candidates/ - GET, POST  
  
<b>Interviewer/candidate delete and update</b>  
[o] api/interviewers/<pk> - DELETE, PUT  
[o] api/candidates/<pk> - DELETE, PUT  
  
<b>Create Interviewer/Candidate timeslot and view a list</b>  
[o] api/timeslots/candidates/<pk> - GET, POST  
[o] api/timeslots/interviewers/<pk> - GET, POST    

<b>Interviewer/Candidate timeslot delete and update</b>  
[o] api/timeslots/<pk>/candidates/ - DELETE, PUT  
[o] api/timeslots/<pk>/interviewers/ - DELETE, PUT  
  
<b>Get matches between given interviewers and candidate for a specific date range</b>  
[o] /api/timeslots/candidates/{candidate_pk}/interviewers/?ids={interviewer_pk}&start_date=2018-08-20&end_date=2018-08-24&smcheck=0  

*Start date and End date required since it is the most general case (matches for next week regulated with front end)  
**smcheck param to check interviewers together or separately (The case when on interview present several interviewers at the same time)  
