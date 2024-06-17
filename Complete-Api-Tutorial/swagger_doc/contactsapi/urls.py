from django.urls import path
from .views import ContactList, ContactDetail

urlpatterns = [
    path('listcreate/',ContactList.as_view()),
    path('listcreatedetail/<int:id>/',ContactDetail.as_view())
]