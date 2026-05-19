from datetime import datetime, timedelta
import os
art = [
"                                                                                                    ",
"         ###########                                                                                ",
"      #################                                                                             ",
"    #####################                                  #####        #########       #####      ",
"   #######################                              ###########    #############   #########    ",
"   ################                                         #####      #####   #####    #####       ",
"   #######################                                 #####       #####   #####      #####     ",
"    #####################                              ###########    #############   ###########   ",
"      #################                                   #####        #########       #####       ",
"         ###########                                                                                ",
"                                                                                                    ",
]
start = datetime(2023, 1, 1, 12, 0, 0)
end   = datetime(2026, 5, 19, 12, 0, 0)

total_days = (end - start).days
width = len(art[0])
step = total_days // width

for y, row in enumerate(art):
    for x, cell in enumerate(row):
        if cell != " ":
            day = start + timedelta(days=x * step + y)
            date = day.strftime("%Y-%m-%dT12:00:00")

            with open("art.txt", "a") as f:
                f.write(f"{date}\n")

            os.system("git add art.txt")
            os.system(
                f'GIT_AUTHOR_DATE="{date}" '
                f'GIT_COMMITTER_DATE="{date}" '
                f'git commit --allow-empty -m "pacman {x}-{y}"'
            )

print("Done!")
