from django import template
from django.template.defaultfilters import safe
from django.utils.safestring import mark_safe
from menu.models import Menu

register = template.Library()

@register.simple_tag
def draw_menu (name_menu):
    items = Menu.objects.filter(name=name_menu).select_related('parent')
    return mark_safe(custom_render(items))



def custom_render(items):
    result_html = '<ul>'
    for item in items:
        result_html += '<li>'
        if item.url:
            result_html += f'<a href="{item.url}">{item.name}</a>'
        elif item.named_url:
            result_html += f'<a href="{item.named_url}">{item.name}</a>'
        else:
            result_html += item.name
        if item.children.exists():
            result_html += custom_render(item.children.all())
        result_html += '</li>'
    result_html += '</ul>'
    return result_html