from django.shortcuts import render, HttpResponse
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import permission_required

# Create your views here.
permission_required('auth.view_user')
def test_app_view(request):
    return render(request, 'testapphome.html')

