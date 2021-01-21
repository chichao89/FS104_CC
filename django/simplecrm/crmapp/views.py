#from rest_framework import generics,
from rest_framework import viewsets
from .models import Account, Activity, ActivityStatus, Contact, ContactSource, ContactStatus
from .serializers import AccountSerializer, ActivitySerializer, ActivityStatusSerializer, ContactSerializer, ContactSourceSerializer, ContactStatusSerializer

# Create your views here.
class AccountAPIView(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class ActivityAPIView(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class ActivityStatusAPIView(viewsets.ModelViewSet):
    queryset = ActivityStatus.objects.all()
    serializer_class = ActivitySerializer

class ContactAPIView(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class ContactStatusAPIView(viewsets.ModelViewSet):
    queryset = ContactStatus.objects.all()
    serializer_class = ContactSerializer

class ContactSourceAPIView(viewsets.ModelViewSet):
    queryset = ContactSource.objects.all()
    serializer_class = ContactSourceSerializer