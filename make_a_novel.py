import gpt_2_simple as gpt2
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


def postprocess_file():
    outfile = open('processedstory.txt', 'w')
    with open('storyguide.txt', 'r') as infile:
        raw_text = infile.readline()
        while raw_text:
            print(raw_text)
            if raw_text and raw_text[0] not in ['>', '-', '+']:
                outfile.write(raw_text)
            raw_text = infile.readline()
    outfile.close()


def makethenovel():
    sess = gpt2.start_tf_sess()
    gpt2.load_gpt2(sess)  # Loads the fine-tuned model
    with open('processedstory.txt', 'r') as infile, \
            open('masterpiece.txt', 'w') as novel:
        raw_text = infile.readline()
        while raw_text:
            while not raw_text:  # Skip blank lines
                print("no blank lines, silly")
                raw_text = infile.readline()
            print(f"Processing: {raw_text}")
            novel_line = gpt2.generate(sess, prefix=raw_text,
                                       return_as_list=True)[0]
            print(novel_line, file=novel)
            raw_text = infile.readline()


if __name__ == '__main__':
    play_filename = create_textworld_ulx()
    pt.play_text(play_filename)
    postprocess_file()
    makethenovel()
