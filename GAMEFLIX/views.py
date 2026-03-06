from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Plan
from .models import Game
from .models import Rental


def game_list(request):
    query = request.GET.get("q", "").strip()

    if query:
        games = Game.objects.filter(title__icontains=query).order_by("title")
    else:
        games = Game.objects.all().order_by("title")

    return render(request, "GAMEFLIX/game_list.html", {"games": games, "query": query})


def logout_get(request):
    logout(request)
    return redirect("/")


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/accounts/login/")
    else:
        form = UserCreationForm()

    return render(request, "registration/register.html", {"form": form})


def about(request):
    return render(request, "about.html")


class GameCreateView(CreateView):
    model = Game
    fields = ["title", "platform", "genre", "price_per_rental", "is_active"]
    template_name = "GAMEFLIX/form.html"
    success_url = reverse_lazy("game_list")


class GameUpdateView(UpdateView):
    model = Game
    fields = ["title", "platform", "genre", "price_per_rental", "is_active"]
    template_name = "GAMEFLIX/form.html"
    success_url = reverse_lazy("game_list")


class GameDeleteView(DeleteView):
    model = Game
    template_name = "GAMEFLIX/confirm_delete.html"
    success_url = reverse_lazy("game_list")

def plan_list(request):
    plans = Plan.objects.all().order_by("name")
    return render(request, "GAMEFLIX/plan_list.html", {"plans": plans})

class PlanCreateView(CreateView):
    model = Plan
    fields = ["name", "monthly_price", "is_active"]
    template_name = "GAMEFLIX/form.html"
    success_url = reverse_lazy("plan_list")


class PlanUpdateView(UpdateView):
    model = Plan
    fields = ["name", "monthly_price", "is_active"]
    template_name = "GAMEFLIX/form.html"
    success_url = reverse_lazy("plan_list")


class PlanDeleteView(DeleteView):
    model = Plan
    template_name = "GAMEFLIX/confirm_delete.html"
    success_url = reverse_lazy("plan_list")

def rental_list(request):
    rentals = Rental.objects.all().order_by("-start_date")
    return render(request, "GAMEFLIX/rental_list.html", {"rentals": rentals})
    