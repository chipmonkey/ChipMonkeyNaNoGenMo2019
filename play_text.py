import gym
import textworld.gym


def play_text(ulx_filename):
    # Register a text-based game as a new Gym's environment.
    env_id = textworld.gym.register_game(ulx_filename,
                                         max_episode_steps=50)

    env = gym.make(env_id)  # Start the environment.

    obs, infos = env.reset()  # Start new episode.
    env.render()

    outfile = open('storyguide.txt', 'w+')

    score, moves, done = 0, 0, False
    while not done:
        command = input("> ")
        obs, score, done, infos = env.step(command)
        env.render()
        outfile.write(env.render('text'))
        moves += 1
        # import pdb; pdb.set_trace()

    env.close()
    print("moves: {}; score: {}".format(moves, score))

if __name__ == "__main__":
    play_text("tw_games/game2.ulx")
