from django.urls import path
from .views import NewCourse
urlpatterns=[
    path("new/",NewCourse.as_view(),name="course-new")

]