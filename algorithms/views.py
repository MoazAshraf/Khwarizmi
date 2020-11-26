from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Algorithm


# Create your views here.
def home(request):
    context = {
        'title': 'Home',
        'algorithms': Algorithm.objects.all()
    }
    return render(request, 'algorithms/home.html', context)


class AlgorithmListView(ListView):
    model = Algorithm
    template_name = 'algorithms/home.html'
    context_object_name = 'algorithms'
    ordering = ['-date_created']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home'
        return context


class AlgorithmDetailView(DetailView):
    model = Algorithm


class AlgorithmCreateView(LoginRequiredMixin, CreateView):
    model = Algorithm
    fields = ['title', 'content']

    def form_valid(self, form):
        # set the author of the algorithm to the current logged in user
        form.instance.author = self.request.user
        return super().form_valid(form)


class AlgorithmUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Algorithm
    fields = ['title', 'content']

    def form_valid(self, form):
        # set the author of the algorithm to the current logged in user
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        # make sure only the author can edit the algorithm
        algorithm = self.get_object()
        if self.request.user == algorithm.author:
            return True
        return False


class AlgorithmDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Algorithm
    success_url = '/'

    def test_func(self):
        # make sure only the author can delete the algorithm
        algorithm = self.get_object()
        if self.request.user == algorithm.author:
            return True
        return False
    
