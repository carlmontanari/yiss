"""yiss.decorators"""


def require_model(wrapped_func):
    """
    Enforce having 'model_version' set for methods requiring model data

    Args:
        wrapped_func: function to be wrapped

    Returns:
        wrapped function if permitted

    Raises:
        ValueError: if no model version is set

    """

    def decorate(self, *args, **kwargs):
        if getattr(self, "model_version") is None:
            raise ValueError("No model version set...")
        return wrapped_func(self, *args, **kwargs)

    return decorate
