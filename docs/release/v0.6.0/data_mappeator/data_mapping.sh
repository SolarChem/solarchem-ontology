#!/bin/bash

START=$(date +%s)

echo "Starting with data conversion from db..."
python3 db_data_conversion/main.py

END=$(date +%s)
DIFF=$(( $END - $START ))

echo "Data conversion done. Time needed: $DIFF seconds"

START=$(date +%s)

echo "Starting with the mapping process..."
java -jar r2rml.jar ./config.properties

END=$(date +%s)
DIFF=$(( $END - $START ))

echo "Mapping done. Time needed: $DIFF seconds"