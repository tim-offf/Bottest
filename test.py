import tracemalloc
import sys

tracemalloc.start()

full_list = [_ for _ in range(10_000)]
snap = tracemalloc.take_snapshot()

mini_list = [_ for _ in range(500)]
mini_snap = tracemalloc.take_snapshot()

for stat in snap.statistics('lineno'):
    print(stat)

for stat in mini_snap.compare_to(snap, 'lineno'):
    print(stat)

print(sys.getsizeof(mini_list))
print(sys.getrefcount(full_list))

print("Pizda blyat")
#jjj
