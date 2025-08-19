

struct Zip<'a, T, U>(&'a [T], &'a [U]);

struct ZipIt<T: Iterator, U: Iterator>(T, U);

impl<T: Iterator, U: Iterator> Iterator for ZipIt<T, U> {
    type Item = (T::Item, U::Item);

    fn next(&mut self) -> Option<Self::Item> {
        if let (Some(a), Some(b)) = (self.0.next(), self.1.next()) {
            Some((a, b))
        } else {
            None
        }
    }
}

impl<'a, T, U> IntoIterator for Zip<'a, T, U> {
    type Item = (&'a T, &'a U);
    type IntoIter = ZipIt<std::slice::Iter<'a, T>, std::slice::Iter<'a, U>>;

    fn into_iter(self) -> Self::IntoIter {
        ZipIt(self.0.iter(), self.1.iter())
    }
}

/* Cannot implement: we need reference proxy object for this but Index has strict
 *                   requirement of returning normal reference sadly
 *                   This proves that Rust cannot support container type in question

impl<'a, T, U> std::ops::Index<usize> for Zip<'a, T, U> {
    type Output = (&'a T, &'a U);

    fn index(&self, index: usize) -> &Self::Output {
        &(&self.0[index], &self.1[index])
    }
}
*/


fn main() {
    let names = ["Andrzej", "Błażej", "Czesław"];
    let ages = [10, 20, 30];
    let db = Zip(&names[..], &ages[..]);

    println!("db[1] = {:?}", db[1]);

    for (name, age) in db {
        println!("{name} is {age} years old");
    }
}
