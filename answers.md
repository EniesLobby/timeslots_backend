# Questions/Answers  
## Django answers
<li>Why serializers inherit form HyperlinkedModelSerializer ? Is it the best choice in this case?</li>  
<li>There is no caching for this app, when would you use it?</li>  
HyperlinkedModelSerializer works like ModelSerializer, but uses another way to represent relationships - it uses hyperlinks.
HyperlinkedModelSerializer helps for comfortable frontend usage (easy access to the related objects)

Within our project ModelSerializer looks better choice since it is simplier. HyperlinkedModelSerializer is better for more nested cases.

Database queries are still the most expensive part of the system. Caching makes it faster. When application makes big amount of requests to the database, system must ensure that the majority of them come from a cache. Amount of requests to the database should be as few as possible.

## Python answers
<li>In serializers.py is it necessary to extract StartDateEndDateOrderChecker class? Does it promote readability? Will the code be better without it?</li>  
StartDateEndDateOrderChecker is validator to ensure that start_date doesn't come after end_date. This can lead to the wrong results. I would rather check it inside respective serializers for more readability and flexibility.

## SQL answers
<li>Why are the tables normalized this way? Why is this approach good? What would be the different one?</li>  
<li>Intersection of intervals of dates is calculated on the python side, instead of database side. Why?</li>  
<li>When would you consider to calculate something on the side of database?</li>  
Complex calculation is better to be done on the server side, since they are scalable here better. Computation on database side leads to grow of (significantly) rows and cols which makes database less flexible (SQL is not good language for computations). Communication between database and server is always time consuming and as much as possible calculations have to be done on the server side.

Interviewers and Candidates should be separated for scalability. For example, Interviewer can have more properties such as position,age, group. Timeslots tables are separeted for the same. Also, in future, with millions of rows, it will be faster. As alternative, in the current project, Interviewers and Candidates could be stored in the same table.

## Docker answers
<li>Explain the reason for usuing docker.</li>  
<li>Why docker-compose?</li>  
Docker is engine to provide functions like Virtual Machine has.
Helps to deliver and run applications with different complexity.
Docker container keeps all dependencies inside and deploys application as one complete unit.  

Docker-compose is a tool to manage multi-container docker applications. Main file is docker-compose.yml with all params to run containers.

Docker swarm operates docker comands among a group of machines.
<i>A swarm is a group of machines that are running Docker and joined into a cluster. After that has happened, you continue to run the Docker commands you’re used to, but now they are executed on a cluster by a swarm manager. The machines in a swarm can be physical or virtual. After joining a swarm, they are referred to as nodes. - https://docs.docker.com/get-started/part4/#prerequisites</i>

## Tests answers
<li>Why there are no integration testing?</li>  
<li>Right now Model Mommy framework generates very limited set of data. What else would you test and how? i.e. names with apostrophee.</li>  
Our app is too simple and made by one author.
Intergration testing more about moduled systems with different understandings and programmic logics.

More deep tests include:  
Different time formats, timezones (YYY-dd-mm)  
Repeated timedates  
Security testing like XSS, SQL injections  
Name started with number  
Email without @  
Past dates  
Start date and End date have different dates  

## Code answers
<li>Current code allows for dates to be posted in the past. Why is this?</li>  
This should not be a case. Perhaps for testing purposes.

## Cloud answers  
<li>What Redis is? When would you use it?</li>  
Remote Dictionary Server - used to store data like {key - Value}.
NoRelation database. 
Mostly used for session cache and queues