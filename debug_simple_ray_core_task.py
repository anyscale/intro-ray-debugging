import ray

@ray.remote
def my_task(x):
    breakpoint()
    return x


object_refs = [my_task.remote(i) for i in range(2)]
object_result = ray.get(object_refs)
assert object_result == [0, 1]
