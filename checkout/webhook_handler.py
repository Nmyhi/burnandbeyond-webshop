from django.http import HttpResponse

class StripeWH_Handler:
    """ Class to handle stripe webhooks """
    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """ Handlewebhook events """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}'
        )