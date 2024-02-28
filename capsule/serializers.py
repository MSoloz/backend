from rest_framework import serializers
from .models import Capsule


class CapsuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Capsule
        fields = '__all__'
        extra_kwargs = {
            'sponsors': {'required': False}
        }