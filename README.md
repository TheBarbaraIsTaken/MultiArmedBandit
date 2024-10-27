# Multi-armed Bandit

This repository provides a Python implementation of the **Multi-Armed Bandit** problem, a foundational concept in reinforcement learning (RL). The project emulates the core functionalities of the [OpenAI Gym environment](https://github.com/openai/gym), for an intuitive and flexible simulation environment for bandit-based RL problems.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The **Multi-Armed Bandit** problem models a scenario where an agent must choose between multiple options (or "arms"), each providing a reward from a probability distribution. The agent's objective is to maximize cumulative rewards over time by balancing exploration (trying different arms) and exploitation (favoring arms known to yield higher rewards). One simulation ends if the agent won or lost the game. The agent can win the game if he gets reward `win_num` times in a row. The agent can lose the game if he pulled an arm `max_game_num` times and didn't win the game. This repository offers a simulation environment to test and analyze various strategies for tackling this problem.

To learn more about the multi-armed bandit, see this [Wikipedia entry](https://en.wikipedia.org/wiki/Multi-armed_bandit).

## Installation

Clone the repository and install the required dependencies using:

```bash
git clone https://github.com/yourusername/multi-armed-bandit.git
cd multiArmedBandit
pip install -r requirements.txt
```

## Usage

### Setting up the Environment

To use the environment, import `BanditEnv` from `multi_armed_bandit.py`, specifying the number of arms, reward probabilities for each, maximum number of games allowed and number of victories required in a row to win the game:

```python
from multi_armed_bandit import BanditEnv

# Initialize environment with 3 arms
env = BanditEnv(N=3, probs=(0.2, 0.3, 0.5), rewards=(0, 1), max_game_num=200, win_num=25)
```

## Examples

To see a full experiment in action, refer to `main.ipynb`, which contains scripts for evaluating different agent performances and plotting cumulative rewards over time.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
