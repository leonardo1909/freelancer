from django.urls import path

from rest_framework import routers

from habilidades.viewsets import FreelancerExperienceViewSet


router = routers.DefaultRouter()


urlpatterns = [
    # url('', include(router.urls)),
    path('frelancer/experience/', FreelancerExperienceViewSet.as_view({'post': 'post'})),
]
