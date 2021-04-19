from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy

from .forms import SubjectForm, FieldForm
from .models import Subject, Field

from django.views import generic


# Create your views here.
def index(request):
    return HttpResponse("Home")


class SubjectListView(generic.ListView):
    template_name = 'score/list.html'
    context_object_name = 'lst'
    extra_context = {'add_url': reverse_lazy("score:new_subject")}

    def get_queryset(self):
        return Subject.objects.all()


class FieldListView(generic.ListView):
    template_name = 'score/list.html'
    context_object_name = 'lst'
    extra_context = {'add_url': reverse_lazy("score:new_field")}

    def get_queryset(self):
        return Field.objects.all()


class SubjectDetailView(generic.DetailView):
    model = Subject
    template_name = 'score/detail.html'
    context_object_name = 'subject'


class FieldDetailView(generic.DetailView):
    model = Field
    template_name = 'score/detail.html'
    context_object_name = 'model'


class SubjectFormView(generic.edit.FormView):
    template_name = 'score/new.html'
    form_class = SubjectForm
    success_url = '/'

    def form_valid(self, form):
        s = Subject(name=form.cleaned_data['name'])
        s.max_points = form.cleaned_data['max_pkt']
        s.my_points = form.cleaned_data['your_pkt']
        s.save()
        return super().form_valid(form)


class FieldFormView(generic.edit.FormView):
    template_name = 'score/new.html'
    form_class = FieldForm
    success_url = '/'

    def form_valid(self, form):
        f = Field(name=form.cleaned_data['name'])
        f.r1 = form.cleaned_data['r1']
        f.r2 = form.cleaned_data['r2']
        f.save()

        return super().form_valid(form)

