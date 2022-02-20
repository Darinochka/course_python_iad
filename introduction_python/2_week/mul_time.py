h_1, m_1, s_1 = int(input()), int(input()), int(input())
h_2, m_2, s_2 = int(input()), int(input()), int(input())

seconds_1 = h_1 * 3600 + m_1 * 60 + s_1
seconds_2 = h_2 * 3600 + m_2 * 60 + s_2
print(seconds_2 - seconds_1)