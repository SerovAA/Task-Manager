from django.urls import path

from task_manager.users import views

urlpatterns = [
    path("", views.Users.as_view(), name="users"),
    path("create/", views.Users_Create.as_view(), name="users_create"),
    path("<int:user_id>/update/", views.Users_Update.as_view(),
         name="users_update"),
    path("<int:user_id>/delete/", views.User_Delete.as_view(),
         name="users_delete"),
]
