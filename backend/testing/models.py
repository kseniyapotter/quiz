from django.db import models


class Test(models.Model):
	"""Test - model with informations about test"""
	name = models.CharField(max_length=200)
	text = models.TextField()

	def __str__(self):
		return self.name

class Question(models.Model):
	"""Question - model with questions"""
	name = models.CharField(max_length=200)
	text = models.TextField()
	time_second = models.IntegerField(default=180)
	test = models.ForeignKey(Test, on_delete=models.CASCADE)

	def __str__(self):
		return self.name

	def get_answers(self):
		answers = Answer.objects.filter(question=self.id)
		for answer in answers:
			yield answer

	def get_right_answers_id(self):
		return Answer.objects.filter(question=self.id, correct=True).values_list('id', flat = True)

class Answer(models.Model):
	"""Answer - model with answers"""
	question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
	text = models.TextField()
	correct = models.BooleanField()

	def __str__(self):
		return 'Ответ к %s' % self.question.name

class Suite(models.Model):
	"""Suite - model with informations about suites"""
	name = models.CharField(max_length=200)
	text = models.TextField()

	def __str__(self):
		return self.name
		
class TestSuite(models.Model):
	"""TestSuite - model with suites of tests"""
	suite = models.ForeignKey(Suite, on_delete=models.CASCADE)
	test = models.ForeignKey(Test, on_delete=models.CASCADE) #TODO

	def __str__(self):
		return '%s - %s' % (self.suite.name, self.test.name)

#TODO Add save test results
class UserTestResult(models.Model):
	"""UserTestResult - model with tests results"""
	user_id = models.IntegerField()
	test = models.ForeignKey(Test, on_delete=models.CASCADE)
	result = models.CharField(max_length=200)
	time = models.DateTimeField(auto_now_add=True)

	class META:
		ordering = ('time', )