from rest_framework import serializers
from .models import User, UTMParameter


# Serializer for User Authertication (optional)
class UserSerializer(serializers.ModelSerializer):

    user_id = serializers.CharField(required=False)
    user_name = serializers.CharField(required=False)
    user_email = serializers.EmailField(required=False)

    # Let Django generate a set of fields based on the (User) Model
    class Meta:
        model = User
        fields = '__all__'


# Serializer for queryset and list of objects (instead of creating object instances)
class UTMParameterSerializer(serializers.ModelSerializer):

    # Leave not required fields for data post
    campaign_term = serializers.CharField(required=False)  # organic
    campaign_content = serializers.CharField(required=False)  # 39
    campaign_url = serializers.CharField(
        required=False, allow_blank=True)  # 39
    campaign_hashed_url = serializers.CharField(
        required=False, allow_blank=True)  # 39

    # Let Django generate a set of fields based on the (UTMParameter) Model
    class Meta:
        model = UTMParameter
        fields = ('website_url', 'campaign_source', 'campaign_medium',
                  'campaign_term', 'campaign_content', 'campaign_name', 'campaign_url', 'campaign_hashed_url')
