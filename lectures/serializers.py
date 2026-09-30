from .models import *
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = ['name']

class NoteSerializer(ModelSerializer):
    class Meta:
        model = Note
        fields = ['title', 'content']

class LectureSerializer(ModelSerializer):
    link_ids = serializers.PrimaryKeyRelatedField(many=True, queryset=Link.objects.all())
    class Meta:
        model = Lecture
        fields = ['title', 'description', 'professor_name', 'slides', 'link_ids']

class LinkSerializer(ModelSerializer):
    class Meta:
        model = Link
        fields = ['url']
