<h1 align="center">
<img src="static/Favicon.png" width="128"/>
<br>
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
<p align="center">
	Developed by : <i> Ishita Datta </i>
</p>

## About
Studee is a student portal application that helps students and teachers communicate both virtually and physically by keeping students ENGAGE-ed to use the platform with the help of a <i> Credit-based system </i>.

<ul>  <b> Tools and Technologies</b>
<ul>
	<li>django</li>
	<li>HTML</li>
	<li>CSS</li>
	<li>JavaScript</li>
	<li>Python</li>
	<li>Figma</li>
	<li>Chart.js</li>
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
        <li><a href="#vaccination-tracker">Vaccination Tracker</a></li>
        <li><a href="#submission">Submission tool</a></li>
        <li><a href="#online-forum">Online Forum</a></li>
      </ul>
    </li>
    <li>
      <a href="#additional-features">Additional Features</a>
      <ul>
        <li><a href="#authentication">Authentication</a></li>
        <li><a href="#credit-system">Credit System</a></li>
        <li><a href="#courses">Courses</a></li>
	<li><a href="#user-profile">User Profile</a></li>
	<li><a href="#clubs">Clubs</a></li>
      </ul>
    </li>
    <li>
      <a href="#other-features">Other Features</a>
   </li>
  </ol>
</details>

## Basic Features

### Vaccination Tracker
 1. Student can select option for offline/online class 
 2. Student can select vaccination status (not vaccinated/ partially vaccinated/ fully vaccinated)
 3. If vaccinated, student must upload latest vaccination certificate
 4. Display notice for students on dashboard to update vaccination status not done
 5. Teacher will receive list of all student preferences

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
 14. Teacher can grade assignments

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
 10. Increment hit count of a post every time a new user views the post
 11. Delete post (and its trailing comments and replies) by post owner
 12. Delete comment (and its trailing replies) by comment owner
 13. Delete comment reply by its owner

## Additional Features

### Authentication
 1. Sign Up by entering user details (firstname, lastname, email,type of user, password, re-enter password)
 2. Create two sets of users - Student and Teacher
 3. Unique username and email authentication
 4. Password length check
 5. Password strength check (too short/too common/all numbers)
 6. Sign In by entering user details (email and password)
 7. Superuser for admin privileges
 8. Logout 
 9. Session storage

### Credit System
 1. Credits earned for posts on forum
 2. Credits earned from commenting on posts on forum
 3. Credits earned from replying to comments on forum
 4. Credits earned from assignment submission
 5. Credits earned from uploading vaccination certificate
 6. Credit distribution split-up representation using Chart.js
 7. Credit redeem options

### Courses
 1. Create course option for teachers (course name, course image, course description, credits)
 2. Course view option for students (course name, teacher name, course description, credits, duration)
 3. Enroll into course option for students
 4. Withdraw from a course option for students
 5. Delete a course is user is a teacher
 6. Edit a course if user is a teacher

### User Profile
 1. Upload profile picture
 2. Change password
 3. Edit Profile
 4. Delete Profile
 5. Minimise dashboard side drawer

### Clubs
 1. Create a club (club name, club description, approval required) 
 2. Founders must have high credits (30 credits required to create a club)
 3. Make creater of the club, the founder of a club 
 4. Create an event (event name, date, location, duration, description)
 5. Attend an event (credits awarded)
 6. Show calendar with event date
 7. Allow members to join a club
 8. List current members of the club
 9. Send teacher approval request for joining club  
 10. Teacher approval notification

## Other Features
1. Responsive to device resolution 


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

<i>Special thanks to my mentor Mr. Prasanna Kulkarni for his valuable advice and assistance in the development of this project.</i>

