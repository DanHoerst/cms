from django import template
from django.db.models import get_model

def do_latest_content(parser, token):
    bits = token.contents.split()
    # Checks to make sure that there are 5 words in the tag
    if len(bits) != 5:
        raise template.TemplateSyntaxError("'get_latest_content' tag takes exactly four arguments")
    model_args = bits[1].split('.')
    # Checks to make sure first argument is appname.model name
    if len(model_args) != 2:
        raise template.TemplateSyntaxError("First argument to 'get_latest_content' must be an 'application name'.'model name' string")
    model = get_model(*model_args)
    # Checks to make sure model is != none
    if model is None:
        raise template.TemplateSyntaxError("'get_latest_content' tag got an invalid model: %s" % bits[1])
    return LatestContentNode(model, bits[2], bits[4])

class LatestContentNode(template.Node):
    def __init__(self, model, num, varname):
        self.model = model
        # convert num to int
        self.num = int(num)
        self.varname = varname
    
    def render(self, context):
        # uses default manager for Entry.live.all() instances
        context[self.varname] = self.model._default_manager.all()[:self.num]
        return ''

register = template.Library()
register.tag('get_latest_content', do_latest_content)

