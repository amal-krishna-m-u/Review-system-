from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def dashboard_view(request):
    # Get user id from session
    user_id = request.session['login_session']

    # Get user object from database
    user = User.objects.get(pk=user_id)

    return render(request, 'dashboard.html', {'user': user})
