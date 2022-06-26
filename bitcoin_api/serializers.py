from rest_framework import serializers
from bitcoin_api.models import Bitcoin


class BitcoinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bitcoin
        fields = (
            "id",
            "timestamp", 
            "price",
            "description",
            "created_at",
            "updated_at",
        )