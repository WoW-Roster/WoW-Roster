import re

from django import template
from django.urls import NoReverseMatch, reverse

register = template.Library()
HTML_CLASS_ACTIVE, HTML_CLASS_NOT_ACTIVE = "active", ""


def split_url(url, levels):
    return "/".join(url.split("/")[0:levels]) + "/"


@register.simple_tag(takes_context=True)
def is_active(context, view_name, levels=2):
    if not levels:
        try:
            pattern = "^%s$" % reverse(view_name)
        except NoReverseMatch:
            pattern = view_name
        path = context["request"].path
        return HTML_CLASS_ACTIVE if re.search(pattern, path) else HTML_CLASS_NOT_ACTIVE
    levels += 1
    partial_path = split_url(context["request"].path, levels)
    check_paths = [split_url(reverse(url), levels) for url in view_name.split()]
    if partial_path not in check_paths:
        return HTML_CLASS_NOT_ACTIVE
    return HTML_CLASS_ACTIVE
