import django.contrib.admin.widgets
from django.utils.safestring import mark_safe
from django.core.urlresolvers import reverse
from django.contrib.admin.templatetags.admin_static import static
from django.utils.translation import ugettext as _

class MyRelatedFieldWidgetWrapper(django.contrib.admin.widgets.RelatedFieldWidgetWrapper):

    def get_edit_url(self, object):
        url = reverse('admin:%s_%s_change' %(object._meta.app_label,  object._meta.module_name),  args=[object.id] )
        return u'<a href="%s">Edit %s</a>' %(url,  object.__unicode__())

    def render(self, name, value, *args, **kwargs):

        edit_url = None

        if value:
            try:
                obj = self.rel.to.objects.get(pk=value)
                edit_url = self.get_edit_url(obj)
            except Exception, e:
                pass

        rel_to = self.rel.to
        info = (rel_to._meta.app_label, rel_to._meta.object_name.lower())
        self.widget.choices = self.choices
        output = [self.widget.render(name, value, *args, **kwargs)]
        if self.can_add_related:
            related_url = reverse('admin:%s_%s_add' % info, current_app=self.admin_site.name)
            # TODO: "add_id_" is hard-coded here. This should instead use the
            # correct API to determine the ID dynamically.
            output.append('<a href="%s" class="add-another" id="add_id_%s" onclick="return showAddAnotherPopup(this);"> '
                          % (related_url, name))
            output.append('<img src="%s" width="10" height="10" alt="%s"/></a>'
                          % (static('admin/img/icon_addlink.gif'), _('Add Another')))

            if edit_url:
                output.append('%s' % edit_url)


        if output:
            return mark_safe(''.join(output))


# Monkeypatch it
django.contrib.admin.widgets.RelatedFieldWidgetWrapper = MyRelatedFieldWidgetWrapper