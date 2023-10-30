from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet, ModelViewSet

from demo.models import Comment
from demo.serializers import CommentSerializer


# Create your views here.

class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['user']

    search_fields = ['text', ]
    ordering_filets = ['id', 'user', 'text']
