from wsgiref.validate import validator
from rest_framework import serializers

from inmuebleslist_app.models import Edificacion,Empresa

class EdificacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Edificacion
        fields = "__all__"
        
    
class EmpresaSerializer(serializers.ModelSerializer):
    edificacionlist = EdificacionSerializer(many=True,read_only=True)
    class Meta:
        model = Empresa
        fields = "__all__"

        
 