HyperPUT
=============================


HyperPUT: Program Under Test generator to challenge, compare, study and improve automated testing frameworks. It supports fuzzing frameworks, symbolic execution engines and model checking tools.

------------------------------



### Configuration files:

- **utilities/config.py:** Main program settings. Several examples of configuration parameters are provided in the comments in order to produce different batches of Programs Under Test (PUTs).
- **transformation.list:** List of transformations to apply with corresponding input sources and parameters.


### Add new transformations 

New transformations can be defined in file *hyperput.h*.
The corresponding scripts to generate valid inputs are located in folder *\<HYPER_PUT_DIR\>/transformations/*.


### Add new testing frameworks

New testing frameworks can be added by defining a function test_<testing_framework_name> in file *transform.sh*.


### Add new categories of tests

New categories of tests can be executed by combining the available parameters in file *utilities/config.py*.
In addition, it is possible to implement new variations in file *test.py*.


### Execution

After the selection of program settings (as previously described), the PUT generator can be started with the following commands:


```
chmod u+x test.py
./test.py
```



Test outcomes are saved in file *transform.sh.csv*.


### Example

After the execution of the previous command, based on the default configuration, a simple PUT composed of seven transformations is produced and it is analyzed by AFL with a timeout of one hour.


### Software dependencies

- Python3
- Bash
- A compiler (at least). Supported compilers include: GCC, LLVM (clang).
- A testing framework (at least). Supported testing frameworks include: AFL, KLEE, CBMC, zzuf.





*HyperPUT v0.407. Prototype implementation.*
*Included external dependencies are the property of their respective owners.*
