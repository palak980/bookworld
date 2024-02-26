

# from django.urls import path,include
# from rest_framework.routers import DefaultRouter
# # from .views import *


# router = DefaultRouter()
# router.register('cg',Catagorys,basename="Catagory"),
# router.register('product',Products,basename="Product"),


# urlpatterns = [
#     path('',include(router.urls)),
#     path('',include(router.urls)),
    
    
# ]

from rest_framework import routers
from .views import CatagoryViewSet , ProductViewSet

router = routers.DefaultRouter()
router.register(r'cat', CatagoryViewSet)
router.register(r'pro', ProductViewSet)
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = router.urls
                            