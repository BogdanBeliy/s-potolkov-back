from django.urls import path
from .views import *


urlpatterns = [
    path('api/cards/', CardView.as_view(), name='cards'),
    path('api/testimonials/', TestimonialsView.as_view(), name='testimonial'),
    path('api/newclient/', NewClientView.as_view(), name="newClient"),
    path('api/new-potolok-sale/', NewPotolok.as_view(), name='new-potolok'),
]
