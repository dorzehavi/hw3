ids = ["211567706", "209087998"]


class DroneAgent:
    def __init__(self, n, m):
        self.mode = 'train'  # do not change this!
        self.N = n
        self.M = m


    def select_action(self, obs0):
        actions = get_actions(obs0, self.N, self.M)
        raise NotImplemented

    def train(self):
        self.mode = 'train'  # do not change this!

    def eval(self):
        self.mode = 'eval'  # do not change this!

    def update(self, obs0, action, obs1, reward):
        # your code here
        raise NotImplemented


def get_actions(obs0, N, M):
    action_set = {"reset", "move_down", "move_up", "move_right", "move_left", "pick", "deliver"}
    drone_loc = obs0["drone_location"]
    if drone_loc[0] - 1 < 0:
        action_set.remove("move_up")
    if drone_loc[0] + 1 > N:
        action_set.remove("move_down")
    if drone_loc[1] - 1 < 0:
        action_set.remove("move_left")
    if drone_loc[1] + 1 > M:
        action_set.remove("move_right")
    if drone_loc != obs0['target_location']:
        action_set.remove("deliver")
    for pack in obs0[""]