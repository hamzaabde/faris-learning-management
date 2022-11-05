from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from . import views

user_routes = [
    path('', views.Account.as_view(), name='account'),
    path('courses/', views.UserCourses.as_view(), name='user_courses'),
    path('users/', views.Users.as_view(), name="users"),
    path('course/<int:pk>/users/',
         views.CourseUsersList.as_view(), name="course_users"),
    path('register/course/<int:pk>/',
         views.RegisterCourse.as_view(), name='register_course'),
    path('unregister/course/<int:pk>/',
         views.UnregisterCourse.as_view(), name='unregister_course'),
]

course_routes = [
    path('add/', views.AddCourse.as_view(), name='add_course'),
    path('<int:pk>/edit/', views.EditCourse.as_view(), name='edit_course'),
    path('<int:pk>/delete/', views.DeleteCourse.as_view(), name='delete_course'),
]

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('login/', LoginView.as_view(template_name='base/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('account/', include(user_routes)),
    path('courses/', include(course_routes)),
]
