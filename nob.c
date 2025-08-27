#define _GNU_SOURCE
#include <assert.h>
#include <unistd.h>
#include <stdbool.h>

#define NOB_IMPLEMENTATION
#define NOB_STRIP_PREFIX
#include "nob.h"

static void pushd(char const* dir);
static void popd();

struct {
	char const *language;
	char const *directory;
	char const ***commands;

	bool execute;
} static examples[] = {
	{ "C++", "cpp"
	, (char const**[]) { (char const*[]) { "c++", "-std=c++23", "-o", "main", "main.cpp", 0 }
		                 , (char const*[]) { "./main", 0 }
										 , 0
										 }
	},
	{ "C#", "csharp"
	, (char const**[]) { (char const*[]) { "dotnet", "run", 0 }
		                 , 0
										 }
	},
	{ "D", "d"
	, (char const**[]) { (char const*[]) { "dmd", "-run", "main.d", 0 }
		                 , 0
										 }
	},
	{ "Python", "python"
	, (char const**[]) { (char const*[]) { "python3", "main.py", 0 }
		                 , 0
										 }
	},
	{ "Rust", "rust"
	, (char const**[]) { (char const*[]) { "cargo", "run", 0 }
		                 , 0
										 }
	},
};

int main(int argc, char **argv)
{
	NOB_GO_REBUILD_URSELF(argc, argv);

	bool enabled_anything = false;

	while (argc > 0) {
		char const *arg = nob_shift(argv, argc);
		for (size_t i = 0; i < ARRAY_LEN(examples); ++i) {
			if (strcmp(arg, examples[i].language) == 0 || strcmp(arg, examples[i].directory) == 0) {
				examples[i].execute = true;
				enabled_anything = true;
			}
		}
	}

	Cmd cmd = {};

	for (size_t i = 0; i < ARRAY_LEN(examples); ++i) {
		if (enabled_anything && !examples[i].execute) continue;

		nob_log(NOB_INFO, "Language: %s (directory %s)", examples[i].language, examples[i].directory);
		pushd(examples[i].directory);
		for (char const*** cmds = examples[i].commands; *cmds; ++cmds) {
			for (char const** arg = *cmds; *arg; ++arg) da_append(&cmd, *arg);
			cmd_run(&cmd);
		}
		popd();
	}
}

struct
{
	char const** items;
	size_t count, capacity;
} static dirs = {};


void pushd(char const* dir)
{
	da_append(&dirs, get_current_dir_name());
	chdir(dir);
}

void popd()
{
	assert(dirs.count > 0);
	chdir(dirs.items[--dirs.count]);
}

