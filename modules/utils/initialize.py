import logging
# import os
import importlib.util
from pathlib import Path


def setup_logging():
    project_root = Path(__file__).parent.parent.parent
    log_dir = project_root / "logs"
    log_dir.mkdir(exist_ok=True)
    log_file = log_dir / "aitools.log"

    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )

    return logging.getLogger(__name__)


def load_config():
    project_root = Path(__file__).parent.parent.parent
    config_path = project_root / "config.py"

    if not config_path.exists():
        raise FileNotFoundError(f"Configuration file not found: {config_path}")

    spec = importlib.util.spec_from_file_location("config", config_path)
    config_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(config_module)

    return {
        "user_name": getattr(config_module, "USER_NAME", "User"),
        "model_name": getattr(config_module, "MODEL_NAME", "llama3.1:latest")
    }


def initialize():
    logger = setup_logging()
    config = load_config()
    logger.info("Initialization complete")
    return logger, config


if __name__ == "__main__":
    logger, config = initialize()
    logger.info(f"Configuration loaded: {config}")
