from django.shortcuts import render
from django.http import JsonResponse
from .models import Student
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
import json

# Create your views here.

@method_decorator(csrf_exempt, name='dispatch')
class StudentView(View):
    def get(self, request):
        students = list(Student.objects.values())
        return JsonResponse({'students': students})
    
    def post(self, request):
        data = json.loads(request.body)
        student = Student.objects.create(
            name=data['name'],
            address=data['address']
        )
        return JsonResponse({
            'id': student.id,
            'name': student.name,
            'address': student.address
        })

def student_list(request):
    if request.method == 'GET':
        students = Student.objects.all()
        data = [{'id': s.id, 'name': s.name, 'address': s.address} for s in students]
        return JsonResponse({'students': data})
