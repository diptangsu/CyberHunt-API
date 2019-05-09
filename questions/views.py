from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from .models import Question, File, Image, Submission
from teams.models import Team


def question(request, question_id):
    this_question = get_object_or_404(Question, id=question_id)

    if request.method == 'GET':

        images = Image.objects.filter(question_id=this_question.id)
        files = File.objects.filter(question_id=this_question.id)

        image_urls = [{'image': image.image.url} for image in images]
        file_urls = [{'file': file.file.url} for file in files]

        ques = vars(this_question)
        ques.pop('_state')
        ques.pop('answer')

        ques['images'] = image_urls
        ques['files'] = file_urls

        return JsonResponse(ques)
    elif request.method == 'POST':
        answer = request.POST.get('answer', None)
        team_id = 1
        try:
            team = Team.objects.get(team_id=team_id)
        except Team.DoesNotExist:
            return JsonResponse({'error': 'Team does not exist'})

        points = 0

        try:
            Submission.objects.get(team_id=team_id, question_id=this_question.id)
            message = 'You have already answered this question'
        except Submission.DoesNotExist:
            if answer == this_question.answer:
                points = this_question.points
                message = f'Congratulations! You get {this_question.points} points!'

                submission = Submission()
                submission.question = this_question
                submission.team = team
                submission.save()
            else:
                message = 'Wrong answer! Try again!'

        data = {
            'points': points,
            'message': message
        }

        return JsonResponse(data)
    else:
        return JsonResponse({'error': 'Invalid parameters'})


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
