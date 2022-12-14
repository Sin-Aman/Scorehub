# **Scorehub**

**Team Name:**

CODE PANDAS
IST 303 – Software Development

**Team Members**

 [Maria Assumpta Komugabe](https://cgu.instructure.com/groups/6458/users/19802)

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
4. Follow our Twitter account @Scorehub_303 and turn on the post-notifications for the account, specifically "tweets". This is where the live in-game updates will be displayed.
5. Request the .env file from the ScoreHub group, you will need it to run the twitter bot. There are credentials within the file that cannot be posted, or else our project could be hacked!
6. Once the credentials from the .env file are obtained, the twitter bot code can be run. The twitter bot is set to run during time periods of when matches are happening. As long as the match is underway, the twitter bot will scrape data for that match, and post the live notifications when a team scores.

 
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
* Use python libraries for game information
* Use existing api to push notifications (twitter-bot)
* Use exisiting api to scrap real time data (SERP API)
* Turn on notifications for a specific twitter profile when a goal is scored




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


### Milestone 2.0
**Iteration 4** Due 06/12/2022
Part D

1. Present to your class Milestone 2.0 of your project.
* As a user, I want to recieve notifications of my favorite teams when they are playing.
*As a user I want to receive this information in real time so I can stay on top of vital game information.
*As a user I want score information to be minimal and distinguishable so I can easily consume it through out my match.
2. The three most important things we learned about software development in your project:
a. We learned how to use Github to collaborate together. Utilizing this tool was very useful, especially if we could not all meet together. Updating and pushing content to the GitHub repo allowed us to show progress, which was especially helpful when we could not all meet together.
b. We learned that user stories can always change. Projects such as these that use agile development can constantly change and evolve, and this one was no different. As our user stories changed, our velocity also needed to be adjusted as well. We learned how to adapt quickly, and think of creative ways to deal with the new hurdles that we found in front of us.
c. We learned how to install various amounts of packages into Python to develop our project. 

**Meetings log**
Virtual meetups over Zoom are logged in this file.
[meetings.log.xlsx](https://github.com/Sin-Aman/Scorehub/files/10171220/meetings.log.xlsx)

