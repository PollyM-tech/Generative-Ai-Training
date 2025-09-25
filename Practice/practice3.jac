walker HelloWalker {
    can start with entry;
}

impl HelloWalker.start {
    print("Hello, I’m walking too fast!");
}

with entry {
   root spawn HelloWalker();
}
