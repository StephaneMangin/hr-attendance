# Copyright 2024 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models


class HrAttendance(models.Model):
    _name = "hr.attendance"
    _inherit = ["hr.attendance", "hr.employee.hour.mixin"]

    def prepare_hr_employee_hour_values(self, **kwargs):
        model_id = self._get_model_id()
        values_list = []
        cached_by_date = self.env.context.get("attendances_by_date")
        for attendance in self:
            check_in_date = attendance.check_in.date()
            contract_hours, contract_day = self._contract_hours_day(
                attendance.employee_id,
                check_in_date,
                cache=cached_by_date,
            )
            values = {
                "model_id": model_id,
                "res_id": attendance.id,
                "type": "attendance",
                "date": check_in_date,
                "employee_id": attendance.employee_id.id,
                "hours_qty": attendance.worked_hours,
                "days_qty": attendance.worked_hours / contract_hours,
                "check_in": attendance.check_in,
                "check_out": attendance.check_out,
            }
            values_list.append(values)
        return values_list
