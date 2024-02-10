from django.http import HttpResponse

class StripeWH_Handler:
    """ Class to handle stripe webhooks """
    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """ Handlewebhook events """
        return HttpResponse(
            content=f'Unhandled Webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """ Method to handle succeeded payment intent webhook """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """ Method to handle failed payment intent webhook """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)