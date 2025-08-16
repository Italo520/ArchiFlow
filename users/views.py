from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import Profile
from .serializers import UserRegistrationSerializer, ProfileSerializer

class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = (AllowAny,)

class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user.profile