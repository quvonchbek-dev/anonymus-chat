from django.shortcuts import render, redirect, get_object_or_404
from .models import Message
from .forms import MessageForm
from django.http import HttpResponseRedirect


def index(request):

    form = None
    if request.method == "POST":
        form = MessageForm(request.POST)
        print()
        if form.is_valid() and "body=" in str(request.read()):
            form.save()
            return HttpResponseRedirect('/')
        message = get_object_or_404(Message, pk=request.POST.__getitem__("id"))
        message.delete()
        return redirect('/')
    else:
        form = MessageForm()
    messages = Message.objects.all().order_by('created_at')
    return render(request, 'index.html',{'form':form, "messages": messages})
