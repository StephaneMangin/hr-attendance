This module adds a dashboard to manage attendances and contractual hours.

General overview
================

Main purpose of this dashboard is to allow employee and manager to have an overview of their attendances according to their contract.

Two dashboards will be needed to have two axes of analysis and will cover the attendance and the contractual time of the employee.

Detailed requirements
=====================

Dashboard Attendances report
----------------------------

Attendance report will allow to calculate the undertime or overtime of the employee at a day level. For this purpose we need to calculate the contractual hours the employee is requested to do for each day. Sum of the contractual hours, leaves and attendances will give the time variation according to the contract.

Contractual hours should be calculated taking in account the following requirements:

- Calculation per day should take in account the contract valid at the date (for the future if there is no end date for the contract we use the current one)
- Working time per day will use the work plan (resource calendar) on the employee contract with the data per day and if not available the average per day (only the working days)
- Bank holiday should be excluded and they can come from the the calendar or the OCA module Public holiday (if installed)
- Number will be show in negative (in order that the final sum is negative if there is insufficient attendances according to the contract time

Attendance section have the following requirement

- Working time and time off should be clearly separated (two columns)
- Time off are taken only if fully validated
- By default we filter the current year until today and the user data.

Global requirement
------------------
Data coming from the attendances should always represent the situation we get if we go to the attendances app (data should be in real time). We accept that the data linked to the contract are updated every 24 hours.

At the initialisation the system should be able to generate the past data.

Security
--------

Employee should not see data from other employees.
One exception for a manager that can see all the data from employees he is the manager of.

Pitfalls
========

- Limit cases about hours on weekend and hours worked at night inbetween 2 days.
