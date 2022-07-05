from os import name
from django.urls import path
from dashboard.views import JettyDetailsView, logon, route_dataset, jetty_dataset, DashboardView, index, user_logout, KeplerDashboardView, SlideoutView, AppearView, signup, registration_view, landingView, JettyDetailsView, JettyListView, upload_csv
from django.contrib.auth.decorators import login_required, permission_required


# Create the views here
urlpatterns = [
    path("", landingView.as_view(), name='homepage'),
    path('login/', logon.as_view(), name= 'login'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('signout/', user_logout, name = "signout"),
    path('kepler/', KeplerDashboardView.as_view(), name = "kepler"),
    path('slideout/', SlideoutView.as_view(), name='slideout'),
    path('appear/',AppearView.as_view(), name= "appear"),
    path('register/', registration_view, name= 'register'),
    path('jetty_data/', jetty_dataset, name = 'jetty_data'),
    path('route_data/', route_dataset, name = 'route_data'),
    path('jetty/', JettyListView.as_view(), name = 'jetty_list'),
    path('jetty/<int:pk>/', JettyDetailsView.as_view(),name= "jetty_page"),
    path('upload/csv/', upload_csv, name='upload_csv'),
]