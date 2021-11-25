from abc import ABC, abstractmethod


class ActionError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.value = None

class ActionResult:
    def __init__(self, value=None, error=None):
        self.value = value
        self.error = error

    @property
    def succeeded(self):
        return self.error is None

    @property
    def failed(self):
        return self.error is not None


class Action(ABC):
    arguments = list()

    @abstractmethod
    def perform(self): pass

    def fail(self, value):
        raise ActionError(value)

    @classmethod
    def call(cls, **inputs):
        value = error = None

        try:
            value = cls._handle(inputs)
        except Exception as exc:
            error = ActionError('Execution Failed')
            error.__cause__ = exc
            error.value = exc.args[0] if exc.args else None

        return ActionResult(value=value, error=error)

    @classmethod
    def _handle(cls, inputs):
        instance = cls()

        for argument in instance.arguments:
            value = inputs.get(argument)
            setattr(instance, argument, value)

        return instance.perform()
