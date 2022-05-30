from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import gettext_lazy as _

@plugin_pool.register_plugin
class HeaderPlugin(CMSPluginBase):
    model = CMSPlugin
    name = _("Portal Header Plugin")
    render_template = "portal_header_plugin.html"
    cache = False

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        return context

@plugin_pool.register_plugin
class MenuPlugin(CMSPluginBase):
    model = CMSPlugin
    name = _("Portal Menu Plugin")
    render_template = "portal_menu_plugin.html"
    cache = False

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        return context
        
@plugin_pool.register_plugin
class ContentPlugin(CMSPluginBase):
    model = CMSPlugin
    name = _("Portal Content Plugin")
    render_template = "portal_content_plugin.html"
    cache = False

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        return context