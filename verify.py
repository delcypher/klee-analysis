#!/usr/bin/env python3

from argparse import ArgumentParser
from kleeanalysis import Batch

def main(argv):
	parser = ArgumentParser(description="Perform verification of a klee-runner result yaml file and associated working directory")
	parser.add_argument("path", help="path to the .yml file")
	args = parser.parse_args(args=argv)
	batch = Batch(args.path)
	for result in batch.results:
		failure_found = False
		kleedir = result["klee_dir"]
		if result["exit_code"] is not None and result["exit_code"] != 0:
			failure_found = True
			print(kleedir.path, "terminated with exit code", result["exit_code"])
		if result["out_of_memory"]:
			failure_found = True
			print(kleedir.path, "killed due to running out of memory")
		if result["backend_timeout"]:
			failure_found = True
			print(kleedir.path, "killed due to running out allotted time")
		if not kleedir.is_valid:
			failure_found = True
			print(kleedir.path, "is not valid")
		else:
			if len(result["failures"]) > 0:
				failure_found = True
				print(kleedir.path, ":", sep="")
				for fail_task in result["failures"]:
					print("  Verification failures for task ", fail_task.task, ":", sep="")
					for fail in fail_task.failures:
						print("    Test {:06} in {}:{}".format(fail.identifier, fail.error.file, fail.error.line))
		if failure_found:
			print()

if __name__ == '__main__':
	import sys
	main(sys.argv[1:])
