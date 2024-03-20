# improvements:
# better logging/error handling - custom exceptions, more reliable messages with what is the status/went wrong (Warning, Critical,...)
# more tests - test all the functions in the controller, test the RabbitMQ, test the database)
# better naming of the variables and functions
# better documentation
# improve RabbitMQ - dead letter queue (if message fails to process, it will be moved to the dead letter queue), message acknowledgment (if message is processed, it will be removed from the queue)
# add pre-commit hooks (ruff, mypy,...)
# field description to models


# General improvements/next steps
# add gitlab_ci
# add dockerfile
# add kubernetes
