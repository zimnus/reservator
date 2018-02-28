# -*- coding: utf-8 -*-

import re
from urllib.parse import urlsplit, urlunsplit

from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponse
from django.utils.http import is_safe_url, urlunquote
from django.utils.translation import (
    LANGUAGE_SESSION_KEY, check_for_language
)

from . import settings as MySettings


def lang(request, lang_code):
    next = request.POST.get('next', request.GET.get('next'))
    if (next or not request.is_ajax()) and not is_safe_url(url=next, host=request.get_host()):
        next = request.META.get('HTTP_REFERER')
        if next:
            next = urlunquote(next)  # HTTP_REFERER may be encoded.
        if not is_safe_url(url=next, host=request.get_host()):
            next = '/'
    response = HttpResponseRedirect(next) if next else HttpResponse(status=204)

    if lang_code and check_for_language(lang_code):
        if next:
            # Ниже идёт пояснение MySettings.LANGUAGES
            for code_tuple in MySettings.LANGUAGES:
                settings_lang_code = "/" + code_tuple[0]
                parsed = urlsplit(next)
                if parsed.path.startswith(settings_lang_code):
                    path = re.sub('^' + settings_lang_code, '', parsed.path)
                    next = urlunsplit((parsed.scheme, parsed.netloc, path, parsed.query, parsed.fragment))
            response = HttpResponseRedirect(next)
        if hasattr(request, 'session'):
            request.session[LANGUAGE_SESSION_KEY] = lang_code
        else:
            response.set_cookie(
                settings.LANGUAGE_COOKIE_NAME, lang_code,
                max_age=settings.LANGUAGE_COOKIE_AGE,
                path=settings.LANGUAGE_COOKIE_PATH,
                domain=settings.LANGUAGE_COOKIE_DOMAIN,
            )
    return response