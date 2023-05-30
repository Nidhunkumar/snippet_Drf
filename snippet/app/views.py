from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, permissions
from rest_framework.response import Response
from .serializers import UserSerializer,SnippetSerializer,TagSerializer
from django.contrib.auth.models import User
from rest_framework import status
from .models import Snippet,Tag


class UserRegistration(generics.CreateAPIView):
    queryset=User.objects.all()
    serializer_class = UserSerializer
    
class SnippetView(APIView):
	permission_classes = (IsAuthenticated, )
	serializer_class = SnippetSerializer

	def get(self, request):
		snippets = Snippet.objects.all()
		serializer = self.serializer_class(snippets, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)

	def post(self, request):
		serializer = SnippetSerializer(data=request.data)
		if serializer.is_valid():
					title = serializer.validated_data.get('title')
					content = serializer.validated_data.get('content')
					tag_title = serializer.validated_data.get('tag')['tag_title']
					try:
							tag = Tag.objects.get(tag_title=tag_title)
					except Tag.DoesNotExist:
							tag = Tag.objects.create(title=tag_title)
					user = request.user
					snippet = Snippet.objects.create(snippet_title=title, content=content, user=user, tag=tag)
					snippet_serializer = SnippetSerializer(snippet)
					return Response(snippet_serializer.data, status=status.HTTP_201_CREATED)
		else:
				return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SnippetDetailView(APIView):
	permission_classes = (IsAuthenticated, )
	serializer_class = SnippetSerializer

	def get(self, request, id):
		snippets = Snippet.objects.get(id=id)
		serializer = self.serializer_class(snippets)
		return Response(serializer.data, status=status.HTTP_200_OK)

	def put(self, request, id):
		snippets = Snippet.objects.get(id=id)
		serializer = SnippetSerializer(snippets, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request,id):
		snippets = Snippet.objects.get(id=id)
		snippets.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
			


class TagListView(APIView):
	permission_classes = (IsAuthenticated, )
	serializer_class = TagSerializer

	def get(self, request):
		tags = Tag.objects.all()
		serializer = self.serializer_class(tags, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)


class SnippetByTagView(APIView):
	permission_classes = (IsAuthenticated, )
	serializer_class = SnippetSerializer

	def get(self,request,id):
		snippets = Snippet.objects.get(tag_id=id)
		serializer = self.serializer_class(snippets, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)
