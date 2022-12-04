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

* Application required to run:
  Install the Requirements file 
  

***Steps to run the application***
Make sure `git` is installed on your local machine. Clone the entire project source code from github by running command below in command prompt :
git clone https://github.com/Sin-Aman/Scorehub.git`
1. Clone or Pull the latest changes from the repository
2. Open terminal or Command prompt and navigate to the location of scorehub repository
3. install the requirements file,  pip install -r requirements.txt
4. Make sure you are in the right directory in command prompt
5. run the scorehub.py file  python -m scorehub
6. You will get two tables, one will print in the terminal and the other one will export the index.html file



**Click on RUN ALL**
 
**Application Concept:**

A soccer notification application. The app will track score updates on live sporting events. The updates will include details such as which player scored, assisted, has been disciplined, how much time is left in the match, etc.

**Stakeholders:**

Any sports/soccer fan looking to keep up to date with their favorite teams or sports around the world when they cannot watch the live event.

**User Stories:**

1. As a user, I am interested in some but not all game details and most sports apps out there spam me with too much information. 
2. As a user I want to receive this information in real time so I can stay on top of vital game information. 
3. As a user, I want to follow this information through twitter, so I can receive notifications of FIFA world cup 2022.
4. As a user I want score information to be minimal and distinguishable so I can easily consume it through out my match. 
5. As a user, I can pick my favorite teams to receive constant in-game notifications of their matches.

**Requirements:**

* Display real time notifications
*  Use python libraries for game information
* Use existing api to push notifications (twitter)
* Set notifications for a specific twitter profile when a goal is scored




**Project Roadmap**

We will be working in two week iteration cycles. Each iteration we will complete the assigned user story and acceptance criteria. 

**Iteration 1** Due 10/4

* As a user, I am interested in some but not all game details and most sports apps out there spam me with too much information. **Story Points: 8** 
* Identifying a data source
* Parse desired data [Good Article](https://towardsdatascience.com/web-scraping-advanced-football-statistics-11cace1d863a) 

**Iteration 2** Due 10/18

* As a user I want to receive live (EPL) league standings in real time so I can stay on top of vital league information. **Story Points: 5**
* Identify a way to host data on web platform
* Import the desired data into our website 
* As a user, I want to follow this information through twitter, so I can receive notifications of big soccer matches around the world. **Story Points: 5** 

### Milestone 1.0
**Iteration 3** Due 11/1
1. Present to your class Milestone 1.0 of your project.
   - **User Story:** As a user I want to see score information to be minimal and distinguishable so I can easily consume it through out my day. **Story Points: 8**
2. You must present working code and explain what it does and how it fulfils the user stories.
   - [ScoreHub.ipynb](https://github.com/Sin-Aman/Scorehub/blob/main/ScoreHub.ipynb)
   - Python Modules
      - Pandas
      - Jupyter notebooks
      - Numpy
      - Request
      - [BeautifulSoup](https://pypi.org/project/beautifulsoup4/)
   - Scrapping Data from: https://understat.com/
   - Save score data as pandas dataframe
   - Convert to an html format
   - Display the html site
3. Show and explain how the code was tested.
   - If there is no changes to the table, exit and do not update the site. 
4. Explain what remains to be done to accomplish Milestone 2.0.
   - As a user, I can pick my favorite teams to receive constant in-game notifications of their matches. **Story Points: 5** 
   - As a user, I can mute notifications of certain teams or leagues that I am not that interested in. **Story Points: 5** 


**Iteration 4** Due 11/15

* As a user, I can pick my favorite teams to receive constant in-game notifications of their matches. **Story Points: 5** 
* As a user, I can mute notifications of certain teams or leagues that I am not that interested in. **Story Points: 5** 

**Velocity:** 
* Ideal velocity : 0.9
* Current velocity : 0.35

**Burn Down Chart**
![BurnDownChart](https://user-images.githubusercontent.com/108439592/197363025-ae7b7d30-4cf4-4912-ab07-a7115fca19c0.jpg)

**Meetings log**

Virtual meetups over Zoom are logged in this file.
[meetings log.xlsx](https://github.com/Sin-Aman/Scorehub/files/9912684/meetings.log.xlsx)
