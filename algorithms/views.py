from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    FormView,
)
from .models import Algorithm, Comment
from .forms import CommentCreateForm


class AlgorithmListView(ListView):
    model = Algorithm
    template_name = 'algorithms/home.html'
    context_object_name = 'algorithms'
    ordering = ['-date_created']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home'
        return context


def algorithm_detail(request, pk):
    template_name = 'algorithms/algorithm_detail.html'
    # TODO: try get_object_or_404
    algorithm = Algorithm.objects.get(pk=pk)
    user = request.user
    comments = algorithm.comment_set.order_by("-date_created")      # list of algorithm comments
    if request.method == 'POST':
        comment_form = CommentCreateForm(request.POST)      # the comment creation form
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)   # create the object but don't save
            new_comment.algorithm = algorithm               # set the algorithm
            new_comment.author = user                       # set the user
            new_comment.save()                              # save the comment
            return redirect(algorithm)
    else:
        comment_form = CommentCreateForm()

    context = {
        'object': algorithm,
        'comment_form': comment_form,
        'comments': comments
    }

    return render(request, template_name, context)


# class AlgorithmDetailView(FormView):
#     template_name = 'algorithms/algorithm_detail.html'

#     def get_context_data(self, *args, **kwargs):
#         context = super().get_context_data(**kwargs)

#         # the comment creation form
#         comment_form = CommentCreateForm()
#         context['comment_form'] = comment_form

#         # list of algorithm comments
#         algorithm = self.get_object()
#         comments = algorithm.comment_set.order_by("-date_created")
#         context['comments'] = comments

#         return context

    # def form_valid(self, form):
    #     algorithm = self.get_object()
    #     comment_content = form.cleaned_data.get("content")
    #     comment_author = self.request.user
    #     Comment.objects.create(author=comment_author, content=comment_content, algorithm=algorithm) # automatically saves it in the database
    #     return super().form_valid(form)

    # def test_func(self):
    #     # make sure only the author can edit the algorithm
    #     algorithm = self.get_object()
    #     if self.request.user == algorithm.author:
    #         return True
    #     return False


class AlgorithmCreateView(LoginRequiredMixin, CreateView):
    model = Algorithm
    fields = ['title', 'description', 'code']

    def form_valid(self, form):
        # set the author of the algorithm to the current logged in user
        form.instance.author = self.request.user
        return super().form_valid(form)


class AlgorithmUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Algorithm
    fields = ['title', 'description', 'code']

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
    
