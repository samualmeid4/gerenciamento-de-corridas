from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
                                            TokenObtainPairView, # login: devolve access + refresh
                                            TokenRefreshView, # renova o access usando o refresh
                                            )
from backend import views
from backend.views import LoginView

router = DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),

    path('signup/', views.signup),
    # path('login/', TokenObtainPairView.as_view(), name='login'),
    path('login/', LoginView.as_view(), name='login'),
    path('refresh/', TokenRefreshView.as_view(), name='refresh'),
    path('perfil/', views.perfil),
    path('', include(router.urls)),
]
