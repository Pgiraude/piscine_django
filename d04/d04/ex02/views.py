from django.shortcuts import render, redirect
import logging
from . import forms

# Create your views here.


def index(request):
    logger = logging.getLogger('history')

    if request.method == 'POST':
        form = forms.History(request.POST)
        if form.is_valid():
            logger.info(form.cleaned_data['history'])
        return redirect('/ex02')
    try:
        f = open(settings.history_logs, 'r')
        historys = [line for line in f.readlines()]
    except:
        historys = []

    return render(request, 'ex02/index.html', {'form': forms.History(), 'historys': historys})