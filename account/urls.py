from django.urls import path, include
# from .views import AccountListView, AccountDetailView
from .views import AccountView, UserAccountView, UserAccount
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'accounts', AccountView, basename="accounts")

router2 = DefaultRouter()
router2.register(r'account/me', AccountView, basename="user_accounts")




urlpatterns = [
    # path('Account/', AccountListView.as_view(), name='account-list'),
    # path('Account/<int:pk>/', AccountDetailView.as_view(), name='account-detail'),
    path("", include(router.urls)),
    path('account/me/', UserAccount.as_view(), name='user_account')
]