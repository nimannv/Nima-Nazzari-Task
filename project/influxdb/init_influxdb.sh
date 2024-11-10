#!/bin/sh

sleep 10

# Load initial data from CSV file
influx write --bucket spectral --format csv --org spectral --file /docker-entrypoint-initdb.d/initial_data.csv --header "#constant measurement,meterusage" --header "#datatype dateTime:RFC3339,double" --skipRowOnError