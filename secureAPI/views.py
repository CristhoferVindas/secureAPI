from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

class HomeView(APIView):
    def get(self, request):
        context = {
            'title': 'Welcome to the Secure API',
            'description': 'This is the homepage of the API. Here you can find important information about the services provided.',
            'available_endpoints': [
                {'name': 'Create User', 'endpoint': '/users/register/', 'method': 'POST'},
                {'name': 'Protected View', 'endpoint': '/users/protected/', 'method': 'GET'},
                {'name': 'Get Token', 'endpoint': '/users/token/', 'method': 'POST'},
                {'name': 'Books List', 'endpoint': '/books/', 'method': 'GET/POST'},
                {'name': 'Book Detail', 'endpoint': '/books/<id>/', 'method': 'GET/PUT/DELETE'}
            ]
        }
        return render(request, 'home.html', context)
