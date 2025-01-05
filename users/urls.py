from django.urls import path
from .views import CreateUserView, ProtectedView, TokenView

urlpatterns = [
    path('register/', CreateUserView.as_view(), name='register'),
    path('protected/', ProtectedView.as_view(), name='protected'),
    path('token/', TokenView.as_view(), name='token'),
]
