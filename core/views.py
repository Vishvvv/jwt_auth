from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .permissions import IsTeacher, IsStudent
from .serializers import RegisterSerializer
from rest_framework import status
from rest_framework.permissions import AllowAny

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        print("Received data:", request.data)
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User created successfully!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TeacherView(APIView):
    permission_classes = [IsAuthenticated, IsTeacher]

    def get(self, request):
        return Response({"message": "Welcome Teacher!"})

class StudentView(APIView):
    permission_classes = [IsAuthenticated, IsStudent]

    def get(self, request):
        return Response({"message": "Welcome Student!"})