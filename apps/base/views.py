from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, RedirectView, UpdateView, DeleteView
from .models import User, Course
from .forms import UserRegistrationForm


class Home(ListView):
    template_name = "base/home.html"
    model = Course
    context_object_name = "courses"


class RegisterUser(CreateView):
    template_name = 'base/register.html'
    model = User
    # form_class = UserRegistrationForm
    fields = ('username', 'password')
    success_url = reverse_lazy('account')


class RegisterCourse(RedirectView):
    permanent = True

    def get_redirect_url(self, pk, *args, **kwargs):
        user = self.request.user

        if user.is_anonymous:
            return reverse('register')

        course = get_object_or_404(Course, id=pk)
        user.courses.add(course)

        return reverse('account')


class UnregisterCourse(RedirectView):
    permanent = True

    def get_redirect_url(self, pk, *args, **kwargs):
        user = self.request.user
        course = get_object_or_404(Course, id=pk)
        user.courses.remove(course)

        return reverse('account')


class Account(ListView):
    template_name = 'base/account.html'
    model = Course
    context_object_name = "courses"


class UserCourses(Account):
    def get_queryset(self):
        user = self.request.user

        if user.is_authenticated:
            return user.courses.all()


class AddCourse(CreateView):
    model = Course
    fields = "title",
    success_url = reverse_lazy('account')


class EditCourse(UpdateView):
    template_name = "base/course_form.html"
    model = Course
    fields = "title",
    success_url = reverse_lazy('account')


class DeleteCourse(DeleteView):
    template_name = "base/confirm_delete.html"
    model = Course
    success_url = reverse_lazy('account')


class Users(ListView):
    template_name = "base/users.html"
    model = User
    context_object_name = "users"


class CourseUsersList(Users):

    def get_queryset(self):
        course = get_object_or_404(Course, id=self.kwargs.get('pk'))

        return course.users.all()
