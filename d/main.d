void main() {
	import std.stdio : writeln;
	import std.range : zip;
	import std.algorithm.sorting : sort;

	auto xs = [1, 3, 2];
	auto ys = ["1", "3", "2"];
	auto zs = [4, 6, 5];

	zip(xs, ys, zs).sort();

	writeln(xs, " ", ys, " ", zs);
}
