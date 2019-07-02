# Create your views here.


from django.shortcuts import render
from django.http import HttpResponse
"""
def hello(request):
	return render(request, 'blog/hello.html',{})
"""
def post_list(request):
    return render(request, 'blog/post_list.html', {})
