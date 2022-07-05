from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.core.serializers import serialize
from api.forms import UserForm, UserProfileForm
from django.db.models import Sum, Count
from django.db.models.functions import TruncYear, TruncMonth
import pandas as pd
from scipy.interpolate import griddata
import numpy as np
# Import Model
from api.models import UserProfileInfo, Jetty, Route, Jetty_Pictures, Ridership, Jetty_Supervisors, Jetty_Bathymetry

# Serializer to display data



# Create your views here.
class landingView(TemplateView):
    template_name = "dashboard/landing.html"
    title = "Homepage"
    def get(self, request):
        return render(request, self.template_name, context={'pageTitle': self.title})
        
class DashboardView(TemplateView):
    template_name = "dashboard/kepler.html"
    title = "Dashboard"

    def get(self, request):
        return render(request, self.template_name, context={'pageTitle': self.title})

# To remove
class KeplerDashboardView(LoginRequiredMixin, TemplateView):
    template_name = "dashboard/kepler.html"
    title = "Kepler Dashboard"

    def get(self, request):
        return render(request, self.template_name, context={'pageTitle': self.title})

class SlideoutView(TemplateView):
    template_name = "dashboard/slideout.html"

class AppearView(TemplateView):
    template_name = "dashboard/appear.html"

@login_required
def user_logout(request):
    logout(request)
    return redirect('login')

# Change this to Show Dashboard Directly
class index(TemplateView):
    template_name = 'dashboard/login.html'
    title = "Login"
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard')
        
        return super(index, self).dispatch(request, *args, **kwargs)

class logon(TemplateView):
    template_name = 'dashboard/login.html'
    title = 'LogIn Page'

    def post(self, request):
        email = self.request.POST['username']
        password= self.request.POST['password']
        user = authenticate(username= email, password= password)
        print(user)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('dashboard'))
            else:
                return HttpResponse('Invalid Account Details')
        else:
            print('Someone tried to log on')
            print('Email', email)
            print('Password', password)
            return render(request, self.template_name, context={'pageTitle': self.title, 'errorMessage':"Invalid Login Details"})

    def get(self, request):
        return render(request, self.template_name, context={'pageTitle': self.title, 'errorMessage':""})


class signup(CreateView):
    form_class = UserForm
    success_url = reverse_lazy('login')
    template_name= 'dashboard/register.html'
    title= "Sign Up Page"

class Registration(CreateView):
    model = User
    fields = ('first_name', 'last_name','email', 'password')
    child_model = UserProfileInfo
    child_form_class = UserForm
    child_fields = ('department', 'profile_pics',)
    template_name= "dashboard/registration.html"

