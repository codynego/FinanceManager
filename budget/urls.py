from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BudgetViewAdmin, BudgetViewUser

router = DefaultRouter()
router.register(r'admin/budgets', BudgetViewAdmin, basename='budgets')


urlpatterns = [
    path('', include(router.urls)),
    path('budgets/', BudgetViewUser.as_view())
]