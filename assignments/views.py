from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader
from django.contrib import messages
from django.shortcuts import redirect
import os
import json
from django.conf import settings
from django.db.models import F

from .forms import AssignmentCreateForm, AssignmentSubmissionForm
from .models import Assignment, AssignmentSubmission
from authentication.models import Account
from courses.models import Course


# Create assignment view
@login_required
def AssignmentCreateView(request, id=None):
    if request.user.type == 'Teacher':
        if request.POST:
            form = AssignmentCreateForm(request.POST)
            if form.is_valid():
                assignment = form.save(commit=False)
                assignment_change = "created"
                if request.POST['create-assignment'] != "None":
                    assignment.id = request.POST['create-assignment']
                    assignment_change = "updated"
                assignment.user = Account.objects.get(username=request.user.username)
                assignment.save()
                messages.success(
                    request, f'Your assignment has been {assignment_change} successfully!')

                return redirect('assignments:home')
        else:
            template = loader.get_template(
                'assignments/assignment_create.html')
            form = AssignmentCreateForm()
            if id is not None:
                assignment = Assignment.objects.get(id=id)
                form = AssignmentCreateForm(
                    initial={
                        'title': assignment.title,
                        'content': assignment.content,
                        'course': assignment.course,
                        'marks': assignment.marks,
                        'deadline': assignment.deadline.date().isoformat()
                    }
                )
            context = {
                'create_form': form,
                'id': id
            }
            return HttpResponse(template.render(context, request))
    else:
        messages.warning(request, f'You are not authorised to create assignments!')
        return redirect('assignments:home')


# Assignment list view
@login_required
def AssignmentView(request):
    if request.method == 'POST':
        if 'delete-assignment' in request.POST:
            Assignment.objects.filter(id=request.POST['delete-assignment']).delete()
            # os.remove(f"{settings.BASE_DIR}{AssignmentSubmission.objects.get(assignment__id=request.POST['delete-assignment']).file.url}")
        return redirect('assignments:home')
    else:
        events = list(Assignment.objects.filter().values().all())
        event_data = get_deadlines(events)
        if request.user.type == 'Student':
            assignments = Assignment.objects.filter(course__id__in=request.user.enrolled_courses).values().all()
            submissions = list(AssignmentSubmission.objects.filter(
                user__username=request.user.username).values_list('assignment__id', flat=True))
        else:
            assignments = Assignment.objects.filter(user=Account.objects.get(username=request.user.username)).all()
            submissions = None
        context = {
            'assignments': assignments,
            'submissions': submissions,
            'event_data': json.dumps(event_data),
            'type': 'assignments'
        }
        template = loader.get_template('assignments/assignments.html')
        return HttpResponse(template.render(context, request))


# Assignment submission view for student
@login_required
def AssignmentSubmissionView(request, id):
    if request.user.type == 'Student':
        if request.POST:
            form = AssignmentSubmissionForm(request.POST, request.FILES)
            if form.is_valid():
                if AssignmentSubmission.objects.filter(assignment=Assignment.objects.get(id=id), user=Account.objects.get(username=request.user.username)).all().count() > 0:
                    os.remove(
                        f'{settings.BASE_DIR}{AssignmentSubmission.objects.get(assignment=Assignment.objects.get(id=id), user=Account.objects.get(username=request.user.username)).file.url}')
                    AssignmentSubmission.objects.filter(
                        assignment=Assignment.objects.get(id=id),
                        user=Account.objects.get(
                            username=request.user.username)
                    ).delete()
                    credit_account = Account.objects.get(username=request.user.username)
                    credit_account.forum_credits = F('assignment_credits') - 1
                    credit_account.save()
                else:
                    credit_account = Account.objects.get(username=request.user.username)
                    credit_account.forum_credits = F('assignment_credits') + 1
                    credit_account.save()
                submit = AssignmentSubmission(file=request.FILES['file'], user=Account.objects.get(
                    username=request.user.username), assignment=Assignment.objects.get(id=id))
                submit.save()
                messages.success(
                    request, f'Your assignment has been submitted!')

                return redirect('assignments:home')

        else:
            template = loader.get_template(
                'assignments/assignment_submission.html')
            form = AssignmentSubmissionForm()
            context = {
                'create_form': form
            }
            return HttpResponse(template.render(context, request))
    else:
        return redirect('assignments:home')


# Submitted assignment view for teacher
@login_required
def SubmittedAssignment(request, id):
    if request.method == 'POST':
        os.remove(f'{settings.BASE_DIR}{AssignmentSubmission.objects.get(assignment=Assignment.objects.get(id=id), user=Account.objects.get(username=request.user.username)).file.url}')
        AssignmentSubmission.objects.filter(assignment=Assignment.objects.get(id=id), user=Account.objects.get(username=request.user.username)).delete()
        return redirect('assignments:home')
    else:
        submission = AssignmentSubmission.objects.filter(
            assignment__id=id, user__username=request.user.username).all()
        submission = submission[len(submission) - 1]
        context = {
            'submission': submission
        }
        template = loader.get_template('assignments/assignment_submitted.html')
        return HttpResponse(template.render(context, request))


# Assignment submission list view
@login_required
def AssignmentSubmissionListView(request, id):
    if request.method == 'POST':
        grade = AssignmentSubmission.objects.get(assignment__id=id, user__username=request.POST['student'])
        grade.marks = request.POST['grade']
        grade.save()
        messages.success(request, f"{Account.objects.get(username=request.POST['student'])}'s assignment has been graded!")
        return redirect('assignments:submissions', id)
    else:
        assignment = Assignment.objects.get(id=id)
        submissions = AssignmentSubmission.objects.filter(assignment=assignment).all()
        template = loader.get_template('assignments/assignment_submission_list.html')
        ticks = range(0, assignment.marks + 1, int(assignment.marks/10))
        context = {
            'assignment': assignment,
            'submissions': submissions,
            'ticks': ticks
        }
        return HttpResponse(template.render(context, request))

# Assignment submission deadlines
def get_deadlines(assignments):
    assignment_list = []
    for assignment in assignments:
        assignment_list.append({
            'name': assignment['title'],
            'description': assignment['content'],
            'club': Course.objects.get(id=assignment['course_id']).name,
            'year': assignment['deadline'].year,
            'month': assignment['deadline'].month,
            'day': assignment['deadline'].day,
            'hour': assignment['deadline'].hour,
            'minute': assignment['deadline'].minute,
            'duration': None,
        })
    return {
        'events': assignment_list
    }
