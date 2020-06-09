# fibo

Technical home task for a job.

Script to calculate Fibonacci sequence and write it to file.


## Usage

You can just run the script with python:

```python3 fibo.py```

And enter the number when it asks.

You also could you arguments:
* --count --- to enter the count of Fibonacci numbers without ask;
* --path --- path of the output file (default ./fibo.txt).

To test the script install PyTest and run it in script directory.


## Docker

Build Docker image:

```./build_docker.sh```

And run it:

```./run_docker.sh```

Enter the number when it asks. The result file will be in ./result/fibo.txt file.
