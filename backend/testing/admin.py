from django.contrib import admin

from .models import Question, Test, Answer, Suite, TestSuite

admin.site.register(Test)
admin.site.register(Question)
admin.site.register(Answer)

class SuitToTestSuite(admin.TabularInline):
	model = TestSuite
	extra = 1

class SuiteAdmin(admin.ModelAdmin):
	inlines = (SuitToTestSuite, )

# class TestAdmin(admin.ModelAdmin):
	# inlines = (SuitToTestSuite, )


admin.site.register(Suite, SuiteAdmin)
