## About

Here, we talk about the custom response class created at `api/lib/response.py`. This is to ensure consistency in the structure of the response body we are sending to the clients.

We decided to ensure that all responses are structured as below

```python

# For success response: Errors should always be None

{
    "message": "success",
    "data": { ... },
    "errors": None
}

# For error response : Data should always be None

{
    "message": "failure",
    "data": None
    "errors": { ... }
}

```
The message value is auto-generated based on what data and errors are. However, what goes in the data or errors dictionaries is decided by the developer, but this custom response class ensures the top level structure.

## About Errors

Usually, errors can come from validation of fields or other type of business contraints validations and due to this, the developer should structure the errors if there are any as below

```python

{
    "message": "failure",
    "data": None
    "errors": {
        "field-1": [ ... ],
        "field-2": [ ... ],
        ...
        ...
        "field-n": [ ... ],
        "_others": [ ... ],
    }
}

```

Notice the `_others` field in the errors dictionary, that is to hold all errors not specific to a field. If it is not provided, it will automatically be added and set to an empty list - `[]`
