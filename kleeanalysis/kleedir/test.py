"""KLEE test cases"""

import os
import re
from collections import namedtuple
from ..exceptions import InputError

def _force_match(regex, line, message, path):
	match = regex.fullmatch(line)
	if not match:
		raise InputError(message.format(path))
	return match

Early = namedtuple("Early", ["message"])
def _parse_early(path):
	"""Load a .early file"""
	try:
		with open(path) as file:
			return Early(file.readlines())
	except FileNotFoundError:
		return None

ErrorFile = namedtuple("ErrorFile", ["message", "file", "line", "assembly_line", "stack"])

_RE_ERROR = re.compile(r"Error: (.*)\r?\n")
_RE_FILE = re.compile(r"File: (.*)\r?\n")
_RE_LINE = re.compile(r"Line: (\d+)\r?\n")
_RE_ASSEMBLY_LINE = re.compile(r"assembly.ll line: (\d+)\r?\n")

def _parse_error(path):
	try:
		with open(path) as file:
			match = _force_match(_RE_ERROR, file.readline(), "{}: Invalid error message in line 1", path)
			message = match.group(1)
			match = _force_match(_RE_FILE, file.readline(), "{}: Invalid file in line 2", path)
			filename = match.group(1)
			match = _force_match(_RE_LINE, file.readline(), "{}: Invalid line number in line 3", path)
			line = int(match.group(1))
			match = _force_match(_RE_ASSEMBLY_LINE, file.readline(), "{}: Invalid assembly.ll line number in line 4", path)
			assline = int(match.group(1))
			if file.readline().rstrip() != "Stack:":
				raise InputError("{}: Invalid begin stacktrace stack in line 5".format(path))
			stack = file.readlines()
			return ErrorFile(message, filename, line, assline, stack)
	except FileNotFoundError:
		return None

class Test:
	"""
	A KLEE test case

	Attributes:
		early -- early termination info (None if it did not happen)
		error -- execution error info (None if it did not happen)
		abort -- abortion error info (None if it did not happen)
		assertion -- assertion error info (None if it did not happen)
		division -- division error info (None if it did not happen)
	"""

	def __mkerror(self, name, suffix):
		"""load error file if it exists and add an attribute for it"""
		error = _parse_error(self.__pathstub + suffix)
		self.__dict__[name] = error
		if error is not None:
			assert self.error is None
			self.error = error

	def __init__(self, path: "path to the klee working directory", identifier: "numeric identifier"):
		"""Load a KLEE test case"""
		self.__pathstub = os.path.join(path, "test{:06}".format(identifier))
		self.error = None
		self.early = _parse_early(self.__pathstub + ".early")
		self.__mkerror("execution_error", ".exec.err")
		self.__mkerror("abort", ".abort.err")
		self.__mkerror("division", ".div.err")
		self.__mkerror("assertion", ".assert.err")
		self.__mkerror("free", ".free.err")
		self.__mkerror("ptr", ".ptr.err")
		self.__mkerror("overshift", ".overshift.err")
		self.__mkerror("readonly_error", ".readonly.err")
		self.__mkerror("user_error", ".user.err")
		self.__mkerror("overflow", ".overflow.err")

	@property
	def ktest_path(self):
		"""Path to the matching .ktest file"""
		return self.__pathstub + ".ktest"

	@property
	def pc_path(self):
		"""Path to the matching .pc file"""
		return self.__pathstub + ".pc"
