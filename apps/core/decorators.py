from decouple import config

from apps.core.constants import (
    DEVELOPMENT_SERVER,
    LOCAL_SERVER,
)


def restrict_command_to_development_environment(function):
    def wrapper(*args, **kwargs):
        if config("ENV_NAME") not in [LOCAL_SERVER, DEVELOPMENT_SERVER]:
            print(
                "Error: Cannot run this command in non-testing environment.",
            )
            return
        return function(*args, **kwargs)

    return wrapper
