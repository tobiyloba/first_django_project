from django.urls import include, path
from rest_framework import routers
from . import views as v


router = routers.DefaultRouter()

router.register('', v.SongList)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
]