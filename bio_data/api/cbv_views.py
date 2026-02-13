from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status

from bio_data.models import BioData
from bio_data.api.serializers import BiodataSerializer

class BiodataListCreateCBV(APIView):
    def get(self, request):
        biodata = BioData.objects.all()
        serializer = BiodataSerializer(biodata, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = BiodataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class BiodataDetailCBV(APIView):
    def get_object(self, pk):
        return get_object_or_404(BioData, pk=pk)
    
    def get(self, request, pk):
        biodata = self.get_object(pk)
        serializer = BiodataSerializer(biodata)
        return Response(serializer.data)
    
    def put(self, request, pk):
        biodata = self.get_object(pk)
        serializer = BiodataSerializer(biodata, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk):
        biodata = self.get_object(pk)
        serializer = BiodataSerializer(biodata, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        biodata = self.get_object(pk)
        biodata.delete()
        return Response({"message: Deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    
