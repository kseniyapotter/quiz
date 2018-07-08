from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from django.http import HttpResponse

from .serializers import QuestionSerializer, TestSerializer
from testing.models import Question, Test, Answer


@api_view(['GET'])
def testList(request):
    """ List all test. """
    if request.method == 'GET':
        test_list = Test.objects.all()
        serializer = TestSerializer(test_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def test(request, test_id):
    """ Return test with id = test_id. """
    try:
        test = Question.objects.filter(test = test_id)
    except Test.DoesNotExist:
        return HttpResponse(status = 404)
    serializer = QuestionSerializer(test, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['PUT'])
def result(request, test_id):
    """ Return result. """
    serializer = QuestionSerializer(data=request.data, many=True)
    if serializer.is_valid(): 
        test = Test.objects.get(pk=test_id) 
        str_result = testResult(test, request.data) 
        return Response({'text': str_result}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def testResult(test, questions_result):
    """ Calculate result. """
    right_questions_count = 0
    user_answers = {}
    # Calculate set like {quetion id = {answers id if user set it in True}}
    for question in questions_result:
        user_answers_set = set()
        for answer in question['answers']:
            if answer['correct']:
                user_answers_set.add(answer['id'])
        user_answers[question['id']] = user_answers_set

    # Calculate set with right questions from db
    right_questions = Question.objects.prefetch_related('answers').filter(test=test)
    rigth_user_answers = {}
    for question in right_questions:
        rigth_user_answers[question.id] = set(answer.id for answer in question.answers.all() if answer.correct)

    # Calculate result
    for key in user_answers.keys():
        if user_answers[key] == rigth_user_answers[key]:
           right_questions_count += 1

    return "%s from %s" % (right_questions_count, len(right_questions))


