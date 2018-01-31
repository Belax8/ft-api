"""
ft_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls import url

from rest_framework_signature import views as authentication_views

from ft_api.exercise.views import ExerciseHandler
from ft_api.exercise_type.views import ExerciseTypeHandler
from ft_api.fitness_plan.views import FitnessPlanHandler
from ft_api.fitness_plan_type.views import FitnessPlanTypeHandler
from ft_api.user.views import UserHandler

urlpatterns = [
    url(r'^auth/login$', authentication_views.obtain_auth_token, name='login'),

    url(r'^(?P<parent_resource>[a-zA-z]+)/(?P<parent_pk>[0-9]+)/exercises', ExerciseHandler.as_view()),
    url(r'^(?P<parent_resource>[a-zA-z]+)/(?P<parent_pk>[0-9]+)/fitnessPlans', FitnessPlanHandler.as_view()),
    url(r'^exercises/(?P<pk>[0-9]+)$', ExerciseHandler.as_view()),
    url(r'^exercises$', ExerciseHandler.as_view()),
    url(r'^exerciseTypes/(?P<pk>[0-9]+)$', ExerciseTypeHandler.as_view()),
    url(r'^exerciseTypes$', ExerciseTypeHandler.as_view()),
    url(r'^fitnessPlans/(?P<pk>[0-9]+)$', FitnessPlanHandler.as_view()),
    url(r'^fitnessPlans$', FitnessPlanHandler.as_view()),
    url(r'^fitnessPlanTypes/(?P<pk>[0-9]+)$', FitnessPlanTypeHandler.as_view()),
    url(r'^fitnessPlanTypes$', FitnessPlanTypeHandler.as_view()),
    url(r'^users/(?P<pk>[0-9]+)$', UserHandler.as_view()),
    url(r'^users$', UserHandler.as_view())

]
