# Copyright 2024 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from .common import HrDashboardAttendanceCommon


class TestHrAttendance(HrDashboardAttendanceCommon):
    def test_create_employee_hours_from_attendance(self):
        heh_lines = self._get_related_hours(self.attendances)
        nb_days = 21
        self.assertEqual(len(heh_lines), nb_days * 2)
        self.assertEqual(sum(heh_lines.mapped("hours_qty")), nb_days * 7)
        self.assertAlmostEqual(sum(heh_lines.mapped("days_qty")), 24.0)

    def test_update_employee_hours_from_attendance(self):
        for attendance in self.attendances:
            if attendance.check_out.hour == 17:
                attendance.check_out = attendance.check_out.replace(hour=18)
        heh_lines = self._get_related_hours(self.attendances)
        nb_days = 21
        self.assertEqual(len(heh_lines), nb_days * 2)
        self.assertEqual(sum(heh_lines.mapped("hours_qty")), nb_days * 8)
        self.assertAlmostEqual(sum(heh_lines.mapped("days_qty")), 24 * 8 / 7)

    def test_delete_employee_hours_from_attendance(self):
        deleted_ids = self.attendances.ids
        self.attendances.unlink()
        heh_lines = self._get_related_hours(self.attendances, deleted_ids)
        self.assertEqual(heh_lines.ids, [])

    def test_prepare_hr_employee_hour_values_should_always_return_a_list(self):
        values = self.env["hr.attendance"].prepare_hr_employee_hour_values()
        self.assertEqual(values, [])
