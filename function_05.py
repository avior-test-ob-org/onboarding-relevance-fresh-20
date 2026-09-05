import logging

logger = logging.getLogger(__name__)


def function_05(value: int) -> int:
    logger.info("function_05 received value=%s", value)
    return value + 5
