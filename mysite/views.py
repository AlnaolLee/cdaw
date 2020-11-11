from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from django.db import IntegrityError
from accounts.forms import CourseChangeForm
from accounts.models import availableCourses, CourseModel
# import json

def option(request):
    return render(request, "option.html")

# @login_required
def home(request):
    return render(request, "home.html", {})

# def avCourseList(request):
#     data = availableCourses.objects.all()
#
#     tab = {
#         "course": data
#     }
#     return render(request, "submit.html", tab)

def submissionList(request):
    list = CourseModel.objects.all()
    context = {}
    context['subList'] = list
    return render(request, "adminhome.html", context)

def courseForm(request):
    data = availableCourses.objects.filter(isavailable = "yes")
    context = {}
    context['form'] = CourseChangeForm()
    context['allCourses'] = data
    return render(request, "submit.html", context)

def thankYouForm(request):
    return render(request, "thankyou.html")

def handleForm(request):
    if request.method == 'POST':
        theForm = CourseChangeForm(request.POST)
        theForm.customStuff(request.POST)  # Some custom processing for the mutliple value fields.
        if theForm.is_valid():
            try:
                theForm.save()
                return redirect("/thankyou/")
            except IntegrityError as e:  # If any of the required fields are left out!
                return render(request, "submit.html", { 'form': theForm, 'error': str(e) })  # Only pass the exception string for development.
                # return render(request, "submit.html", { 'form': theForm })

        # print(theForm)
        # theFormString = json.dumps(request.POST)
        # print(theFormString)
        # with open('formFile', 'w') as ff:
            # ff.write(str(request.POST))
        # print(theForm.cleaned_data['addCourse'])
        # print(request.POST)
        # print(theForm.cleaned_data)

    return render(request, "submit.html")
