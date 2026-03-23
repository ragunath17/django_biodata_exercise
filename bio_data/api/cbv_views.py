from rest_framework.views import APIView
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.template import loader
from rest_framework.response import Response
from rest_framework import status

from bio_data.models import BioData
from bio_data.api.serializers import BiodataSerializer, BiodataClassSerializer


def biodata_list(request):
    all_data = BioData.objects.all().values()
    count = all_data.count()

    template = loader.get_template('data.html')

    context = {
        'all_data': all_data,
        'count': count
    }

    return HttpResponse(template.render(context, request))

def biodata_detail(request, pk):
    person = BioData.objects.get(pk=pk)

    template = loader.get_template('biodata_detail.html')

    context = {
        'person': person,
    }

    return HttpResponse(template.render(context, request))

def biodata_create(request):
    if request.method == 'POST':
        BioData.objects.create(
            first_name=request.POST.get('first_name'),
            last_name=request.POST.get('last_name'),
            gender=request.POST.get('gender'),
            date_of_birth=request.POST.get('date_of_birth'),
            age=request.POST.get('age'),
            marital_status=request.POST.get('marital_status'),
            nationality=request.POST.get('nationality'),
            email=request.POST.get('email'),
            phone_number=request.POST.get('phone_number'),
            alternate_phone_number=request.POST.get('alternate_phone_number', ''),
            address_line_1=request.POST.get('address_line_1'),
            address_line_2=request.POST.get('address_line_2', ''),
            city=request.POST.get('city'),
            state=request.POST.get('state'),
            country=request.POST.get('country'),
            zip_code=request.POST.get('zip_code'),
            postal_code=request.POST.get('postal_code'),
            height=request.POST.get('height'),
            weight=request.POST.get('weight'),
            blood_group=request.POST.get('blood_group'),
            highest_qualification=request.POST.get('highest_qualification'),
            university_name=request.POST.get('university_name'),
            year_of_passing=request.POST.get('year_of_passing'),
            occupation=request.POST.get('occupation'),
            company_name=request.POST.get('company_name', ''),
            job_title=request.POST.get('job_title', ''),
            years_of_experience=request.POST.get('years_of_experience'),
            expected_salary=request.POST.get('expected_salary') or None,
            website=request.POST.get('website', ''),
            linkedin_profile=request.POST.get('linkedin_profile', ''),
            github_profile=request.POST.get('github_profile', ''),
            skills=request.POST.get('skills', ''),
            languages_known=request.POST.get('languages_known', ''),
            is_active=True if request.POST.get('is_active') == 'on' else False,
        )
        return redirect('/biodata/template_list/')

    return render(request, 'biodata_form.html')


class BiodataListCreateCBV(APIView):
    def get(self, request):
        biodata = BioData.objects.all()
        serializer = BiodataClassSerializer(biodata, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = BiodataClassSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class BiodataDetailCBV(APIView):
    def get_object(self, pk):
        return get_object_or_404(BioData, pk=pk)
    
    def get(self, request, pk):
        biodata = self.get_object(pk)
        serializer = BiodataClassSerializer(biodata)
        return Response(serializer.data)
    
    def put(self, request, pk):
        biodata = self.get_object(pk)
        serializer = BiodataClassSerializer(biodata, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk):
        biodata = self.get_object(pk)
        serializer = BiodataClassSerializer(biodata, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        biodata = self.get_object(pk)
        biodata.delete()
        return Response({"message": "Deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    
