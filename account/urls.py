from django.urls import path, include
# from .views import AccountListView, AccountDetailView
from .views import AccountView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'accounts', AccountView, basename="accounts")




urlpatterns = [
    # path('Account/', AccountListView.as_view(), name='account-list'),
    # path('Account/<int:pk>/', AccountDetailView.as_view(), name='account-detail'),
    path("", include(router.urls))
]