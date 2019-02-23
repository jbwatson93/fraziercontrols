from rest_framework import serializers
from .models import Projects, Exhibits, ProjectExhibits


class ProjectSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = Projects
        fields = ('projectid', 'startdate', 'estimatedcompdate', 'projectname','description','creationdate',
'updatedate','company','customerid'  )

class ExhibitsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Exhibits
        fields = ('exhibitID','exhibitName','description','estimatedGal','desiredTurnover','systemFlow',
'creationDate','updateDate','type')

class ProjectExhibitsSerializer(serializers.ModelSerializer):
    project = ProjectSerializer(many=True, read_only=True)
    exhibits = ExhibitsSerializer(many=True, read_only=True)
    class Meta:
        model = ProjectExhibits
        fields = ('project', 'exhibits', 'exhibitid','projectid','newconstruction','creationdate','updatedate')
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('userName', 'passWord', 'email', 'user_id')
