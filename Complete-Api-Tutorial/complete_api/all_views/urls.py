from django.urls import path,include
from . import views

urlpatterns = [
    # function based views urls
    path('poll', views.poll),
    path('poll/<int:pk>/', views.poll_details),
    # class based views urls
    path('pollapiview/', views.PollAPIViews.as_view()),
    path('polldetail/<int:pk>/', views.PollAPIViewsDetail.as_view()),

    # generics based views urls
    path('generics/', views.PolltList.as_view()),
    path('generics/<int:pk>/', views.PolltListDetail.as_view()),
    # authentication urls
    path('auth/', include('rest_framework.urls'))
    
]
