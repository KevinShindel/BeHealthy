import json
from time import sleep

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View

from home.models import Questions
from home.utils import define_expression, set_up_expression


class HomeView(View):

    def get(self, request):
        return render(request, 'home.html')

    def post(self, request):

        data = {
            'systolic_bp': int(request.POST.get('sys_bp', '0')),
            'diastolic_bp': int(request.POST.get('dias_bp', '0')),
            'gender': request.POST.get('sex', ''),
            'age': int(request.POST.get('age', '0')),
            'abdominal_pain': True if request.POST.get('abd_pain', '') == 'on' else False
        }
        missed_params = define_expression(data)
        data['response'] = []
        rules_query = Questions.objects.all()
        for missed_param in missed_params:
            rules_query = rules_query.exclude(expression__icontains=missed_param)
        rules = rules_query.all()
        for rule in rules:
            if set_up_expression(parameters=data, expression_dict=rule.rule):
                data['response'].append({'question': rule.ask_question})
        sleep(1)
        return HttpResponse(json.dumps(data))
