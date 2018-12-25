from rest_framework import serializers
from .models import (Project,PLanguage)
from django.contrib.auth.models import User


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PLanguage
        fields = ('id','name')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','email')

class ProjectSerializer(serializers.ModelSerializer):
    language = LanguageSerializer(many=False)
    users    = UserSerializer(many=True)
    class Meta:
        model = Project
        fields = ('id','thumbnail','description','is_finished','author','github','upvotes','downvotes','is_pinned','title','language','users')