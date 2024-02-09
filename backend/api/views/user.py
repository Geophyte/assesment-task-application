from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from ..models import CustomUser
from ..serializers.user import UserSerializer
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from ..forms import UserLoginForm, UserRegistrationForm, UserLogoutForm
from ..permissions import IsAuthenticated, IsUnauthenticated, AuthenticatedUserCanReadAndModify


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [AuthenticatedUserCanReadAndModify]

    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


@api_view(['GET', 'POST'])
@permission_classes([IsUnauthenticated])
def register(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(user.password)
            print(f"register: {user.username}, {user.password}")
            user.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        form = UserRegistrationForm()
        return render(request, 'register.html', {'form': form})


@api_view(['GET', 'POST'])
@permission_classes([IsUnauthenticated])
def login_user(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')
        print(f"login: {username}, {password}")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return Response(status=status.HTTP_200_OK)
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    else:
        form = UserLoginForm()
        return render(request, 'login.html', {'form': form})


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def logout_user(request):
    if request.method == 'POST':
        logout(request)
        return Response(status=status.HTTP_200_OK)
    else:
        form = UserLogoutForm()
        return render(request, 'logout.html', {'form': form})
