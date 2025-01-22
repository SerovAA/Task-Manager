from django.urls import path

from task_manager.tasks import views

urlpatterns = [
    path("", views.TaskHome.as_view(), name="tasks"),
    path("create/", views.TaskCreate.as_view(), name="create_task"),
    path("<int:task_id>/", views.TaskShow.as_view(), name="task"),
    path("<int:task_id>/update/", views.TaskUpdate.as_view(),
         name="task_update"),
    path("<int:task_id>/delete/", views.TaskDelete.as_view(),
         name="task_delete"),
]