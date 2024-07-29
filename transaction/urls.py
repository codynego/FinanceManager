from django.urls import path, include
# from .views import AccountListView, AccountDetailView
from .views import TransactionViewAdmin
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'transactions', TransactionViewAdmin, basename="transactions")



urlpatterns = [
    path("", include(router.urls)),

]