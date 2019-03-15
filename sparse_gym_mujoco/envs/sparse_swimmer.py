import numpy as np
from gym import utils
from sparse_gym_mujoco.envs.mujoco_env import MujocoEnv


class SparseSwimmerEnv(MujocoEnv, utils.EzPickle):
    def __init__(self):
        MujocoEnv.__init__(self, 'swimmer.xml', 4)
        utils.EzPickle.__init__(self)

    def _step(self, a):
        ctrl_cost_coeff = 0.0001
        xposbefore = self.model.data.qpos[0, 0]
        self.do_simulation(a, self.frame_skip)
        xposafter = self.model.data.qpos[0, 0]

        # --------- Dense Reward ---------
        # reward_fwd = (xposafter - xposbefore) / self.dt
        # reward_ctrl = - ctrl_cost_coeff * np.square(a).sum()
        # reward = reward_fwd + reward_ctrl

        # --------- Sparse Reward ---------
        # a reward +1 is given for every time the agent moves forward over a specific number of units.
        if xposafter - self.init_qpos[0] > 1.:
            reward=1.
        else:
            reward=0.

        ob = self._get_obs()
        return ob, reward, False, {}

    def _get_obs(self):
        qpos = self.model.data.qpos
        qvel = self.model.data.qvel
        return np.concatenate([qpos.flat[2:], qvel.flat])

    def reset_model(self):
        self.set_state(
            self.init_qpos + self.np_random.uniform(low=-.1, high=.1, size=self.model.nq),
            self.init_qvel + self.np_random.uniform(low=-.1, high=.1, size=self.model.nv)
        )
        return self._get_obs()