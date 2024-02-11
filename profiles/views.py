from django.shortcuts import render

def profile(request):
    """ View to display user profile """

    template = 'profiles/profile.html'
    context = {}
    return render(request, template, context)