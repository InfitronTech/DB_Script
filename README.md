# Database Data Fetcher

This Python script connects to a PostgreSQL database, queries data based on provided names, and exports the fetched data to a JSON file.

## Table of Contents

- [Introduction](#introduction)
- [Requirements](#requirements)
- [Setup](#setup)
  - [1. Install Dependencies](#1-install-dependencies)
  - [2. Create Virtual Environment (Optional)](#2-create-virtual-environment-optional)
- [Usage](#usage)
- [Additional Notes](#additional-notes)

## Introduction

The `fetch_data.py` script connects to a PostgreSQL database, retrieves data based on a list of names provided in a `names.txt` file, and exports the fetched data to a JSON file named `data.json`.

## Requirements

- `Python 3.x`
- `psycopg2` library (for PostgreSQL database connection)

## Setup

### 1. Install Dependencies

To install the required dependencies, run:

```
pip install psycopg2
```
### 2. Create Virtual Environment (Optional)
It's recommended to use a virtual environment to manage dependencies and isolate the project environment:

- Install virtualenv if you haven't already:
```pip install virtualenv```

- Create a new virtual environment:
`virtualenv venv`

- Activate the virtual environment:

On Windows:
`venv\Scripts\activate`

On macOS and Linux:
`source venv/bin/activate`

## Usage
Run the script:
`python fetch_data.py`

The script connects to the database, fetches data based on the names provided in names.txt, and exports the fetched data to data.json.

## Additional Notes
- Modify the database connection parameters (`dbname`, `user`, `password`, `host`) in the script according to your PostgreSQL database configuration.

- Customize the input source for names by uncommenting the relevant section in the script (reading from a CSV file or directly from code).

- Ensure proper permissions to read from names.txt and write to data.json.

- Handle errors that may occur during database connection, query execution, or file operations.