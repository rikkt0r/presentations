#!/bin/bash
taskset 1 python3 bench.py &
taskset 1 python3 bench.py &
taskset 2 python3 bench.py &
taskset 2 python3 bench.py &
taskset 2 python3 bench.py &
taskset 2 python3 bench.py &

