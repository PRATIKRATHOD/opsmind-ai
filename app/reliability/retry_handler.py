import time


def execute_with_retry(function, retries=3, delay=2):

    last_exception = None

    for attempt in range(1, retries + 1):

        try:

            print(f"Attempt {attempt} running...")

            return function()

        except Exception as error:

            print(f"Attempt {attempt} failed: {error}")

            last_exception = error

            time.sleep(delay)

    raise last_exception