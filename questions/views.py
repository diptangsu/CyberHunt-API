from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from .models import Question, File, Image


def question(request, question_id):
    ques = get_object_or_404(Question, id=question_id)

    images = Image.objects.filter(question_id=ques.id)
    files = File.objects.filter(question_id=ques.id)

    image_urls = [{'image': image.image.url} for image in images]
    file_urls = [{'file': file.file.url} for file in files]

    ques = vars(ques)
    ques.pop('_state')
    ques.pop('answer')

    ques['images'] = image_urls
    ques['files'] = file_urls

    return JsonResponse(ques)


def leaderboard(request):
    pass


def all_questions(request):
    questions = Question.objects.all()

    data = {
        'questions': []
    }
    for ques in questions:
        q = vars(ques)
        q.pop('_state')
        q.pop('answer')
        q.pop('body')
        data['questions'].append(q)

    return JsonResponse(data)
