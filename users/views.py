from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from .forms import UserSignupForm, UserUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import UpdateView, DetailView
from .models import Profile


def signup(request):
    if request.user.is_authenticated:
        return redirect('logout')   # logout before signing up
    else:
        if request.method == 'POST':
            form = UserSignupForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, f"Your account has been created! You are now able to login.")
                return redirect('login')
        else:
            form = UserSignupForm()
        return render(request, 'users/signup.html', {'form': form})


def login(request, *args, **kwargs):
    if request.user.is_authenticated:
        return redirect('home')     # if logged in go to home
    else:
        return auth_views.LoginView.as_view(template_name='users/login.html')(request, *args, **kwargs)


class ProfileDetailView(DetailView):
    model = Profile
    fields = ['display_name', 'bio', 'image']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['algorithms'] = self.get_object().user.algorithm_set.order_by('-date_created')
        return context


class ProfileUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Profile
    template_name = "users/profile_settings.html"
    fields = ['display_name', 'bio', 'image']

    def test_func(self):
        # make sure only the user can edit their profile
        profile = self.get_object()
        if self.request.user == profile.user:
            return True
        return False