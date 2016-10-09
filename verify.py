#!/usr/bin/env python3

from argparse import ArgumentParser
from kleeanalysis import Batch

def main(argv):
	parser = ArgumentParser(description="Perform verification of a klee-runner result yaml file and associated working directory")
	parser.add_argument("path", help="path to the .yml file")
	args = parser.parse_args(args=argv)
	batch = Batch(args.path)
	for result in batch.results:
		kleedir = result["klee_dir"]
		if not kleedir.is_valid:
			print(kleedir.path, "is not valid")
	print()
	for result in batch.results:
		for fail_task in result["failures"]:
			print("Verification failures for task ", fail_task.task, ":", sep="")
			for fail in fail_task.failures:
				print("  ", fail.file, ":", fail.line, sep="")

if __name__ == '__main__':
	import sys
	main(sys.argv[1:])
