from rest_framework.generics import RetrieveAPIView, ListAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView, ListCreateAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
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
# Endpoints: '/courses/<course_id>/lectures/<lecture_id>/notes/', '/courses/<course_id>/lectures/<lecture_id>/notes/<note_id>/'
# Permissions: Any one can create notes, but the student can only show his notes and the professor notes. The student can't show another student notes.

# Lectures
# Operations: CRUD
# Endpoints: '/courses/<course_id>/lectures/', '/courses/<course_id>/lectures/<lecture_id>/'
# Permissions: Only the professor and admin can make Create, Update, Delete operations. Students can do Read operations
