# Copyright 2024 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "HR Attendance Overview",
    "version": "15.0.1.0.0",
    "author": "Camptocamp SA, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "category": "Human Resources",
    "depends": ["hr_timesheet_overview", "hr_attendance"],
    "website": "https://github.com/OCA/hr-attendance",
    "data": [
        "security/ir.model.access.csv",
        "wizards/hr_employee_hour_updater_view.xml",
        "report/hr_employee_attendance_report_views.xml",
    ],
    "installable": True,
}
