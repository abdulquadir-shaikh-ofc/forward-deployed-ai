from config import APP_NAME, VERSION
from logger import logger


def main() -> None:
    logger.info(f"Starting {APP_NAME}")
    logger.info(f"Version {VERSION}")

    print()
    print("=" * 50)
    print(APP_NAME)
    print(f"Version: {VERSION}")
    print("=" * 50)
    print("Application started successfully.")
    print()


if __name__ == "__main__":
    main()