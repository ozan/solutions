#![feature(iter_arith)]

pub fn square_of_sum(n: i32) -> i32 {
    square((0..n + 1).sum())
}

pub fn sum_of_squares(n: i32) -> i32 {
    (0..n + 1).map(square).sum()
}

pub fn difference(n: i32) -> i32 {
    square_of_sum(n) - sum_of_squares(n)
}

fn square(n: i32) -> i32 {
    n * n
}
