import re
from inmuebleslist_app.api.serializers import EdificacionSerializer, EmpresaSerializer
from inmuebleslist_app.models import Empresa, Edificacion
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
# Create your views here.


class EmpresaAV(APIView):
    def get(self,request):
        empresas = Empresa.objects.all()
        serializer = EmpresaSerializer(empresas,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        deSerializer = EmpresaSerializer(data=request.data)
        if deSerializer.is_valid():
            deSerializer.save()
            return Response(deSerializer.data)
        else:
            return Response(deSerializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
class EdificacionesListAV(APIView):
    def get(self,request):
        inmuebles = Edificacion.objects.all()
        serializer = EdificacionSerializer(inmuebles,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        deSerializer = EdificacionSerializer(data=request.data)
        if deSerializer.is_valid():
            deSerializer.save()
            return Response(deSerializer.data)
        else:
            return Response(deSerializer.errors,status=status.HTTP_400_BAD_REQUEST)

class EdificacionDetalleAV(APIView):
    def get(self,request,pk):
        try:
            edificacion = Edificacion.objects.get(pk=pk)
        except Edificacion.DoesNotExist:
            return Response({'error': 'el inmueble no existe'},status=status.HTTP_404_NOT_FOUND)
        serializer = EdificacionSerializer(edificacion)
        return Response(serializer.data)
    
    def put(self,request,pk):
        try:
            edificacion = Edificacion.objects.get(pk=pk)
        except Edificacion.DoesNotExist:
            return Response({'error': 'el inmueble no existe'},status=status.HTTP_404_NOT_FOUND)
        serializer = EdificacionSerializer(Edificacion,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
    def delete(self,request,pk):
        try:
            edificacion = Edificacion.objects.get(pk=pk)
        except Edificacion.DoesNotExist:
            return Response({'error': 'el inmueble no existe'},status=status.HTTP_404_NOT_FOUND)
        edificacion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
   