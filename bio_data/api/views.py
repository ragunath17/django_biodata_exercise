from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import get_object_or_404
# from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from bio_data.models import BioData
from bio_data.api.serializers import BiodataSerializer
from bio_data.api.paginations import BiodataPaginationCBV
from bio_data.api.filters import BiodataFilter

@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def biodata_list_create(request):
    if request.method == 'GET':
        biodata = BioData.objects.all()
        
        filterset = BiodataFilter(request.GET, queryset=biodata)
        biodata = filterset.qs
        
        paginator = BiodataPaginationCBV()
        
        result_page = paginator.paginate_queryset(biodata, request)
        serializer = BiodataSerializer(result_page, many=True)
        
        return paginator.get_paginated_response(serializer.data)
    
    if request.method == 'POST':
        serializer = BiodataSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
# def biodata_detail(request, pk):
#     if request.method == 'GET':
#         try:
#             biodata = get_object_or_404(BioData, pk=pk)
#         except BioData.DoesNotExist:
#             return Response({"error: Data Not Found"}, status=status.HTTP_404_NOT_FOUND)
#         serializer = BiodataSerializer(biodata)
#         return Response(serializer.data)
    
#     if request.method == 'PUT':
#         biodata = get_object_or_404(BioData, pk=pk)
#         serializer = BiodataSerializer(biodata, data=request.data)
        
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     if request.method == 'PATCH':
#         biodata = get_object_or_404(BioData, pk=pk)
#         serializer = BiodataSerializer(biodata, data=request.data, partial=True)
        
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     if request.method == 'DELETE':
#         biodata = get_object_or_404(BioData, pk=pk)
#         biodata.delete()
#         return Response({"message: Deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    
        

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def biodata_detail(request, pk):
    
    biodata = get_object_or_404(BioData, pk=pk)

    if request.method == 'GET':
        serializer = BiodataSerializer(biodata)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = BiodataSerializer(biodata, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PATCH':
        serializer = BiodataSerializer(biodata, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        biodata.delete()
        return Response(
            {"message": "Deleted successfully"},
            status=status.HTTP_204_NO_CONTENT
        )
