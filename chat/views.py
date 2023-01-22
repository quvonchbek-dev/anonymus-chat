from django.shortcuts import render, redirect, get_object_or_404
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

def message_delete(request, pk):
    message = get_object_or_404(Message, pk=pk)  # Get your current message

    if request.method == 'POST':         # If method is POST,
        message.delete()                     # delete the message.
        return redirect('/')             # Finally, redirect to the homepage.

    return render(request, 'index.html', {'message': message})