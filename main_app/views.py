from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from django.contrib.auth.models import User
from .serializers import UserSerializer

class UserApi(APIView):

    permission_classes = [permissions.AllowAny,]
    
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response({'data': serializer.data})

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        try:
            user = User.objects.create_user(username=username)
            user.set_password(password)
            return Response({'status': 'OK'})
        except:
            return Response({'status': 'Error'})


class UserDetailApi(APIView):

    permission_classes = [permissions.AllowAny,]

    def get(self, request, pk):
        user = User.objects.filter(pk=pk)
        serializer = UserSerializer(user, many=True)
        return Response({'data': serializer.data})

    def put(self, request, pk):
        username = request.data.get('username')
        try:
            user = User.objects.filter(pk=pk)
            user.update(username=username)
            return Response({'status': 'OK'})
        except:
            return Response({'status': 'Error'})

    def delete(self, request, pk):
        try:
            user = User.objects.filter(pk=pk)
            user.delete()
            return Response({'status': 'OK'})
        except:
            return Response({'status': 'Error'})
