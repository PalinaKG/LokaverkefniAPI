from django.urls import path
import Subject.views as views
urlpatterns = [
    path('subject/', views.SubjectModel.as_view(), name = 'api_subject'),
]