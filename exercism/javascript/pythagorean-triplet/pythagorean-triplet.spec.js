var Triplet = require('./pythagorean-triplet');

describe('Triplet', function () {

  it('calculates the sum', function () {
    expect(new Triplet(3, 4, 5).sum()).toBe(12);
  });

  it('calculates the product', function () {
    expect(new Triplet(3, 4, 5).product()).toBe(60);
  });

  it('can recognize a pythagorean triplet', function () {
    expect(new Triplet(3, 4, 5).isPythagorean()).toBe(true);
  });

  it('can recognize a non pythagorean triplet', function () {
    expect(new Triplet(5, 6, 7).isPythagorean()).toBe(false);
  });

  it('can make triplets up to 10', function () {
    var triplets = Triplet.where({ maxFactor: 10 });
    var products = triplets.sort().map( function (triplet) {
      return triplet.product();
    });
    expect(products).toEqual([60, 480]);
  });

  it('can make triplets 11 through 20', function () {
    var triplets = Triplet.where({ minFactor: 11, maxFactor: 20 });
    var products = triplets.sort().map( function (triplet) {
      return triplet.product();
    });
    expect(products).toEqual([3840]);
  });

  it('can filter on sum', function () {
    var triplets = Triplet.where({ sum: 180, maxFactor: 100 });
    var products = triplets.sort().map( function (triplet) {
      return triplet.product();
    });
    expect(products).toEqual([118080, 168480, 202500]);
  });

});
