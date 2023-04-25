from django.contrib import admin



from .models import Question

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date', 'question_identifier')
    #admin_order_field = 'question_identifier'

admin.site.register(Question, QuestionAdmin)
