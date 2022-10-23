# **Scorehub**

**Team Name:**

CODE PANDAS
IST 303 – Software Development

**Team Members**

[Maria Assumpta](https://cgu.instructure.com/groups/6458/users/19802)

[Richard Caballero](https://cgu.instructure.com/groups/6458/users/17970)

[Aman Sinha](https://cgu.instructure.com/groups/6458/users/18675)

[Patrick Watkins](https://cgu.instructure.com/groups/6458/users/19938)

### How to run this application:

Environment to run the application:
* Python 3.10.7
* Pip 22.2.2

***Steps to run the application***

* Make sure `git` is installed on your local machine. Clone the entire project source code from github by running command below in command prompt : 

 `git clone https://github.com/Sin-Aman/Scorehub.git`

* In command prompt, access the the directory "Scorehub"

 `cd Scorehub`

* Create a Virtual Environment

* Install virtual environment:

 `pip install virtualenv`

Create virtual environment named "venvi" (Note : In command prompt make sure you are accessing same root folder where you have cloned source code in step 1)

 `python -m virtualenv venvi`

* Activate the virtual environment:

 For Windows OS use command below

 `venvi\Scripts\activate`

 For Mac and other Linux OS use command below.

 `source venvi/bin/activate`

* Install the packages you need from requirements.txt. To install, use the commamd below.

 `(venvi)$ pip install -r requirements.txt`

Run the server on your machine

`(venvi)$ python main.py`

 The website can be accessed at `http://127.0.0.1:8000`

**Application Concept:**

A soccer notification application. The app will track score updates on live sporting events. The updates will include details such as which player scored, assisted, has been disciplined, how much time is left in the match, etc.

**Stakeholders:**

Any sports/soccer fan looking to keep up to date with their favorite teams or sports around the world when they cannot watch the live event.

**User Stories:**

1. As a user, I am interested in some but not all game details and most sports apps out there spam me with too much information. 
2. As a user I want to receive this information in real time so I can stay on top of vital game information. 
3. As a user, I want to follow this information through twitter, so I can receive notifications of big soccer matches around the world.
4. As a user I want score information to be minimal and distinguishable so I can easily consume it through out my day. 
5. As a user, I can pick my favorite teams to receive constant in-game notifications of their matches.
6. As a user, I can mute notifications of certain teams or leagues that I am not that interested in.

**Requirements:**

* Display real time notifications
* Display logo of the team appearing as the notification appears
* Use python libraries for game information
* Database to host information
* Use existing api to push notifications (twitter)
* Set notifications for a specific twitter profile
* Minimal information about the game such as: score, who scored, assist info, substitutions, disciplinary action, etc.



**Project Roadmap**

We will be working in four week iteration cycles. Each iteration we will complete the assigned user story and acceptance criteria. 

**Iteration 1** Due 10/4

* As a user, I am interested in some but not all game details and most sports apps out there spam me with too much information. **Story Points: 8** 
* Identifying a data source
* Parse desired data [Good Article](https://towardsdatascience.com/web-scraping-advanced-football-statistics-11cace1d863a)
* Build a simple local database 
* Import the desired data into our database 

**Iteration 2** Due 10/18

* As a user I want to receive this information in real time so I can stay on top of vital game information. **Story Points: 5** 
* Identify a way to host database [Free Azure hosting](https://azure.microsoft.com/en-us/free/sql-on-azure/)
* As a user, I want to follow this information through twitter, so I can receive notifications of big soccer matches around the world. **Story Points: 5** 

**Iteration 3** Due 11/1

* As a user I want score information to be minimal and distinguishable so I can easily consume it through out my day. **Story Points: 8** 

**Iteration 4** Due 11/15

* As a user, I can pick my favorite teams to receive constant in-game notifications of their matches. **Story Points: 5** 
* As a user, I can mute notifications of certain teams or leagues that I am not that interested in. **Story Points: 5** 

**Velocity:** 
* Ideal velocity : 0.9
* Current velocity : 0.35

**Burn Down Chart**
![BurnDownChart](https://user-images.githubusercontent.com/108439592/197363025-ae7b7d30-4cf4-4912-ab07-a7115fca19c0.jpg)
