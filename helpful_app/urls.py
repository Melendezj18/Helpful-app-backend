from django.urls import path
from .views.user_views import SignUp, SignIn, SignOut
from .views.house_views import HousesView, HouseDetailView
from .views.appointment_views import AppointmentsView,AppointmentDetailView


urlpatterns = [
    # Restful routing
    path('houses/', HousesView.as_view()),
    path('houses/<int:pk>/', HouseDetailView.as_view()),
    path('appointments/', AppointmentsView.as_view()),
    path('appointments/<int:pk>/', AppointmentDetailView.as_view()),
    path('sign-up/', SignUp.as_view(), name='sign-up'),
    path('sign-in/', SignIn.as_view(), name='sign-in'),
    path('sign-out/', SignOut.as_view(), name='sign-out'),
]
