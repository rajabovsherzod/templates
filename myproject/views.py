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

def journal_subscriptions(request):
    return render(request, 'sumbit/permissions/journal_subscriptions.html')

def activate_access_token(request):
    return render(request, 'sumbit/permissions/activate_access_token.html')

def permissions_for_our_content(request):
    return render(request, 'sumbit/permissions/permission_for_our_content.html')

def cite_an_article(request):
    return render(request, 'sumbit/permissions/cite_an_article.html')

def about_the_journal(request):
    return render(request, 'about/about_the_journal.html')

def editorial_board(request):
    return render(request, 'about/editorial_board.html') 