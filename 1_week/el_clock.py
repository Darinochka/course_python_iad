n = int(input())

# --------------- first task------------------------

# hours = n // 60 % 24
# minutes = n % 60

# print(hours, minutes)

# ---------------- second task---------------------

hours = n // 3600 % 24
minutes = n // 60 % 60
seconds = n % 60

print(f"{hours}:{minutes:02n}:{seconds:02n}")
