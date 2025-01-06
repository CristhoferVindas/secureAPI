from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.throttling import UserRateThrottle
from .serializers import UserSerializer
from .models import User

class CreateUserView(APIView):
    throttle_classes = [UserRateThrottle]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"message": "User created successfully!"}, status=201)
        return Response(serializer.errors, status=400)

class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": "This is a protected view!"})

class TokenView(APIView):
    throttle_classes = [UserRateThrottle]

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        if not email or not password:
            return Response({"error": "Email and password are required"}, status=400)
        try:
            user = User.objects.get(email=email)
            if user.check_password(password):
                refresh = RefreshToken.for_user(user)
                return Response({
                    'access': str(refresh.access_token),
                    'refresh': str(refresh),
                })
            else:
                return Response({"error": "Invalid credentials"}, status=400)
        except User.DoesNotExist:
            return Response({"error": "Invalid credentials"}, status=400)
