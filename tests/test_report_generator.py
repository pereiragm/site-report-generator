import pandas as pd

from reports import SiteReportGenerator


def test_report_generator_success():
    base_path = "tests/fixtures/"
    input_file = f"{base_path}test_input_refresh_template.xlsx"
    rg = SiteReportGenerator(input_file)
    rg.run()

    output_filepath = f"{base_path}output_5_days_report.xlsx"
    output_file_df = pd.read_excel(output_filepath, header=None)

    expected_header = [
        'Day of Month',
        'Date',
        'Site ID',
        'Page Views',
        'Unique Visitors',
        'Total Time Spent',
        'Visits',
        'Average Time Spent on Site',
    ]

    header = list(output_file_df.values[0])
    shape = output_file_df.values.shape

    assert shape == (11, 8)
    assert header == expected_header

    assert output_file_df.values[1][0] == 1
    assert output_file_df.values[1][1] == "2021/01/01"
    assert output_file_df.values[1][2] == "site 1"
    assert output_file_df.values[1][3] == 6
    assert output_file_df.values[1][4] == 4
    assert output_file_df.values[1][5] == 11
    assert output_file_df.values[1][6] == 4
    assert output_file_df.values[1][7] == 0.1

    assert output_file_df.values[10][0] == 5
    assert output_file_df.values[10][1] == "2021/01/05"
    assert output_file_df.values[10][2] == "site 2"
    assert output_file_df.values[10][3] == 5
    assert output_file_df.values[10][4] == 3
    assert output_file_df.values[10][5] == 6
    assert output_file_df.values[10][6] == 3
    assert output_file_df.values[10][7] == 0.1
