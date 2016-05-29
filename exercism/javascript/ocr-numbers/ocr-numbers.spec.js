var ocr = require('./ocr-numbers');

describe('ocr', function () {

  it('recognizes zero', function () {
    expect(ocr.convert(
      ' _ \n' +
      '| |\n' +
      '|_|\n' +
      '   '
    )).toBe('0');
  });

  it('recognizes one', function () {
    expect(ocr.convert(
      '   \n' +
      '  |\n' +
      '  |\n' +
      '   '
    )).toBe('1');
  });

  it('recognizes two', function () {
    expect(ocr.convert(
      ' _ \n' +
      ' _|\n' +
      '|_ \n' +
      '   '
    )).toBe('2');
  });

  it('recognizes three', function () {
    expect(ocr.convert(
      ' _ \n' +
      ' _|\n' +
      ' _|\n' +
      '   '
    )).toBe('3');
  });

  it('recognizes four', function () {
    expect(ocr.convert(
      '   \n' +
      '|_|\n' +
      '  |\n' +
      '   '
    )).toBe('4');
  });

  it('recognizes five', function () {
    expect(ocr.convert(
      ' _ \n' +
      '|_ \n' +
      ' _|\n' +
      '   '
    )).toBe('5');
  });

  it('recognizes six', function () {
    expect(ocr.convert(
      ' _ \n' +
      '|_ \n' +
      '|_|\n' +
      '   '
    )).toBe('6');
  });

  it('recognizes seven', function () {
    expect(ocr.convert(
      ' _ \n' +
      '  |\n' +
      '  |\n' +
      '   '
    )).toBe('7');
  });

  it('recognizes eight', function () {
    expect(ocr.convert(
      ' _ \n' +
      '|_|\n' +
      '|_|\n' +
      '   '
    )).toBe('8');
  });

  it('recognizes nine', function () {
    expect(ocr.convert(
      ' _ \n' +
      '|_|\n' +
      ' _|\n' +
      '   '
    )).toBe('9');
  });

  it('recognizes ten', function () {
    expect(ocr.convert(
      '    _ \n' +
      '  || |\n' +
      '  ||_|\n' +
      '      '
    )).toBe('10');
  });

  it('identifies garble', function () {
    expect(ocr.convert(
      '   \n' +
      '| |\n' +
      '| |\n' +
      '   '
    )).toBe('?');
  });

  it('converts 110101100', function () {
    expect(ocr.convert(
      '       _     _        _  _ \n' +
      '  |  || |  || |  |  || || |\n' +
      '  |  ||_|  ||_|  |  ||_||_|\n' +
      '                           '
    )).toBe('110101100');
  });

  it('identifies garble mixed in', function () {
    expect(ocr.convert(
      '       _     _           _ \n' +
      '  |  || |  || |     || || |\n' +
      '  |  | _|  ||_|  |  ||_||_|\n' +
      '                           '
    )).toBe('11?10?1?0');
  });

  it('converts 1234567890', function () {
    expect(ocr.convert(
      '    _  _     _  _  _  _  _  _ \n' +
      '  | _| _||_||_ |_   ||_||_|| |\n' +
      '  ||_  _|  | _||_|  ||_| _||_|\n' +
      '                              '
    )).toBe('1234567890');
  });

  it('converts 123 456 789', function () {
    expect(ocr.convert(
      '    _  _ \n' +
      '  | _| _|\n' +
      '  ||_  _|\n' +
      '         \n' +
      '    _  _ \n' +
      '|_||_ |_ \n' +
      '  | _||_|\n' +
      '         \n' +
      ' _  _  _ \n' +
      '  ||_||_|\n' +
      '  ||_| _|\n' +
      '         '
    )).toBe('123,456,789');
  });

});
