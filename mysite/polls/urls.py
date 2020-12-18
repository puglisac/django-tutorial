from django.urls import path

from . import views

# creates a namespace for the polls urls. ex: href="{url 'polls:index'}"
app_name = 'polls'

# urls for polls app
urlpatterns = [
    # path(url, view function, optional name)
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote')
]