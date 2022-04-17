from urllib.request import Request
from django.http import HttpResponse
from rest_framework import viewsets
from polls.models import Question
from drfpolls.serializers import QuestionSerializer
from rest_framework.decorators import action


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    @action(detail=True, methods=["post"])
    def vote(self, request: Request, *args, **kwargs):
        question = self.get_object()
        choice_id = request.data.get("choice_id")  # type: ignore
        choice = question.choices.get(id=choice_id)
        choice.votes = choice.votes
        choice.save()

        return HttpResponse(status=200)
