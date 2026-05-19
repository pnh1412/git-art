from datetime import datetime, timedelta
import os

start = datetime(2023, 1, 1, 12, 0, 0)
end = datetime(2026, 5, 19, 12, 0, 0)

current = start

while current <= end:
    date = current.strftime("%Y-%m-%dT12:00:00")

    with open("art.txt", "a") as f:
        f.write(f"{date}\n")

    os.system("git add art.txt")
    os.system(
        f'GIT_AUTHOR_DATE="{date}" '
        f'GIT_COMMITTER_DATE="{date}" '
        f'git commit --allow-empty -m "contribution {date}"'
    )

    current += timedelta(days=1)

print("Done!")
