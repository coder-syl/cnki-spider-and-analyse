from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from backend import views

urlpatterns = [

                  # 爬虫
                  path('testSpider', views.spider, name="testSpider"),

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
