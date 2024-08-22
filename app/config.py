import json
from typing import Dict
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Config:
    def __init__(self, config_file: str):
        try:
            with open(config_file, encoding="utf-8") as file:
                self._config: Dict[str, str] = json.load(file)
        except FileNotFoundError:
            logger.error(f"Config file {config_file} not found.")
            self._config = {}
        except json.JSONDecodeError:
            logger.error(
                f"Error decoding JSON in config file {config_file}."
            )
            self._config = {}
        except Exception as e:
            logger.error(
                f"Unexpected error reading config file {config_file}: {e}"
            )
            self._config = {}

    @property
    def current_version(self) -> str:
        return self._config.get("current_version", "Unknown")
