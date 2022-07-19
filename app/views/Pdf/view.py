from django.http import HttpResponse
from django.views.generic import View
from app.service_provider import app_service_provider

from django.template.loader import get_template
from app.utiles.utility import render_to_pdf


# Creating our view, it is a class based view
class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        # application = app_service_provider.application_management_service().get_application(application_id)
        # context = {
        #     'application': application
        # }
        pdf = render_to_pdf('exam_slip.html')

        # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')