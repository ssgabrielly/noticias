from django.shortcuts import render

def post_list(request):
    return render(request, 'noticias/post_list.html', {})