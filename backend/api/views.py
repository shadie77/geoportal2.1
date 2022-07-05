from rest_framework import viewsets
from rest_framework.decorators import action
from django.contrib.auth.models import User
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Sum
import nltk
from nltk.tokenize import word_tokenize
from collections import Counter
from .serializers import UserSerializer, jettySerializer, routeSerializer, bathySerializer, UserInfoSerializer, depthSerializer, boundarySerializer, ridershipSerializer, accidentSerializer, jettyPictureSerializer
from .models import Jetty_Pictures, Route, Bathy, Jetty, UserProfileInfo, Depth, Water_Boundary, Ridership, Accident


# Create your viewsets here.
class UserProfileViewSet(viewsets.ModelViewSet):
    queryset= UserProfileInfo.objects.all()
    serializer_class = UserInfoSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class bathyViewSet(viewsets.ModelViewSet):
    queryset = Bathy.objects.all()
    serializer_class = bathySerializer

class routeViewSet(viewsets.ModelViewSet):
    queryset = Route.objects.all()
    serializer_class = routeSerializer

class jettyViewSet(viewsets.ModelViewSet):
    queryset = Jetty.objects.all()
    serializer_class = jettySerializer

    # Return total number oj jetties 
    #Make details true later
    @action(detail=False)
    def count(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        count = queryset.count()
        content = {'count': count}
        return Response(content)

class depthViewSet(viewsets.ModelViewSet):
    queryset = Depth.objects.all()
    serializer_class = depthSerializer

class boundaryViewSet(viewsets.ModelViewSet):
    queryset = Water_Boundary.objects.all()
    serializer_class = boundarySerializer

class ridershipViewset(viewsets.ModelViewSet):
    queryset = Ridership.objects.all()
    serializer_class = ridershipSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['jetty_id']

    #Make details true later
    @action(detail= False)
    def average_daily_count(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        first_day = queryset.order_by("arrival_departure_time").first().arrival_departure_time
        last_day = queryset.order_by("arrival_departure_time").last().arrival_departure_time
        number_of_days = last_day - first_day
        total_passenger = queryset.aggregate(Sum('number_of_passengers'))
        total_boat_ride = queryset.count()
        content = {
            'first_day': first_day,
            'last_day': last_day,
            'number_of_days': number_of_days.days,
            'total_number_of_passengers': total_passenger['number_of_passengers__sum'],
            'average_daily_passenger': round(total_passenger['number_of_passengers__sum']/number_of_days.days,2),
            'total_boat_ride' : total_boat_ride,
            'average_daily_boat_ride': round(total_boat_ride/number_of_days.days, 2)
            }
        return Response(content)

class accidentViewset(viewsets.ModelViewSet):
    queryset = Accident.objects.all()
    serializer_class = accidentSerializer

    #Make details true later
    @action(detail= False)
    def accident_data(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        casuality = queryset.aggregate(Sum('number_of_casuality'))['number_of_casuality__sum']
        injuries = queryset.aggregate(Sum('number_of_injuries'))['number_of_injuries__sum']
        death = queryset.aggregate(Sum('number_of_death'))['number_of_death__sum']
        rescue = queryset.aggregate(Sum('number_of_rescues'))['number_of_rescues__sum']
        accident_cause_list = list(queryset.values_list('cause', flat = True))
        sw = nltk.corpus.stopwords.words('english')
        bag_of_words = []
        ## Remove stopwords
        for word in accident_cause_list:
            tokens = word_tokenize(word)
            for eachtoken in tokens:
                if eachtoken not in sw:
                    bag_of_words.append(eachtoken)
        word_count= dict(Counter(bag_of_words))
        

        content = {
            'casuality': casuality,
            'injury_rate': round(injuries/ casuality*100,2),
            'death_rate': round(death / casuality *100,2),
            'rescue_rate':round(rescue / casuality *100, 2),
            'word_count': word_count
            }
        return Response(content)

class jettyPictureViewset(viewsets.ModelViewSet):
    queryset = Jetty_Pictures.objects.all()
    serializer_class = jettyPictureSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['jetty_id']


    