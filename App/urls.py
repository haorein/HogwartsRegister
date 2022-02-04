from App import views
from django.urls import include, path
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'houses', views.HouseViewSet)
router.register(r'students', views.StudentViewSet)
router.register(r'mistake-records', views.MistakeRecordViewSet)
router.register(r'wands', views.WandViewSet)
router.register(r'magics', views.MagicViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]