pub fn is_leap_year(year: i32) -> bool {
    (year % 400 == 0) || (year % 4 == 0) && (year % 100 != 0)
}
