from django.contrib import admin
from django.urls import path
from exam import views

urlpatterns = [
      path("", views.home, name="home"),
    path('admin/', admin.site.urls),

    path('students/', views.student_list, name='student_list'),
    path('students/add/', views.add_student),
    path('students/edit/<int:id>/', views.edit_student),
    path('students/delete/<int:id>/', views.delete_student),

    
    path('conditional_statements/', views.conditional_view),
]
