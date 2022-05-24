from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('plants/', views.plants_index, name='index'),
    path('plants/<int:plant_id>/', views.plants_detail, name='detail'),
    path('plants/create/', views.PlantCreate, name='plants_create'),
    path('plants/<int:pk>/update/', views.PlantUpdate, name='plants_update'),
    path('plants/<int:pk>/delete/', views.PlantDelete, name='plants_delete'),
    path('plants/<int:plant_id>/add_watering/', views.add_watering, name='add_watering'),
    # path('plants/<int:plant_id>/add_photo/', views.add_photo, name='add_photo'),
    path('plants/<int:plant_id>/assoc_fertilizer/<int:fertilizer_id>/', views.assoc_fertilizer, name='assoc_fertilizer'),
    path('plants/<int:plant_id>/unassoc_fertilizer/<int:fertilizer_id>/', views.unassoc_fertilizer, name='unassoc_fertilizer'),
    path('fertilizers/', views.FertilizerList.as_view(), name='fertilizers_index'),
    path('fertilizers/<int:pk>/', views.FertilizerDetail.as_view(), name='fertilizers_detail'),
    path('fertilizers/create/', views.FertilizerCreate.as_view(), name='fertilizers_create'),
    path('fertilizers/<int:pk>/update/', views.FertilizerUpdate.as_view(), name='fertilizers_update'),
    path('fertilizers/<int:pk>/delete/', views.FertilizerDelete.as_view(), name='fertilizers_delete'),
    # path('accounts/signup/', views.signup, name='signup'),
]