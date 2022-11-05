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
  Jupyter notebook
  
  Install Jupyter notebook using command prompt:
  `pip install jupyterlab`


***Steps to run the application***

* Make sure `git` is installed on your local machine. Clone the entire project source code from github by running command below in command prompt : 

 `git clone https://github.com/Sin-Aman/Scorehub.git`

* Run Jupyter notebook from command prompt using the code:
  `jupyter notebook`
  
* Navigate to the directory inside Jupyter notebook where Scorehub is cloned and open the file named `ScoreHub.ipynb`. 

* Run the codes together by selecting "Run All" from the drop down Cell tab.
![image](https://user-images.githubusercontent.com/112525909/200098224-477b8aa1-d711-43fb-ba54-bfaf8f88a84d.png)

Click on clone and download zip
Double click on the file to extract all files 

![image](https://user-images.githubusercontent.com/112525909/200098239-46b0bbf0-1bb6-46c5-a796-65a45e1ad0ea.png)
 Copy the ScoreHub.ipynb to any location where you can access it after launching jupyter notebook.
 ![image](https://user-images.githubusercontent.com/112525909/200098260-3265548f-650b-4ec6-a8a6-9c666d292c32.png)
Double click on Jupyter Notebook
![image](https://user-images.githubusercontent.com/112525909/200098296-fb2b440a-97f8-4543-9966-668894b5c58f.png)
It will open a file like this.
Search for your file in ether documents or desktop depending on where you saved it.
![image](https://user-images.githubusercontent.com/112525909/200098310-c5982308-272b-48cf-8a0d-82aee6a49650.png)
Mine was saved in documents
Click on ScoreHub.ipynb 
![image](https://user-images.githubusercontent.com/112525909/200098319-b2570a9d-8c24-467d-9912-7f1a160f4284.png)
Click on Cell
![image](https://user-images.githubusercontent.com/112525909/200098336-65fdb011-df4c-4890-91f4-3b9dbdfadf97.png)
Click on RUN ALL
 
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
* Use existing api to push notifications (twitter)
* Set notifications for a specific twitter profile
* Minimal information about the game such as: score, who scored, assist info, substitutions, disciplinary action, etc.



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
