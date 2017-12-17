
from play_base import Play

from tactics.tactic_keep import TacticKeep
from tactics.tactic_interpose import TacticInterpose
from tactics.tactic_position import TacticPosition
import constants

class PlayTheirIndirect(Play):
    def __init__(self):
        super(PlayTheirIndirect, self).__init__('PlayTheirIndirect')

        self.applicable = "THEIR_INDIRECT"
        self.done_aborted = "THEIR_INDIRECT"

        keep_x = -constants.FieldHalfX + constants.RobotRadius * 2.0
        self.roles[0].loop_enable = True
        self.roles[0].behavior.add_child(
                TacticKeep('TacticKeep', self.roles[0].my_role, keep_x = keep_x,
                    range_high = constants.GoalHalfSize,
                    range_low = -constants.GoalHalfSize)
                )

        self.roles[1].loop_enable = True
        self.roles[1].behavior.add_child(
                TacticInterpose('TacticInterpose', self.roles[1].my_role, 
                    from_dist = 0.5)
                )

        for i in range(2,6):
            x = -3.0
            y = 0.45 - 0.3*(i-2)
            theta = 0

            self.roles[i].loop_enable = True
            self.roles[i].behavior.add_child(
                    TacticPosition('TacticPosition', self.roles[i].my_role,
                        x, y ,theta))
