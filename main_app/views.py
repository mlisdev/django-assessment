from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, DeleteView
from .models import Widget



# Create your views here.
def index(request):
    widgets = Widget.objects.all()
    totalWidgets = 0
    for widget in widgets:
            totalWidgets += widget.quantity 
    return render(request, 'index.html', { 'widgets': widgets, 'totalWidgets': totalWidgets })

class WidgetCreate(CreateView):
    model = Widget
    fields = "__all__"

def delete_widget(request, id):
    Widget.objects.get(id=id).delete()
    return redirect('/')