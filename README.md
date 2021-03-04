

<!-- PROJECT LOGO -->
<h3 align="center">Period 4 Birds</h3>
<h3 align="center">http://104.2.84.172/</h3>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
          <li><a href="#getting-started">Getting Started</a><li> 
          <li><a href="#scrum-board">Scrum Board</a></li>
          <li><a href="#contributes">Contributes</a></li>
          <li><a href="#games">Games</a></li>
          <li><a href="#easter-egg">Easter Egg</a></li>
          <li><a href="#contact">Contact</a></li>
          <li><a href="#map-of-project-to-ap-csp-requirements">Map of project to AP CSP requirements</a></li>
      <ul>
    </li>
  </ol>
  </ol>
    <li>
       <a href="#previous-assignments">Previous Assignments</a>
</details>

# MAJOR TECHINALS

## Deployment and Production 
Created by Max

Documents that assisted me in the [Deployment](http://nighthawkcoders.cf/lesson/pi-webserver/) and [Production](http://nighthawkcoders.cf/lesson/pi-deploy/) setup

For the initial process of getting the Intellij project onto the web. I obtained a machine called the Raspberry Pi which uses Linex and cloned my github repository onto my machine. From there, I tested the website to run on my local host network than throught the process of port forwarding I made the website avaliable on my public internet host know as my public ip address. Then, using the previous process, I created a virtual environment and installed servers to help run the website such as Nginx and Gunicorn. These process were simple to follow if you understood the instructions provided. 

## Javascript Games

### Blackjack
We created a simple blackjack card game which gives the user a probability of winning the match. The player will be playing against a AI dealer that is fully working. The game will be played just as how most regular blackjack games are. As well, the wins and losses are displayed on the screen to keep track of the player's winnings and losings.

### War
We are going to create a card game where the user can play war against an ai bot, where both players randomly draw a card from a deck. After the player draws a card, we give them the probability of him winning the game. The player plays their card and the ai bot plays a random card, and the higher valued card wins. We will have animation for the player as they play the game. For the home page, it can be an entrance to a fake online casino for visual effect.

## Web Api
f

## Database
Created by Ahmad

The first 5 lines of the [code](https://github.com/shekark642/P4Birds/blob/d37dc2ddc183bb0a178160710a1c647643a48984/view.py#L13-L18) are for creating the database, after executed this will create an [id, username, email, and password column class LoginForm & RegisterForm](https://github.com/shekark642/P4Birds/blob/d37dc2ddc183bb0a178160710a1c647643a48984/view.py#L25-L43) are built off of a module that was imported called FlaskForm these are simple forms that set quick constraints for login & signup forms. For starters, both Signup and Login app routes will need access to methods GET and POST in order to receive information front the database as well as adding to it. The Signup function simply takes the value inputted in each corresponding input field and later creates a new user after setting the different user specific variables to the values. The Login function checks the database of existing users by searching or querying through and validates whether the values inputted are valid and connected to a user. The dashboard function simply takes the information from the current user and extracts the username and uses a jinja variable to display it lastly, the logout function uses a similar library to log the user out and later redirect them because they are no longer logged in.

## HTML/CSS
f

## Easter Egg
The Easter Egg on our project is a secret page that contains our [Linkedin Page](http://104.2.84.172/easteregg1?) that can be accessed from the secret button underneath the generate button in the random fact generator section on our home page. The code for the easter egg can be found here. [Button](https://github.com/shekark642/P4Birds/blob/879e02f71c478fa0ae9fa744ac6925df4f63bd2e/templates/index.html#L83), [Blueprint](https://github.com/shekark642/P4Birds/blob/main/easteregg/__init__.py), [Python](https://github.com/shekark642/P4Birds/blob/main/easteregg/view.py)

## Leaderboards
f

## Tech Talks, College Board, and Individually Researched Topics
f

# About The Project
[![name](https://raw.githubusercontent.com/shekark642/P4Birds/main/static/images/card%20game%20main%20page.PNG)](http://104.2.84.172/)
Once you are on the website, navigate to the menu at the top and head either to the Blackjack game or War game. For the blackjack game, select the Start button and then continue to play the game. If you do not remember the rules, scroll down to the blackjack section of this Readme. For the war game, select the Start button and continue to Flip. The first to 10 wins. If you do not remember the rules, scroll down to the war section of this Readme. If you would like to review our main page, we have other discriptions of the orgins of these games and other artifacts.

# Getting Started
Use this runtime link to get started
http://104.2.84.172/

# [Scrum Board](https://github.com/shekark642/P4Birds/projects/1?fullscreen=true)
Our scrum board holds all of our progress throughout the creation period. We have "tickets" that track our process such as items to do, in progress, and done.

# Contributes 
Team Contributes will be found [HERE](https://github.com/shekark642/P4Birds/graphs/contributors), this shows each contributer, with data of their contributes such as detail of commit, quantity of commit, and time of commit

# Games



# Contact
[Max Vukovich](https://github.com/MaxVukovich)

[Shekar Krishnamoorthy](https://github.com/shekark642)

[Ryan Shay](ryanshay18)

[Ahmad Nasim](OpticStranger)

[Github Repository Link](https://github.com/shekark642/P4Birds)

# Map of project to AP CSP requirements
[Computer Science Principlse Course Cpnten description pages 19, 20, 21](https://apcentral.collegeboard.org/pdf/ap-computer-science-principles-course-and-exam-description.pdf?course=ap-computer-science-principles)

| Unit | Percentage | Hello Series usage |
| ------------- | ----------- | ----------- |
|  Big Idea 1: Creative Computing | 10-13% | Plans for multiple animations for game such as board, cards, and the dealer through the usage of HTML, CSS, and Javascript.  |
|  Big Idea 2: Data | 17-22% | Probability and user defined data in the entirety of the game. Leaderboard:using data of scores of users with profiles.  |
|  Big Idea 3: Algorithms and Programming | 30-35% | Usage of old ideas such as Jinja and simple html tasks and new ideas. |
|  Big Idea 4: Computer Systems and Network | 11-15% | Further invest into deployment and GET and POST that relates to newly learned information.  |
|  Big Idea 5: Impact of Computing | 21-26% |  Usage of a game that shows defined data like old game wins and probability and is user friendly so individuals can access and play easy.. |

# Previous Assignments

##  Async / Code, Code, Code Review
This week we began working on the leaderboard database for our javascript games. We began experimenting with code such as Trish's Tech Talk code that was shared with us on Wednesday and began to see if we can incorperate and use samples of her code. We are also inspired to work on our database because the Crossover Event has helped us see what is needed to be worked on and they also told us to work on the leaderboards so we are inspired to show them progress. [Click here to view samples](https://github.com/shekark642/P4Birds/issues/3#issue-811466457).

As well as that, we have been working on preparing for the AP Test by filling out the AP CSP Requirements Reflection to assist us in preperation [here](https://docs.google.com/document/d/1D6bg7dFzYDKtqmCdGzZwiL_vwn_P35ku-pP1h785Jkc/edit).
## Scrum Team Cards/Ticket
Our 4 goals were War Game, Blackjack Game, Deployment, and Embed both games into HTML. All goals were [met](https://github.com/shekark642/P4Birds/projects/1#column-11994163). Each individual completed their task fully but was a bit sloppy so Max(Scrum Leader) decided to knock -1 off. The sloppiness mostly refers to routing of the images of the cards and for deployment, the background on the war game would load in our Intellij's local host but not the deployment so -1 for Max. The background for the War Game should look like [this](https://github.com/shekark642/P4Birds/issues/2#issue-787376063).

## 4 Big Tickets Assignment
| Name | Big Ticket | Scrum Board/Github Code Artifcat |
| ------------- | ----------- | ----------- |
|  Ahmad Nasim 19/20| Black Game embed on Website | The Big Ticket is the blackjack code I created from python, however we need to transfer it to javascript to be able to run it in html. In order to play the game, you would click 'start' 'hit' or'stand' and the goal is to get 21 or more than the dealer. Github: https://github.com/shekark642/P4Birds/blob/main/templates/blackjack.html
|  Shekar Krishnamoorthy 19/20| Embed War on Website| Embedded the actual war game Ryan Shay made by using API called Transcrypt which turns python code into javascript in order to be ran on a website Github: https://github.com/shekark642/P4Birds/blob/main/templates/war.html   |
|  Ryan Shay 19/20| Create War Game | Created the War game with python (later turned into Javascript) Click 'Flip' to play when on runtime Github: https://github.com/shekark642/P4Birds/commit/f270a6989529d6b2f4d7125c2f006a939cfa1884 |
|  Max Vukovich 19/20| Deployment of Website| Cloned new repository and deployed new project off of raspberry pi [HERE](http://104.2.84.172/)

# Card game Project
Contributed by shekark642([Shekar](https://github.com/shekark642)), ryanshay18([Ryan](https://github.com/ryanshay18)), MaxVukovich([Max](https://github.com/MaxVukovich)), and OpticStranger([Irfan](https://github.com/OpticStranger))

[Project Plan](https://docs.google.com/document/d/1Nq75atZIfA2RrfW4srFa7otY4vGe2uMvYm_lhiyLZ0k/edit) and [Scrum Board](https://github.com/shekark642/P4Birds/projects/1)

Casino Themed Website with Card Games like War and Blackjack with Animations and Probability of Winning Displayed
