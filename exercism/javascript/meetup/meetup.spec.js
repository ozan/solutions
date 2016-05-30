var meetupDay = require('./meetup');


function MeetupDayException(message) {
   this.message = message;
   this.name = 'MeetupDayException';
}

describe('meetupDay()', function() {
  it('monteenth of may 2013', function() {
    expect(meetupDay(2013, 4, 'Monday', 'teenth')).toEqual(new Date(2013, 4, 13));
  });

  it('saturteenth of february 2013', function() {
    expect(meetupDay(2013, 1, 'Saturday', 'teenth')).toEqual(new Date(2013, 1, 16));
  });

  it('first tuesday of may 2013', function() {
    expect(meetupDay(2013, 4, 'Tuesday', '1st')).toEqual(new Date(2013, 4, 7));
  });

  it('second monday of april 2013', function() {
    expect(meetupDay(2013, 3, 'Monday', '2nd')).toEqual(new Date(2013, 3, 8));
  });

  it('third thursday of september 2013', function() {
    expect(meetupDay(2013, 8, 'Thursday', '3rd')).toEqual(new Date(2013, 8, 19));
  });

  it('fourth sunday of march 2013', function() {
    expect(meetupDay(2013, 2, 'Sunday', '4th')).toEqual(new Date(2013, 2, 24));
  });

  it('last thursday of october 2013', function() {
    expect(meetupDay(2013, 9, 'Thursday', 'last')).toEqual(new Date(2013, 9, 31));
  });

  it('last wednesday of february 2012', function() {
    expect(meetupDay(2012, 1, 'Wednesday', 'last')).toEqual(new Date(2012, 1, 29));
  });

  it('last wednesday of december 2014', function() {
    expect(meetupDay(2014, 11, 'Wednesday', 'last')).toEqual(new Date(2014, 11, 31));
  });

  it('last sunday of only four week february 2015', function() {
    expect(meetupDay(2015, 1, 'Sunday', 'last')).toEqual(new Date(2015, 1, 22));
  });

  it('first friday of december 2012', function() {
    expect(meetupDay(2012, 11, 'Friday', '1st')).toEqual(new Date(2012, 11, 7));
  });

  it('fifth monday of march 2015', function() {
    expect(meetupDay(2015, 2, 'Monday', '5th')).toEqual(new Date(2015, 2, 30));
  });

  it('nonexistent fifth monday of february 2015', function() {
    expect(function () { meetupDay(2015, 1, 'Monday', '5th'); }).toThrow();
  });
});
