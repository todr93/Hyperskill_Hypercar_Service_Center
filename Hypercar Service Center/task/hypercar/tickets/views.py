from django.views import View
from django.http.response import HttpResponse
from django.shortcuts import render


menu = [
    ['Change oil', 'change_oil'],
    ['Inflate tires', 'inflate_tires'],
    ['Get diagnostics test', 'diagnostic'],
]

class WelcomeView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('<h2>Welcome to the Hypercar Service!</h2>')


class MenuView(View):
    def get(self, request, *args, **kwargs):
        # menu_links = [[menu_item, menu_item.replace(" ", "_").lower()] for menu_item in menu]
        return render(request, template_name='tickets/menu.html', context={'menu': menu})
