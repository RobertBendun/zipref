#include <array>
#include <iostream>
#include <ranges>
#include <string_view>
#include <print>
#include <algorithm>

int main()
{
	using namespace std::string_view_literals;

	std::array xs = { 1, 3, 2 };
	std::array ys = { "1"sv, "3"sv, "2"sv };
	std::array zs = { 4, 6, 5 };

	std::ranges::sort(std::ranges::views::zip(xs, ys, zs));
	std::println("{} {} {}", xs, ys, zs);
}
