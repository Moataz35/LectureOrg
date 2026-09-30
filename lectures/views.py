from rest_framework.generics import RetrieveAPIView, ListAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView,  RetrieveUpdateDestroyAPIView, RetrieveDestroyAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import *
from .serializers import *
from .permissions import *

# Courses
# Operations: CRUD
# Endpoints: '/courses/', '/courses/<course_id>/'
# Permissions: Only the professor and admin can make Create, Update, Delete operations. Students can do Read operations
class CoursesListView(ListAPIView):
    """A view to get all courses details with GET Method"""
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

class CourseDetailsView(RetrieveAPIView):
    """A view to get a specific course details with GET Method"""
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

class CourseUpdateView(UpdateAPIView):
    """A simple view to update Course details using PUT/PATCH Methods"""
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedAdmin | IsAuthenticatedProfessor]

class CourseDeleteView(DestroyAPIView):
    """A simple view to delete a Course using DELETE Method"""
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedAdmin | IsAuthenticatedProfessor]

class CourseCreateView(CreateAPIView):
    """A simple view to create new Courses using POST Methods"""
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedAdmin | IsAuthenticatedProfessor]

# Links
# Operations: CRD
# Endpoints: '/courses/<course_id>/lectures/<lecture_id>/links/', '/courses/<course_id>/lectures/<lecture_id>/links/<link_id>'
# Permissions: Only the professor and admin can add links
class LinkListView(ListAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedProfessor | IsAuthenticatedAdmin]

class LinkDetailsView(RetrieveAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

class LinkDeleteView(DestroyAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedProfessor | IsAuthenticatedAdmin]

# Notes
# Operations: CRUD
# Endpoints: '/lectures/<lecture_id>/notes/', 'lectures/<lecture_id>/notes/<note_id>/'
# Permissions: Any one can create notes, but the student can only show his notes and the professor notes. 
# The student can't show/edit/delete another student notes.
class NoteListView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, lecture_id):
        user_id = request.user.id
        user_notes = Note.objects.filter(user_id_id=user_id, user_id__role=Role.PROFESSOR, lecture_id=lecture_id)
        serializer = NoteSerializer(instance=user_notes, many=True)
        return Response(serializer.data)

    def post(self, request, lecture_id):
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            title = serializer.validated_data['title']
            content = serializer.validated_data['content']
            lecture = get_object_or_404(Lecture, id=lecture_id)
            new_note = Note(
                        title= title,
                        content= content,
                        user_id= request.user.id,
                        lecture_id= lecture
                      )
            new_note.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class NoteRetrieveEditView(RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsOwner]

# Lectures
# Operations: CRUD
# Endpoints: '/courses/<course_id>/lectures/', '/courses/<course_id>/lectures/<lecture_id>/'
# Permissions: Only the professor and admin can make Create, Update, Delete operations. Students can do Read operations
class LectureCreateView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedAdmin | IsAuthenticatedProfessor]

    def get(self, request, course_id):
        course = get_object_or_404(Course, id=course_id)
        lectures = Lecture.objects.filter(course_id=course)
        serializer = LectureSerializer(lectures, many=True)
        return Response(serializer.data)

    def post(self, request, course_id):
        serializer = LectureSerializer(data=request.data)
        if serializer.is_valid():
            course = get_object_or_404(Course, id=course_id)
            links_list = serializer.validated_data.pop('link_ids', [])
            file = serializer.validated_data.pop('slides')

            lecture = Lecture.objects.create(course_id=course, **serializer.validated_data)
            lecture.link_ids.set(links_list)
            lecture.slides = file
            lecture.save()

            new_serializer = LectureSerializer(lecture)
            return Response(new_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LectureUpdateDeleteView(RetrieveDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedAdmin | IsAuthenticatedProfessor]
