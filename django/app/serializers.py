from rest_framework import serializers
from .models import TaskCompletionRecords

class TaskRecordsSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TaskCompletionRecords
        fields = '__all__'