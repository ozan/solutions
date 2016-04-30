using System;
using System.Collections.Generic;
using System.Linq;

namespace Exercism
{
    public enum Schedule {
        First,
        Second,
        Teenth,
        Third,
        Fourth,
        Last
    };

    public class Meetup {
        int month;
        int year;

        Dictionary<Schedule, IEnumerable<int>> rangeForSchedule = new Dictionary<Schedule, IEnumerable<int>> {
            { Schedule.First, Enumerable.Range(1, 7) },
            { Schedule.Second, Enumerable.Range(8, 14) },
            { Schedule.Teenth, Enumerable.Range(13, 19) },
            { Schedule.Third, Enumerable.Range(15, 21) },
            { Schedule.Fourth, Enumerable.Range(22, 28) }
        };

        public Meetup(int m, int y)
        {
            month = m;
            year = y;
        }

        public DateTime Day(DayOfWeek dayOfWeek, Schedule schedule)
        {
            var lastDay = DateTime.DaysInMonth(year, month);
            var range = schedule == Schedule.Last
              ? Enumerable.Range(lastDay - 6, lastDay)
              : rangeForSchedule[schedule];

            return range
                .Select(day => new DateTime(year, month, day))
                .Where(dt => dt.DayOfWeek == dayOfWeek)
                .First();
        }
    }
}
