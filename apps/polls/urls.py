from django.urls import path

from . import views

urlpatterns = [
    path("questions/", views.get_questions, name="questions"),
    path("questions/<int:id>/", views.get_question, name="question"),
    path("questions/<int:id>/vote/", views.vote, name="vote"),
]
