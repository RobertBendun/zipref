# TODO: Explain why this approach doesn't work

def bubble_sort[T](xs: list[T]):
    n = len(xs)
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, n):
            if xs[i - 1] > xs[i]:
                xs[i-1], xs[i] = xs[i], xs[i-1]
                swapped = True
        n -= 1


class ZipRef[T, U]:
    def __init__(self, xs: list[T], ys: list[U]):
        self.xs, self.ys = xs, ys

    def __len__(self) -> int:
        return min(len(self.xs), len(self.ys))

    def __getitem__(self, index: int) -> 'Cell':
        assert isinstance(index, int), "slices are not implemented yet"
        return Cell(self, index)

    def __setitem__(self, index: int, cell: 'Cell'):
        assert isinstance(index, int), "slices are not implemented yet"
        print(self[index], cell)
        self.xs[index], self.ys[index] = cell.zr.xs[cell.index], cell.zr.ys[cell.index]



class Cell[T, U]:
    def __init__(self, zr: ZipRef[T, U], index: int):
        self.zr, self.index = zr, index

    def __iter__(self):
        return iter((self.zr.xs[self.index], self.zr.ys[self.index]))

    def __lt__(self, other: 'Cell'):
        return (*self, ) < (*other, ) if isinstance(other, Cell) else NotImplemented

    def __repr__(self) -> str:
        x, y = self.zr.xs[self.index], self.zr.ys[self.index]
        return f"Cell({repr(x)}, {repr(y)})"


def main():
    nums = [10, 1, 5, 3, 2]
    bubble_sort(nums)
    assert nums == [1, 2, 3, 5, 10]

    xs = [1, 3, 2]
    ys = ["1", "3", "2"]

    zs = ZipRef(xs, ys)
    bubble_sort(zs)
    print(xs, ys)


if __name__ == "__main__":
    main()
