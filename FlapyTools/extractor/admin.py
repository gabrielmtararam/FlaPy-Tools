from django.contrib import admin
from extractor import models as mod
from extractor import forms as forms
from djangoql.admin import DjangoQLSearchMixin
from simple_history.admin import SimpleHistoryAdmin

class AdvancedQueryAdmin(DjangoQLSearchMixin):
    """
    Added advanced query to admin.

    Use this class on the first place on all admin extensions.

    This admin add the DjangoQLSearchMixin class, this class implements
    a SQL like query on all admins. That reduced the query time on big tables
    to 10 minutes to 8 seconds.
    """

    djangoql_completion_enabled_by_default = True
    suggest_options = True


@admin.register(mod.PypiSimpleIndexLinks)
class PypiSimpleIndexLinksAdmin(SimpleHistoryAdmin, DjangoQLSearchMixin):
    """StationCodeType model admin."""

    form = forms.PypiSimpleIndexLinksForm


@admin.register(mod.PypiProcessedLink)
class PypiProcessedLinkAdmin(SimpleHistoryAdmin, DjangoQLSearchMixin):
    """StationCodeType model admin."""

    form = forms.PypiProcessedLinkForm

@admin.register(mod.GlobalProcessorParameters)
class GlobalProcessorParametersAdmin(SimpleHistoryAdmin, DjangoQLSearchMixin):
    """StationCodeType model admin."""

    form = forms.GlobalProcessorParametersForm

@admin.register(mod.PyPiFlapyIndexLinks)
class PyPiFlapyIndexLinksAdmin(DjangoQLSearchMixin, SimpleHistoryAdmin):
    """StationCodeType model admin."""

    form = forms.PyPiFlapyIndexLinksForm
    list_display = (
        "pk",
        "url",
    )


@admin.register(mod.ALIndexLinks)
class ALIndexLinksAdmin(DjangoQLSearchMixin, SimpleHistoryAdmin):
    """StationCodeType model admin."""

    form = forms.ALIndexLinksForm
    list_display = (
        "pk",
        "flapy_link",
        "similar_flapy_link",
        "url",
        "processed_by_flapy_message",
        "processed_by_flapy",
        "short_description",
        "can_run_flapy",
    )
    list_editable = [ 'short_description', 'can_run_flapy']
