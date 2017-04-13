import numpy as np
import time

np.set_printoptions(threshold=np.nan)

start = np.random.choice([0, 1], size=(32, 32))
print('starting array:\n', start)


def update(arr):
    new_arr = np.copy(arr)
    for (x, y), cell in np.ndenumerate(arr):
        count = arr[x - 1:x + 2, y - 1:y + 2].sum()
        count = count - cell
        if cell:
            if count < 2:
                cell = 0
            if count > 3:
                cell = 0
            if count >= 2 and count <= 3:
                cell = 1
        else:
            if count == 3:
                cell = 1

        new_arr[x, y] = cell

    return new_arr


nxt = start
for _ in range(32):
    nxt = update(nxt)
    print('\n' * 5,
          nxt,
          '\n' * 5)
    time.sleep(0.1)
