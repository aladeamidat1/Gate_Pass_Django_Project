from django.urls import path

from resident import views

urlpatterns = [
    path('add/house', views.add_house, name='add_house'),

    path('invite', views.create_invite, name='create_invite'),
    # path('register',views.CreateUserView.as_view(), name='register'),
    #path('house/<int:house_number>', views.view_house, name='view_house'),
]
