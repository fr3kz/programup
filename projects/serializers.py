from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ('id','thumbnail','description','is_finished','author','github','upvotes','downvotes','is_pinned','title')
