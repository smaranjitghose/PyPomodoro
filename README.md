# PyPomodoro 
This is a simple python script crafted with ❤ for anyone who wants to level up their productivity or learning by 10x

## Pomodoro Technique: A little briefing about the golden tradition 🎯

The Pomodoro Method is a time management philosophy that aims to provide the user with maximum focus and creative freshness, thereby allowing them to complete projects faster with less mental fatigue.

This is how it goes:

- For every project throughout the day, you budget your time into short increments and take breaks periodically.
- You work for 25 minutes, then take break for five minutes.
- Each 25-minute work period is called a “pomodoro”, named after the Italian word for tomato 🍅. Francesco Cirillo used a kitchen timer⏲ shaped like a tomato as his personal timer, and thus the method’s name.
- After four “pomodoros” have passed, (100 minutes of work time with 15 minutes of break time) you then take a 15-20 minute break.
- Every time you finish a pomodoro, you mark your progress with an “X”, and note the number of times you had the impulse to procrastinate or switch gears to work on another task for each 25-minute chunk of time.

![Infographic](http://www.fedracongressi.com/fedra/wp-content/uploads/2016/02/fedra-11-marzo.jpg)

## How to use this script without any hastle:

- Download the ```pomo_py.exe``` file
- Run the file
- Click on the Ok Button
- Your pomodoro is set to 25 minutes by default
- You will be alerted once its over followed by a break
- You will be asked if you want more pomodoro slots
- When you are done for the day, sit back and amaze yourself by the pomodoros you have completed to get the jon done!

## Ways to contribute:

1. Adding the feature of **Blocking of certain websites during pomodoro slots** 🚫

One way of doing this is  changing the host file in ```c:\Windows\System32\drivers\etc ``` so that any IP address can be redirected to the local host and thereby denying access to it

I had integrated this component intially however I found out that this needs the script to be always executed with admin priviledges and which was not feasible for me to incorporate while making an exe files

2. Improving the GUI using ```tkinter``` or anything you wish  🎨

3.Adding a feature of taking in input the total number of hours to be dedidcated and then automatically providing slots as per the Pomodoro technique: 5 min breaks for every 4 slots followed by 15 min break after a cumalative slot time of 2 hrs 🤖

4.Storing the log details of the various pomodoro sessions in a ```log.txt``` file 🧾

5.Storing the log files in ```.csv``` file or in a local database

6.Having logs for different users

7.Using Flutter to build a small app with this working under the hood

