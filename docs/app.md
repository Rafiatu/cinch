## About

The app folder houses actions that the api will depend on for handling request. These actions are service objects or simply objects where we define our actual business logics within this project. This is because we do not want business logics to live in Django views as this is a common practice for most projects and MIGHT not make it easy to add more features or maintain the project.

## Base Action Class

All action classes that will be defined within our project must inherit from the base action class defined in `app/action.py`. This base class ensures that the developer specifies what the action arguments, implements the method `perform` that describes what needs to happen and is able to execute the action by calling the class method `call`

```python

# Import base action class

from app.action import Action

# Define the action !!!

class CreateArtist(Action):
    arguments = ['name', 'gender']

    def perform(self):
        # Desribe what needs to happen here and you can even create more
        # method within this action class that will be called here.

        # Instance attributes self.name & self.gender will automatically
        # be availble with values passed into the action during call.
        pass

# Call the action !!!
# Through result object returned, you have access to two attributes, namely
#   [value] The return value from the `perform` method
#   [error] Exception object representing error raised during action execution

result = CreateArtist.call(name='John Doe', gender='Male')
result.value
result.error

```

## Notes & Caveats

- As long as action inherit from the base action class, everything should work as expected
- Actions can be grouped into related set of actions. E.g actions for sending emails
- Watch out for updates to the base action class to be sure that they do not break the system
