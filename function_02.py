import logging

logger = logging.getLogger(__name__)


def function_02(value: int) -> int:
    logger.info("function_02 received value=%s", value)
    return value + 2
