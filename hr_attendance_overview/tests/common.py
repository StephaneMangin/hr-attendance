from datetime import datetime

from odoo import tools

from odoo.addons.hr_timesheet_overview.tests.common import (
    VALID_DAYS_JAN_2022,
    HrDashboardCommon,
)


class HrDashboardAttendanceCommon(HrDashboardCommon):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        all_days = [day for week in VALID_DAYS_JAN_2022 for (day, day_length) in week]
        cls.attendances = cls.create_attendances(2022, 1, all_days)

    @classmethod
    def create_attendances(cls, year, month, days):
        with tools.mute_logger(
            "odoo.addons.hr_timesheet_overview.models.hr_employee_hour"
        ):
            records = cls.env["hr.attendance"].create(
                [
                    {
                        "employee_id": cls.employee.id,
                        "check_in": datetime(year, month, day, hour_in),
                        "check_out": datetime(year, month, day, hour_out),
                    }
                    for day in days
                    for hour_in, hour_out in [(8, 12), (14, 17)]
                ]
            )
            records.flush()
        # Set create/write date of created records
        query = (
            "UPDATE hr_attendance SET create_date=check_out, "
            "write_date=check_out WHERE id IN %s;"
        )
        cls.env.cr.execute(query, (tuple(records.ids),))
        return records
