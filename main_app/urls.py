from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('widgets/addwidget/', views.WidgetCreate.as_view(), name="add_widget"),
    path('deletewidget/<int:id>', views.delete_widget, name='delete_widget')
]