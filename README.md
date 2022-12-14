# Closed Bracket 
CP317 Implementation docs, Group 2

## Table of Contents
- Description 
- Requirements 
- Installation 
- Running the code 
- File Structure
- Navigating the platform 

## Description 
Closed Bracket is a web-based application and interface that allows users to practice, learn from, and collaborate in coding challenges in a unique and competitive way. Users can improve their coding skills by completing challenges that are matched to their skill level and updated daily. Users can also compete in daily challenges and user-vs-user timed challenges to become more proficient coders in a fun and engaging way.

## Requirements
To run this project locally you will need python and django installed on your machine. You will also be required to start a virtual environment before running your `manage.py` file. In this document we will go over how to install python and django on mac along with starting a virtual environment to run the project. 

## Installation 
#### Cloning the repo 
To clone the repo for the sake of simplicity once you've opened up your terminal type `cd desktop` to step into your desktop directory. Once you've done that type `git clone` and then paste the link of the repo within your terminal. You should see a folder appear on your desktop called `closedbracket`.

#### Installing python 
To install python you can use their offical website [Installing Python](https://www.python.org/downloads/) which will let you download the latest release available to the public. After you download the required packages you can complete the installation by following the wizard thats provided. 

#### Activating the virtual environment 
Before installing Django and running the project you'll need to activate a python virtual environment. To do so `cd` in to the  `closedbracket` directory within your terminal and then type `ls` so you can see whats on that level. You should see 2 folders titled `env` and `closedbracket`. To activate the virtual environment type `source env/bin/activate` and you should see a `(env)` appear next to your prefix within the terminal. 

#### Installing Django
Once your virtual environment is active, you can now install Django. To do so run the command `python3 -m pip install django` in your terminal. You'll see multiple dependencies being installed and once you a successfull message that means you're successful in adding Django to this directory. 

## Running the code
To run the project `cd` into the `closedbracket` directory and then type `ls` to see all the files. You should see a file titled `manage.py`. This is the file which you need to initialize to run the project locally. Type `python3 manage.py runserver` in your terminal and you'll several commands being run to activate your local host. Once you see the message `starting development server at` followed by your local host address you'll be able to copy paste that into your browser to view the platform. 

## File Structure 
At this point you should be at the directory level which has 2 folders named `closedbracket` and `closedbracketfinal`. The `closedbracket` folder contains the files that are auto created when you create a new Django project. These take care of the required dependencies and you don't really need to interact with any of these base files. All the code for the project resides in the `closedbracketfinal` folder. Within the `closedbracketfinal` folder you'll see 7 files and 2 more folders. The `templates` folder contains the static HTML files that are used for our front end. The `static` folder contains another directory called `closedbracketfinal` which has all the images and icons used on the platform.

The files which you'll be referring to for actual project code are all the HTML files in the `static` folder along with `models.py`, `admin.py`, `urls.py`, and `views.py`. 

## Navigating the platform 
Once you've successfully begun running the platform locally, after pasting the localhost link in your browser you???ll be able to use the ClosedBracket system. Within your search bar you should have an address that resembles `http://000.0.0.1:8000/`. Type `profile` after the port designation `8000/` and you'll be taken to our profile page. You can now begin navigating the platform by clicking different buttons on the navbar and the body of the page. If you want to see a specific content all you'll need to do is type `signup`, `signin`, `profile`, `friends`, `leaderboard`, `play`, `results`, `admin`, or `editor` next to the port designation. Authentication runs in a different container and won't be responsive while running the platform locally so you'll need to force navigate to those pages using the search bar if you wish to see their layout. 

To view the admin console type `admin` in the search bar and login with `username: gautamsood` and `password: 01100111`. Here you can view the different users on the platform and also the different questions which users can attempt. You can add or remove questions depending on what the individuals are being tested on. 

# Made with love by the ClosedBracket Team ??????







