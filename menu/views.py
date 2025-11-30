from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = "menu/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_path'] = self.request.path
        return context
