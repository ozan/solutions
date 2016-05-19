var Trinary = require('./trinary');

describe('Trinary', function () {

  it('1 is decimal 1', function() {
    expect(1).toEqual(new Trinary('1').toDecimal());
  });

  it('2 is decimal 2', function() {
    expect(2).toEqual(new Trinary('2').toDecimal());
  });

  it('10 is decimal 3', function() {
    expect(3).toEqual(new Trinary('10').toDecimal());
  });

  it('11 is decimal 4', function() {
    expect(4).toEqual(new Trinary('11').toDecimal());
  });

  it('100 is decimal 9', function() {
    expect(9).toEqual(new Trinary('100').toDecimal());
  });

  it('112 is decimal 14', function() {
    expect(14).toEqual(new Trinary('112').toDecimal());
  });

  it('222 is 26', function() {
    expect(26).toEqual(new Trinary('222').toDecimal());
  });

  it('1122000120 is 32091', function() {
    expect(32091).toEqual(new Trinary('1122000120').toDecimal());
  });

  it('invalid trinary is decimal 0', function() {
    expect(0).toEqual(new Trinary('carrot').toDecimal());
  });

});
