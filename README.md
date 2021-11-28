<h1 align="center">
	<a href="https://studee-app.herokuapp.com/"><img src="static/Favicon.png" width="128"/></a>
<br>
 STUDEE
  <br>
</h1>
<h4 align="center">Committed To Lifelong Learning In A Caring Environment</h4>
<p align="center">
  <a href="#about">About</a> •
  <a href="#features">Features</a> •
  <a href="#installation">Installation</a> •
  <a href="#cicd">CI/CD</a>
	
</p>
<p align="center">
	Developed by : <i> Ishita Datta </i>
</p>

<p align="center">
    <img src="https://img.shields.io/badge/license-MIT-69BBBE">
    <img src="https://img.shields.io/badge/build-pass-69BBBE">
    <img src="coverage.svg">
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
	<li> Heroku </li>
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
Students can provide their vaccination status and their preferred mode of classes and teacher can receiver a roster consisting of these student details.
 1. Students can select option for offline/online class 
 2. Students can select vaccination status (not vaccinated/ partially vaccinated/ fully vaccinated)
 3. If vaccinated, students must upload latest vaccination certificate
 4. Display notice for students on dashboard to update vaccination status not done
 5. Teachers will receive list of all student preferences <br>
 <i> *All teachers are assumed to be fully vaccinated </i>
 

### Submission 
Student can upload their assignments and teachers can grade the assignments
 1. Teachers can create a new assignment(assignment title, assignment detail, assignment course, marks, submission due date)
 2. Students can view assignments if the student is enrolled in the course
 3. Students assignment submission form - to upload assignment document
 4. Teachers can view assignment submissions
 5. Teachers can download each assignment
 6. Teachers can edit assignment
 7. Teachers can delete assignment uploaded by them
 8. Students can delete assignment submitted by them
 9. Students can re-submit assignment
 10. Students can view submitted assignment
 11. Display pending assignment submission deadlines on calendar
 12. Display number of pending days till deadline (emphasis on days remaining if deadline less than or equal to 2 days)
 13. Auto-update assignment expiry status post submission deadline
 14. Teachers can grade assignments

### Online Forum
Students and teachers can interact in the forum in the form of posts which are segregated into categories.

#### Category View
A category is a topic of conversation.
 1. Segment each post under an existing category or create a new category for a post
 2. Display latest post of each category in category list 
 3. Display number of posts of each category
 4. Map each category to an engagement score (0 Enagement Topic, Low Engagement Topic, Popular, High Engagement, Closed Topic)
 5. Display category and its posts engagement score using legend icons

#### Post View
 1. Create a new post
 2. Add tags to posts
 3. Display date and user next to post/comment/reply
 4. Comment on a post
 5. Reply to a comment on a post
 6. View other comments and replies
 7. Show user type (teacher/student) for each post, comment, reply
 8. Display number of comments and number of views for the post  
 9. Increment engagement score for each user forum activity
 10. Increment hit count of a post every time a new user views the post
 11. Delete post (and its trailing comments and replies) by post owner
 12. Delete comment (and its trailing replies) by comment owner
 13. Delete comment reply by its owner

## Additional Features

### Authentication
New users can create a new account and existing users can log in to their accounts.
 1. Sign Up by entering user details (firstname, lastname, email,type of user, password, re-enter password)
 2. Create two sets of users - Student and Teacher
 3. Unique username and email authentication
 4. Password length check
 5. Password strength check (too short/too common/all numbers)
 6. Sign In by entering user details (email and password)
 7. Superuser for admin privileges
 8. Logout 
 9. Session storage
 10. Automatic login for user if he/she is already logged in
 11. Display account successfully created message for new users

### Credit System
Every functionality in the application has some actions that can earn the user some credits.
 1. Credits earned for posts on forum
 2. Credits earned from commenting on posts on forum
 3. Credits earned from replying to comments on forum
 4. Credits earned from assignment submission
 5. Credits earned from joining a club
 6. Credits earned from attending an event
 7. Credits earned from enrolling for a course
 8. Credit distribution split-up representation using Chart.js
 9. Credit redeem options
 10. Display student with highest credits as 'Top Credit student' in dashboard
 11. Credits deducted if posts/comments/replies are deleted
 12. Credits deducted if assignment submission is deleted
 13. Credits deducted on leaving a club
 14. Credits deducted on skipping an event
 15. Credits deducted on withdrawing from a course

### Courses
Teachers can create a course which a student can get enrolled into and receive assignments for the course.
 1. Create course option for teachers (course name, course image, course description, credits)
 2. Course view option for students (course name, teacher name, course description, credits, duration)
 3. Enroll into course option for students 
 4. Withdraw from a course option for students
 5. Delete a course if user is a teacher
 6. Edit a course if user is a teacher

### User Profile
Users can update their profile details.
 1. Upload profile picture
 2. View total credits
 3. View user email id
 4. Update user bio
 5. Choose to cancel or save current changes of edit profile details

### Clubs
Students and teachers can create and join clubs and organise and attend events of the club
 1. Create a club (club name, club description, approval required) 
 2. Student founders must have high credits (30 credits required to create a club)
 3. Teacher club founders can create clubs without having minimum credit requirement
 4. Assign founder of the club as the head of the club 
 5. Club founders can create an event (event name, date, location, duration, description)
 6. Show calendar with event date
 7. Allow members to join a club
 8. List current members of the club
 9. Send teacher approval request for joining club  
 10. Teacher approval notification
 11. Attend an event
 12. Skip an event
 13. Cancel an event
 14. Club founders can delete a club
 15. Display club member details regarding vaccination (if all members are vaccinated)
 16. Leave a club
 
## Other Features
1. Responsive to device resolution 
2. Minimise and maximise dashboard side drawer
3. Display vaccination card as fully vaccinated on dashboard for teachers
4. Change password
5. Delete account

 # Installation
1) Install python3
2) Install pip for python3
3) Install virtualenv
  `pip install virtualenv` or `pip3 install virtualenv`
4) Create virtual environment and cd into it
  `virtualenv studee-app --python python3 && cd studee-app`
5) Clone git repository into src folder and cd into it `git clone https://github.com/ishitadatta/Studee src && cd src`
6) Install requirements `pip install -r requirements.txt` or `pip3 install -r requirements.txt`
7) Make appropriate changes to settings module and make migrations using `python manage.py makemigrations` and then 
  `python manage.py migrate`
8) Run using `python manage.py runserver`
9) Create superuser to log into admin `python manage.py createsuperuser`
10) Paste the server address [127.0.0.1:8000](http://127.0.0.1:8000) on any browser to see the webpage working on your local machine
11) To view as a superuser user go to url address:  [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

# CI/CD
1. Software used for agile development - Azure Boards
2. Version control - Git & GitHub
3. Requirement specification - Traceability Matrix
4. Unit Testing - Coverage in Django
5. Static testing - Desk checking of code
6. Deployment - Heroku

###### For better experience, use the app on your local server :smiley: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
# Additional Links
* [UI/UX designs on Figma](https://www.figma.com/file/PkDsRCRLRE0WZ6yj0GkkNC/Studee?node-id=0%3A1)
* [Video Demo](https://youtu.be/Lx0FmP3NpPI)

---
#### Developed For Microsoft Engage Mentorship Program '21.
###### _Special thanks to my mentor, Mr. Prasanna Kulkarni, for his valuable advice and assistance in the development of this project._
