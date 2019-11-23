
'''
Token non reconnu dans l'analyse d'une expression
'''

class ExpressionError(Exception):
    def __init__(self, message, errors = None):

        # Call the base class constructor with the parameters it needs
        super().__init__(message)

        # Now for your custom code...
        self.errors = errors