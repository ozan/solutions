var Isogram = require('./isogram');

describe('Isogram Test Suite', function () {
  it('duplicates', function () {
    var word = new Isogram('duplicates');

    expect(word.isIsogram()).toEqual(true);
  });

  it('eleven', function () {
    var word = new Isogram('eleven');

    expect(word.isIsogram()).toEqual(false);
  });

  it('subdermatoglyphic', function () {
    var word = new Isogram('subdermatoglyphic');

    expect(word.isIsogram()).toEqual(true);
  });

  it('Alphabet', function () {
    var word = new Isogram('Alphabet');

    expect(word.isIsogram()).toEqual(false);
  });

  it('thumbscrew-japingly', function () {
    var word = new Isogram('thumbscrew-japingly');

    expect(word.isIsogram()).toEqual(true);
  });

  it('Hjelmqvist-Gryb-Zock-Pfund-Wax', function () {
    var word = new Isogram('Hjelmqvist-Gryb-Zock-Pfund-Wax');

    expect(word.isIsogram()).toEqual(true);
  });

  it('Heizölrückstoßabdämpfung', function () {
    var word = new Isogram('Heizölrückstoßabdämpfung');

    expect(word.isIsogram()).toEqual(true);
  });

  it('the quick brown fox', function () {
    var word = new Isogram('the quick brown fox');

    expect(word.isIsogram()).toEqual(false);
  });

  it('Emily Jung Schwartzkopf', function () {
    var word = new Isogram('Emily Jung Schwartzkopf');

    expect(word.isIsogram()).toEqual(true);
  });
});
