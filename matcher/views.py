from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignUpForm, ProfileForm, SportSkillForm, GameForm
from django.contrib.auth import login
from .models import Profile, SportSkill, Game
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .forms import ProfileForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('create_profile')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def create_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('add_sport')
    else:
        form = ProfileForm()
    return render(request, 'create_profile.html', {'form': form})

@login_required
def add_sport(request):
    if request.method == 'POST':
        form = SportSkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.profile = request.user.profile
            skill.save()
            return redirect('home')
    else:
        form = SportSkillForm()
    return render(request, 'add_sport.html', {'form': form})

@login_required
def home(request):
    games = Game.objects.filter(time__gte=timezone.now()).order_by('time')
    return render(request, 'home.html', {'games': games})

@login_required
def create_game(request):
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            game = form.save(commit=False)
            game.creator = request.user
            game.save()
            return redirect('home')
    else:
        form = GameForm()
    return render(request, 'create_game.html', {'form': form})

@login_required
def join_game(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    game.players.add(request.user)
    return redirect('home')

@login_required
def view_local_players(request):
    players = Profile.objects.exclude(user=request.user)
    return render(request, 'view_players.html', {'players': players})

@login_required
def update_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProfileForm(instance=request.user.profile)
    return render(request, 'update_profile.html', {'form': form})

@login_required
def my_profile(request):
    # Get the current user's profile
    user = request.user
    # Render the my_profile template with the user's information
    return render(request, 'my_profile.html', {'user': user})