def registration_view(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        userinfo_form = UserProfileForm(request.POST)
        if user_form.is_valid() and userinfo_form.is_valid():
            userdetails= user_form.save()
            print(userdetails.pk)
            userinfodata= userinfo_form.save(commit=False)
            userinfodata.user = userdetails
            userinfodata.save()
            new_user = authenticate(username=user_form.cleaned_data.get('email'),
                                    password=user_form.cleaned_data.get('password1'),
                                    )
            login(request, new_user)
            return HttpResponseRedirect(reverse("dashboard"))
        else:
            print("Invalid form")
            print(user_form.errors)
    else:
        print('Not post')
        user_form = UserForm()
        userinfo_form = UserProfileForm()
    context = {'user_form':user_form, 'userinfo_form':userinfo_form, 'pageTitle':'Registration Page'}
    return render(request, "dashboard/registration.html", context)

#def jetty_details(request, pk):
#    model = 
    
class JettyDetailsView(DetailView):
    model = Jetty
    template_name = "dashboard/jetty_detail.html"
    # add other models to this page using context
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(JettyDetailsView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['jetty_pictures'] = Jetty_Pictures.objects.filter(jetty_id= self.kwargs['pk'])
        context['arrival_count'] = Ridership.objects.filter(jetty_id=self.kwargs['pk']).filter(arrival_departure="Arrival").aggregate(Sum('number_of_passengers'))
        context['departure_count'] = Ridership.objects.filter(jetty_id=self.kwargs['pk']).filter(arrival_departure="Departure").aggregate(Sum('number_of_passengers'))
        context['arrival_boat_count'] = Ridership.objects.filter(jetty_id = self.kwargs['pk']).filter(arrival_departure="Arrival").count()
        context['departure_boat_count'] = Ridership.objects.filter(jetty_id=self.kwargs['pk']).filter(arrival_departure="Departure").count()
        context['ridership'] = Ridership.objects.filter(jetty_id= self.kwargs['pk'])
        context['passenger_percent_In'] = round((context['arrival_count']['number_of_passengers__sum']/(context['arrival_count']['number_of_passengers__sum'] + context['departure_count']['number_of_passengers__sum'])) *100, 1)
        context['boat_percent_In'] = round((context['arrival_boat_count']/(context['arrival_boat_count'] + context['departure_boat_count'])) *100, 1)
        context['jetty_supervisors'] = Jetty_Supervisors.objects.filter(jetty_id= self.kwargs['pk'])
        context['passengers_in_list'] = Ridership.objects.filter(jetty_id=self.kwargs['pk']).filter(arrival_departure="Arrival")
        passengerArrival = Ridership.objects.filter(jetty_id=self.kwargs['pk']).filter(arrival_departure="Arrival")
        passengerList = passengerArrival.annotate(year=TruncYear('arrival_departure_time')).values('year').annotate(Sum('number_of_passengers')).order_by('year')
        passengerDeparture = Ridership.objects.filter(jetty_id=self.kwargs['pk']).filter(arrival_departure="Departure")
        passengerDepartureList = passengerDeparture.annotate(year=TruncYear('arrival_departure_time')).values('year').annotate(Sum('number_of_passengers')).order_by('year')
        labels = [eachyear['year'].strftime('%Y') for eachyear in passengerList]
        passengerInCount = [num['number_of_passengers__sum'] for num in passengerList]
        labelsOut = [eachyear['year'].strftime('%Y') for eachyear in passengerDepartureList]
        passengerOutCount = [out['number_of_passengers__sum'] for out in passengerDepartureList]
        context['passenger_in'] = {'label_in': labels, 'passenger_in':passengerInCount,'label_out':labelsOut, 'passenger_out':passengerOutCount}
        # Bathymetry data for jetty
        bathy = pd.read_csv(Jetty_Bathymetry.objects.get(jetty_id= self.kwargs['pk']).bathymetry.path)
        bathy_x = np.array(bathy.X)
        bathy_y = np.array(bathy.Y)
        bathy_z = np.array(bathy.Z)
        bathy_xi = np.linspace(bathy_x.min(), bathy_x.max(), 100)
        bathy_yi = np.linspace(bathy_y.min(), bathy_y.max(), 100)
        bathy_X, bathy_Y = np.meshgrid(bathy_xi, bathy_yi)
        bathy_Z = griddata((bathy_x, bathy_y), bathy_z,( bathy_X, bathy_Y), method='nearest', fill_value= 0.0)
        context['bathy_data'] = {'x':bathy_xi.tolist(), 'y': bathy_yi.tolist(), "z":bathy_Z.tolist()}

        # Prepare travel data for frontend. Create a function for this later
        tripArrival = passengerArrival.values('arrival_departure_location').annotate(total= Count('arrival_departure_location')).order_by('total')
        tripDeparture= passengerDeparture.values('arrival_departure_location').annotate(total= Count('arrival_departure_location')).order_by('total')
        tripArrivalLocation = [element['arrival_departure_location'] for element in reversed(tripArrival)]
        tripArrivalTotal = [element['total'] for element in reversed(tripArrival)]
        tripDepartureLocation = [element['arrival_departure_location'] for element in reversed(tripDeparture)]
        tripDepartureTotal = [element['total'] for element in reversed(tripDeparture)]
        context['tripData'] = {}
        return context

class JettyListView(ListView):
    model = Jetty


def total_jetty (request):
    totalJetty = Jetty.objects.all().count()
    return HttpResponse(totalJetty)


def jetty_dataset(request):
    bathy = serialize('geojson', Jetty.objects.all())
    return HttpResponse(bathy, content_type= 'json')

def route_dataset(request):
    routes = serialize('geojson', Route.objects.all())
    return HttpResponse(routes, content_type = 'json')


def upload_csv(request):
    data = {}
    if "GET" == request.method:
        return render(request, "dashboard/upload_csv.html", data)
    # if not GET, then proceed
    try:
        csv_file = request.FILES["csv_file"]
        if not csv_file.name.endswith('.csv'):
            #messages.error(request,'File is not CSV type')
            return HttpResponseRedirect(reverse("myapp:upload_csv"))
        #if file is too large, return
        if csv_file.multiple_chunks():
			#messages.error(request,"Uploaded file is too big (%.2f MB)." % (csv_file.size/(1000*1000),))
            return HttpResponseRedirect(reverse("myapp:upload_csv"))
        
        file_data = csv_file.read().decode("utf-8")		
        lines = file_data.split("\n")
		#loop over the lines and save them in db. If error , store as string and then display
        for line in lines:						
            fields = line.split(",")
            data_dict = {}
            data_dict["name"] = fields[0]
            data_dict["start_date_time"] = fields[1]
            data_dict["end_date_time"] = fields[2]
            data_dict["notes"] = fields[3]
            try:
                print(data_dict)
            except:
                print('No show')
    except Exception as e:
        logging.getLogger("error_logger").error("Unable to upload file. "+repr(e))
        messages.error(request,"Unable to upload file. "+repr(e))

    return HttpResponseRedirect(reverse("myapp:upload_csv"))
