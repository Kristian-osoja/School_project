from django.shortcuts import render
from .models import TodoItem

def home(request):
    query = request.GET.get("q", "").lower()

    employees = [
        {'name': 'Al Beback', 'email': 'al.beback@company.com', 'phone': '555-000-1111', 'age': 34, 'photo': 'myapp/images/AlBeback.jpg', 'position': 'Master of Comebacks'},
        {'name': 'Justin Case', 'email': 'justin.case@company.com', 'phone': '555-000-2222', 'age': 29, 'photo': 'myapp/images/JustinCase.webp', 'position': 'Emergency Preparedness Officer'},
        {'name': 'Sue Flay', 'email': 'sue.flay@company.com', 'phone': '555-000-3333', 'age': 41, 'photo': 'myapp/images/SueFlay.jpg', 'position': 'Chief Disaster Chef'},
        {'name': 'Anita Bug', 'email': 'anita.bug@company.com', 'phone': '555-000-4444', 'age': 27, 'photo': 'myapp/images/AnitaBug.jpg', 'position': 'Bug Exterminator Extraordinaire'},
        {'name': 'Rick OShea', 'email': 'rick.oshea@company.com', 'phone': '555-000-5555', 'age': 38, 'photo': 'myapp/images/RickOShea.jpg', 'position': 'Head of Bounce Back'},
        {'name': 'Paige Turner', 'email': 'paige.turner@company.com', 'phone': '555-000-6666', 'age': 31, 'photo': 'myapp/images/PaigeTurner.webp', 'position': 'Director of Storytelling'},
        {'name': 'Holly Woodwork', 'email': 'holly.woodwork@company.com', 'phone': '555-000-7777', 'age': 35, 'photo': 'myapp/images/HollyWoodwork.jpg', 'position': 'Construction Diva'},
        {'name': 'Warren Peace', 'email': 'warren.peace@company.com', 'phone': '555-000-8888', 'age': 42, 'photo': 'myapp/images/WarrenPeace.jpg', 'position': 'Chief Truce Negotiator'},
        {'name': 'Jonce Na', 'email': 'jonce.na@company.com', 'phone': '555-000-9999', 'age': 28, 'photo': 'myapp/images/JonceNa.webp', 'position': 'On-the-Go Specialist'},
    ]

    if query:
        employees = [
            emp for emp in employees
            if query in emp['name'].lower() or query in emp['position'].lower()
        ]

    return render(request, "home.html", {"employees": employees, "query": query})


def todos(request):
    items = TodoItem.objects.all()
    return render(request, "myapp/todos.html", {"todos": items})
