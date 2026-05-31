# Exercise 42: Data Analysis Pipeline
# Objective: Process sales data from file using statistics module

import statistics
import os

FILE = "sales.txt"

def create_sample_sales():
    with open(FILE, "w") as f:
        f.write("1500\n2300\n1800\n4200\n3100\n2750\n1950\n3600\n")

def analyze_sales(filename):
    try:
        with open(filename, "r") as f:
            lines = f.readlines()
        data = []
        for line in lines:
            try:
                data.append(float(line.strip()))
            except ValueError:
                print(f"  Skipping invalid value: '{line.strip()}'")
        if not data:
            raise ValueError("No valid data in file.")
        print(f"Sales Data : {data}")
        print(f"Count      : {len(data)}")
        print(f"Mean       : Rs.{statistics.mean(data):.2f}")
        print(f"Median     : Rs.{statistics.median(data):.2f}")
        print(f"Std Dev    : Rs.{statistics.stdev(data):.2f}")
    except FileNotFoundError:
        print(f"Error: '{filename}' not found.")

create_sample_sales()
analyze_sales(FILE)
