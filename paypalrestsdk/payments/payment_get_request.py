# This class was generated on Sat, 27 Jan 2018 13:28:17 CST by version 0.1.0-dev+30efd2 of Braintree SDK Generator
# payment_get_request.py
# @version 0.1.0-dev+30efd2
# @type request
# @data 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
# DO NOT EDIT
import braintreehttp

try:
    from urllib import quote  # Python 2.X
except ImportError:
    from urllib.parse import quote  # Python 3+

class PaymentGetRequest:
    """
    Shows details for a payment, by ID, that has yet to complete. For example, shows details for a payment that was created, approved, or failed.
    """
    def __init__(self, payment_id):
        self.verb = "GET"
        self.path = "/v1/payments/payment/{payment_id}?".replace("{payment_id}", quote(str(payment_id)))
        self.headers = {}
        self.headers["Content-Type"] = "application/json"
        self.body = None

    
