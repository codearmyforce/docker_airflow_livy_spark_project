#!/bin/bash

curl POST --data '{"file": "file:/opt/jars/test.py", "className": "org.apache.spark.examples.SparkPi"}' -H "Content-Type: application/json" http://172.19.0.4:8998/batches/

