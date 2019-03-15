# register all sparse envs (self-made) to gym
from gym.envs.registration import register

register(
    id='SparseHalfCheetah-v1',
    entry_point='sparse_gym_mujoco.envs.sparse_halfcheetah:SparseHalfCheetahEnv',
    max_episode_steps=1000,
    reward_threshold=4800.0,
)

register(
    id='SparseHopper-v1',
    entry_point='sparse_gym_mujoco.envs.sparse_hopper:SparseHopperEnv',
    max_episode_steps=1000,
    reward_threshold=3800.0,
)

register(
    id='SparseSwimmer-v1',
    entry_point='sparse_gym_mujoco.envs.sparse_swimmer:SparseSwimmerEnv',
    max_episode_steps=1000,
    reward_threshold=360.0,
)

register(
    id='SparseWalker2d-v1',
    max_episode_steps=1000,
    entry_point='sparse_gym_mujoco.envs.sparse_walker2d:SparseWalker2dEnv',
)

register(
    id='SparseAnt-v1',
    entry_point='sparse_gym_mujoco.envs.sparse_ant:SparseAntEnv',
    max_episode_steps=1000,
    reward_threshold=6000.0,
)

register(
    id='SparseHumanoid-v1',
    entry_point='sparse_gym_mujoco.envs.sparse_humanoid:SparseHumanoidEnv',
    max_episode_steps=1000,
)