from bio_data.models import BioData
from rest_framework import serializers

class BiodataClassSerializer(serializers.ModelSerializer):
    class Meta:
        model= BioData
        fields= '__all__'
        
    def validate_age(self, value):
        if value < 18:
            raise serializers.ValidationError('Age must be 18 or above')
        return value

    def validate_email(self, value):
        queryset = BioData.objects.filter(email=value)
        if self.instance:
            queryset = queryset.exclude(pk=self.instance.pk)
        
        if queryset.exists():
            raise serializers.ValidationError("This email already exists.")
        return value
    
    def validate_phone_number(self, value):
        if not value.isdigit():
            raise serializers.ValidationError("Phone number must contain digits only.")

        if len(value) != 10:
            raise serializers.ValidationError("Phone number must be exactly 10 digits.")
    
        queryset = BioData.objects.filter(phone_number=value)
        if self.instance:
            queryset = queryset.exclude(pk=self.instance.pk)
        
        if queryset.exists():
            raise serializers.ValidationError("This Phone number already exists.")
        return value
    
    def validate(self, data):
        first_name = data.get('first_name', getattr(self.instance, 'first_name', None))
        last_name = data.get('last_name', getattr(self.instance, 'last_name', None))
        
        if first_name and last_name and first_name.lower() == last_name.lower():
            raise serializers.ValidationError({
                'non_field_errors': ['First name and last name cannot be the same']
            })
        
        return data
    
    



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
    
    def validate_age(self, value):
        if value < 18:
            raise serializers.ValidationError('Age must be 18 or above')
        return value
    
    def validate(self, data):
        first_name = data.get('first_name', getattr(self.instance, 'first_name', None))
        last_name = data.get('last_name', getattr(self.instance, 'last_name', None))
        
        if first_name and last_name and first_name.lower() == last_name.lower():
            raise serializers.ValidationError({
                'non-field-errors': ['First name and last name cannot be the same']
            })
        
        return data
