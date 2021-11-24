from django.test import TestCase, RequestFactory
from django.contrib.messages.storage.fallback import FallbackStorage
from django.contrib.sessions.middleware import SessionMiddleware
from django.contrib.auth.models import AnonymousUser
from datetime import datetime
from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO
import sys
from PIL import Image

from authentication.views import *
from assignments.views import *
from clubs.views import *
from clubs.views import home as club
from courses.views import *
from scheduler.views import *
from forum.views import *
from forum.views import home as forum


# Create your tests here.

# Testing models
class ModelTesting(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.student = Account.objects.create_user(
            username='test@example.com', firstname='John', lastname='Doe', password='test@123', type='Student'
        )
        self.teacher = Account.objects.create_user(
            username='test_teacher@example.com', firstname='John', lastname='Deer', password='test@123', type='Teacher'
        )
        self.superuser = Account.objects.create_superuser(
            username='superuser@example.com', firstname='John', lastname='Super', password='test@123'
        )
        self.file_path = 'C:/Users/hrudh/OneDrive/Personal Files/Microsoft Engage/Engagetemp/media/assignments/doc2.txt'
        self.file_bytes = BytesIO(open(self.file_path, 'rb').read())
        self.file_bytes.seek(0)
        self.file = InMemoryUploadedFile(self.file_bytes, 'doc2', 'doc2.txt', 'text/plain', sys.getsizeof(self.file_bytes), None)
        self.img = Image.new('RGBA', size=(100, 100), color=(155, 0, 0))
        self.image_file = BytesIO()
        self.img.save(self.image_file, "png")
        self.image_file.name = 'default.png'
        self.image_file.seek(0)
        # self.image_file = SimpleUploadedFile('default.png', content=self.image_bytes, content_type='image/png')
        MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'

    def get_test_student(self, url):
        request = self.factory.get(url)
        request.user = self.student
        middleware = SessionMiddleware()
        middleware.process_request(request)
        request.session.save()
        setattr(request, '_messages', FallbackStorage(request))
        return request

    def get_test_teacher(self, url):
        request = self.factory.get(url)
        request.user = self.teacher
        middleware = SessionMiddleware()
        middleware.process_request(request)
        request.session.save()
        setattr(request, '_messages', FallbackStorage(request))
        return request

    def test_details(self):
        # Register
        request = self.factory.post(
            'register',
            {
                'username': 'reg@example.com',
                'firstname': 'Regina',
                'lastname': 'Phelange',
                'type': 'Student',
                'password1': 'test@123',
                'password2': 'test@123'
            }
        )
        middleware = SessionMiddleware()
        middleware.process_request(request)
        request.session.save()
        request.user = self.teacher
        # setattr(request, 'session', {'session_key': 'session'})
        setattr(request, '_messages', FallbackStorage(request))
        register(request)
        request = self.factory.post(
            'register',
            {
                'username': 'reg@example.com',
                'firstname': 'Regina',
                'lastname': 'Phelange',
                'type': 'Student',
                'password1': 'test@123'
            }
        )
        middleware = SessionMiddleware()
        middleware.process_request(request)
        request.session.save()
        request.user = self.teacher
        # setattr(request, 'session', {'session_key': 'session'})
        setattr(request, '_messages', FallbackStorage(request))
        register(request)
        register(self.get_test_student('register'))

        # Login
        request = self.factory.post(
            'accounts/login',
            {
                'username': 'reg@example.com',
                'password': 'test@123',
            }
        )
        middleware = SessionMiddleware()
        middleware.process_request(request)
        request.session.save()
        request.user = AnonymousUser
        request.user.is_authenticated = False
        # setattr(request, 'session', {'session_key': 'session'})
        setattr(request, '_messages', FallbackStorage(request))
        loginView(request)

        # Wrong Login
        request = self.factory.post(
            'accounts/login',
            {
                'username': 'reg@example.com',
                'password': 'test@12345',
            }
        )
        middleware = SessionMiddleware()
        middleware.process_request(request)
        request.session.save()
        request.user = AnonymousUser
        request.user.is_authenticated = False
        # setattr(request, 'session', {'session_key': 'session'})
        setattr(request, '_messages', FallbackStorage(request))
        loginView(request)

        # Student Preference
        request = self.factory.post(
            'scheduler',
            {
                'mode': 'Online',
                'vaccination_status': 'Fully Vaccinated',
                'file': self.file
            }
        )
        request.user = self.student
        with open(self.file_path, 'rb') as f:
            request.FILES['file'] = f
            request.FILES['file'].read()
        request.POST = {'mode': 'Online', 'vaccination_status': 'Fully Vaccinated', 'file': self.file}
        request.FILES['file'] = self.file
        setattr(request, 'session', 'session')
        setattr(request, '_messages', FallbackStorage(request))
        StudentPreference(request)
        StudentPreference(self.get_test_student('scheduler'))

        #LandingPage
        landingPage(self.get_test_student(''))

        # Profile
        profile(self.get_test_student('profile'))

        # Edit Profile
        editProfile(self.get_test_student('editProfile'))
        request = self.factory.post(
            'editProfile',
            {
                'bio': 'This is my bio',
                'profile_pic': self.image_file
            }
        )
        request.user = self.student
        request.POST = {'bio': 'This is my bio', 'profile_pic': self.image_file}
        setattr(request, 'session', 'session')
        setattr(request, '_messages', FallbackStorage(request))
        editProfile(request)

        # Create Course
        request = self.factory.post(
            'courses/create',
            {
                'name': 'OOPS',
                'description': 'This is a CS course',
                'credits': 4,
                'create-course': 'None'
            }
        )
        request.user = self.teacher
        setattr(request, 'session', 'session')
        setattr(request, '_messages', FallbackStorage(request))
        CourseCreateView(request)

        # Edit Course
        request = self.factory.post(
            'courses/create/1',
            {
                'name': 'OOPS',
                'description': 'This is a CS course',
                'credits': 4,
                'create-course': '1'
            }
        )
        request.user = self.teacher
        setattr(request, 'session', 'session')
        setattr(request, '_messages', FallbackStorage(request))
        CourseCreateView(request)

        # Create Course Page
        CourseCreateView(self.get_test_teacher('courses/create'))

        # Edit Course Page
        CourseCreateView(self.get_test_teacher('courses/create/1'), 1)

        # Student Courses Page
        CourseCreateView(self.get_test_student('courses/create'))
        CourseView(self.get_test_student('courses'))

        # Enroll Course
        request = self.factory.post('courses', {'enroll-course': 1})
        request.user = self.student
        setattr(request, 'session', 'session')
        setattr(request, '_messages', FallbackStorage(request))
        CourseView(request)

        # Withdraw Course
        request = self.factory.post('courses', {'withdraw-course': 1})
        request.user = self.student
        setattr(request, 'session', 'session')
        setattr(request, '_messages', FallbackStorage(request))
        CourseView(request)

        # Create Assignment
        request = self.factory.post(
            'assignment/create',
            {
                'course': '1',
                'content': 'This is about object oriented programming',
                'title': 'OOPS',
                'marks': '10',
                'deadline': datetime.now(),
                'create-assignment': 'None'
            }
        )
        request.user = self.teacher
        setattr(request, 'session', 'session')
        setattr(request, '_messages', FallbackStorage(request))
        AssignmentCreateView(request)

        # Edit Assignment
        request = self.factory.post(
            'assignment/create/1',
            {
                'course': '1',
                'content': 'This is about object oriented programming',
                'title': 'OOPS',
                'marks': '10',
                'deadline': datetime.now(),
                'create-assignment': '1'
            }
        )
        request.user = self.teacher
        setattr(request, 'session', 'session')
        setattr(request, '_messages', FallbackStorage(request))
        AssignmentCreateView(request)

        # Create Assignment Page
        AssignmentCreateView(self.get_test_teacher('assignment/create'))

        # Edit Assignment Page
        AssignmentCreateView(self.get_test_teacher('assignment/create'), 1)

        # Student Create Assignment
        AssignmentCreateView(self.get_test_student('assignment/create'))

        # Student Assignments
        AssignmentView(self.get_test_student('assignment'))

        # Teacher Assignments
        AssignmentView(self.get_test_teacher('assignment/create'))

        # Teacher Submit Assignment
        AssignmentSubmissionView(self.get_test_teacher('assignment/submit/1'), 1)

        # Student Submit Assignment Page
        AssignmentSubmissionView(self.get_test_student('assignment/submit/1'), 1)

        # Student Submit Assignment Page
        request = self.factory.post('assignment/submit/1', {'file': self.file})
        request.user = self.student
        with open(self.file_path, 'rb') as f:
            request.FILES['file'] = f
            request.FILES['file'].read()
        request.POST = {'file': self.file}
        request.FILES['file'] = self.file
        setattr(request, 'session', 'session')
        setattr(request, '_messages', FallbackStorage(request))
        AssignmentSubmissionView(request, 1)

        # Student Re-Submit Assignment Page
        request = self.factory.post('assignment/submit/1', {'file': self.file})
        request.user = self.student
        with open(self.file_path, 'rb') as f:
            request.FILES['file'] = f
            request.FILES['file'].read()
        request.POST = {'file': self.file}
        request.FILES['file'] = self.file
        setattr(request, 'session', 'session')
        setattr(request, '_messages', FallbackStorage(request))
        AssignmentSubmissionView(request, 1)

        # Teacher Assignment Submissions
        AssignmentSubmissionListView(self.get_test_teacher('assignment/submission/1'), 1)

        # Grade Assignment
        request = self.factory.post(
            'assignment/submission/1',
            {
                'student': 'test@example.com',
                'grade': 10
            }
        )
        request.user = self.teacher
        setattr(request, 'session', 'session')
        setattr(request, '_messages', FallbackStorage(request))
        AssignmentSubmissionListView(request, 1)

        # View Assignment Submission
        SubmittedAssignment(self.get_test_student('assignment/submit-view/1'), 1)

        # Create Club
        create_club(self.get_test_student('club/create_club'))
        request = self.factory.post('club/create_club', {'name': 'Test Club', 'description': 'Unit testing club', 'approval_required': 'True'})
        request.user = self.teacher
        setattr(request, 'session', 'session')
        setattr(request, '_messages', FallbackStorage(request))
        create_club(request)

        # Clubs Home
        club(self.get_test_student('club'))
        request = self.factory.post('club', {'join-club': 'test-club'})
        request.user = self.student
        setattr(request, 'session', 'session')
        setattr(request, '_messages', FallbackStorage(request))
        club(request)

        # Create Event
        request = self.factory.post(
            'club/create_event/test-club',
            {'name': 'Test Event', 'description': 'This is a Unit Test Event', 'location': 'Bangalore', 'duration': 2, 'date': datetime.now()}
        )
        request.user = self.teacher
        setattr(request, 'session', 'session')
        setattr(request, '_messages', FallbackStorage(request))
        create_event(request, 'test-club')
        create_event(self.get_test_teacher('club/create_event/test-club'), 'test-club')

        # Club Page
        club_view(self.get_test_student('club/test-club'), 'test-club')

        # Teacher Preference
        request = self.factory.post(
            'scheduler',
            {
                'mode': 'Online',
                'vaccination_status': 'Partially Vaccinated',
                'file': self.file
            }
        )
        request.user = self.teacher
        with open(self.file_path, 'rb') as f:
            request.FILES['file'] = f
            request.FILES['file'].read()
        request.POST = {'mode': 'Online', 'vaccination_status': 'Partially Vaccinated', 'file': self.file}
        request.FILES['file'] = self.file
        setattr(request, 'session', 'session')
        setattr(request, '_messages', FallbackStorage(request))
        StudentPreference(request)
        StudentPreference(self.get_test_teacher('scheduler'))

        # Club Page
        club_view(self.get_test_student('club/test-club'), 'test-club')

        # Teacher Preference
        request = self.factory.post(
            'scheduler',
            {
                'mode': 'Online',
                'vaccination_status': 'Fully Vaccinated',
                'file': self.file
            }
        )
        request.user = self.teacher
        with open(self.file_path, 'rb') as f:
            request.FILES['file'] = f
            request.FILES['file'].read()
        request.POST = {'mode': 'Online', 'vaccination_status': 'Fully Vaccinated', 'file': self.file}
        request.FILES['file'] = self.file
        setattr(request, 'session', 'session')
        setattr(request, '_messages', FallbackStorage(request))
        StudentPreference(request)
        StudentPreference(self.get_test_teacher('scheduler'))

        # Club Page
        club_view(self.get_test_student('club/test-club'), 'test-club')

        # Approve Member
        request = self.factory.post('club/approve_member', {'approve-member': f'test-club_{self.student.username}'})
        request.user = self.teacher
        setattr(request, 'session', 'session')
        setattr(request, '_messages', FallbackStorage(request))
        approve_member(request)

        # Attend Event
        request = self.factory.post('club/test-club', {'attend-event': 1})
        request.user = self.student
        setattr(request, 'session', 'session')
        setattr(request, '_messages', FallbackStorage(request))
        club_view(request, 'test-club')

        # Skip Event
        request = self.factory.post('club/test-club', {'skip-event': 1})
        request.user = self.student
        setattr(request, 'session', 'session')
        setattr(request, '_messages', FallbackStorage(request))
        club_view(request, 'test-club')

        # Leave Club
        request = self.factory.post('club/test-club', {'leave-club': 'test-club'})
        request.user = self.student
        setattr(request, 'session', 'session')
        setattr(request, '_messages', FallbackStorage(request))
        club_view(request, 'test-club')

        # Join Club
        request = self.factory.post('club/test-club', {'join-club': 'test-club'})
        request.user = self.student
        setattr(request, 'session', 'session')
        setattr(request, '_messages', FallbackStorage(request))
        club_view(request, 'test-club')


        # Forum Home
        forum(self.get_test_student('forum/'))
        request = self.factory.post(
            'forum/create_post',
            {
                'post-title': 'Unit testing is good',
                'post-content': 'Unit testing is always good and helps find the code coverage and unused code',
                'post-tags': 'unit testing, code coverage',
                'category-title': 'Unit Testing',
                'category-description': 'Discussions related to Unit Testing',
                'post-categories': ''
            }
        )
        request.user = self.student
        setattr(request, 'session', 'session')
        setattr(request, '_messages', FallbackStorage(request))
        create_post(request)

        # Testing existing category
        forum(self.get_test_student('forum/'))
        request = self.factory.post(
            'forum/create_post',
            {
                'post-title': 'Unit testing is annoying',
                'post-content': 'Unit testing is very time consuming and annoying',
                'post-tags': 'unit testing, code coverage',
                'category-title': '',
                'category-description': '',
                'post-categories': '1'
            }
        )
        request.user = self.student
        setattr(request, 'session', 'session')
        setattr(request, '_messages', FallbackStorage(request))
        create_post(request)

        request = self.factory.post(
            'forum/create_post',
            {
                'post-title': 'Machine Learning robot',
                'post-content': "Does ML mean, machines can go to school?",
                'post-tags': 'machine learning',
                'category-title': 'Machine Learning',
                'category-description': 'Discussions about ML',
                'post-categories': ''
            }
        )
        request.user = self.student
        setattr(request, 'session', 'session')
        setattr(request, '_messages', FallbackStorage(request))
        create_post(request)

        create_post(self.get_test_student('forum/create_post'))

        posts(self.get_test_student('forum/posts/unit-testing'), 'unit-testing')
        request = self.factory.post('forum/posts/unit-testing', {'delete-post': 'unit-testing-is-annoying'})
        request.user = self.student
        setattr(request, 'session', 'session')
        setattr(request, '_messages', FallbackStorage(request))
        posts(request, 'unit-testing')

        request = self.factory.post(
            'forum/create_post',
            {
                'post-title': 'Unit testing is not annoying',
                'post-content': 'Unit testing is not very time consuming and annoying',
                'post-tags': 'unit testing, code coverage',
                'category-title': '',
                'category-description': '',
                'post-categories': '1'
            }
        )
        request.user = self.student
        setattr(request, 'session', 'session')
        setattr(request, '_messages', FallbackStorage(request))
        create_post(request)
        create_post(self.get_test_student('forum/create_post'))

        request = self.factory.post('forum/detail/unit-testing-is-not-annoying', {'delete-post': 'unit-testing-is-not-annoying'})
        request.user = self.student
        setattr(request, 'session', 'session')
        setattr(request, '_messages', FallbackStorage(request))
        detail(request, 'unit-testing-is-not-annoying')

        detail(self.get_test_student('forum/detail/unit-testing-is-good'), 'unit-testing-is-good')
        request = self.factory.post(
            'forum/detail/unit-testing-is-good',
            {
                'comment-content': 'Yes, I agree'
            }
        )
        request.user = self.teacher
        setattr(request, 'session', 'session')
        setattr(request, '_messages', FallbackStorage(request))
        detail(request, 'unit-testing-is-good')

        request = self.factory.post(
            'forum/detail/unit-testing-is-good',
            {
                'reply-content': 'Thank you sir',
                'comment_id': 1
            }
        )
        request.user = self.student
        setattr(request, 'session', 'session')
        setattr(request, '_messages', FallbackStorage(request))
        detail(request, 'unit-testing-is-good')

        request = self.factory.post('forum/detail/unit-testing-is-good', {'delete-reply': 1})
        request.user = self.student
        setattr(request, 'session', 'session')
        setattr(request, '_messages', FallbackStorage(request))
        detail(request, 'unit-testing-is-good')

        request = self.factory.post('forum/detail/unit-testing-is-good', {'delete-comment': 1})
        request.user = self.teacher
        setattr(request, 'session', 'session')
        setattr(request, '_messages', FallbackStorage(request))
        detail(request, 'unit-testing-is-good')

        request = self.factory.post('forum/detail/unit-testing-is-good', {'delete-post': 'unit-testing-is-good'})
        request.user = self.student
        setattr(request, 'session', 'session')
        setattr(request, '_messages', FallbackStorage(request))
        detail(request, 'unit-testing-is-good')

        request = self.factory.get('forum/posts/machine-learning-robot')
        request.user = AnonymousUser()
        request.user.is_authenticated = False
        middleware = SessionMiddleware()
        middleware.process_request(request)
        request.session.save()
        setattr(request, '_messages', FallbackStorage(request))
        detail(request, 'machine-learning-robot')

        request = self.factory.post('forum/posts/machine-learning', {'delete-post': 'machine-learning-robot'})
        request.user = self.student
        setattr(request, 'session', 'session')
        setattr(request, '_messages', FallbackStorage(request))
        posts(request, 'machine-learning')





        # ------------------------------All deletions------------------------------#

        # Teacher Preference
        request = self.factory.post(
            'scheduler',
            {
                'mode': 'Online',
                'vaccination_status': 'Not Vaccinated'
            }
        )
        request.user = self.teacher
        setattr(request, 'session', 'session')
        setattr(request, '_messages', FallbackStorage(request))
        StudentPreference(request)

        # HomePage
        homePage(self.get_test_student('home'))
        homePage(self.get_test_teacher('home'))

        # Delete Assignment Submission
        request = self.factory.post('assignment/submit-view/1', {'delete-submission': 1})
        request.user = self.student
        setattr(request, 'session', 'session')
        setattr(request, '_messages', FallbackStorage(request))
        SubmittedAssignment(request, 1)

        # Delete Assignment
        request = self.factory.post('assignment', {'delete-assignment': 1})
        request.user = self.teacher
        setattr(request, 'session', 'session')
        setattr(request, '_messages', FallbackStorage(request))
        AssignmentView(request)

        # Delete Course
        request = self.factory.post('courses', {'delete-course': 1})
        request.user = self.teacher
        setattr(request, 'session', 'session')
        setattr(request, '_messages', FallbackStorage(request))
        CourseView(request)

        # Delete Club
        request = self.factory.post('club/test-club', {'delete-club': 'test-club'})
        request.user = self.teacher
        setattr(request, 'session', 'session')
        setattr(request, '_messages', FallbackStorage(request))
        club_view(request, 'test-club')

        homePage(self.get_test_student('home'))

        # logout
        logout_view(self.get_test_student('logout'))

        # LandingPage
        request = self.factory.get('')
        request.user = AnonymousUser()
        request.user.is_authenticated = True
        landingPage(request)
        loginView(request)
        request.user = AnonymousUser()
        request.user.is_authenticated = False
        landingPage(request)
        loginView(request)

        # Account Settings
        accountSettings(self.get_test_student('account_settings'))
        password_change_done(self.get_test_student('password_change/done'))

        # Delete User
        deleteuser(self.get_test_student('authentication/deleteuser'))
        request = self.factory.post('authentication/deleteuser', {'delete-account': ''})
        request.user = self.student
        middleware = SessionMiddleware()
        middleware.process_request(request)
        request.session.save()
        setattr(request, '_messages', FallbackStorage(request))
        deleteuser(request)
