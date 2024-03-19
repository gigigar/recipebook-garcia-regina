from django.urls import path
from .views import RecipeDetailsView, RecipeListView

urlpatterns = [
    path('', RecipeListView.as_view(), name='recipe_list'),
    path('list/', RecipeListView.as_view(), name='recipe_list'),
    path('<int:pk>/detail', RecipeDetailsView.as_view(), name='recipe_details'),
]

app_name = 'ledger'