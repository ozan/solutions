extern crate hello_world;

#[test]
fn test_no_name() {
    assert_eq!("Hello, World!", hello_world::hello(None));
}

#[test]
fn test_sample_name() {
    assert_eq!("Hello, Alice!", hello_world::hello(Some("Alice")));
}

#[test]
fn test_other_same_name() {
    assert_eq!("Hello, Bob!", hello_world::hello(Some("Bob")));
}
