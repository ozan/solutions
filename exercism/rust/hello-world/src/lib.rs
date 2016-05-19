pub fn hello(name: Option<&str>) -> String {
    format!("Hello, {}!", name.unwrap_or("World"))
}
