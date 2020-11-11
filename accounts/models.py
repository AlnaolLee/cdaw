from django.db import models

class CourseModel(models.Model):
    fName = models.CharField(null=True, max_length=250)
    lName = models.CharField(null=True, max_length=250)
    advisorName = models.CharField(null=True, max_length=250)

    gradeYear = models.CharField(choices = [('9', '9'), ('10', '10'),
                                             ('11', '11'), ('12', '12')]
                                             , null=True, max_length=2
                                             )

    addCourse = models.CharField(null=True, max_length=250)
    addCourseBlock = models.CharField(choices = [('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'),
                                                  ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H')],
                                                  null=True, max_length=250)
    addCourseTerm = models.CharField(choices = [('Sem1', 'Sem1'), ('Sem2', 'Sem2'),
                                                ('Yearly', 'Yearly'), ('Fall', 'Fall'),
                                                ('Winter', 'Winter'), ('Spring', 'Spring')], null=True, max_length=250)

    dropCourse = models.CharField(null=True, max_length=250)
    dropCourseBlock = models.CharField(choices = [('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'),
                                                  ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H')],
                                                  null=True, max_length=250)
    dropCourseTerm = models.CharField(choices = [('Sem1', 'Sem1'), ('Sem2', 'Sem2'),
                                                ('Yearly', 'Yearly'), ('Fall', 'Fall'),
                                                ('Winter', 'Winter'), ('Spring', 'Spring')], null=True, max_length=250)

class availableCourses(models.Model):
    coursename = models.CharField(null=True, max_length=250)
    courseid = models.CharField(max_length=250)
    coursecredit = models.CharField(max_length=250)
    courseblock = models.CharField(null=True,max_length=250)
    isavailable = models.CharField(default="yes", max_length=250)






    # def save(self, *args, **kwargs):
    #     print("CourseModel: save: self.addCourse:", self.addCourse)
    #     super(CourseModel, self).save(*args, **kwargs)

    # def set_addCourse(self, dataValue):
    #     self.addCourse = dataValue
    #     print("CourseModel", dataValue)

    # @property
    # def addCourse(self):
    #     print("CourseModel: addCourse.")
    #     return self._addCourse

    # @addCourse.setter
    # def addCourse(self, dataValue):
    #     # self._addCourse = dataValue
    #     self._addCourse = "something"
    #     print("CourseModel", dataValue)

    # def get_addCourse(self):
    #     print("CourseModel: get_addCourse.")
    #     return self._addCourse

    # def set_addCourse(self, dataValue):
    #     self._addCourse = "something"
    #     print("CourseModel", dataValue)

    # addCourse = property(get_addCourse, set_addCourse)
