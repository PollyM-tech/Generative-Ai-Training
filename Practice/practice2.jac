obj Cat {
    has name: str;

    def meow;
}

with entry {
    kitty = Cat("Mimi");
    kitty.meow();   
}

impl Cat.meow {
    print(f"{self.name} says Meeoow!");
}