from django.urls import path


from . import views

app_name = 'cmsparser'
urlpatterns = [
    path('', views.view, name='index'),
    path('view/controls/', views.controls, name='controls'),
    path('process/controls/', views.process, name='process'),

            #path('', views.IndexView.as_view(), name='index'),
               # path('<int:pk>/', views.DetailView.as_view(), name='detail'),
               # path('<int:pk>/results', views.ResultsView.as_view(), name='results'),
               # path('<int:question_id>/vote/', views.vote, name='vote')

               ]
