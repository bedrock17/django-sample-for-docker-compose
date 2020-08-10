from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index")
    , path('signup', views.signup, name="signup")
    , path('write', views.write, name="write")
    , path('list', views.list, name="list")
    , path('listall', views.listAll, name="listAll")
    , path('login', views.userLogin, name="login")
    , path('logout', views.userLogout, name="logout")
    , path('read/<int:id>', views.read, name="read")
    , path('delete/<int:id>', views.delete, name="delete")
    , path('edit/<int:id>', views.edit, name="edit")
]
