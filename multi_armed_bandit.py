from random import random

class Env():
    def __init__(self, N=3, probs=(0.2, 0.3, 0.5), rewards=(0, 1), max_game_num=200, win_num=25):
        """
        Initializes the environment for the Multi-Armed Bandit problem.

        Args:
            N (int): Number of arms.
            probs (list of floats): Winning probability for each arm.
            rewards (list of floats): Rewards for losing and winning.
            max_game_num (int): Maximum number of games allowed.
            win_num (int): Number of wins required in a row to win the game.
        """
        if N != len(probs):
            raise Exception("Number of probabilities should be equal to the number of arms.")
        
        for p in probs:
            if not (0 <= p <= 1):
                raise Exception("The probabilities should be in interval [0, 1].")

        self.N = N
        self.probs = probs
        self.action_space = [i for i in range(N)]
        self.reward_win, self.reward_lose = rewards
        self.max_game_num = max_game_num
        self.win_num = win_num
        self.game_num = 0
        self.streak = 0


    def reset(self):
        self.game_num = 0
        self.streak = 0

    def step(self, action):
        self.game_num += 1
        if action not in self.action_space:
            raise Exception("Invalid action.")

        r = random()
        p = self.probs[action]

        reward = self.reward_lose
        if r < p:
            reward = self.reward_win
            self.streak += 1
        else:
            self.streak = 0

        observation = ()
        terminated = self.streak == self.win_num
        truncated = self.game_num + 1 > self.max_game_num
        info = dict()

        return observation, reward, terminated, truncated, info



