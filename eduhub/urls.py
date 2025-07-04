from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from core.views import RegisterView, TeacherView, StudentView, getUsers

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('teacher/', TeacherView.as_view(), name='teacher-view'),
    path('student/', StudentView.as_view(), name='student-view'),
    path('get-users/', getUsers.as_view(), name='user-list'),
]
