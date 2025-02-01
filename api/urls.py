from django.urls import path
from .views import CodeConverterView

urlpatterns = [
    path('convert/', CodeConverterView.as_view(), name='convert-code'),
]
