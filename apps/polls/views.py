from traceback import print_stack
from django.http import HttpRequest, HttpResponse, JsonResponse
from polls.models import Question, Choice
from django.views.decorators.csrf import csrf_exempt
import json


def get_questions(request: HttpRequest):
    questions = list(Question.objects.all().order_by("id").values())
    return JsonResponse(
        questions, safe=False, json_dumps_params={"ensure_ascii": False}
    )


def get_question(request: HttpRequest, id: int):
    question = Question.objects.get(id=id)
    response = dict()
    response["id"] = question.id
    response["question_text"] = question.question_text
    response["pub_date"] = question.pub_date
    response["choices"] = list(question.choices.all().values())
    return JsonResponse(response, safe=False, json_dumps_params={"ensure_ascii": False})


@csrf_exempt
def vote(request: HttpRequest, id: int):
    choice = Choice.objects.get(
        question__id=id, id=json.loads(request.body).get("choice_id")
    )
    choice.votes += 1
    choice.save()
    return HttpResponse(status=200)
