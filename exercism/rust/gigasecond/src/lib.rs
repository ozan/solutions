extern crate chrono;
use chrono::*;

pub fn after(dt: DateTime<UTC>) -> DateTime<UTC> {
    dt + Duration::seconds(1_000_000_000)
}
