from client.megaverse_client import MegaverseClient


def run_challenge():
    client = MegaverseClient()

    goal_megaverse = client.get_goal()
    for megaverse_object in goal_megaverse:
        if megaverse_object.is_astral_object():
            client.create_astral_object(megaverse_object)


if __name__ == '__main__':
    run_challenge()
