from rest_framework import serializers
from testing.models import Question, Answer, Test


class AnswerSerializer(serializers.ModelSerializer):
	# Set 'correct' to False in all answers to send
	def to_representation(self, obj):
		return {
			'id': obj.id,
			'text': obj.text,
			'correct': False
		}

	class Meta:
		model = Answer
		fields = ('id', 'text', 'correct')

class QuestionSerializer(serializers.ModelSerializer):
	answers = AnswerSerializer(many=True)

	class Meta:
		model = Question
		fields = ('id', 'text', 'name', 'time_second', 'answers')

class TestSerializer(serializers.ModelSerializer):
	class Meta:
		model = Test
		fields = ('id', 'name', 'text')
