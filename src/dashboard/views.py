from django.shortcuts import render
from django.shortcuts import redirect


def dashboard(request, *args, **kwargs):
    # print(request.user, request.user.is_authenticated)
    if not request.user.is_authenticated:
        return redirect("auth/google/login/")

    return render(request, "dashboard/main.html")

    # dashboard_html = TEMPLATE_DIR / 'dashboard.html'
    # if not dashboard_html.exists():
    #     return HttpResponse("Dashboard template not found.", status=404)
    # return render(request, 'dashboard.html')


def about(request, *args, **kwargs):
    return render(request, "about.html")
