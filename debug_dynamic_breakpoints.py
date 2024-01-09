import ray

def part1():
    return 1

def part2(x: int) -> int:
    ret = x * 4
    ret = ret + 1
    ret = ret + 3
    return ret

@ray.remote
def my_main_task() -> int:
    breakpoint()
    x = part1()
    y = part2(x)
    return y


object_ref = my_main_task.remote()
object_result = ray.get(object_ref)
assert object_result == 8