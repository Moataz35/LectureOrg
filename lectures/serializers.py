from .models import *
from rest_framework.serializers import ModelSerializer

class NoteSerializer(ModelSerializer):
    class Meta:
        model = Note
        fields = ['title', 'content']

class LectureSerializer(ModelSerializer):
    class Meta:
        model = Lecture
        fields = ['title', 'description', 'professor_name', 'slides']
