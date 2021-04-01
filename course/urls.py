from django.urls import path
from .views import NewCourse,ViewCourse
urlpatterns=[
    path("new/",NewCourse.as_view(),name="course-new"),
    path("view/",ViewCourse.as_view(),name="course-view")

]