"""Parse a whole run from a yaml file"""

from collections import namedtuple
from .kleedir import KleeDir
from .verificationtasks import TASKS

def get_yaml_load():
	"""Acquires the yaml load function"""
	from yaml import load
	try:
		from yaml import CLoader as Loader
	except ImportError:
		from yaml import Loader
	return lambda file: load(file, Loader)
yaml_load = get_yaml_load()

VerificationFailure = namedtuple("VerificationFailure", ["task", "failures"])

class Batch:
	"""A whole klee-runner batch"""

	def __init__(self, path):
		with open(path) as file:
			self.results = yaml_load(file)["results"]
		for result in self.results:
			kleedir = KleeDir(result["klee_dir"])
			result["klee_dir"] = kleedir
			with open(result["invocation_info"]["misc"]["augmented_spec_file"]) as file:
				spec = yaml_load(file)
			result["spec"] = spec
			failures = []
			for name, task in TASKS.items():
				task_failures = list(task(spec["verification_tasks"][name], kleedir))
				if len(task_failures) > 0:
					failures.append(VerificationFailure(name, task_failures))
			result["failures"] = failures