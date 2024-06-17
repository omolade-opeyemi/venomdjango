from django.urls import path, include
from .views import UserList, UserDetail, SnippetList, SnippetDetail, api_root, SnippetHighlight

urlpatterns = [
    path('', api_root),
    path('snippets/<int:pk>/highlight/', SnippetHighlight.as_view()),
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
    path('snippets/', SnippetList.as_view()),
    path('snippets/<int:pk>/', SnippetDetail.as_view()),
    path('api-auth/', include('rest_framework.urls')),
]
