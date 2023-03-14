from django.urls import path
from .views.user_views import SignUp, SignIn, SignOut


urlpatterns = [
    # Restful routing
    path('sign-up/', SignUp.as_view(), name='sign-up'),
    path('sign-in/', SignIn.as_view(), name='sign-in'),
    path('sign-out/', SignOut.as_view(), name='sign-out'),
]
