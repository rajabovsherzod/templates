from django.shortcuts import render

def index(request):
    return render(request, 'journal_home.html')

def current_issue(request):
    return render(request, 'current_issue.html')

def all_issues(request):
    return render(request, 'all_issues.html')

def submission_guidelines(request):
    return render(request, 'sumbit/submission_guidelines.html')

def how_to_access_articles(request):
    return render(request, 'sumbit/permissions/how_to_access_articles.html')

def library_recommendation_form(request):
    return render(request, 'sumbit/permissions/library-recommendation-form.html') 