from django import forms
from . import models

class TaskRecordForm(forms.Form):
    task = forms.ModelChoiceField(
        queryset=models.Task.objects.all(),
        empty_label="Add new task"
    )
    