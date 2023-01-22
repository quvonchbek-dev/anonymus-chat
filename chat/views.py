from django.shortcuts import render
from .models import Message
from .forms import MessageForm
from django.http import HttpResponseRedirect


def index(request):

    form = None
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = MessageForm()
    data = Message.objects.all().order_by('created_at')
    return render(request, 'index.html',{'form':form, "data": data})