var Hamming = require('./hamming');

describe('Hamming', function () {
  var hamming = new Hamming();

  it('no difference between identical strands', function () {
    expect(hamming.compute('A', 'A')).toEqual(0);
  });

  it('complete hamming distance for single nucleotide strand', function () {
    expect(hamming.compute('A','G')).toEqual(1);
  });

  it('complete hamming distance for small strand', function () {
    expect(hamming.compute('AG','CT')).toEqual(2);
  });

  it('small hamming distance', function () {
    expect(hamming.compute('AT','CT')).toEqual(1);
  });

  it('small hamming distance in longer strand', function () {
    expect(hamming.compute('GGACG', 'GGTCG')).toEqual(1);
  });

  it('large hamming distance', function () {
    expect(hamming.compute('GATACA', 'GCATAA')).toEqual(4);
  });

  it('hamming distance in very long strand', function () {
    expect(hamming.compute('GGACGGATTCTG', 'AGGACGGATTCT')).toEqual(9);
  });

  it('throws error when strands are not equal length', function() {
    expect(function() { hamming.compute('GGACGGATTCTG', 'AGGAC'); }).toThrow(
      new Error('DNA strands must be of equal length.')
    );
  });

});
