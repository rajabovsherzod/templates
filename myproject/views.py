from django.shortcuts import render

def index(request):
    return render(request, 'journal_home.html')

def current_issue(request):
    return render(request, 'current_issue.html')

def all_issues(request):
    return render(request, 'all_issues.html') 