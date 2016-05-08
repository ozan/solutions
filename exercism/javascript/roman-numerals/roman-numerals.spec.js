var toRoman = require('./roman-numerals');

describe('toRoman()', function() {
  it('converts 1', function() {
    expect(toRoman(1)).toEqual('I');
  });

  it('converts 2', function() {
    expect(toRoman(2)).toEqual('II');
  });

  it('converts 3', function() {
    expect(toRoman(3)).toEqual('III');
  });

  it('converts 4', function() {
    expect(toRoman(4)).toEqual('IV');
  });

  it('converts 5', function() {
    expect(toRoman(5)).toEqual('V');
  });

  it('converts 6', function() {
    expect(toRoman(6)).toEqual('VI');
  });

  it('converts 9', function() {
    expect(toRoman(9)).toEqual('IX');
  });

  it('converts 27', function() {
    expect(toRoman(27)).toEqual('XXVII');
  });

  it('converts 48', function() {
    expect(toRoman(48)).toEqual('XLVIII');
  });

  it('converts 59', function() {
    expect(toRoman(59)).toEqual('LIX');
  });

  it('converts 93', function() {
    expect(toRoman(93)).toEqual('XCIII');
  });

  it('converts 141', function() {
    expect(toRoman(141)).toEqual('CXLI');
  });

  it('converts 163', function() {
    expect(toRoman(163)).toEqual('CLXIII');
  });

  it('converts 402', function() {
    expect(toRoman(402)).toEqual('CDII');
  });

  it('converts 575', function() {
    expect(toRoman(575)).toEqual('DLXXV');
  });

  it('converts 911', function() {
    expect(toRoman(911)).toEqual('CMXI');
  });

  it('converts 1024', function() {
    expect(toRoman(1024)).toEqual('MXXIV');
  });

  it('converts 3000', function() {
    expect(toRoman(3000)).toEqual('MMM');
  });
});
