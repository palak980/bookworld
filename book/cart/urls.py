#from django.urls import include, path
from rest_framework import routers
#from . import views
from .views import UserViewSet , CartViewSet , OrderItemViewSet

router = routers.DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'cart', CartViewSet)
#router.register(r'delivery-cost', views.DeliveryCostViewSet)
router.register(r'OrderItem',OrderItemViewSet)
#router.register(r'user', views.UserViewSet)

# urlpatterns = [
#     path('', include((router.urls, 'cart'))),

urlpatterns = router.urls
