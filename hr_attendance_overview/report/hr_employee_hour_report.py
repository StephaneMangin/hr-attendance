# Copyright 2024 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models

from ..models.hr_employee_hour import ONDELETE_SELECTION, TYPE_SELECTION


class HrEmployeeHourReport(models.Model):
    _inherit = "hr.employee.hour.report"

    type = fields.Selection(selection_add=TYPE_SELECTION, ondelete=ONDELETE_SELECTION)

    def where_types(self):
        return super().where_types() + ["attendance"]
