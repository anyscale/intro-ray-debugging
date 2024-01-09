import ray

@ray.remote
def flaky_double(x):
    if x == 1:
        raise ValueError("I don't like 1")
    return 2 * x


object_ref = flaky_double.remote(1)
object_results = ray.get(object_ref)
assert object_results == 2
