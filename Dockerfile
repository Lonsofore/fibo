# test stage
FROM python:3-slim

# copy script files
COPY ./fibo.py ./test_fibo.py ./requirements_test.txt /app/

# test the script
RUN pip install --no-cache-dir -r /app/requirements_test.txt
RUN pytest /app


# final stage
FROM python:3-slim

# copy script file
COPY ./fibo.py /app/

# run script
CMD python /app/fibo.py
