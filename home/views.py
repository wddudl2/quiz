from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import *
import random
import json



def home(request):
    
    context = {'categories' : Category.objects.all}
    return render(request, 'home.html' ,context)


def get_quiz(request):
    try:
        question_objs = list(Question.objects.all())
        data = []

        random.shuffle(question_objs)

        for question_obj in question_objs:
            data.append({
                "category": question_obj.category.category_name,
                "question": question_obj.question,
                "marks": question_obj.marks,
            })

        # Convert the data list to a string before passing it to the payload dictionary.
        data = json.dumps(data)
        payload = {'status': True, 'data': data}
        return JsonResponse(payload)

    except Exception as e:
        print(e)
        return HttpResponse("something wrong")
