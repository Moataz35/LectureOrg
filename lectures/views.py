from rest_framework.generics import RetrieveUpdateDestroyAPIView, RetrieveDestroyAPIView, ListCreateAPIView
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
class CoursesListCreateView(ListCreateAPIView):
    """A view to get all courses details and create new ones with GET and POST Methods"""
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    authentication_classes = [JWTAuthentication]

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAuthenticatedAdminOrProf()]
        elif self.request.method == 'GET':
            return [IsAuthenticated()]
        return super().get_permissions()

class CourseEditRetrieveView(RetrieveUpdateDestroyAPIView):
    """A view to get a specific course details, update a course and delete a course."""
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    authentication_classes = [JWTAuthentication]

    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticated()]
        if self.request.method in ('PUT', 'PATCH', 'DELETE'):
            return [IsAuthenticatedAdminOrProf()]
        return super().get_permissions()
#=====================================================================================

class LinkListCreateView(ListCreateAPIView):
    """A class view to create a new link, and get all available links"""
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
    authentication_classes = [JWTAuthentication]

    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticated()]
        if self.request.method == 'POST':
            return [IsAuthenticatedAdminOrProf()]
        return super().get_permissions()

class LinkEditRetrieveView(RetrieveUpdateDestroyAPIView):
    """A class view to get a link details, update/delete a link"""
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
    authentication_classes = [JWTAuthentication]

    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticated()]
        if self.request.method in ('PUT', 'PATCH', 'DELETE'):
            return [IsAuthenticatedAdminOrProf()]
        return super().get_permissions()
#=====================================================================================

# Notes
# Operations: CRUD
# Endpoints: '/lectures/<lecture_id>/notes/', 'lectures/<lecture_id>/notes/<note_id>/'
# Permissions: Any one can create notes, but the student can only show his notes and the professor notes. 
# The student can't show/edit/delete another student notes.
class NoteListCreateView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, lecture_id):
        lecture = get_object_or_404(Lecture, id=lecture_id)
        user_id = request.user.id
        user_notes = Note.objects.filter(user_id_id=user_id, user_id__role=Role.PROFESSOR, lecture_id=lecture)
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
                        user_id= request.user,
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
# Endpoints: '/courses/<course_id>/lectures/', 'lectures/<lecture_id>/'
# Permissions: Only the professor and admin can make Create, Update, Delete operations. Students can do Read operations
class LectureListCreateView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedAdminOrProf]

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
            # The old serializer doesn't have link_ids and slides fields
            new_serializer = LectureSerializer(lecture)
            return Response(new_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LectureDetailsDeleteView(RetrieveDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedAdminOrProf]
