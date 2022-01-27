from django.urls import path
from . import views

urlpatterns = [
    path('main_page/', views.MainPageView.as_view(), name='main-page'),
    path('delete_employee/<int:id>/', views.DeleteEmployeeView.as_view(), name='delete-view'),
    path('update_employee/<int:id>/', views.UpdateEmployeeView.as_view(), name='update-view'),

]
