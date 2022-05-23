from django.urls import path


from . import views

urlpatterns = [
    path('', views.loginUser, name='login'),
    path('home', views.home, name='home'),
    path('logout', views.logoutUser, name='logout'),
    path('report', views.reports, name='reports'),
    path('support', views.support, name='support'),
    path('profile', views.ProfilePage, name='Profile'),
    path('agreements', views.agreements, name='agreements')
    

]

# This does not work 
#     path('reports', views.reports, name='hello'),