# Copyright 2024 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import _, fields, models

TYPE_SELECTION = [
    ("attendance", _("Check-In")),
]
ONDELETE_SELECTION = {
    "attendance": "set default",
}


class HrEmployeeHour(models.Model):
    _inherit = "hr.employee.hour"

    type = fields.Selection(selection_add=TYPE_SELECTION, ondelete=ONDELETE_SELECTION)
    check_in = fields.Datetime()
    check_out = fields.Datetime()
