## The Question

Suppose that you have this general sorting algorithm definition in your favourite language:

```python
def bubble_sort[T](xs: list[T]):
    n = len(xs)
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, n):
            if xs[i - 1] > xs[i]:
                swap(xs[i-1], xs[i])
                swapped = True
        n -= 1
```

Can you implement operation `zip(xs, ys)` that would produce O(1) abstraction that would behave like: `[(x, y) for zip(xs, ys)]`?

Requirements:

- Operator overloading
- Tuples (or tuple-like objects)
- References (or proxy objects that have overloaded assigment operators)

## Results

| Language   | Can you do it? | Comment  |
|------------|----------------|-----------|
| Ada        | Unknown        | |
| C#         | Unknown        | |
| C++        | Yes            | [Provided by standard library](https://en.cppreference.com/w/cpp/ranges/zip_view.html) |
| D          | Yes            | [Provided by standard library](https://dlang.org/library/std/range/zip.html) |
| Go         | No             | No operator overloading     |
| Haskell    | Unknown        | |
| JavaScript | No             | No operator overloading     |
| Julia      | Unknown        | |
| Kotlin     | Unknown        | |
| Lua        | Unknown        | |
| Nim        | Unknown        | |
| Python     | Yes            | |
| Raku       | Unknown        | |
| Rust       | No             | Index must return reference |
| Scala      | Unknown        | |
