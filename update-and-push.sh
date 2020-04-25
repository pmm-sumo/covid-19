#!/usr/bin/env bash
jupyter nbconvert --ExecutePreprocessor.timeout=600 --to notebook --allow-errors --execute Realtime\ R0.ipynb
./push_data.py