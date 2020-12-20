from django.urls import path

from . import views

# creates a namespace for the polls urls. ex: href="{url 'polls:index'}"
app_name = 'polls'

# urls for polls app
urlpatterns = [
    # path(url, view function, optional name)
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote')
]