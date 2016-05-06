var HelloWorld = require('./hello-world');

describe('Hello World', function() {
  var helloWorld = new HelloWorld();

  it('says hello world with no name', function() {
    expect(helloWorld.hello('')).toEqual('Hello, World!');
  });

  it('says hello to bob', function() {
    expect(helloWorld.hello('Bob')).toEqual('Hello, Bob!');
  });

  it('says hello to sally', function() {
    expect(helloWorld.hello('Sally')).toEqual('Hello, Sally!');
  });
});
