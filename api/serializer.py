from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class RegistrationSerializer(serializers.ModelSerializer):
    role = serializers.CharField(max_length=50, required=False)
    first_name = serializers.CharField(max_length=255, required=False)
    last_name = serializers.CharField(max_length=255, required=False)
    middle_name = serializers.CharField(max_length=255, required=False)
    phone_number = serializers.CharField(max_length=255, required=False)
    address = serializers.CharField(max_length=255, required=False)

    
    class Meta:
        model = User
        fields = ['username', 'password', 'role', 'id', 'first_name', 'last_name', 'middle_name', 'phone_number', 'address']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']  # Include any other fields you want

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('name', 'start_date', 'end_date', 'comments', 'status')

class RoutineInterviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoutineInterview
        fields = '__all__'

class IndividualRecordFormSerializer(serializers.ModelSerializer):
    profile = serializers.StringRelatedField()

    class Meta:
        model = IndividualRecordForm
        fields = '__all__'

class CareerTrackingSerializer(serializers.ModelSerializer):
    class Meta:
        model = CareerTracking
        fields = '__all__'  

class ConferenceFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConferenceForm
        fields = '__all__'  

class MS_ImpactEvaluationSerializer(serializers.ModelSerializer):
    class Meta:
        model = MS_ImpactEvaluation
        fields = '__all__'  

class MS_CounselingServiceEvaluationSerializer(serializers.ModelSerializer):
    class Meta:
        model = MS_CounselingServiceEvaluation
        fields = '__all__'  

class Guidance_Class_EvaluationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guidance_Class_Evaluation
        fields = '__all__'  

class KinderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kinder
        fields = '__all__'

class Grade_OneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade_One
        fields = '__all__'

class Grade_TwoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade_Two
        fields = '__all__'

class Grade_ThreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade_Three
        fields = '__all__'        

class Grade_FourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade_Four
        fields = '__all__'       

class Grade_FiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade_Five
        fields = '__all__'  

class Grade_SixSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade_Six
        fields = '__all__'  

class Grade_SevenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade_Seven
        fields = '__all__'  

class Grade_EightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade_Eight
        fields = '__all__'  

class Grade_NineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade_Nine
        fields = '__all__'  

class Grade_TenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade_Ten
        fields = '__all__'  

class Grade_ElevenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade_Eleven
        fields = '__all__'  

class Grade_TwelveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade_Twelve
        fields = '__all__'  

class First_YearSerializer(serializers.ModelSerializer):
    class Meta:
        model = First_Year
        fields = '__all__'  

class Second_YearSerializer(serializers.ModelSerializer):
    class Meta:
        model = Second_Year
        fields = '__all__'  

class Third_YearSerializer(serializers.ModelSerializer):
    class Meta:
        model = Third_Year
        fields = '__all__'  

class Fourth_YearSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fourth_Year
        fields = '__all__'  

class ResourceSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()  # This will return the user's string representation (e.g., username)

    class Meta:
        model = Resource
        fields = '__all__'


class AppointmentSerializer(serializers.ModelSerializer):
    counselor_user = serializers.CharField(source='counselor.user', read_only=True)
    sr_code = serializers.SlugRelatedField(
        queryset=IndividualRecordForm.objects.all(),
        slug_field='sr_code'
    )

    class Meta:
        model = Appointment
        fields = '__all__'

    def validate(self, data):
        # Check if the Profile (Counselor) exists
        if not Profile.objects.filter(id=data['counselor'].id).exists():
            raise serializers.ValidationError("Invalid counselor reference.")
        
        return data

class CounselorAppointmentSerializer(serializers.ModelSerializer):
    time_in_date = serializers.DateTimeField()
    time_out_date = serializers.DateTimeField()
    grade = serializers.CharField(max_length=50)
    name = serializers.CharField(max_length=255)
    purpose = serializers.CharField(max_length=500)
    section = serializers.CharField(max_length=50)
    sr_code = serializers.SlugRelatedField(
        queryset=IndividualRecordForm.objects.all(),
        slug_field='sr_code'
    )

    
    class Meta:
        model = Appointment
        fields = [
            'grade',
            'name',
            'purpose',
            'section',
            'sr_code',
            'time_in_date',
            'time_out_date',
            'start',
            'end',
            'date',
            'time',
            'counselor'
        ]

    def validate(self, data):
        time_in_date = data.get('time_in_date')
        time_out_date = data.get('time_out_date')

        if time_in_date is None or time_out_date is None:
            return data

        if time_in_date >= time_out_date:
            raise serializers.ValidationError("End time must be after start time")
        return data


    def create(self, validated_data):
        time_in_date = validated_data.get('time_in_date')
        time_out_date = validated_data.get('time_out_date')
        
        # Still populate these fields even though they're not in the serializer
        validated_data['date'] = time_in_date.date()
        validated_data['start'] = time_in_date.strftime('%H:%M')
        validated_data['end'] = time_out_date.strftime('%H:%M')
        validated_data['time'] = time_in_date.time()
        
        return Appointment.objects.create(**validated_data)



