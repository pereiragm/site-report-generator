from typing import Any, List

import pandas as pd


class SiteReportGenerator:
    def __init__(self, file_path: str, input_sheet_name: str, output_sheet_name: str):
        self.file_path = file_path
        self.input_sheet_name = input_sheet_name
        self.output_sheet_name = output_sheet_name
        self.df = pd.read_excel(
            self.file_path,
            sheet_name=input_sheet_name,
            header=None,  # do not consider first row as header
        )

    def _get_headers(self) -> List[str]:
        headers = ["Day of Month", "Date", "Site ID"]
        # Extract the following column names
        for cn in self.df.values[1][1:]:
            if cn != headers[-1]:
                headers.append(cn)
        return headers

    def _extract_data_from_input_sheet(self, n_days_period) -> List[List[Any]]:
        output_data = []
        site_idx = 3  # First row idx for the site
        n_rows, n_cols = self.df.values.shape
        while site_idx <= n_rows:
            site_id = self.df.values[site_idx][0]
            for day_of_month in range(1, n_days_period + 1):
                date = (self.df.values[site_idx - 1][day_of_month])
                page_views = self.df.values[site_idx][day_of_month]
                unique_visitors = self.df.values[site_idx][day_of_month + n_days_period]
                total_time_spent = self.df.values[site_idx][
                    day_of_month + (2 * n_days_period)]
                visits = self.df.values[site_idx][day_of_month + (3 * n_days_period)]
                avg_time_spent = self.df.values[site_idx][
                    day_of_month + (4 * n_days_period)]

                output_data.append([
                    day_of_month,
                    date.strftime("%Y/%m/%d"),
                    site_id,
                    page_views,
                    unique_visitors,
                    total_time_spent,
                    visits,
                    avg_time_spent,
                ])

            site_idx += 3

        return output_data

    def _save(self, data, headers):
        with pd.ExcelWriter(self.file_path, engine="openpyxl", mode="a",
                            if_sheet_exists="replace") as writer:
            df_out = pd.DataFrame(data, columns=headers)
            df_out.to_excel(writer, sheet_name=self.output_sheet_name, index=False)

    def run(self):
        """Extract, format and save report data in another sheet of the same file."""

        start_date = self.df.values[0][0]
        end_date = self.df.values[1][0]
        n_days_period = (end_date - start_date).days + 1
        headers = self._get_headers()
        output_data = self._extract_data_from_input_sheet(n_days_period)
        self._save(output_data, headers)
