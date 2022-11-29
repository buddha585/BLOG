""" utils.py """

def get_user_from_request(request):
    """ get request from request or None """
    return request.user if not request.user.is_anonymous else None