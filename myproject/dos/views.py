from unittest.mock import DEFAULT
from django.shortcuts import render
from django.core.cache import cache
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseServerError

TIME_FRAME_LENGTH = 5
MAX_REQUESTS = 5
DEFAULT_CNT_VALUE = -1

def index(request):
    id = request.GET.get('clientId', None)
    if not id:
        return HttpResponseBadRequest("Missing parameter \"clientId\"")

    with cache.lock(id + '_lock'):
        cnt = cache.get(id, DEFAULT_CNT_VALUE)
        if cnt == DEFAULT_CNT_VALUE:
            cache.set(id, 0, TIME_FRAME_LENGTH)
        cache.incr(id)

    if cnt < MAX_REQUESTS:
        return HttpResponse("Client {} requests left {}".format(id, MAX_REQUESTS - (cnt + 1)))

    serverError = HttpResponseServerError("Client {} blocked. ".format(id))
    serverError.status_code = 503
    return serverError
