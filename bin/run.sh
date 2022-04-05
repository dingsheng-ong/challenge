#!/bin/sh

mkdir results
python3 bin/calc_fractal.py 3 results/data.dat
python3 bin/fig1.py
python3 bin/calc_fractal.py 5 results/data.dat
python3 bin/fig2.py
python3 bin/calc_fractal.py 6 results/data.dat
python3 bin/fig3.py
python3 bin/fig4.py