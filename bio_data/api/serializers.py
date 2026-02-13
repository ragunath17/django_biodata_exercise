from bio_data.models import BioData
from rest_framework import serializers

class BiodataSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    gender = serializers.CharField(max_length=20)
    date_of_birth = serializers.DateField()
    age = serializers.IntegerField()
    marital_status = serializers.CharField(max_length=20)
    nationality = serializers.CharField(max_length=50)
    email = serializers.EmailField()
    phone_number = serializers.CharField(max_length=15)
    alternate_phone_number = serializers.CharField(max_length=15, allow_blank=True)
    address_line_1 = serializers.CharField(max_length=255)
    address_line_2 = serializers.CharField(max_length=255, required=False, allow_blank=True)
    city = serializers.CharField(max_length=50)
    state = serializers.CharField(max_length=50)
    country = serializers.CharField(max_length=50)
    zip_code = serializers.CharField(max_length=50)
    
    height = serializers.FloatField(help_text= "Height in cm")
    weight = serializers.FloatField(help_text= "Weight in kg")
    blood_group = serializers.CharField(max_length=5)
    
    highest_qualification = serializers.CharField(max_length=100)
    university_name = serializers.CharField(max_length=150)
    year_of_passing = serializers.IntegerField()
    
    occupation = serializers.CharField(max_length=100)
    company_name = serializers.CharField(max_length=150, allow_blank=True, required=False)
    job_title = serializers.CharField(max_length=150, allow_blank=True, required=False)
    years_of_experience = serializers.IntegerField(min_value=0)
    expected_salary = serializers.IntegerField(allow_null=True)
    
    website = serializers.URLField(required=False, allow_blank=True)
    linkedin_profile = serializers.URLField(required=False, allow_blank=True)
    github_profile = serializers.URLField(required=False, allow_blank=True)
    
    skills = serializers.CharField(required=False, allow_blank=True)
    languages_known = serializers.CharField(required=False, allow_blank=True)
    
    is_active = serializers.BooleanField(default=True)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    
    def create(self, validated_data):
        return BioData.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
    
    def validate(self, data):
        if data['first_name'].lower() == data['last_name'].lower():
            raise serializers.ValidationError('First name and last name cannot be the same')

        if data['age'] < 18:
            raise serializers.ValidationError('Age must be 18 or above')
        
        return data
    