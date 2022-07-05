

from django.db import models as nmodels
from django.contrib.gis.db import models
from django.contrib.auth.models import User
from numpy import size
from phonenumber_field.modelfields import PhoneNumberField
from django_resized import ResizedImageField

# Make Email address unique
User._meta.get_field('email')._unique = True


# Change the ModelBackend to Login With Email only
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(email=username)
        except UserModel.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
        return None

# Change the Model Backend to Login with Either Email or Username
from django.contrib.auth.backends import ModelBackend, UserModel
from django.db.models import Q

class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try: #to allow authentication through phone number or any other field, modify the below statement
            user = UserModel.objects.get(Q(username__iexact=username) | Q(email__iexact=username))
        except UserModel.DoesNotExist:
            UserModel().set_password(password)
        except MultipleObjectsReturned:
            return User.objects.filter(email=username).order_by('id').first()
        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user

    def get_user(self, user_id):
        try:
            user = UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None

        return user if self.user_can_authenticate(user) else None

# Create your models here.
class UserProfileInfo(nmodels.Model):
    user = nmodels.OneToOneField(User,default=None, null=True, related_name="user_profile", on_delete=models.CASCADE)
    #Additional Information
    department = nmodels.CharField(max_length=20, blank = True)
    phone_number = PhoneNumberField(blank = True)
    profile_pic = nmodels.ImageField(upload_to="profile_pics", blank=True)
    created_at = nmodels.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.email


class Route(models.Model):
    name = models.CharField(max_length=254)
    route_id = models.CharField(max_length=254)
    avg_depth = models.FloatField()
    geom = models.MultiLineStringField(srid=4326)

BOAT_TYPES= (
    ('Wooden', "Wooden"),
    ("Fiber", "Fiber"),
    ('Aluminium', "Aluminiun"),
    ("Steel", "Steel"),
    ("Others", "Others")
)

class Jetty(models.Model):
    name = models.CharField(max_length=254)
    terminal = models.CharField(max_length=254)
    type = models.CharField(max_length=254)
    geom = models.MultiPointField(srid=4326)
    boat_type = models.CharField(max_length=254, choices=BOAT_TYPES, default= None, blank=True, null = True)
    number_of_boats = models.IntegerField(blank= True, null=True)
    picture = ResizedImageField(size= [250,150], upload_to = "small_jetty", blank= True)

    def __str__(self):
        return self.name


class Bathy(models.Model):
    depth = models.FloatField()
    long = models.FloatField()
    lat = models.FloatField()
    geom = models.MultiPointField(srid=4326)


class Depth(models.Model):
    value = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)

# Water Boundary class
class Water_Boundary(models.Model):
    id_number = models.IntegerField()
    geom = models.MultiPolygonField(srid=4326)

class Jetty_Supervisors(nmodels.Model):
    firstname= nmodels.CharField(max_length=254, blank=True)
    surname = nmodels.CharField(max_length=254, blank=True)
    email = nmodels.EmailField(unique=True,  blank=True)
    phone_number = PhoneNumberField(blank = True)
    jetty_id = nmodels.ForeignKey(Jetty, on_delete=nmodels.CASCADE)

    def __str__(self):
        return self.email

class Jetty_Pictures(nmodels.Model):
    jetty_id = nmodels.ForeignKey(Jetty, on_delete= nmodels.CASCADE)
    picture = ResizedImageField(size = [1920, 1080], upload_to = "jetty", blank = True)
    header_picture = ResizedImageField(size = [1050, 300], upload_to = "header_jetty", blank = True)
    medium_picture = ResizedImageField(size= [500,300], upload_to ="medium_jetty", blank= True)

    def __str__(self):
        return self.jetty_id.name

class Jetty_Videos(nmodels.Model):
    jetty_id = nmodels.ForeignKey(Jetty, on_delete= nmodels.CASCADE)
    video = nmodels.FileField()

class Jetty_Bathymetry(nmodels.Model):
    jetty_id= nmodels.ForeignKey(Jetty, on_delete=nmodels.CASCADE)
    bathymetry = nmodels.FileField(upload_to='bathymetry')

class Drivers(nmodels.Model):
    first_name = nmodels.CharField(max_length= 254, blank= True)
    last_name = nmodels.CharField(max_length= 254, blank= True)
    email = nmodels.EmailField(blank= True)
    date_of_birth = nmodels.DateField()

class Boat (nmodels.Model):
    boat_name = nmodels.CharField(max_length=254, blank= True)
    boat_type = nmodels.CharField(max_length=254, choices=BOAT_TYPES, default=None, blank=True)
    boat_driver = nmodels.ForeignKey(Drivers, on_delete=nmodels.CASCADE)
    boat_capacity = nmodels.IntegerField(blank = True, null = True)

RIDERSHIP_OPTIONS = (
    ("Arrival", "Arrival"),
    ("Departure", "Departure")
)
class Ridership(nmodels.Model):
    jetty_id = nmodels.ForeignKey(Jetty, related_name = "ridershipLocation" ,on_delete= nmodels.CASCADE)
    arrival_departure = nmodels.CharField(max_length=254, choices=RIDERSHIP_OPTIONS, default = None)
    arrival_departure_time = nmodels.DateTimeField()
    arrival_departure_location = nmodels.ForeignKey(Jetty, related_name= "arrivalOrDepartureLocation", on_delete = nmodels.CASCADE)
    number_of_passengers = nmodels.IntegerField()
    transport_fare = nmodels.PositiveIntegerField(blank=True)
    boat_id = nmodels.ForeignKey(Boat, on_delete= nmodels.CASCADE)
    waterguard = nmodels.CharField(max_length = 254, blank= True)

class Accident(nmodels.Model):
    Boat_type_or_name = nmodels.TextField(blank = True)
    accident_date = nmodels.DateField(blank=True, null= True)
    accident_time = nmodels.TimeField(blank=True, null = True)
    location = nmodels.CharField(max_length=254, blank= True)
    number_of_casuality = nmodels.IntegerField(blank= True)
    number_of_injuries = nmodels.IntegerField(blank= True)
    number_of_death = nmodels.IntegerField(blank=True)
    number_of_rescues = nmodels.IntegerField(blank=True)
    cause = nmodels.TextField(blank=True)

