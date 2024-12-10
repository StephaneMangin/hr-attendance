import logging

from odoo import fields, models
from odoo.osv import expression

_logger = logging.getLogger(__name__)


class WizardHrEmployeeHourUpdater(models.TransientModel):
    _inherit = "wizard.hr.employee.hour.updater"

    attendance_hours = fields.Boolean("Attendance hours", default=True)

    def search_attendances_domain(self):
        """Search filter rules for attendances"""
        base_domain = [
            ("employee_id", "in", self.employee_ids.ids),
        ]
        date_domain = expression.AND(
            [
                [("write_date", ">=", self.date_from)],
                [("write_date", "<=", self.date_to)],
            ]
        )
        domain = expression.AND([base_domain, date_domain])
        return domain

    def _prepare_attendance_values(self):
        """Retrieve attendance values"""
        hl_model = self.env["hr.attendance"]
        search_domain = self.search_attendances_domain()
        attendances = hl_model.with_context(active_test=False).search(search_domain)
        _logger.info(f"Will process {len(attendances)} attendance lines")
        return attendances.prepare_hr_employee_hour_values()

    def prepare_values(self):
        values = super().prepare_values()
        if self.attendance_hours:
            values.extend(self._prepare_attendance_values())
        return values
