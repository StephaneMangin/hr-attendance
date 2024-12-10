# Copyright 2024 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models

from ..models.hr_employee_hour import ONDELETE_SELECTION, TYPE_SELECTION


class HrEmployeeAttendanceReport(models.Model):
    _name = "hr.employee.attendance.report"
    _description = "Employee Attendance Report"
    _inherit = "hr.employee.hour.report.abstract"
    _auto = False  # Will be processed in init method

    type = fields.Selection(selection_add=TYPE_SELECTION, ondelete=ONDELETE_SELECTION)
    check_in = fields.Datetime()
    check_out = fields.Datetime()

    def select_hook_custom_fields(self):
        return """
            SUM(heh.days_qty) AS days_qty_abs,
            SUM(heh.hours_qty) AS hours_qty_abs,
            SUM(heh.days_qty) AS days_qty,
            SUM(heh.hours_qty) AS hours_qty,
            heh.check_in,
            heh.check_out,
        """

    def where_types(self):
        return ["attendance"]

    def group_by_hook_custom_fields(self):
        return "heh.check_in, heh.check_out,"
