from django.db import models

class StudyCenter(models.Model):
    name = models.CharField('Name', max_length=30)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    fullname = models.CharField(max_length=30)
    about = models.TextField()
    experinece = models.CharField(max_length=30)
    study_center = models.ForeignKey(StudyCenter, on_delete=models.CASCADE, blank=True, null=True)
    phone_number = models.CharField(max_length=30)

    def __str__(self):
        return self.fullname
    
class Student(models.Model):
    fullname = models.CharField(max_length=30)
    about = models.TextField()
    phone_number = models.CharField(max_length=30)
    study_center = models.ForeignKey(StudyCenter, on_delete=models.CASCADE, blank=True, null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.fullname
    