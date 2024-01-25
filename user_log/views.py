from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User,College,Games
from .serializers import UserSerializer,LoginSerializer,CollegeSerializer, GamesSerializer
from rest_framework.authtoken.models import Token
from django.db.models import Q
from rest_framework_simplejwt.tokens import RefreshToken


class SignupView(APIView):
    
    serializer_class = UserSerializer
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"data":serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)        

 
class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')
        user = User.objects.filter(Q(password=password) and Q(email=email)).first()
        return Response(status=status.HTTP_200_OK, data={
            'access': str(RefreshToken.for_user(user).access_token),
            'refresh': str(RefreshToken.for_user(user)),
            'user': {
                "name":user.name,
                "email":user.email,
                "phone":user.phone,
                "age ":user.age,
                "college":user.college,
                "password":user.password,
                'email': user.email,
                'is_active': user.is_active
            }
        })
        
class Users(APIView):
    def get(self,request):
        users = User.objects.all()
        serializer = UserSerializer(users,many=True)
        return Response(serializer.data)
    


        
class CollegeListCreateView(APIView):
    def get(self, request):
        colleges = College.objects.all()
        serializer = CollegeSerializer(colleges, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CollegeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GamesListCreateView(APIView):
    def get(self, request):
        games = Games.objects.all()
        serializer = GamesSerializer(games, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = GamesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
