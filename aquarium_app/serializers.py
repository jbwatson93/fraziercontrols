from rest_framework import serializers
from .models import Projects


class ProjectSerializer(serializers.ModelSerializer):
    project = ProjectSerializer(many=True, read_only=True)
    

    class Meta:
        model = Projects
        fields = ('projectname', 'description', 'startdate', 'customerid',
                  'company', 'projectid', )

# class CommentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Comment
#         fields = ("userId", "postId", "date", "commentText", "commentVoteCount")

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('userName', 'passWord', 'email', 'user_id')
