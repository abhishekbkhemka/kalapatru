# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from app.models import OS, Population, Browser, BrowserDownload, ResolutionByYear,Test

from model_report.report import reports, ReportAdmin
from model_report.utils import (usd_format, avg_column, sum_column, count_column,less_than_column)
from LR.models import *


# class OrganizationList(ReportAdmin):
#     model = Organization
#     fields = [
#         'name',
#         'user',
#
#     ]
#     list_group_by = ('name', )
#     list_filter = ('name',)
#     type = 'report'
#     override_field_labels = {
#         'date__year': lambda x, y: _('Year'),
#         'date__month': lambda x, y: _('Month'),
#         'date__day': lambda x, y: _('Day'),
#     }
#
# reports.register('OrganizationList-by-Name', OrganizationList)

# def transporter__name(report, field):
#     return _("[transporter] name")

# def browser__name_label(report, field):
#     return _("[Browser] Name")


class ForwardingNote(ReportAdmin):
    model = ForwardingNote
    fields = [
        'id',
        'billDates',
        'transporter__name',
        'transporter__contactNumber',
        'transporterStation',
        'customer',
        'createdDate',
        'billNo',
        'billValues',
        'cases',
        'marka',
        'permitNo',
        'consignor',
        'commodity',
        'isDispatched',
        'company',
        'company__name',
        'fnDate',
        'transporter',

    ]

    list_group_by = ('commodity','permitNo','marka','billValues','billNo','transporterStation','billDates','transporter','customer','createdDate','cases','consignor','company','isDispatched','fnDate' )
    list_filter = ('transporter','customer','createdDate','cases','consignor','company','isDispatched','fnDate')
    type = 'report'
    override_field_labels = {
        'date__year': lambda x, y: _('Year'),
        'date__month': lambda x, y: _('Month'),
        'date__day': lambda x, y: _('Day'),
        'transporter__contactNumber':'Transporter Contact Number',
        'transporter__name':'Transporter Name',
        'transporter':'TransporterId',
        'company__name':'Company Name',
        'company':'CompanyId'
    }

reports.register('ForwardingNote', ForwardingNote)

import datetime
def forwardingNote__fnDate(value, instance):
    res = 'NA'
    if len(value)>0:
        res = value[0].strftime("%d-%m-%y")
    return _(res)



class Dispatch(ReportAdmin):
    model = Dispatch
    fields = [
        'date',
        'forwardingNote',
        'forwardingNote__fnDate',
        'vanNo',
        'name',
        'remarks',
        'isLocked',
    ]

    list_group_by = ('date','forwardingNote','vanNo' )
    list_filter = ('date','forwardingNote','vanNo','name','remarks','isLocked',)
    type = 'report'
    override_field_labels = {
        'forwardingNote':'forwardingNoteId',
        'forwardingNote__fnDate':'forwardingNote FN Date',

    }
    override_field_formats = {

                'forwardingNote__fnDate': forwardingNote__fnDate,
            }

reports.register('Dispatch', Dispatch)













