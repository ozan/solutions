use std::ascii::AsciiExt;

pub fn anagrams_for(word: String, others: [String]) -> Vec<&str> {
    // TODO shouldn't neet to key word every time
    others.filter(|x| key(x) == key(word))
}

fn key(word: String) -> String {
    word.to_lower().chars().sort()
}
