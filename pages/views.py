from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def home(request):
    # Mock data so UI renders now
    courses = [
        {"code": "CSCI150", "name": "Intro to Programming"},
        {"code": "CSCI151", "name": "Data Structures"},
        {"code": "CSCI232", "name": "Algorithms"},
    ]
    days = list(enumerate(["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]))

    slots = [
        {"ta": "Emma R.", "ta_username": "emma", "courses": ["CSCI150", "CSCI151"], "day": "Mon", "start": "10:00", "end": "12:00"},
        {"ta": "Luis M.", "ta_username": "luis", "courses": ["CSCI232"], "day": "Tue", "start": "13:00", "end": "15:00"},
        {"ta": "Ava K.",  "ta_username": "ava",  "courses": ["CSCI151"], "day": "Thu", "start": "09:30", "end": "11:00"},
    ]

    course = request.GET.get("course")
    day = request.GET.get("day")
    if course:
        slots = [s for s in slots if course in s["courses"]]
    if day not in (None, ""):
        try:
            idx = int(day)
            day_name = days[idx][1]
            slots = [s for s in slots if s["day"] == day_name]
        except Exception:
            pass

    return render(request, "home.html", {"courses": courses, "days": days, "slots": slots})

def ta_detail(request, username):
    db = {
        "emma": {"name": "Emma R.", "bio": "Python, debugging, patient coach.", "courses": ["CSCI150", "CSCI151"]},
        "luis": {"name": "Luis M.", "bio": "Loves algorithms and proofs.", "courses": ["CSCI232"]},
        "ava":  {"name": "Ava K.",  "bio": "Data structures guru.", "courses": ["CSCI151"]},
    }
    ta = db.get(username)
    return render(request, "ta_detail.html", {"ta": ta})

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "signup.html", {"form": form})
