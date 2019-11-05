from django.urls import include, path
from rest_framework import routers
from . import views
from django.conf.urls import url
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GoodsViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
	url(r'^userdate/(?P<date>.+)/$', views.UserDateViewSet.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]