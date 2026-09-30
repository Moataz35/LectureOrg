from django.db import models
from authentication.models import CustomUser

def create_lecture_path(instance, name):
    return f"lectures/lecture{instance.id}.pptx"

class Course(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Link(models.Model):
    url = models.URLField()

    def __str__(self):
            return self.url

class Lecture(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    professor_name = models.CharField(max_length=50)
    slides = models.FileField(upload_to=create_lecture_path)
    course_id = models.ForeignKey(Course, models.CASCADE, related_name='lectures')
    link_ids = models.ManyToManyField(Link, related_name='lectures', null=True, blank=True)

    def __str__(self):
        return self.title
    
class Note(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='notes')
    lecture_id = models.ForeignKey(Lecture, on_delete=models.CASCADE, related_name='notes')

    def __str__(self):
        return self.title
