# Studee
A student portal application for Engage 2021

<h1 align="center">
 STUDEE
  <br>
</h1>
<h4 align="center">Committed To Lifelong Learning In A Caring Environment</h4>
<p align="center">
  <a href="#about">About</a> •
  <a href="#features">Features</a> •
  <a href="#installation">Installation</a> •
  <a href="#ci/cd">CI/CD</a>
	
</p>
<!-- <p align="center">
	Developed by : <i> Ishita Datta </i>
</p> -->

## About
Studee is a student portal application that helps students and teachers communicate both virtually and physically and helps students stay ENGAGE-ed with a credit-based system.
<ul>  <b> Tools and Technologies</b>
<ul>
<li>django</li>
<li>HTML</li>
<li>CSS</li>
<li>JavaScript</li>
<li>Figma</li>
<li>Azure Boards</li>
</ul>
</ul>

## Features
<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#basic-features">Basic Features</a>
      <ul>
        <li><a href="#scheduler">Scheduler</a></li>
        <li><a href="#submission">Submission tool</a></li>
        <li><a href="#online-forum">Online Forum</a></li>
      </ul>
    </li>
    <li>
      <a href="#additional-features">Additional Features</a>
   </li>
      <ul>
        <li><a href="#authentication">Authentication</a></li>
        <li><a href="#credit-system">Credit System</a></li>
        <li><a href="#courses">Courses</a></li>
	<li><a href="#user-profile">User Profile</a></li>
	<li><a href="#clubs">Clubs</a></li>
      </ul>
    </li>
  </ol>
</details>

## Basic Features

### Scheduler
 1. Upload vaccination certificate
 2. Credits allotted to students who have uploaded vaccination certificate
 3. Student can select option for offline/online class (form)
 4. Teacher will receive list of all student preferences

### Submission 
 1. Teacher can create a new assignment(assignment title, assignment detail, assignment course, marks, submission due date)
 2. Students can view assignments
 3. Student assignment submission form - to upload assignment document
 4. Teacher can view assignment submissions
 5. Teacher can download each assignment
 6. Teacher can edit assignment
 7. Teacher can delete assignment uploaded by them
 8. Student can delete assignment submitted by them
 9. Student can re-submit assignment
 10. Student can view submitted assignment
 11. Display pending assignment submission deadlines on calendar
 12. Display number of pending days till deadline (emphasis on deadline less than or equal to 2 days)
 13. Auto-update assignment expiry status post submission deadline
 14. Credits allotted for in-time assignment submission

### Online Forum
 1. Create a new post
 2. Categorise each post under a subject or create a new category for a post
 3. Map each category to an engagement score (0 Enagement Topic, Low Engagement Topic, Popular, High Engagement, Closed Topic)
 4. Add tags to posts
 5. Comment on a post
 6. Reply to a comment on a post
 7. Show user type (teacher/student) for each post, comment, reply
 8. Display user profile next to post/comment/reply
 9. Increment engagement score for each user forum activity
 10. Delete post and its trailing comments and replies by post owner
 11. Delete comment and its trailing replies by comment owner
 12. Delete comment reply by its owner

## Additional Features

### Authentication
 1. Sign Up by entering user details (firstname, lastname, email,type of user, password, re-enter password)
 2. Create two sets of users - Student and Teacher
 3. Unique username and email authentication
 4. Password length check
 5. Password strength check (too short/too common)
 6. Sign In by entering user details (email and password)
 7. Superuser for admin privileges
 8. Logout 
 9. Session storage

### Credit System
 1. Credits earned from engaging posts from Forum
 2. Credits earned from assignment submission
 3. Credits earned from uploading vaccination certificate
 4. Credit distribution split-up representation
 5. Credit redeem options

### Courses
 1. Create course option for teachers (course name, course image, course description, credits)
 2. Course view option for students (course name, teacher name, course description, credits, duration)
 3. Enroll into course option for students
 4. Delete a course by course owner

### User Profile
 1. Upload profile picture

### Clubs
 1. Create a club (club name, club description, approval required)
 2. Make creater of the club, the founder of a club 
 3. Create an event (event name, date, location, duration, description)
 4. Send faculty approval request after creating event request 
 5. Show calendar with event date
 6. Allow members to join a club
 7. List current members of the club


 # Installation
1) Install python3
2) Install pip for python3
3) Install virtualenv
  `pip install virtualenv` or `pip3 install virtualenv`
4) Create virtual environment and cd into it
  `virtualenv django-quiz --python python3 && cd django-quiz`
5) Clone git repository into src folder and cd into it `git clone <url> src && cd src`
6) Install requirements `pip install -r requirements.txt` or `pip3 install -r requirements.txt`
7) Make appropriate changes to settings module and make migrations using `python manage.py makemigrations` and then 
  `python manage.py migrate`
8) Run using `python manage.py runserver`
9) Create superuser to log into admin `python manage.py createsuperuser`

# CI/CD
1. Software used for agile development - Azure Boards
2. Version control - Git & GitHub
3. Requirement specification - Traceability Matrix
4. Unit Testing
5. Component Testing
6. Positive Testing
7. Negative Testing
