from dataclasses import (
    dataclass,
    field,
)

from src.infrastructure.db.config import DBConfig
from src.settings.config import (
    API_HOST,
    API_PORT,
)


@dataclass
class APIConfig:
    host: str = API_HOST
    port: int = API_PORT
    debug: bool = __debug__


@dataclass
class MConfig:
    db: DBConfig = field(default_factory=DBConfig)
    api: APIConfig = field(default_factory=APIConfig)
