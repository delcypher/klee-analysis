"""
unit tests for the kleeparser.kleedir.Info class
"""

import unittest
import os
from datetime import datetime, timedelta

from ..context import kleeparser
from ..context import TEST_RUNNERDIR

class TestInfoMembers(unittest.TestCase):
	"""
	Test the kleeparser.RunnerDirectory class members
	"""
	@classmethod
	def setUpClass(cls):
		cls.info = kleeparser.kleedir.info.Info(os.path.join(TEST_RUNNERDIR, "klee-wd", "info"))

	def test_member_empty(self):
		"""Test the "empty" member"""
		self.assertIsInstance(self.info.empty, bool)
		self.assertEqual(False, self.info.empty)

	def test_member_command(self):
		"""Test the "command" member"""
		self.assertIsInstance(self.info.command, str)
		# pylint: disable=C0301
		self.assertEqual(self.info.command, r"/home/user/klee/build/Release+Asserts/bin/klee --solver-backend=z3 -libc=uclibc -use-cex-cache=1 --posix-runtime -output-dir=/home/user/out/workdir-0/klee-wd -max-memory=8192 -max-time=1800 /home/user/issta2017/fp-bench/build/benchmarks/c/aachen/real/diction_style.x86_64.bc")
		# pylint: enable=C0301

	def test_member_pid(self):
		"""Test the "pid" member"""
		self.assertIsInstance(self.info.pid, int)
		self.assertEqual(100287, self.info.pid)

	def test_member_start(self):
		"""Test the "start" member"""
		self.assertIsInstance(self.info.start, datetime)
		self.assertEqual(r"2016-10-08T17:14:03", self.info.start.isoformat())

	def test_member_finish(self):
		"""Test the "finish" member"""
		self.assertIsInstance(self.info.start, datetime)
		self.assertEqual(r"2016-10-08T17:53:38", self.info.finish.isoformat())

	def test_member_elapsed(self):
		"""Test the "elapsed" member"""
		self.assertIsInstance(self.info.elapsed, timedelta)
		self.assertEqual(2375, self.info.elapsed.total_seconds())

	def test_member_searcher(self):
		"""Test the "searcher" member"""
		self.assertIsInstance(self.info.searcher, list)
		self.assertEqual(len(self.info.searcher), 4)
		self.assertEqual(self.info.searcher[0], r"<InterleavedSearcher> containing 2 searchers:")
		self.assertEqual(self.info.searcher[1], r"RandomPathSearcher")
		self.assertEqual(self.info.searcher[2], r"WeightedRandomSearcher::CoveringNew")
		self.assertEqual(self.info.searcher[3], r"</InterleavedSearcher>")

	def test_member_explored_paths(self):
		"""Test the "explored_paths" member"""
		self.assertIsInstance(self.info.explored_paths, int)
		self.assertEqual(self.info.explored_paths, 1)

	def test_member_constructs_per_query(self):
		"""Test the "constructs_per_query" member"""
		self.assertIsInstance(self.info.constructs_per_query, int)
		self.assertEqual(self.info.constructs_per_query, 20)

	def test_member_queries(self):
		"""Test the "queries" member"""
		self.assertIsInstance(self.info.queries, int)
		self.assertEqual(self.info.queries, 3)

	def test_member_satisfiable_queries(self):
		"""Test the "satisfiable_queries" member"""
		self.assertIsInstance(self.info.satisfiable_queries, int)
		self.assertEqual(self.info.satisfiable_queries, 1)

	def test_member_unsatisfiable_queries(self):
		"""Test the "unsatisfiable_queries" member"""
		self.assertIsInstance(self.info.unsatisfiable_queries, int)
		self.assertEqual(self.info.unsatisfiable_queries, 2)

	def test_member_cex(self):
		"""Test the "cex" member"""
		self.assertIsInstance(self.info.cex, int)
		self.assertEqual(self.info.cex, 3)

	def test_member_instructions(self):
		"""Test the "instructions" member"""
		self.assertIsInstance(self.info.instructions, int)
		self.assertEqual(self.info.instructions, 10536)

	def test_member_completed_paths(self):
		"""Test the "completed_paths" member"""
		self.assertIsInstance(self.info.completed_paths, int)
		self.assertEqual(self.info.completed_paths, 1)

	def test_member_tests(self):
		"""Test the "tests" member"""
		self.assertIsInstance(self.info.tests, int)
		self.assertEqual(self.info.tests, 1)

if __name__ == '__main__':
	unittest.main()
