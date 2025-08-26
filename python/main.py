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


class ZipRef[*Lists]:
    def __init__(self, *lists: *Lists):
        self.lists = lists

    def __len__(self) -> int:
        return min(len(l) for l in self.lists)

    def __getitem__(self, index: int) -> tuple[*Lists]:
        assert isinstance(index, int), "slices are not implemented yet"
        return tuple(l[index] for l in self.lists)

    def __setitem__(self, index: int, cell: tuple[*Lists]):
        assert isinstance(index, int), "slices are not implemented yet"
        for l, v in zip(self.lists, cell): l[index] = v


def main():
    nums = [10, 1, 5, 3, 2]
    bubble_sort(nums)
    assert nums == [1, 2, 3, 5, 10]

    xs = [1, 3, 2]
    ys = ["1", "3", "2"]
    zs = [4, 6, 5]

    zr = ZipRef(xs, ys, zs)
    bubble_sort(zr)
    print(xs, ys, zs)


if __name__ == "__main__":
    main()
