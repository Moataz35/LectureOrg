from .models import *
from rest_framework.serializers import ModelSerializer

class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = ['name']

class NoteSerializer(ModelSerializer):
    class Meta:
        model = Note
        fields = ['title', 'content']

class LectureSerializer(ModelSerializer):
    class Meta:
        model = Lecture
        fields = ['title', 'description', 'professor_name', 'slides']

class LinkSerializer(ModelSerializer):
    class Meta:
        model = Link
        fields = ['url']
