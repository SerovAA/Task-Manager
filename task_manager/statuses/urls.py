from django.urls import path

from task_manager.statuses import views

urlpatterns = [
    path("", views.Statuses_Home.as_view(), name="statuses"),
    path("create/", views.Statuses_Create.as_view(), name="statuses_create"),
    path("<int:status_id>/update/", views.Statuses_Update.as_view(), name="statuses_update"),
    path("<int:status_id>/delete/", views.Statuses_Delete.as_view(), name="statuses_delete"),
]