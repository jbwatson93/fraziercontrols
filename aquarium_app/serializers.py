from rest_framework import serializers
from .models import *


class ExhibitsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Exhibits
        fields = ('exhibitID', 'projectid','exhibitName','description','estimatedGal','desiredTurnover','systemFlow',
'creationDate','updateDate','type')
class ProjectSerializer(serializers.ModelSerializer):
    Exhibits = ExhibitsSerializer(many=True, read_only=True)

    class Meta:
        model = Projects
        fields = ('Exhibits','projectid', 'startdate', 'estimatedcompdate', 'projectname','description','creationdate',
'updatedate','company','customerid'  )



class ProjectExhibitsSerializer(serializers.ModelSerializer):
    project = ProjectSerializer(many=True, read_only=True)
    exhibits = ExhibitsSerializer(many=True, read_only=True)
    class Meta:
        model = ProjectExhibits
        fields = ('project', 'exhibits', 'exhibitid','projectid','newconstruction','creationdate','updatedate')

class ItemsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Items
        fields = ('itemNo', 'manufacturer','manufactPartNo','description','pipeSize','HP','diameter','length',
'width','height' ,'voltage','voltageType','creationdate','updatedate')
