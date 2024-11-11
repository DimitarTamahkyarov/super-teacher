

from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, resolve_url, redirect
from django.views.generic import ListView
from pyperclip import copy
from SuperTeacher.accounts.models import TeacherProfile
from SuperTeacher.common.forms import CommentForm

def index(request):
    return render(request, 'common/index.html')


class DashboardView(ListView):
    model = get_user_model()
    context_object_name = 'user'
    template_name = 'common/dashboard.html'


def share_functionality(request, profile_id: int):
    copy(request.META.get('HTTP_HOST') + resolve_url('profile-details', profile_id))

    return redirect(request.META.get('HTTP_REFERER') + f'#{profile_id}')


@login_required
def comment_functionality(request, profile_id: int):
    if request.POST:
        teacher = TeacherProfile.objects.get(pk=profile_id)
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.to_teacher = teacher
            comment.user = request.user
            comment.save()

        return redirect(request.META.get('HTTP_REFERER') + f'#{profile_id}')
