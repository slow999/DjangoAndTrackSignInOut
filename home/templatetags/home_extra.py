from django import template


register = template.Library()


@register.inclusion_tag('sidebar.html')
def get_home_sidebar(request, perms=None):
    return {'request': request, 'perms': perms}