from datetime import datetime

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import *
from . import forms

# Create your views here.


def task_record(request):
    if request.method == 'POST':
        form = forms.TaskRecordForm(request.POST)
        if form.is_valid():
            TaskCompletionRecord(
                user=request.user,
                task=form.cleaned_data["task"]
            ).save()
        return redirect('task_record')
    else:
        form = forms.TaskRecordForm()
    task_records = TaskCompletionRecord.objects.all().order_by("-timestamp")
    return render(request, 'records.html', {"form": form, 'task_records': task_records})