from django.urls import path
from . import views
from .views import RetailerListView

urlpatterns = [

    path('', views.home, name='ops_app_home'),

    path('ops_admin/', views.ops_splash, name='ops_app_splash'),

    path("ops_admin/retailers/", RetailerListView.as_view(),
         name='ops_app_retailers'),

    path('retailers/<retailer>',
         views.ops_checklist, name='ops_app_checklist'),

    path('ops_admin/orders/',
         views.order_calendar, name='ops_app_calendar'),

    path('orders/upload/',
         views.order_upload, name='ops_app_order_upload'),

]
