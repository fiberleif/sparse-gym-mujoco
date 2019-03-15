# sparse-gym-mujoco
sparse gym mujoco: an implementation of sparse mujoco environment in the OpenAI Gym.

This code is used to implement sparse version of various classic mujoco envs in openai gym.
- SparseHopper-v1
- SparseHalfCheetah-v1
- SparseWalker2d-v1
- SparseSwimmer-v1
- SparseAnt-v1
- SparseHumanoid-v1

To install the available environments, simply proceed with:

```python
pip install -e .
```

You will also need to install the mujoco-py binaries and license key, as indicated [here](https://github.com/openai/mujoco-py/tree/0.5). To use the available environments in your code, you need to write these lines:

```python
import gym
import sparse_gym_mujoco

env = gym.make("SparseHopper-v1")
```
