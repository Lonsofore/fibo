FROM python:3-slim

# copy script files
COPY ./fibo.py ./test_fibo.py ./requirements.txt /app/

# test the script
RUN pip install --no-cache-dir -r /app/requirements.txt
RUN pytest /app

CMD python /app/fibo.py
