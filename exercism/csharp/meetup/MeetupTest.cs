using System;
using System.Collections.Generic;
using System.Linq;
using NUnit.Framework;

using Exercism;

[TestFixture]
public class MeetupTest
{

    [Test]
    public void Finds_first_teenth_day_of_week_in_a_month()
    {
        var cases = new [] {
            new { month = 5, dayOfWeek = DayOfWeek.Monday, expectation = "2013-5-13" },
            new { month = 3, dayOfWeek = DayOfWeek.Tuesday, expectation = "2013-3-19" },
            new { month = 1, dayOfWeek = DayOfWeek.Wednesday, expectation = "2013-1-16" },
            new { month = 5, dayOfWeek = DayOfWeek.Thursday, expectation = "2013-5-16" },
            new { month = 4, dayOfWeek = DayOfWeek.Friday, expectation = "2013-4-19" },
            new { month = 2, dayOfWeek = DayOfWeek.Saturday, expectation = "2013-2-16" },
            new { month = 10, dayOfWeek = DayOfWeek.Sunday, expectation = "2013-10-13" }
        }.ToList();
        foreach (var c in cases) {
            DateTime day = new Meetup(c.month, 2013).Day(c.dayOfWeek, Schedule.Teenth);
            Assert.That(day.ToString("yyyy-M-d"), Is.EqualTo(c.expectation));
        }
    }

    [Test]
    public void Finds_first_day_of_week_in_a_month()
    {
        var cases = new [] {
            new { month = 3, dayOfWeek = DayOfWeek.Monday, expectation = "2013-3-4" },
            new { month = 5, dayOfWeek = DayOfWeek.Tuesday, expectation = "2013-5-7" },
            new { month = 7, dayOfWeek = DayOfWeek.Wednesday, expectation = "2013-7-3" },
            new { month = 9, dayOfWeek = DayOfWeek.Thursday, expectation = "2013-9-5" },
            new { month = 11, dayOfWeek = DayOfWeek.Friday, expectation = "2013-11-1" },
            new { month = 1, dayOfWeek = DayOfWeek.Saturday, expectation = "2013-1-5" },
            new { month = 4, dayOfWeek = DayOfWeek.Sunday, expectation = "2013-4-7" }
        };
        foreach (var c in cases) {
            DateTime day = new Meetup(c.month, 2013).Day(c.dayOfWeek, Schedule.First);
            Assert.That(day.ToString("yyyy-M-d"), Is.EqualTo(c.expectation));
        }
    }

    [Test]
    public void Finds_second_day_of_week_in_a_month()
    {
        var cases = new [] {
            new { month = 3, dayOfWeek = DayOfWeek.Monday, expectation = "2013-3-11" },
            new { month = 5, dayOfWeek = DayOfWeek.Tuesday, expectation = "2013-5-14" },
            new { month = 7, dayOfWeek = DayOfWeek.Wednesday, expectation = "2013-7-10" },
            new { month = 9, dayOfWeek = DayOfWeek.Thursday, expectation = "2013-9-12" },
            new { month = 12, dayOfWeek = DayOfWeek.Friday, expectation = "2013-12-13" },
            new { month = 2, dayOfWeek = DayOfWeek.Saturday, expectation = "2013-2-9" },
            new { month = 4, dayOfWeek = DayOfWeek.Sunday, expectation = "2013-4-14" }
        };
        foreach (var c in cases) {
            DateTime day = new Meetup(c.month, 2013).Day(c.dayOfWeek, Schedule.Second);
            Assert.That(day.ToString("yyyy-M-d"), Is.EqualTo(c.expectation));
        }
    }

    [Test]
    public void Finds_third_day_of_week_in_a_month()
    {
        var cases = new [] {
            new { month = 3, dayOfWeek = DayOfWeek.Monday, expectation = "2013-3-18" },
            new { month = 5, dayOfWeek = DayOfWeek.Tuesday, expectation = "2013-5-21" },
            new { month = 7, dayOfWeek = DayOfWeek.Wednesday, expectation = "2013-7-17" },
            new { month = 9, dayOfWeek = DayOfWeek.Thursday, expectation = "2013-9-19" },
            new { month = 12, dayOfWeek = DayOfWeek.Friday, expectation = "2013-12-20" },
            new { month = 2, dayOfWeek = DayOfWeek.Saturday, expectation = "2013-2-16" },
            new { month = 4, dayOfWeek = DayOfWeek.Sunday, expectation = "2013-4-21" }
        };
        foreach (var c in cases) {
            DateTime day = new Meetup(c.month, 2013).Day(c.dayOfWeek, Schedule.Third);
            Assert.That(day.ToString("yyyy-M-d"), Is.EqualTo(c.expectation));
        }
    }

    [Test]
    public void Finds_fourth_day_of_week_in_a_month()
    {
        var cases = new [] {
            new { month = 3, dayOfWeek = DayOfWeek.Monday, expectation = "2013-3-25" },
            new { month = 5, dayOfWeek = DayOfWeek.Tuesday, expectation = "2013-5-28" },
            new { month = 7, dayOfWeek = DayOfWeek.Wednesday, expectation = "2013-7-24" },
            new { month = 9, dayOfWeek = DayOfWeek.Thursday, expectation = "2013-9-26" },
            new { month = 12, dayOfWeek = DayOfWeek.Friday, expectation = "2013-12-27" },
            new { month = 2, dayOfWeek = DayOfWeek.Saturday, expectation = "2013-2-23" },
            new { month = 4, dayOfWeek = DayOfWeek.Sunday, expectation = "2013-4-28" }
        };
        foreach (var c in cases) {
            DateTime day = new Meetup(c.month, 2013).Day(c.dayOfWeek, Schedule.Fourth);
            Assert.That(day.ToString("yyyy-M-d"), Is.EqualTo(c.expectation));
        }
    }

    [Test]
    public void Finds_last_day_of_week_in_a_month()
    {
        var cases = new [] {
            new { month = 3, dayOfWeek = DayOfWeek.Monday, expectation = "2013-3-25" },
            new { month = 5, dayOfWeek = DayOfWeek.Tuesday, expectation = "2013-5-28" },
            new { month = 7, dayOfWeek = DayOfWeek.Wednesday, expectation = "2013-7-31" },
            new { month = 9, dayOfWeek = DayOfWeek.Thursday, expectation = "2013-9-26" },
            new { month = 12, dayOfWeek = DayOfWeek.Friday, expectation = "2013-12-27" },
            new { month = 2, dayOfWeek = DayOfWeek.Saturday, expectation = "2013-2-23" },
            new { month = 3, dayOfWeek = DayOfWeek.Sunday, expectation = "2013-3-31" }
        };
        foreach (var c in cases) {
            DateTime day = new Meetup(c.month, 2013).Day(c.dayOfWeek, Schedule.Last);
            Assert.That(day.ToString("yyyy-M-d"), Is.EqualTo(c.expectation));
        }
    }
}
