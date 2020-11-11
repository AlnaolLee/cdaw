from django import forms
from django.contrib.auth import (
    authenticate,
    get_user_model
)
from .models import CourseModel


User = get_user_model()

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget = forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username = username, password = password)
            if not user:
                raise forms.ValidationError('This user does not exist')
            if not user.check_password(password):
                raise forms.ValidationError('Incorrect Password')
            if not user.is_active:
                raise forms.ValidationError('This user is not active')
        return super(UserLoginForm, self).clean(*args, **kwargs)


class UserRegisterForm(forms.ModelForm):
    email = forms.EmailField(label = 'Email Address')
    email2 = forms.EmailField(label = 'Confirm Email')
    password = forms.CharField(widget = forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'email2',
            'password',
        ]

    def clean_email(self):
        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')
        if email != email2:
            raise forms.ValidationError("emails must match")
        email_qs = User.objects.filter(email = email)
        if email_qs.exists():
            raise forms.ValidationError(
                "This email is already being used"
            )
        return email

class CourseChangeForm (forms.ModelForm):
    class Meta:
        model = CourseModel

        # fields = "__all__"
        fields = [
            "fName",
            "lName",
            "advisorName",
            "gradeYear"
        ]

        labels = {
            "fName" : "Enter your first name",
            "lName" : "Enter your last name",
            "advisorName" : "Enter your advisor name",
            "gradeYear" : "Choose your year",
            # "addCourse" : "Course to Add",
            # "addCourseBlock" : "Block",
            # "addCourseTerm" : "Term",
            # "dropCourse" : "Course to Drop",
            # "dropCourseBlock" : "Block",
            # "dropCourseTerm" : "Term"
        }

        # exclude = []

    addCourse = forms.CharField(max_length=250, label="Course to Add")
    addCourseBlock = forms.ChoiceField(choices = [('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'),
                                                  ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H')],
                                        label="Block"
    )
    addCourseTerm = forms.ChoiceField(choices = [('Sem1', 'Sem1'), ('Sem2', 'Sem2'),
                                                ('Yearly', 'Yearly'), ('Fall', 'Fall'),
                                                ('Winter', 'Winter'), ('Spring', 'Spring')],
                                        label="Term"
    )

    dropCourse = forms.CharField(max_length=250, label="Course to Drop")
    dropCourseBlock = forms.ChoiceField(choices = [('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'),
                                                  ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H')],
                                        label="Block"
    )
    dropCourseTerm = forms.ChoiceField(choices = [('Sem1', 'Sem1'), ('Sem2', 'Sem2'),
                                                ('Yearly', 'Yearly'), ('Fall', 'Fall'),
                                                ('Winter', 'Winter'), ('Spring', 'Spring')],
                                        label="Term"
    )

    # Custom saving to make sure the locally created fields above get correctly mapped over to the model before saving the model.
    def save(self, commit=True):
        course_form = super(CourseChangeForm, self).save(commit=False)

        course_form.addCourse = self.addCourse
        course_form.addCourseBlock = self.addCourseBlock
        course_form.addCourseTerm = self.addCourseTerm

        course_form.dropCourse = self.dropCourse
        course_form.dropCourseBlock = self.dropCourseBlock
        course_form.dropCourseTerm = self.dropCourseTerm

        if commit: course_form.save()
        return course_form

    # Custom processing to combine multiple values in the POST into a single comma-delimited value, before saving the form.
    def customStuff(self, incoming):
        # print('CourseChangeForm: customStuff: incoming:', incoming)
        self.addCourse = ",".join(incoming.getlist('addCourse'))
        # print('CourseChangeForm: customStuff: addCourse:', self.addCourse)
        self.addCourseBlock = ",".join(incoming.getlist('addCourseBlock'))
        self.addCourseTerm = ",".join(incoming.getlist('addCourseTerm'))

        self.dropCourse = ",".join(incoming.getlist('dropCourse'))
        self.dropCourseBlock = ",".join(incoming.getlist('dropCourseBlock'))
        self.dropCourseTerm = ",".join(incoming.getlist('dropCourseTerm'))
