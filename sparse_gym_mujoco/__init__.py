# register all sparse envs (self-made) to gym
from gym.envs.registration import register

register(
    id='SparseHalfCheetah-v1',
    entry_point='sparse_gym_mujoco.envs.sparse_halfcheetah:SparseHalfCheetahEnv',
    max_episode_steps=1000,
    reward_threshold=4800.0,
)

register(
    id='Hopper-v1',
    entry_point='sparse_gym_mujoco.envs.sparse_hopper:SparseHopperEnv',
    max_episode_steps=1000,
    reward_threshold=3800.0,
)

register(
    id='Swimmer-v1',
    entry_point='sparse_gym_mujoco.envs.sparse_swimmer:SparseSwimmerEnv',
    max_episode_steps=1000,
    reward_threshold=360.0,
)

register(
    id='Walker2d-v1',
    max_episode_steps=1000,
    entry_point='sparse_gym_mujoco.envs.sparse_walker2d:SparseWalker2dEnv',
)

register(
    id='Ant-v1',
    entry_point='sparse_gym_mujoco.envs.sparse_ant:SparseAntEnv',
    max_episode_steps=1000,
    reward_threshold=6000.0,
)

register(
    id='Humanoid-v1',
    entry_point='sparse_gym_mujoco.envs.sparse_humanoid:SparseHumanoidEnv',
    max_episode_steps=1000,
)