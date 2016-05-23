var pigLatin = require('./pig-latin');

describe('pigLatin', function () {

  it('translates a word beginning with a', function () {
    expect(pigLatin.translate('apple')).toEqual('appleay');
  });

  it('translates a word beginning with e', function () {
    expect(pigLatin.translate('ear')).toEqual('earay');
  });

  it('translates a word beginning with p', function () {
    expect(pigLatin.translate('pig')).toEqual('igpay');
  });

  it('translates a word beginning with k', function () {
    expect(pigLatin.translate('koala')).toEqual('oalakay');
  });

  it('translates a word beginning with ch', function () {
    expect(pigLatin.translate('chair')).toEqual('airchay');
  });

  it('translates a word beginning with qu', function () {
    expect(pigLatin.translate('queen')).toEqual('eenquay');
  });

  it('translates a word with a consonant preceding qu', function () {
    expect(pigLatin.translate('square')).toEqual('aresquay');
  });

  it('translates a word beginning with th', function () {
    expect(pigLatin.translate('therapy')).toEqual('erapythay');
  });

  it('translates a word beginning with thr', function () {
    expect(pigLatin.translate('thrush')).toEqual('ushthray');
  });

  it('translates a word beginning with sch', function () {
    expect(pigLatin.translate('school')).toEqual('oolschay');
  });

  it('translates a phrase', function () {
    expect(pigLatin.translate('quick fast run'))
      .toEqual('ickquay astfay unray');
  });

});
