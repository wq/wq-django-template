from wq.db.rest.serializers import ModelSerializer
from rest_framework import serializers
from .models import Observation


class ObservationSerializer(ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        fields = "__all__"
        model = Observation
        wq_field_config = {
            "notes": {"multiline": True},
        }
