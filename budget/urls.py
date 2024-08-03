from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BudgetViewAdmin

router = DefaultRouter()
router.register(r'', BudgetViewAdmin, basename='budgets')


urlpatterns = [
    path('', include(router.urls))
]