# class ResolutionByYearReport(ReportAdmin):
#     model = ResolutionByYear
#     fields = [
#         'date',
#         'date__year',
#         'date__month',
#         'date__day',
#         'resolution',
#         'percentage',
#     ]
#     list_group_by = ('date__year', 'date__month',)
#     list_filter = ('resolution',)
#     type = 'report'
#     override_field_labels = {
#         'date__year': lambda x, y: _('Year'),
#         'date__month': lambda x, y: _('Month'),
#         'date__day': lambda x, y: _('Day'),
#     }
#
#
# reports.register('resolution-by-year-report', ResolutionByYearReport)
#
# class TestReport(ReportAdmin):
#     model = Test
#     fields = [
#         'fName',
#         'lName',
#         'address',
#         'city',
#         'state',
#         'country',
#         'age',
#     ]
#     list_group_by = ('fname', 'fName',)
#     list_filter = ('fName','lName','address','city')
#     type = 'report'
#     override_field_labels = {
#         # 'date__year': lambda x, y: _('Year'),
#         # 'date__month': lambda x, y: _('Month'),
#         # 'date__day': lambda x, y: _('Day'),
#     }
#
#
# reports.register('Test-report', TestReport)
#
#
#
# class AddressByAgeReport(ReportAdmin):
#     model = Test
#     fields = [
#         'fName',
#         'lName',
#         'address',
#         'city',
#         'state',
#         'country',
#         'age',
#     ]
#     list_filter = ('age',)
#     list_order_by = ('age',)
#     list_group_by = ('age',)
#     type = 'report'
#     # group_totals = {
#     #     'age': avg_column,
#     #     # 'lName': avg_column
#     # }
#     report_less_than = {
#         'age': less_than_column,
#         # 'lName': sum_column
#     }
#     # override_field_formats = {
#     #     'fName': men_format,
#     #     'lName': women_format,
#     # }
#     # override_field_labels = {
#     #     'fName': men_label,
#     # }
#
#
# reports.register('Address-By-Age', AddressByAgeReport)
#
#
#
#
#
#
#
#
#
# class OSReport(ReportAdmin):
#     model = OS
#     fields = [
#         'company__name',
#         'name',
#     ]
#     list_filter = ('company__name',)
#     type = 'report'
#
#
# reports.register('os-report', OSReport)
#
#
# def men_format(value, instance):
#     return _(u'M %s' % value)
#
#
# def women_format(value, instance):
#     return _(u'F %s' % value)
#
#
# def men_label(report, field):
#     return _("Mens")
#
#
# class PopulationReport(ReportAdmin):
#     model = Population
#     fields = [
#         'age',
#         'men',
#         'women',
#         'self.total',
#     ]
#     list_filter = ('age',)
#     list_order_by = ('age',)
#     list_group_by = ('age',)
#     type = 'report'
#     group_totals = {
#         'men': avg_column,
#         'women': avg_column
#     }
#     report_totals = {
#         'men': sum_column,
#         'women': sum_column
#     }
#     override_field_formats = {
#         'men': men_format,
#         'women': women_format,
#     }
#     override_field_labels = {
#         'men': men_label,
#     }
#
#
# reports.register('population-report', PopulationReport)
#
#
# def browser__name_label(report, field):
#     return _("[Browser] Name")
#
#
# def os__name_label(report, field):
#     return _("[OS] Name")
#
#
# def os__company__name_label(report, field):
#     return _("[OS > Company] Name")
#
# # browser = models.ForeignKey(Browser)
# class BrowserDownloadReport(ReportAdmin):
#     model = BrowserDownload
#     fields = [
#         'download_date',
#         'browser__name',
#         'os__name',
#         'os__company__name',
#         'username',
#         'download_price',
#     ]
#     list_filter = ('browser__name', 'os__name', 'download_date', 'os__company__name',)
#     list_order_by = ('download_date',)
#     list_group_by = ('browser__name', 'os__name', 'os__company__name',)
#     list_serie_fields = ('browser__name', 'os__name', 'download_price')
#     type = 'chart'
#     override_field_labels = {
#         'browser__name': browser__name_label,
#         'os__name': os__name_label,
#         'os__company__name': os__company__name_label,
#     }
#     override_field_formats = {
#         'download_price': usd_format,
#     }
#     group_totals = {
#         'download_date': count_column,
#         'download_price': avg_column,
#     }
#     report_totals = {
#         'download_date': count_column,
#         'download_price': sum_column,
#     }
#     chart_types = ('pie', 'column', 'line')
#
#
# reports.register('browser-download-report', BrowserDownloadReport)
#
#
# class BrowserReport(ReportAdmin):
#     title = _('Browser with Inline Downloads')
#     model = Browser
#     fields = [
#         'name',
#     ]
#     inlines = [BrowserDownloadReport]
#     list_order_by = ('name',)
#     type = 'report'
#
#
# reports.register('browser-report', BrowserReport)
#
#
# def list_to_ul_format(rvalue, instance):
#     if instance.is_value:
#         return '<ul>%s</ul>' % ''.join(['<li>%s</li>' % v for v in rvalue])
#     return rvalue.value[0]
#
#
# def list_to_value(rvalue, instance):
#     return rvalue[0] if len(rvalue) else None
#
#
# def run_on__name_label(report, field):
#     return _("[OS] Name")
#
#
# def supports__name_label(report, field):
#     return _("[Support] Name")
#
#
# def filter_supports__name(report, values):
#     return values.exclude(name__icontains='css')
#
#
# class BrowserListReport(ReportAdmin):
#     title = _('Browser List')
#     model = Browser
#     fields = [
#         'name',
#         'run_on__name',
#         'supports__name',
#         'is_active',
#     ]
#     list_group_by = ('run_on__name', 'supports__name',)
#     list_filter = ('run_on__name', 'supports__name',)
#     list_order_by = ('name',)
#     type = 'chart'
#     chart_types = ('pie', 'column')
#     list_serie_fields = ('run_on__name', 'name')
#     override_field_formats = {
#         'run_on__name': list_to_ul_format,
#         'supports__name': list_to_ul_format,
#     }
#     override_field_labels = {
#         'run_on__name': run_on__name_label,
#         'supports__name': supports__name_label,
#     }
#     group_totals = {
#         'run_on__name': count_column,
#         'supports__name': count_column
#     }
#     report_totals = {
#         'supports__name': sum_column
#     }
#     override_field_filter_values = {
#         'supports__name': filter_supports__name
#     }
#     override_field_choices = {
#         'supports__name': filter_supports__name
#     }
#
#
# reports.register('browser-list-report', BrowserListReport)
