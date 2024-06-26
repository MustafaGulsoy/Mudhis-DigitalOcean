from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .serializers import UserSerializer
from .models import User, Person
import jwt, datetime


class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data.get('password')

        user = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('User not found!')

        if not password == user.password:
            raise AuthenticationFailed('incorrect password!')

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow(),
        }
        token = jwt.encode(payload, 'secret', algorithm='HS256')

        response = Response()
        response.set_cookie(key='jwt', value=token)
        response.data = {'jwt': token}

        return response


class UserView(APIView):
    def get(self, request):
        print(" ")
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated!')
        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])

        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)
        return Response(serializer.data)


class LogoutView(APIView):
    def post(selt, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }

        return response


class CreateChild(APIView):
    def post(self,request):

        childs = request.data.get('childs')

        for i in range(len(childs)):
            child = Person.objects.create()
            child.sex = request.data.get('sex')
            child.name = request.data.get('sex')
            child.surname = request.data.get('sex')
            child.birth_date = request.data.get(datetime.datetime.now())
            child.motion_data = {}
            child.pressure_data = {}
            Person.save(childs[i])
class AddChildren(APIView):

    def post(self,request):
        email = request.data['email']
        password = request.data.get('password')
        user = User.objects.filter(email=email).first()

        user.childs.add(request.data.get('child'))
        user.childs.add
