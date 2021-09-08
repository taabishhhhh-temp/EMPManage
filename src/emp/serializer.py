from enum import unique
from rest_framework import serializers
from .models import Employ
from datetime import date


class EmploySerializer(serializers.ModelSerializer):
    class Meta:
        model = Employ
        fields = [
            'empid','employID', 'fname', 'lname', 'mobile', 'position'
        ]
        # fields = '__all__'

# class EmploySerializer(serializers.Serializer):
    # empid = serializers.AutoField(primary_key=True)
    # employID = serializers.IntegerField()  
    # fname = serializers.CharField(max_length=20)
    # lname = serializers.CharField(max_length=20)
    # personalEmail = serializers.EmailField()
    # fladdraEmail = serializers.EmailField()
    # mobile = serializers.IntegerField()
    # position = serializers.CharField(max_length=16)
    # github = serializers.CharField(max_length=50)
    # education = serializers.CharField(max_length=80)
    # address = serializers.CharField(max_length=)
    # joinedOn = serializers.DateField(default=date.today)
    # is_archived = serializers.BooleanField(default=False)

    # def create(self, validated_data):
    #     return Employ.objects.create(validated_data)

    # def update(self, instance, validated_data):
    #     instance.employID = validated_data.get('employ ID', instance.employID)
    #     instance.fname = validated_data.get('fname', instance.fname)
    #     instance.lname = validated_data.get('lname', instance.lname)
    #     instance.personalEmail = validated_data.get('personalEmail', instance.personalEmail)
    #     instance.fladdraEmail = validated_data.get('fladdraEmail', instance.fladdraEmail)
    #     instance.mobile = validated_data.get('mobile', instance.mobile)
    #     instance.position = validated_data.get('position', instance.position)
    #     instance.github = validated_data.get('github', instance.github)
    #     instance.education = validated_data.get('education', instance.education)
    #     instance.address = validated_data.get('address', instance.address)
    #     instance.joinedOn = validated_data.get('joinedOn', instance.joinedOn)
    #     instance.is_archived = validated_data.get('is_archived', instance.is_archived)
    #     instance.save()
    #     return instance