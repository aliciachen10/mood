from django.urls import include, path, re_path
from rest_framework import routers
from django.contrib import admin
from . import views
from .views import QuestionViewSet

router = routers.DefaultRouter()
router.register(r'question', QuestionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

# urlpatterns = [
#     path('', views.index, name='index'),
# ]


# urlpatterns = [
#     path('admin/', admin.site.urls),
#     re_path(r'^api/students/$', views.students_list),
#     re_path(r'^api/students/([0-9])$', views.students_detail),
# ]


