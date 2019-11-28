import shlex
import subprocess
import play_text as pt


def create_textworld_ulx():
    # short from http://code.activestate.com/recipes/577058/
    valid = {"yes": "yes", "y": "yes", "ye": "yes",
             "no": "no", "n": "no"}
    choice = "dunno"

    prompt = \
        """Do you want to create a new story?
        [N] will use a pre-generated story. [Y/N]"""

    while choice not in valid.keys():
        print(prompt)
        choice = input().lower()
    choice = valid[choice] == "yes"

    print(choice)

    if choice:
        play_filename = "tw_games/game2.ulx"
    else:
        play_filename = "tw_games/custom_game.ulx"

    if not choice:
        cmd = f"tw-make custom --world-size 15 --nb-objects 20 \
                --quest-length 20 --seed 1729 --output {play_filename}"
        args = shlex.split(cmd)
        _ = subprocess.Popen(args)

    return(play_filename)


play_filename = create_textworld_ulx()
pt.play_text(play_filename)
