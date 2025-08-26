List<int> xs = new() { 1, 6, 5, 10, 8 };
List<string> ys = new() { "1", "6", "5", "10", "8" };

var zr = new ZipRef<int, string>(xs, ys);

bubble_sort(zr);

for (var i = 0; i < xs.Count; ++i) {
	Console.WriteLine($"{xs[i]} {ys[i]}");
}


void bubble_sort<T>(IList<T> list)
	where T : IComparable
{
	var n = list.Count();
	bool swapped;
	do {
		swapped = false;
		for (var i = 1; i < n; ++i) {
			if (list[i-1].CompareTo(list[i]) > 0) {
				var t = list[i-1];
				list[i-1] = list[i];
				list[i] = t;
				swapped = true;
			}
		}
		n -= 1;
	} while (swapped);
}

/* Sadly IList doesn't have List.Sort */
class ZipRef<X, Y> : IList<(X, Y)> {
	private IList<X> xs;
	private IList<Y> ys;

	public ZipRef(IList<X> xs, IList<Y> ys) {
		this.xs = xs;
		this.ys = ys;
	}

	public (X, Y) this[int index] {
		get => (this.xs[index], this.ys[index]);
		set {
			this.xs[index] = value.Item1;
			this.ys[index] = value.Item2;
		}
	}

	public int Count {
		get => Math.Min(this.xs.Count(), this.ys.Count());
	}

	public void Add((X, Y) item) {
	}

	public void Clear() {}
	public int IndexOf((X, Y) item) { return -1; }
	public void Insert(int index, (X, Y) item) {}
	public void RemoveAt(int index) {}


	public bool Contains((X, Y) item) { return false; }
	public void CopyTo((X, Y)[] items, int index) {}
	public bool Remove((X, Y) item) { return false; }
	public bool IsReadOnly { get => false; }

	IEnumerator<(X, Y)> IEnumerable<(X, Y)>.GetEnumerator() { return null; }

	System.Collections.IEnumerator System.Collections.IEnumerable.GetEnumerator() { return null; }
}


