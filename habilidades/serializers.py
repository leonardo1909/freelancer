from rest_framework import serializers

from habilidades.validators import ValidateDate


class SkillSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()


class ProfessionalExperienceSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    companyName = serializers.CharField()
    startDate = serializers.CharField(
        validators=[ValidateDate]
    )
    endDate = serializers.CharField(
        validators=[ValidateDate]
    )
    skills = serializers.ListField(
        child=SkillSerializer()
    )


class UserSerializer(serializers.Serializer):
    firstName = serializers.CharField()
    lastName = serializers.CharField()
    jobTitle = serializers.CharField()


class FreelancerSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    user = UserSerializer()
    status = serializers.CharField()
    retribution = serializers.IntegerField()
    availabilityDate = serializers.DateTimeField(
        format='%Y-%m-%dT%H:%M:%S+%Z:%z'
    )
    professionalExperiences = serializers.ListField(
        child=ProfessionalExperienceSerializer()
    )


class FreelancerObjectSerializer(serializers.Serializer):
    freelance = FreelancerSerializer()
