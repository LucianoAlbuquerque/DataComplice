from app_logging.config_logging import get_logger

if __name__ == "__main__":
    # criando o logger
    logger = get_logger("meuapp")
    logger.debug("Logger criado com sucesso! Podemos programar com segurança.")
