from django.views.generic import TemplateView


class AboutView(TemplateView):
     template_name = "about.html"


class BookView(TemplateView):
     template_name = "book.html"


class IndexView(TemplateView):
     template_name = "index.html"


class MenuView(TemplateView):
     template_name = "menu.html"