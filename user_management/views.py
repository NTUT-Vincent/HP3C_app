# Create your views here.
from rest_framework import viewsets, generics

from user_management.serializers import UserSerializers
from user_management.models import User, get_user_with_id_and_password

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers


@csrf_exempt
def user_list(request):
    """
    List all code User, or create a new snippet.
    """
    if request.method == 'GET':
        user_id = 'staff001'
        user = User.objects.all()
        serializer = UserSerializers(user, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def user_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = UserSerializers(user)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = UserSerializers(user, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        user.delete()
        return HttpResponse(status=204)

@csrf_exempt
def user_login(request, id, password):
    """
    List all code User, or create a new snippet.
    """
    if request.method == 'GET':
        user_id = 'staff001'
        user = get_user_with_id_and_password(id, password)
        if len(user) == 0:
            response = {'message': 'login failed'}
            return JsonResponse(response, status=401)
        # for user_detail in user:
        user = user[0]
        user['message'] = 'Login successfully'
        return JsonResponse(user, safe=False)

   

