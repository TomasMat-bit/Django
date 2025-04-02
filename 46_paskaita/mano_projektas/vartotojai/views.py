from django.db.models.fields import return_None
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from .models import Profile

@login_required
def redaguoti_profili(request):
    profilis = request.user.profile
    if request.method == 'POST':
        forma = ProfileForm(request.POST, request.FILES, instance=profilis)
        if forma.is_valid():
            forma.save()
            return redirect('profilis')
    else:
        forma = ProfileForm(instance=profilis)
    return render(request, 'profilis.html', {'forma': forma})

