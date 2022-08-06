from django.urls import path
from . import views
from .views import EditorView

urlpatterns = [
    path('signup/', views.signup, name='signup'),    
    path('signin/', views.signin, name='signin'),
    path('profile/', views.profile, name='profile'),
    path('friends/', views.friends, name ='friends'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
    path('play/', views.play, name='play'),
    path('results/', views.results, name='results'),

    path('editor/', EditorView.as_view(), name ="editor"),

]
