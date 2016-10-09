# Requirements
The only external requirement should be [PyYAML](http://pyyaml.org/wiki/PyYAML)

# Usage
An example tool is provided with [`verify.py`](verify.py), which only takes a single argument, the path to a klee-runner output yaml file.
It will then attempt to load all associated files and find problems with them.

For example, if KLEE has been terminated by klee-runner, the result directory might end up in a broken state.
Should that happen, a message similar to the following will be printed:
```
/home/user/out/run2/workdir-9/klee-wd is not valid
```

The specified verification tasks will also be performed:
```
Verification failures for task no_reach_error_function:
  /home/user/issta2017/fptest/real/gmp/gmp-6.1.1/invalid.c:84
Verification failures for task no_integer_division_by_zero:
  /home/user/issta2017/fptest/real/gmp/gmp-6.1.1/errno.c:55
Verification failures for task no_assert_fail:
  /home/user/issta2017/fptest/real/sorting/main.c:10
```

## Library
The primary library entry point is `kleeanalysis.Batch`, which takes the path to an klee-runner output yaml file and does all of the above.