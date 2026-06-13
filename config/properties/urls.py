from django.urls import path
from . import views

urlpatterns = [

    path(
        '',
        views.property_list,
        name='property_list'
    ),

    path(
        'add/',
        views.add_property,
        name='add_property'
    ),

    path(
        'my-properties/',
        views.my_properties,
        name='my_properties'
    ),

    path(
        '<slug:slug>/',
        views.property_detail,
        name='property_detail'
    ),

    path(
        'sold/<int:pk>/',
        views.toggle_sold,
        name='toggle_sold'
    ),

    path(
        'delete/<int:pk>/',
        views.delete_property,
        name='delete_property'
    ),

    path(
        'edit/<int:pk>/',
        views.edit_property,
        name='edit_property'
    ),

    path(
        'edit/<int:pk>/',
        views.edit_property,
        name='edit_property'
    ),

    path(
        'image/delete/<int:pk>/',
        views.delete_image,
        name='delete_image'
    ),
]