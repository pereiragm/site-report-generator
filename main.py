import logging

from reports import SiteReportGenerator

logger = logging.getLogger(__name__)


def main():
    input_file = "files/input_refresh_template.xlsx"
    rg = SiteReportGenerator(input_file)
    rg.run()
    logger.info(f"Report {input_file} processed successfully!")


if __name__ == '__main__':
    main()
