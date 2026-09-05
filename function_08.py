import logging

logger = logging.getLogger(__name__)


def function_08(value: int) -> int:
    logger.info("function_08 received value=%s", value)
    return value + 8
