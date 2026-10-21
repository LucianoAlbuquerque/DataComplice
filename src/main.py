from app_logging.config_logging import get_logger
from my_package.my_module import my_function


def run() -> None:
    print("Running the main function...")


if __name__ == "__main__":
    # Instale o pacote: python-dotenv
    # Mostrei como no README.md
    my_result = my_function(1, 2)
    print(f"The result is {my_result}")

    logger = get_logger("meuapp")
    logger.debug("Esse é meu primeiro teste")
