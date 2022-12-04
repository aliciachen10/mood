from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from django.http import HttpResponse

from polls.models import Question
from polls.serializers import QuestionSerializer



# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

class QuestionViewSet(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    
