from rest_framework import serializers
from icare.models import Departments,Employees,User,Sport
#from django.contrib.auth.models import User

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Departments 
        fields=('DepartmentId','DepartmentName')

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employees 
        fields=('EmployeeId','EmployeeName','Department','DateOfJoining','PhotoFileName')

class SportSerializer(serializers.ModelSerializer):
    class Meta:
        model=Sport 
        fields=('SportId','SportName','Duree')

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email','height','age','weight')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    sport = SportSerializer(many=True, required=False)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password','height','age','weight','sport')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
           username = self.validated_data['username'], 
            email = self.validated_data['email'], 
            password = self.validated_data['password'],
            age = self.validated_data['age'],
            weight = self.validated_data['weight'],
            height = self.validated_data['height']
            )

        return user