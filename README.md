# Building and running

```
cc -o nob nob.c
./nob
```

To build and run only some examples:

```
./nob cpp python
```

# The Question

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
| C#         | Yes            | Default interfaces in standard library are _awful_ |
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


# Suprises

In C# this is the minimal `IList` implementation:

```
class ZipRef<A, B> : IList<(A, B)> {
	public (A, B) this[int index] {
		get {
			throw new NotImplementedException();
		}
		set {}
	}

	public void Add((A, B) item) {}
	public void Clear() {}
	public int IndexOf((A, B) item) { return -1; }
	public void Insert(int index, (A, B) item) {}
	public void RemoveAt(int index) {}


	public bool Contains((A, B) item) { return false; }
	public void CopyTo((A, B)[] items, int index) {}
	public bool Remove((A, B) item) { return false; }
	public int Count { get => -1; }
	public bool IsReadOnly { get => false; }

	IEnumerator<(A, B)> IEnumerable<(A, B)>.GetEnumerator() { return null; }

	System.Collections.IEnumerator System.Collections.IEnumerable.GetEnumerator() { return null; }
}
```

From what I've seen this is the only generic class that abstracts index operation.
You get the feeling that this standard library isn't as good as one in C++, D or Rust.
