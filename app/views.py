from django.shortcuts import render
from .models import *

# Create your views here.

def task_record(request):
    task_records = TaskCompletionRecord.objects.all()
    return render(request, 'records.html', {'task_records': task_records})
