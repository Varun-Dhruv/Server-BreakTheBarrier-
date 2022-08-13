from rest_framework import serializers
from . models import CustomUser
import re

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username','password','gender']
        #exclude = ['password']       
                # todo_title = validated_data['todo_title']
                # regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
                # if not regex.search(todo_title) == None:
                #     raise serializers.ValidationError(
                #         "todo_title cannot contain special character")
