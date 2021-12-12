from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_events, name='events'),
    path('<int:event_id>/', views.event_detail, name='event_detail'),
    path('add/', views.add_event, name='add_event'),
    path('edit/<int:event_id>/', views.edit_event, name='edit_event'),
    path('delete/<int:event_id>/', views.delete_event, name='delete_event'),
    path('add_pick/', views.add_pick, name='add_pick'),
    path('edit_pick/<int:pick_id>/', views.edit_pick, name='edit_pick'),
    path('delete_pick/<int:pick_id>/', views.delete_pick, name='delete_pick'),
]
