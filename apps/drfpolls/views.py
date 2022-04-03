from rest_framework import viewsets

from polls.models import Question
from drfpolls.serializers import QuestionSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
