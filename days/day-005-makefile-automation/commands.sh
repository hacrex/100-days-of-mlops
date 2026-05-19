#!/bin/bash
# Day 5 - Makefile Automation

# --- Check if make is installed ---
make --version

# --- Run a specific target ---
make install

# --- Run the default target ---
make

# --- Run multiple targets ---
make clean install train

# --- Dry run (show commands without executing) ---
make -n train

# --- Run with a variable override ---
make train MODEL=xgboost

# --- List all available targets (if .PHONY is documented) ---
make help

# --- Run in a specific directory ---
make -C days/day-005-makefile-automation install
