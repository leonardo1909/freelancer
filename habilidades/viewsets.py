from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status

from habilidades.serializers import FreelancerObjectSerializer
from habilidades.utils.freelance import computedSkills


class FreelancerExperienceViewSet(ViewSet):

    def post(self, request):
        serializer = FreelancerObjectSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                status=status.HTTP_422_UNPROCESSABLE_ENTITY
            )
        response = computedSkills(serializer.data)
        return Response(
            response,
            status=status.HTTP_200_OK
        )
