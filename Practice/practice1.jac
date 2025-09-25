
obj Dog {
    has name: str;

    def bark;

}

impl Dog.bark{
    print(f"{self.name} says Woof!");
}

with entry{
    pup = Dog ("Badda");
    eat = Dog ("Pico");
    pup.bark();
    eat.bark();
}