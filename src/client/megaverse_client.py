from typing import Dict, Any

from factories.megaverse_factory import MegaverseFactory
from models.astral_objetcs import AstralObject
from client.crossmint_http_client import CrossmintHttpClient
from models.megaverse_goal import MegaverseGoalBoard


class MegaverseClient(CrossmintHttpClient):

    def get_goal(self) -> MegaverseGoalBoard:
        raw_board = self.get(f"/map/{self._candidate_id}/goal")["goal"]
        board = [
            MegaverseFactory.create_megaverse_object(raw_board[row][column], row, column)
            for row in range(len(raw_board))
            for column in range(len(raw_board[row]))
        ]

        return MegaverseGoalBoard(board)

    def create_astral_object(self, astral_object: AstralObject) -> Dict[str, Any]:
        return self.post(f"/{astral_object.path_resource}", body=astral_object.to_body())

    def delete_astral_object(self, astral_object: AstralObject) -> Dict[str, Any]:
        return self.delete(f"/{astral_object.path_resource}", body=astral_object.to_body())
