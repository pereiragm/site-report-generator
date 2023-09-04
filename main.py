import logging

from reports import SiteReportGenerator

logger = logging.getLogger(__name__)


def main():
    input_file = "inputs/analytics_template.xlsx"
    input_sheet_name = "input_refresh_template"
    output_sheet_name = "output_31_days_report"
    rg = SiteReportGenerator(input_file, input_sheet_name, output_sheet_name)
    rg.run()
    logger.info(f"Report {input_file} processed successfully!")


if __name__ == '__main__':
    main()
