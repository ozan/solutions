
class HelloWorld {
  hello (name) {
    return `Hello, ${name || 'World'}!`
  }
}

module.exports = HelloWorld
