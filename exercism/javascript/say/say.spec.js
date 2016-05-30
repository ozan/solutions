var say = require('./say');

describe('say', function () {

  it('zero', function () {
    expect(say.inEnglish(0)).toBe('zero');
  });

  it('one', function () {
    expect(say.inEnglish(1)).toBe('one');
  });

  it('fourteen', function () {
    expect(say.inEnglish(14)).toBe('fourteen');
  });

  it('twenty', function () {
    expect(say.inEnglish(20)).toBe('twenty');
  });

  it('twenty-two', function () {
    expect(say.inEnglish(22)).toBe('twenty-two');
  });

  it('one hundred', function () {
    expect(say.inEnglish(100)).toBe('one hundred');
  });

  it('one hundred twenty-three', function () {
    expect(say.inEnglish(123)).toBe('one hundred twenty-three');
  });

  it('one thousand', function () {
    expect(say.inEnglish(1000)).toBe('one thousand');
  });

  it('one thousand two hundred thirty-four', function () {
    expect(say.inEnglish(1234)).toBe('one thousand two hundred thirty-four');
  });

  it('one million', function () {
    expect(say.inEnglish(1000000)).toBe('one million');
  });

  it('one million two', function () {
    expect(say.inEnglish(1000002)).toBe('one million two');
  });

  it('one million two thousand three hundred forty-five', function () {
    expect(say.inEnglish(1002345))
      .toBe('one million two thousand three hundred forty-five');
  });

  it('one billion', function () {
    expect(say.inEnglish(1000000000)).toBe('one billion');
  });

  it('a really big number', function () {
    var expected = 'nine hundred eighty-seven billion ';
    expected += 'six hundred fifty-four million ';
    expected += 'three hundred twenty-one thousand ';
    expected += 'one hundred twenty-three';
    expect(say.inEnglish(987654321123)).toBe(expected);
  });

  it('raises an error below zero', function () {
    expect(function () {
      say.inEnglish(-1);
    }).toThrow(new Error('Number must be between 0 and 999,999,999,999.'));
  });

  it('raises an error above 999,999,999,999', function () {
    expect(function () {
      say.inEnglish(1000000000000);
    }).toThrow(new Error('Number must be between 0 and 999,999,999,999.'));
  });

});
