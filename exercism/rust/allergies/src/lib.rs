#[derive(Copy, Clone, Debug, Eq, PartialEq)]
pub enum Allergen {
    Eggs,
    Peanuts,
    Shellfish,
    Strawberries,
    Tomatoes,
    Chocolate,
    Pollen,
    Cats,
}

static ALL_ALLERGENS: [Allergen; 8] = [Allergen::Eggs,
                                       Allergen::Peanuts,
                                       Allergen::Shellfish,
                                       Allergen::Strawberries,
                                       Allergen::Tomatoes,
                                       Allergen::Chocolate,
                                       Allergen::Pollen,
                                       Allergen::Cats];

pub struct Allergies {
    score: i32,
}

impl Allergies {
    pub fn new(score: i32) -> Allergies {
        Allergies { score: score }
    }
    pub fn is_allergic_to(&self, allergen: &Allergen) -> bool {
        let n = 1 << *allergen as i32;
        self.score & n > 0
    }
    pub fn allergies(self) -> Vec<Allergen> {
        ALL_ALLERGENS.iter().filter(|&a| self.is_allergic_to(a)).map(|&a| a).collect()
    }
}
