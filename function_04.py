import logging

logger = logging.getLogger(__name__)


def function_04(value: int) -> int:
    logger.info("function_04 received value=%s", value)
    return value + 4
