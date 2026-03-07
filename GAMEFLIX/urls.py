from django.urls import path
from . import views

urlpatterns = [

    path("", views.game_list, name="game_list"),

    path("games/new/", views.GameCreateView.as_view(), name="game_create"),
    path("games/<int:pk>/edit/", views.GameUpdateView.as_view(), name="game_update"),
    path("games/<int:pk>/delete/", views.GameDeleteView.as_view(), name="game_delete"),

    path("plans/", views.plan_list, name="plan_list"),
    path("plans/new/", views.PlanCreateView.as_view(), name="plan_create"),
    path("plans/<int:pk>/edit/", views.PlanUpdateView.as_view(), name="plan_update"),
    path("plans/<int:pk>/delete/", views.PlanDeleteView.as_view(), name="plan_delete"),

    path("rentals/", views.rental_list, name="rental_list"),

    path("rent/<int:game_id>/", views.rent_game, name="rent_game"),
]