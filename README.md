# site-report-generator
This project contains a script to read an Excel file with non-formatted data about sites
and produces a formated output file with this data organized considering the period
(start date and end date) specified in the input file.

Please check the expected input and output formats as shown on file
[expected_input_output.xlsx](expected_input_output.xlsx)

## Requirements
- Python 3.11.2+

## Installation
Create a virtual environment and activate it:
```commandline
python3 -m venv venv
source venv/bin/activate
```

Install project requirements:
```commandline
pip install -U pip
pip install -r requirements.txt
```

## Usage
Execute the main.py:
```commandline
python main.py
```
Which will process the file located in `files/input_refresh_template.xlsx`
and will generate the output file `output_31_days_report.xlsx` in the folder.

## Tests
To execute the automated tests:
```commandline
pytest -v
```
