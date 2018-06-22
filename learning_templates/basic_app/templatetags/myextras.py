from django import template

register = template.Library()


def xyz(val,arg):
    return val.replace(arg,"")


register.filter('cuts',xyz)