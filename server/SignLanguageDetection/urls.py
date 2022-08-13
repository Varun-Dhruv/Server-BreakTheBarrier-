

from django.urls import path, include
from .views import Home,videoFeed,webcam_feed
urlpatterns = [
    # path('api/',),
    
    path('', Home),
    path('videoFeed',videoFeed,name="videoFeed" ),
   

]
