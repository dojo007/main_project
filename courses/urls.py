from django.contrib import admin


urlpatterns = [
    path('courses', views.index),
    path('courses/create', views.create),
    path('courses/<int:id>', views.comments),
    path('courses/<int:id>/comment', views.create_comment),
    path('courses/<int:id>/delete', views.delete),
]