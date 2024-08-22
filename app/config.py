import json
from typing import Dict


class Config:
    def __init__(self, config_file: str):
        with open(config_file, encoding="utf-8") as file:
            self._config: Dict[str, str] = json.load(file)

    @property
    def current_version(self) -> str:
        return self._config.get("current_version", "Unknown")
