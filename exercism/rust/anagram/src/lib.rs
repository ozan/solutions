pub fn anagrams_for(word: &'static str, others: &[&'static str]) -> Vec<&'static str> {
    others.iter()
        .filter(|other| key(other) == key(word) && lower(other) != lower(word))
        .cloned()
        .collect()
}

fn lower(word: &str) -> String {
    word.to_lowercase()
}

fn key(word: &str) -> String {
    let mut chars: Vec<char> = word.to_lowercase().chars().collect();
    chars.sort();
    chars.into_iter().collect()
}
