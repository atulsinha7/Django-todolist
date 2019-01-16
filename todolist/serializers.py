from rest_framework import serializers
from . models import users, checklist


class userserializers(serializers.ModelSerializer):

    class Meta:
        model = users
        # fields = ('name')
        fields = '__all__'

class checklistserializers(serializers.ModelSerializer):

    class Meta:
        model = checklist
        # fields = ('taskname', 'state')
        fields = '__all__'
