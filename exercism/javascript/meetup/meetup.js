// from calendar import isleap
// from datetime import date, timedelta
//
// STARTS = {
//     '1st': 1,
//     '2nd': 8,
//     '3rd': 15,
//     '4th': 22,
//     '5th': 29,
//     'teenth': 13,
// }
//
// DAY_NAMES = (
//     'Monday',
//     'Tuesday',
//     'Wednesday',
//     'Thursday',
//     'Friday',
//     'Saturday',
//     'Sunday',
// )
//
//
// def meetup_day(year, month, day, case):
//     start = date(year, month, STARTS.get(case, last_day_start(year, month)))
//     offset = DAY_NAMES.index(day) - start.weekday()
//     return start + timedelta(days=offset % 7)
//
//
// def last_day_start(year, month):
//     return([25, 22 + int(isleap(year))] + [25, 24, 25, 24, 25] * 2)[month - 1]
const fp = require('lodash/fp')

const get = fp.get.convert({ fixed: false })

const isLeap = (year) =>
  ((year % 4 == 0) && (year % 100 != 0)) || (year % 400 == 0)

const lastDay = (year, month) =>
  [31, 28 + Number(isLeap(year)), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][month]

const addDays = (days, dt) =>
  new Date(Number(dt) + days * 24 * 60 * 60 * 1000)

const dayNames = [
  'Sunday',
  'Monday',
  'Tuesday',
  'Wednesday',
  'Thursday',
  'Friday',
  'Saturday'
]

const starts = {
  '1st': 1,
  '2nd': 8,
  '3rd': 15,
  '4th': 22,
  '5th': 29,
  'teenth': 13,
}

const meetupDay = (year, month, dayName, ord) => {
  const start = new Date(year, month, get(ord, starts, lastDay(year, month) - 6))
  if (start.getMonth() !== month) throw 'Invalid date'
  const offset = dayNames.indexOf(dayName) - start.getDay()
  return addDays((7 + offset) % 7, start)
}

module.exports = meetupDay
