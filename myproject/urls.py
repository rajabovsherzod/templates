"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('current-issue/', views.current_issue, name='current_issue'),
    path('all-issues/', views.all_issues, name='all_issues'),
    path('submission-guidelines/', views.submission_guidelines, name='submission_guidelines'),
    path('permissions/how-to-access-articles/', views.how_to_access_articles, name='how_to_access_articles'),
    path('permissions/library-recommendation-form/', views.library_recommendation_form, name='library_recommendation_form'),
    path('permissions/journal-subscriptions/', views.journal_subscriptions, name='journal_subscriptions'),
    path('permissions/activate-access-token/', views.activate_access_token, name='activate_access_token'),
    path('permissions/permissions-for-our-content/', views.permissions_for_our_content, name='permissions_for_our_content'),
    path('permissions/cite-an-article/', views.cite_an_article, name='cite_an_article'),
    path('about-the-journal/', views.about_the_journal, name='about_the_journal'),
    path('editorial-board/', views.editorial_board, name='editorial_board'),
    path('about/society/', views.society, name='society'),
    path('about/indexing/', views.indexing, name='indexing'),
    path('subscribe/', views.subscribe, name='subscribe'),
]
