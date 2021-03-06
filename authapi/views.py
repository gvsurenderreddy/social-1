from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView
from rest_framework.response import Response
from newsfeed.serializer import UserSerializer
from rest_framework.exceptions import ValidationError, PermissionDenied


class UserViewSet(APIView):
	"""Validate current user session

	Check whether the current user is logged in and retrieve
	information about the user.

	It could be accessed at :http:get:`/api/auth/check`

	"""
	serializer_class = UserSerializer
	def get(self, request):
		"""Get logged user information

		Args:
			request: Django Rest Framework request object

		Return:
			Current logged username as string, or 403
		"""
		if request.user.is_authenticated():
			response = self.serializer_class(request.user)
			return Response(response.data)
		else:
			raise PermissionDenied()

class LoginViewSet(APIView):
	"""Log a user in with username/password combination

	It could be accessed at :http:post:`/api/auth/login`

	"""
	serializer_class = UserSerializer
	def post(self, request):
		"""Log a user in

		Args:
			request: Django Rest Framework request object

		Return:
			Username or 403
		"""
		if 'username' not in request.data or 'password' not in request.data:
			raise ValidationError('Specify username and password')

		user = authenticate(username=request.data['username'], password=request.data['password'])

		if not user:
			raise PermissionDenied('Cannot log you in')
		if not user.is_active:
			raise PermissionDenied('User disabled')

		login(request, user)
		response = self.serializer_class(user)
		return Response(response.data)

class LogoutViewSet(APIView):
	"""Logout of current session

	It could be accessed at :http:post:`/api/auth/logout`

	"""
	def post(self, request):
		"""Destroy current session

		Args:
			request: Django Rest Framework request object

		Return:
			200
		"""
		logout(request)
		return Response()
