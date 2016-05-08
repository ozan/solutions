var atbash = require('./atbash-cipher');

describe('encode', function() {

  it('encodes no', function() {
    expect(atbash.encode('no')).toEqual('ml');
  });

  it('encodes yes', function() {
    expect(atbash.encode('yes')).toEqual('bvh');
  });

  it('encodes OMG', function() {
    expect(atbash.encode('OMG')).toEqual('lnt');
  });

  it('encodes O M G', function() {
    expect(atbash.encode('O M G')).toEqual('lnt');
  });

  it('encodes long words', function() {
    expect(atbash.encode('mindblowingly')).toEqual('nrmwy oldrm tob');
  });

  it('encodes numbers', function() {
    expect(atbash.encode('Testing, 1 2 3, testing.'))
      .toEqual('gvhgr mt123 gvhgr mt');
  });

  it('encodes sentences', function() {
    expect(atbash.encode('Truth is fiction.')).toEqual('gifgs rhurx grlm');
  });

  it('encodes all the things', function() {
    expect(atbash.encode('The quick brown fox jumps over the lazy dog.'))
      .toEqual('gsvjf rxpyi ldmul cqfnk hlevi gsvoz abwlt');
  });

});
