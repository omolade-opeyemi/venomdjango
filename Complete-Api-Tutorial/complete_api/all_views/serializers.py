from .models import Question
from rest_framework import serializers

class QuestionSerializer(serializers.ModelSerializer):
    created_by = serializers.CharField(read_only=True)
    class Meta:
        model = Question
        fields = ['id','created_by','title','status','start_date','end_date']
