**Scorehub**

**Team Name:**

CODE PANDAS

IST 303 – Software Development

**Team Members**

[Maria Assumpta](https://cgu.instructure.com/groups/6458/users/19802)

[Richard Caballero](https://cgu.instructure.com/groups/6458/users/17970)

[Aman Sinha](https://cgu.instructure.com/groups/6458/users/18675)

[Patrick Watkins](https://cgu.instructure.com/groups/6458/users/19938)

### How to run this application:
1. Clone the repo to your computer. (Unzip if necessary)
2. Navigate on Command Prompt to the repo on your computer
3. Create and run a virtual environment for python: 
   * In Windows.\virtenv\Scripts\activate 
   * In Mac: source virtenv/Scripts/activate
3. Run the requirements.txt file with the following command: `pip! install -r requirements.txt`
4. Run the flasktest.py file in your command prompt. 

**Application Concept:**

A soccer notification application. The app would track score updates on live sporting events. The updates would include details such as which player scored, assisted, has been disciplined, how much time is left in the match, etc.

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

We will be working in two week iteration cycles. Each iteration we will complete the assigned user story and acceptance criteria. 

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
