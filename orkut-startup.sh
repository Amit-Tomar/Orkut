#!/bin/sh

python -m flask db downgrade;
python -m flask db upgrade;
python -m flask seed;
python -m flask --debug run;
