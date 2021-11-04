from django.urls import path
from django.urls.resolvers import URLPattern
from .views import CreateAccount, WorkoutCreate, WorkoutDelete, WorkoutList, WorkoutDetails, WorkoutUpdate, CustomLoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', WorkoutList.as_view(), name='workouts'),
    path('register/', CreateAccount.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name = 'login'),
    path('logout/', LogoutView.as_view(next_page = 'login'), name='logout'),
    path('workout/<int:pk>/', WorkoutDetails.as_view(), name = 'workout'),
    path('create-workout', WorkoutCreate.as_view(), name='create-workout'),
    path('update-workout/<int:pk>/', WorkoutUpdate.as_view(), name = 'update-workout'),
    path('delete-workout/<int:pk>/', WorkoutDelete.as_view(), name = 'delete-workout'),
]