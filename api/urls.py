from django.urls import path
from .views import CodeConverterView,GithubAnalyzerView
urlpatterns = [
    path('convert/', CodeConverterView.as_view(), name='convert-code'),
    path('analyze-github/', GithubAnalyzerView.as_view(), name='analyze-github'),
]
