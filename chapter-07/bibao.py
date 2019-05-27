def make_average():
    val_list = []

    def func(val):
        val_list.append(val)
        print(sum(val_list) / len(val_list))

    return func


m_a = make_average()
m_a(10)
m_a(11)
m_a(12)


def make_average2():
    total = 0
    count = 0

    def func(val):
        nonlocal total, count
        total += val
        count += 1
        print(total / count)

    return func


m_a = make_average2()
m_a(1)
m_a(2)
m_a(4)
