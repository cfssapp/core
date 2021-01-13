from django.urls import path
from .views import CustomUserCreate, BlacklistTokenUpdateView

from . import views

app_name = 'users'

urlpatterns = [
    path('register/', CustomUserCreate.as_view(), name="create_user"),
    path('logout/blacklist/', BlacklistTokenUpdateView.as_view(),
         name='blacklist'),

    path('login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),

    path('current-user/', views.currentUser.as_view(), name="current_user"),
	path('current-user/<int:pk>/', views.currentUserDetail.as_view(), name="current_user_detail"),
]



