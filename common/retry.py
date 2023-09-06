from retrying import retry

def retry_handler(retry_time: int, retry_interval: float, retry_on_exception: [BaseException], *args, **kwargs):
    def is_exception(exception: [BaseException]):
        for exp in retry_on_exception:
            if isinstance(exception,exp):
                return True
        return False
        # return isinstance(exception, retry_on_exception)

    def _retry(*args, **kwargs):
        return Retrying(wait_fixed=retry_interval * 1000).fixed_sleep(*args, **kwargs)

    return retry(
        wait_func=_retry,
        stop_max_attempt_number=retry_time,
        retry_on_exception=is_exception
    )