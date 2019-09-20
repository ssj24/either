from .models import Question, Answer
import random

def add_variable_to_context(request):
    random_question = Question.objects.order_by('?').first
    return {
        'random': random_question,
    }