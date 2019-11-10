import os
from django.shortcuts import render
from django.views.generic import View


class IndexView(View):
    def get(self, request, *args, **kwargs):
        gcp_key = os.environ.get('GCP_KEY')
        return render(request, 'index.html', {'GCP_KEY': gcp_key})


class TestView(View):
    def get(self, request, *args, **kwargs):
        gcp_key = os.environ.get('GCP_KEY')
        return render(request, 'test.html', {'GCP_KEY': gcp_key})

