import logging

from function_01 import function_01
from function_02 import function_02
from function_03 import function_03
from function_04 import function_04
from function_05 import function_05
from function_06 import function_06
from function_07 import function_07
from function_08 import function_08
from function_09 import function_09

logger = logging.getLogger(__name__)


def main() -> None:
    logging.basicConfig(level=logging.INFO)
    functions = (
        function_01,
        function_02,
        function_03,
        function_04,
        function_05,
        function_06,
        function_07,
        function_08,
        function_09,
    )
    value = 0
    for function in functions:
        value = function(value)
    logger.warning("pipeline completed result=%s", value)


if __name__ == "__main__":
    main()
