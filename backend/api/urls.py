from django.urls import path
from django.urls import path, include
from .views import UserViewSet, jettyViewSet, routeViewSet, bathyViewSet, depthViewSet, boundaryViewSet, ridershipViewset, accidentViewset, jettyPictureViewset
from rest_framework import routers


router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('route', routeViewSet)
router.register('jetty', jettyViewSet)
router.register('bathy', bathyViewSet)
router.register('depth', depthViewSet)
router.register("boundary", boundaryViewSet)
router.register('ridership', ridershipViewset)
router.register('accident', accidentViewset)
router.register("jetty_images", jettyPictureViewset)


urlpatterns = router.urls