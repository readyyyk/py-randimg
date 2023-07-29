import random
import drawsvg


def string_to_int64(string):
    res = 1
    for i in string:
        res *= ord(i)
    return res


def hashmap(seed, w, h):
    random.seed(string_to_int64(seed))

    res = drawsvg.Drawing(w, h)
    res.append(drawsvg.Rectangle(0, 0, w, h))
    for i in range(h):
        for j in range(w):
            res.append(
                drawsvg.Rectangle(
                    i, j,
                    1, 1,
                    fill="#000" if random.randint(0, 1) else "#fff")
            )

    res.append_title(f"@{seed}")

    return res.as_svg()
