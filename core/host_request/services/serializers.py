# Imports
from rest_framework.serializers import ModelSerializer

# Models
from host_request.models import RequestModel

class RequestSerializer(ModelSerializer):
    class Meta:
        model = RequestModel
        fields = (
            'cmd',
            'code',
        )