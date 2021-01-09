# News Bytes URL Hashing System Development 

As per the instructions mentioned in the given scenario, the API has been developed using Django REST Framework and a simple python script to test the flow of the API in it's all test case satisfaction.
## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install django and django rest framework.

```bash
pip install django
pip install djangorestframework
```
## Usage
1. Installation and Execution of Django Server
```python
django-admin startproject news_bytes

```
2. Setting up the API URLS on *urls.py* file in project directory 
```python
from django.conf.urls import url

from api.api import UserAuthentication, URL_Hasher

    urlpatterns = [
    # URL Path to the admin console
    path('admin/', admin.site.urls),
    # URL Path to view UTM Parameters and its respective Hashed URL
    url(r'^api/hash_url/$', URL_Hasher.as_view(), name='hash_url'),
    # Default URL path for User Authentication
    url(r'^api/auth/$', UserAuthentication.as_view(),
        name='User Authentication API')

```
##### Usage of Create Django App in Nirang_Zone Project

```python
django-admin startapp api
```

##### Create a Users Model in *models.py*

```python
    website_url = models.CharField(max_length=256)  # Eg. newsbytesapp.com
    campaign_source = models.CharField(max_length=256)  # linkedin
    campaign_medium = models.CharField(max_length=256)  # profile
    campaign_term = models.CharField(max_length=256)  # organic
    campaign_content = models.CharField(max_length=256)  # 39
    campaign_name = models.CharField(max_length=256)  # Course

    campaign_url = models.CharField(
        max_length=1024, blank=True)
    campaign_hashed_url = models.CharField(
        max_length=256, blank=True)
```

##### Create a new *serializer.py* file in **App** directory to Serialize the data from *models.py*
```python
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
```
##### Usage of Django Admin to test with Django UI for easier purpose
```python
http://localhost:8000/admin/api/utmparameter/

```

###### Serialized data from *models.py* is supposed to be used for data transmission in REST API


3. Creation of an API using Python Django Framework.
```python
def get(self, request):

        model = UTMParameter.objects.all()
        serializer = UTMParameterSerializer(model, many=True)

        return Response(serializer.data)


```
 
4. Add New Entries to the Database using the POST method
```python
from .serializers import *

# suppose, we already have 10 billion urls
id = 10000000000
# store url to id in order not to have duplicated url with different id
url2id = {}

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

```

5. Authentication to the Application in Django REST API
Please make sure to update tests as appropriate.
```python
class UserAuthentication(ObtainAuthToken):

    def post(self,request,*args,**kwargs):

        serializer = self.serializer_class(
            data=request.data,
            context={
                'request':request
            }
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)

        return Response(token.key)
```

So, finally in order to run the project, go to the project directory and run the following commands
```python
python manage.py makemigrations # to update models to the database
python manage.py migrate # to add fields on to the database
python manage.py createsuperuser # to create an admin user of Django Administration (in my case admin is the username and password)
python manage.py runserver # to run the server
```
Open 'http://localhost:8000/api/auth/' # Complete your authentication (eg. Username: admin & Password: admin)
Open 'http://localhost:8000/api/auth/' 

##### Use HTTPRedirect (GET) method to view all the UTM Parameters and its respective URL and HASH
##### Use POST Method to post the UTM Parameters and to get a new URL and HASH with UTM Parameters

## Test Cases
#### All the accomplished test cases are published as the Postman Documentation
##### The respected link for the project is in [Postman Documentary](https://documenter.getpostman.com/view/11578501/TVzPneTM)
