#  Game Price Comparer (CS50P Project)

A Python CLI application for querying and comparing game and DLC prices across multiple digital storefronts using a public REST API.

---

## 🇺🇸 EN-US

## Overview

**Game Price Comparer** is a command-line application built with Python that enables users to search for a game or DLC and automatically identify the lowest available price across multiple digital stores.

## Demo
https://github.com/user-attachments/assets/c821e6ac-ca05-46f1-96ad-bf74eb35209b

The application consumes an external REST API to retrieve up-to-date pricing data and presents the results in a clear and structured CLI output.

---

## Features

- Search games or DLCs by name
- Automatic title normalization
- Lowest available price detection
- Regular (market) price display
- Direct link to the store page
- Simple CLI interaction

---

## Tech Stack

- Python 3
- Requests
- JSON
- Pytest

---

## Architecture

- Modular structure
- Object-Oriented Design
- Separation of concerns:
  - API layer
  - Business logic
  - CLI layer
- Readable and testable codebase

---

## Usage

1. Run the application in the terminal
2. Choose **game** or **DLC**
3. Enter the product name
4. View pricing and store information

---

## What This Project Demonstrates

- REST API consumption
- JSON data handling
- CLI application design
- Clean and maintainable Python code
- Practical problem-solving through automation

---

## Scope

- Price comparison only
- No authentication or purchases
- No local data storage
- Dependent on external API availability
- Results reflect real-time API responses
