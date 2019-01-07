import os


def check_env(env_var_name):
    """
    Check and return the type of an environment variable.

    supported types:
        None
        Integer
        String

    @param env_var_name: environment variable name
    @return: string of the type name.
    """
    try:
        val = os.getenv(env_var_name)
        if val is None:
            return 'None'
    except Exception as ex:
        return "None"

    try:
        int_val = int(val)
        return 'Integer'
    except ValueError:
        return 'String'
