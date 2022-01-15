# federal_holiday
package that returns if a date is a federal holiday

## Functions

### is_federal_holiday(date)

returns True if day is a federal holiday

### holiday_name(date)

returns name of holiday given a date, None if there is no holiday

### is_weekend(date)

returns True if day is on a weekend

### is_weekday(date)

returns True if day is on a weekday

### is_working_day(date)

returns True if it's a working day for federal employees

### is_off_day(date)

returns True if it's an off day for federal employees

## Installing as a package:
pip install git+https://github.com/mmcelhan/federalholiday.git#egg=federalholiday

## Source Code
source code is here:
https://github.com/mmcelhan/federal_holiday_calendar_source

The testing file shows all Federal Holidays through 2030 are correctly applied

## Examples

import federalholiday as fh

fh.is_federal_holiday(‘2030-01-01’) # New Years Day, 2030

Returns True

fh.is_federal_holiday(‘2030-1-1’) # to test date formatting

Returns True

fh.is_federal_holiday(‘2030-1-2’) # not a holiday

Returns False

fh.holiday_name(‘2030-01-01’)

Returns ‘New Years Day’

fh.is_day_off(‘2030-01-01’)

Returns True

fh.is_off_day(‘2030-01-01’)

Returns True
