from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
# Create your views here.


def index(request):
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "months": months,
    })


monthly_challenges = {
    "january": "in january we will run",
    "feburary": "in feburary we will learn",
    "march": "in march we will swim",
    "april": "in april we will teach",
    "may": "in may we will work",
    "june": "in june we will cook",
    "july": None,
    "augest": "in augest we will catch",
    "september": "in september we will play",
    "october": "in october we will eat",
    "november": "in november we will fly",
    "december": None,
}


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    redirect_month = months[month-1]

    redirect_path = reverse("monthly_challenge", args=[redirect_month])

    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month_name": month
        })
    except:
        raise Http404()
