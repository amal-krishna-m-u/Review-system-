def logout_view(request):
    request.session.flush()
    return redirect('index')
