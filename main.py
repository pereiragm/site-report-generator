import logging

from reports import SiteReportGenerator

logger = logging.getLogger(__name__)


def main():
    input_file = "files/input_refresh_template.xlsx"
    output_file = "files/output_31_days_report.xlsx"
    rg = SiteReportGenerator(input_file, output_file)
    rg.run()
    logger.info(f"Report {input_file} processed successfully!")


if __name__ == '__main__':
    main()
