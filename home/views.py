import json
import os
from time import sleep

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.generic import View
from home.models import Questions



class HomeView(View):

    def get(self, request):
        return render(request, 'home.html')

    def post(self, request):
        # GET DATA VALUES
        gender = request.POST.get('sex', '')
        age = int(request.POST.get('age', '0'))
        abdominal_pain = request.POST.get('abd_pain', '')
        systolic_bp = int(request.POST.get('sys_bp', '0'))
        diastolic_bp = int(request.POST.get('dias_bp', '0'))

        data = []

        female = 0
        if gender == 'female':
            female = 1

        if abdominal_pain:
            data.append(Questions.objects.get(id=1).tojson())

        if female and age > 45:
            data.append(Questions.objects.get(id=2).tojson())

        if systolic_bp > 140 or diastolic_bp < 90:
            data.append(Questions.objects.get(id=3).tojson())

        sleep(1)
        return HttpResponse(json.dumps(data))
