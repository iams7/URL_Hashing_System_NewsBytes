import re
from django.db import models
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from .serializers import *
from django.conf import settings


# User Authentication API
class UserAuthentication(ObtainAuthToken):

    def post(self, request, *args, **kwargs):

        serializer = self.serializer_class(
            data=request.data,
            context={
                'request': request
            }
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)

        return Response(token.key)


# URL Hashing API
class URL_Hasher(APIView):

    # suppose, we already have 10 billion urls
    id = 10000000000
    # store url to id in order not to have duplicated url with different id
    url2id = {}

    # get all UTM Parameters
    def get(self, request):

        model = UTMParameter.objects.all()
        serializer = UTMParameterSerializer(model, many=True)

        return Response({'response': serializer.data})

    # Method to add the new UTM Parameters for new URL and and generating its Hash
    def post(self, request):

        # optain the Parameters (data) from POST Request
        website_url = request.data['website_url']
        campaign_source = request.data['campaign_source']
        campaign_medium = request.data['campaign_medium']
        campaign_term = request.data['campaign_term']
        campaign_content = request.data['campaign_content']
        campaign_name = request.data['campaign_name']

        campaign_url = request.data['campaign_url']
        campaign_hashed_url = request.data['campaign_hashed_url']

        # URL Generation from the obtained Parameters
        utm_parameter = website_url + "?utm_source=" + campaign_source + "&utm_medium=" + campaign_medium + \
            "&utm_campaign=" + campaign_name + "&utm_term=" + \
            campaign_term + "&utm_content=" + campaign_content

        # HASH URL Generation
        new_hash = str(hash(utm_parameter))
        new_hash = new_hash[1:]
        hash_url = website_url+"?"+new_hash

        # URL and its HASH Updation
        campaign_url = utm_parameter
        campaign_hashed_url = hash_url

        # Response Object
        parameterized_data = {'website_url': website_url, 'campaign_source': campaign_source, 'campaign_medium': campaign_medium,
                              'campaign_term': campaign_term, 'campaign_content': campaign_content, 'campaign_name': campaign_name, 'campaign_url': campaign_url, 'campaign_hashed_url': campaign_hashed_url}

        # Serializer Object Creation
        serializer = UTMParameterSerializer(data=parameterized_data)

        # Serializer Validation
        if serializer.is_valid():

            # Save Response to the Database
            serializer.save()
            response = {'response': serializer.data, 'status': 'CREATED'}

            # Respond to API Window
            return Response(
                response,
                status=status.HTTP_201_CREATED
            )

        # Respond to API Window for any failure cases
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
