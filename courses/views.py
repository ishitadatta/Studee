from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader
from django.contrib import messages, auth

from .models import *
from .forms import CourseCreateForm
from authentication.models import Account

# Create your views here.


# # VIEW FOR COURSE LIST
@login_required
def CourseView(request):
    if request.method == 'POST':
        if 'delete-course' in request.POST:
            Course.objects.filter(id=request.POST['delete-course']).delete()
            messages.success(request, f'Your course has been delete')
        if 'enroll-course' in request.POST:
            enroll = EnrolledCourse(course_id=request.POST['enroll-course'], student_id=request.user.username)
            course = Course.objects.get(id=request.POST['enroll-course'])
            messages.success(request, f"You have been enrolled into {course.name}. You have earned {course.credits} credits")
            enroll.save()
        if 'withdraw-course' in request.POST:
            course = Course.objects.get(id=request.POST['withdraw-course'])
            EnrolledCourse.objects.filter(course_id=request.POST['withdraw-course'], student_id=request.user.username).delete()
            messages.warning(request, f"You have withdrawn from {course.name}. {course.credits} credits deducted")
        return redirect('courses:home')
    else:
        courses = Course.objects.all().order_by('id')
        enrolled = list(EnrolledCourse.objects.filter(
            student__username=request.user.username).values_list('course__id', flat=True))
        context = {
            'courses': courses,
            'enrolled': enrolled
        }
        template = loader.get_template('courses.html')
        return HttpResponse(template.render(context, request))


# COURSE CREATE VIEW
@login_required
def CourseCreateView(request, id=None):
    context = {}
    if request.POST:
        form = CourseCreateForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course_change = "created"
            if request.POST['create-course'] != "None":
                course.id = request.POST['create-course']
                course_change = "updated"
            course.faculty = Account.objects.get(username=request.user.username)
            course.save()
            messages.success(request, f'Your course has been {course_change} successfully!')
            return redirect('courses:home')
    else:
        template = loader.get_template('course_create.html')
        form = CourseCreateForm()
        if id is not None:
            course = Course.objects.get(id=id)
            form = CourseCreateForm(
                initial={
                    'name': course.name,
                    'description': course.description,
                    'credits': course.credits,
                }
            )
        context = {
            # 'title': 'New Assignment',
            'create_form': form,
            "id": id
        }
        return HttpResponse(template.render(context, request))