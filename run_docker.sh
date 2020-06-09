#!/bin/bash
docker run -it -v $(pwd)/result:/app/result fibo python /app/fibo.py --path /app/result/fibo.txt
