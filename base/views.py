from django.shortcuts import render
from django.urls.base import reverse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from django.db.models import Sum

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from.models import Workout

class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('workouts')




# Create your views here.
class WorkoutList(LoginRequiredMixin, ListView):
    model = Workout
    context_object_name = 'workouts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['workouts'] = context['workouts'].filter(user = self.request.user)
        return context


class WorkoutDetails(DetailView):
    model = Workout
    context_object_name = 'workout'
    template_name = 'base/workout.html'


class WorkoutCreate(LoginRequiredMixin, CreateView):
    model = Workout
    fields = ['title', 'instructions','mileage', 'race_type']
    success_url = reverse_lazy('workouts')
    template_name = 'base/create-workout.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(WorkoutCreate, self).form_valid(form)

class WorkoutUpdate(LoginRequiredMixin, UpdateView):
    model = Workout
    fields = ['title', 'instructions','mileage', 'race_type']
    success_url = reverse_lazy('workouts')
    template_name = 'base/update-workout.html'

class WorkoutDelete(LoginRequiredMixin, DeleteView):
    model = Workout
    template_name= 'base/delete-workout.html'
    success_url = reverse_lazy('workouts')

class CreateAccount(FormView):
    template_name = 'base/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('workouts')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(CreateAccount, self).form_valid(form)


    