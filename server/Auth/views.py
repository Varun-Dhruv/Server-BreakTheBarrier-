from django.shortcuts import render
from .models import CustomUser, User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from .serializers import UserSerializer
from django.contrib.auth.hashers import check_password


def function(input_list):
    my_dict = dict()
    for item in input_list:
        my_dict[item[0]] = item[1]

    return my_dict

@api_view(["POST"])
def Signup(request):
    try:
        data = request.data
        # print(data)
        data["password"] = make_password(data["password"])
        serializer = UserSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': True, 'message': "Done Fetched"
            })
    except Exception as e:
        print(e)
        return Response({
            'status': False,
            'message': 'Something went wrong'
        })


@api_view(["POST"])
def Login(request):
    try:
        data = request.data
        obj = CustomUser.objects.filter(username=data['username']).values()
        if obj:
            serializer = UserSerializer(obj,many=True)
            user=list(serializer.data[0].items())
            password = check_password(
                data["password"], user[1][1])
            data=function(user)
            data['password']=""
            if password:
                return Response({
                    'status': True,
                    'message': 'Valid Credentials',
                    'data':data,
                })
            else:
                return Response({
                    'status': False,
                    'message': 'InValid Credentials'
                })
                
        else:
            return Response({
                'status': False,
                'message': 'InValid Credentials'
            })

    except Exception as e:
        print(e)
        return Response({
            'status': False,
            'message': 'Something went wrong'
        })
# Create your views here.
