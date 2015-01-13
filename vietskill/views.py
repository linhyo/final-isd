from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from vietskill.models import StaffProfile, Recruitment, Assessment
from vietskill.forms import ProfileForm, RecruitmentForm, AssessmentForm
from vietskill import models
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'vietskill/index.html', {})


def about(request):
    return render(request, 'vietskill/about.html', {})


def profile_all(request):
    profile_list = StaffProfile.objects.all().order_by("name")
    context_dict = {'profiles': profile_list}
    return render(request, 'vietskill/profile_all.html', context_dict)


def profile_detail(request, pk):
    profile = get_object_or_404(StaffProfile, pk=pk)
    context_dict = {'profile': profile}
    return render(request, 'vietskill/profile_detail.html', context_dict)


@login_required
def profile_add(request):
    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=True)
            return redirect('vietskill.views.profile_detail', pk=profile.pk)
        else:
            print form.errors
    else:
        form = ProfileForm()
    # form = ProfileForm()
    context_dict = {'form': form}
    return render(request, 'vietskill/profile_add.html', context_dict)


@login_required
def profile_edit(request, pk):
    profile = get_object_or_404(StaffProfile, pk=pk)
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            profile = form.save(commit=True)
            return redirect('vietskill.views.profile_detail', pk=profile.pk)
        else:
            print form.errors
    else:
        form = ProfileForm(instance=profile)
    context_dict = {'form': form}
    return render(request, 'vietskill/profile_edit.html', context_dict)


@login_required
def profile_delete(request, pk):
    profile = get_object_or_404(StaffProfile, pk=pk)
    profile.delete()
    return redirect('vietskill.views.profile_all')


#Statistics
def teaching_day(request):
    return render(request, 'statistics/teaching_day.html', {})


def online_day(request):
    return render(request, 'statistics/online_day.html', {})


def absent_day(request):
    return render(request, 'statistics/absent_day.html', {})


def mistake(request):
    return render(request, 'statistics/mistake.html', {})


def recruit_index(request):
    posts = Recruitment.objects.all().order_by('release_date')
    context_dict = {'posts': posts}
    return render(request, 'vietskill/recruitment.html', context_dict)


@login_required
def recruit_add(request):
    if request.method == "POST":
        form = RecruitmentForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return recruit_index(request)
    else:
        form = RecruitmentForm()
    return render(request, 'vietskill/recruitment_edit.html', {'form': form})


@login_required
def recruit_edit(request, pk):
    post = get_object_or_404(models.Recruitment, pk=pk)
    if request.method == "POST":
        form = RecruitmentForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('vietskill.views.recruit_index')
    else:
        form = RecruitmentForm(instance=post)
    return render(request, 'vietskill/recruitment_edit.html', {'form': form})


@login_required
def recruit_delete(request, pk):
    post = get_object_or_404(Recruitment, pk=pk)
    post.delete()
    return redirect('vietskill.views.recruit_index')


def assessment(request):
    assess = Assessment.objects.all().order_by('staff')
    context_dict = {'assess': assess}
    return render(request, 'vietskill/assess.html', context_dict)


@login_required
def assess_add(request):
    if request.method == "POST":
        form = AssessmentForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return assessment(request)
    else:
        form = AssessmentForm()
    return render(request, 'vietskill/assess_edit.html', {'form': form})


@login_required
def assess_edit(request, pk):
    assess = get_object_or_404(models.Assessment, pk=pk)
    if request.method == "POST":
        form = AssessmentForm(request.POST, instance=assess)
        if form.is_valid():
            form.save()
            return redirect('vietskill.views.assessment')
    else:
        form = AssessmentForm(instance=assess)
    return render(request, 'vietskill/assess_edit.html', {'form': form})


@login_required
def assess_delete(request, pk):
    assess = get_object_or_404(Assessment, pk=pk)
    assess.delete()
    return redirect('vietskill.views.assessment')



