from gym.envs.registration import register

register(
    id='easyfrozenlake-v0',
    entry_point='gym_easyfrozenlake.envs:EasyFrozenLakeEnv',
)