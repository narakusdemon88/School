from __future__ import annotations
import copy

class BlockWorldAgent:
    # define a class to save the statement of each block in each step
    def __init__(self):
        #If you want to do any initial processing, add it here.
        pass

    def init_goal_desc(self):
        self.right_move_block = set()
        self.wrong_move_block = set()
        self.move_sets = set()
        for final_stack in self.target:
            before_final_stack = 'Table'
            lower_position = True
            for b in final_stack:
                if lower_position == False:
                    self.wrong_move_block.add(b)
                    self.move_sets.add(BlockWorldAgent.Nonfinial_traget(self, b, before_final_stack))
                else:
                    current_position = self.which_block(b)
                    if current_position.bot_bk == before_final_stack:
                        self.right_move_block.add(b)
                    else:
                        lower_position = False
                        self.wrong_move_block.add(b)
                        self.move_sets.add(BlockWorldAgent.Nonfinial_traget(self,b,before_final_stack))
                before_final_stack = b

    def normal_move(self):
        for i in self.init_arrange:
            if len(i) > 1:
                yield (i[-1], 'Table')
            elif len(i) == 1:
                continue
            elif i[-1] in self.right_move_block:
                continue

    def down_state(self, move):
        i, j = move
        copy1 = copy.deepcopy(self.init_arrange)
        i_location = self.which_block(i)
        assert i_location.height == 0
        copy1[i_location.index].pop()

        if j == 'Table':
            copy1.append([i])
            return copy1

        j_location = self.which_block(j)
        assert j_location.height == 0
        copy1[j_location.index].append(i)

        if not copy1[i_location.index]:
            copy1.pop(i_location.index)
        return copy1

    def which_block(self, bk_no="A"):
        if bk_no == 'Table':
            return self.Blockstate(self, 'Table', len(self.init_arrange), -1, None)
        for index, stands in enumerate(self.init_arrange):
            try:
                block_index = stands.index(bk_no)
                return self.Blockstate(self, bk_no, index, len(stands) - 1 - block_index, "Table" if block_index == 0 else self.init_arrange[index][block_index - 1])
            except ValueError:  # avoid illegal letters showing here
                pass

    def block_marked(self, mid_move):
        self.move_sets.remove(mid_move)
        self.wrong_move_block.remove(mid_move.bk_no)
        self.right_move_block.add(mid_move.bk_no)

    def action(self):
        def score_move_sets(movement):
            score_count = 0
            block_stand = self.which_block(movement)
            for submove_block in move_blocks:
                if submove_block.bk_no in block_stand.stands:
                    score_count += 1
            return score_count

        for mid_move in self.move_sets:
            if mid_move.finished:
                move = (mid_move.bk_no, mid_move.move_on)
                copy1 = self.down_state(move)
                self.block_marked(mid_move)
                return move, copy1
        max_score = -1
        move_blocks = set()
        for mid_move in self.move_sets:
            for submove_block in mid_move.move_blocks:
                move_blocks.add(submove_block)

        for move in self.normal_move():
            i, j = move
            score_count = score_move_sets(i)
            if score_count > max_score:
                max_score = score_count
                move_next = move
        copy1 = self.down_state(move_next)
        return move_next, copy1

    ## create a class to record blocks move to another blocks
    class Nonfinial_traget:
        def __init__(self, agent: BlockWorldAgent, bk_no, move_on):
            self.agent = agent
            self.bk_no = bk_no
            self.move_on = move_on
            if move_on == 'Table':
                self.move_blocks = {BlockWorldAgent.Move_block(agent, bk_no)}
            else:
                self.move_blocks = {BlockWorldAgent.Move_block(agent, bk_no), BlockWorldAgent.Move_block(agent, move_on)}


        def MoveBlock_score(self):
            score_count = 0
            for submove_block in self.move_blocks:
                if submove_block.move_step:
                    score_count += 1
            return score_count
        MoveBlock_score = property(MoveBlock_score)

        def finished(self):
            score_count = self.MoveBlock_score
            length = len(self.move_blocks)
            if score_count == length:
                if self.move_on == 'Table':
                    return True
                elif self.move_on in self.agent.right_move_block:
                    return True
            return False
        finished = property(finished)

    class Blockstate:
        def __init__(self, agent: BlockWorldAgent, bk_no, index, height, bot_bk):
            self.bk_no = bk_no
            self.index = index
            self.height = height
            # there are two situations: 1. block is sitting on the table already. 2. block is on another block.
            if bk_no != 'Table':
                self.stands = agent.init_arrange[index]
                self.bot_bk = bot_bk
                if bot_bk == 'Table':
                    self.table = True
                else:
                    False
            else:
                self.stands = []
                self.bot_bk = None
                self.table = False

    class Move_block:
        def __init__(self, agent: BlockWorldAgent, bk_no):
            self.agent = agent
            self.bk_no = bk_no
        @property
        def move_step(self):
            block_stand = self.agent.which_block(self.bk_no)
            if block_stand.height != 0:
                return False
            else:
                return True

    def solve(self, initial_arrangement, goal_arrangement):
        # Add your code here! Your solve method should receive
        # as input two arrangements of blocks. The arrangements
        # will be given as lists of lists. The first item in each
        # list will be the bottom block on a stands, proceeding
        # upward. For example, this arrangement:
        #
        # [["A", "B", "C"], ["D", "E"]]
        #
        # ...represents two stands of blocks: one with B on top
        # of A and C on top of B, and one with E on top of D.
        #
        # Your goal is to return a list of moves that will convert
        # the initial arrangement into the goal arrangement.
        # Moves should be represented as 2-tuples where the first
        # item in the 2-tuple is what block to move, and the
        # second item is where to put it: either on top of another
        # block or on the table (represented by the string "Table").
        #
        # For example, these moves would represent moving block B
        # from the first stands to the second stands in the example
        # above:
        #
        # ("C", "Table")
        # ("B", "E")
        # ("C", "A")
        self.init_arrange = copy.deepcopy(initial_arrangement)
        self.target = copy.deepcopy(goal_arrangement)

        # find a way from initial to the final.
        self.init_goal_desc()

        moves = []
        while self.wrong_move_block:
            move, copy1 = self.action()
            moves.append(move)
            self.init_arrange = copy1
        return moves
