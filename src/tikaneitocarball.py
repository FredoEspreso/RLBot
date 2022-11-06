import logging
import os
from boxcars_py import parse_replay

from carball.analysis.analysis_manager import AnalysisManager
from carball.controls.controls import ControlsCreator
from carball.extras.per_goal_analysis import PerGoalAnalysis
from carball.json_parser.game import Game
from carball.json_parser.sanity_check.sanity_check import SanityChecker
from carball import decompile_replay

import pandas as pd

_json = decompile_replay('A1ED234F4750489E3B2062BD6CFFFEAB.replay')

game = Game()
game.initialize(loaded_json=_json)

# SanityChecker.check_game(game)
# analysis = AnalysisManager(game)
# analysis.create_analysis(calculate_intensive_events=True, clean=True)
controls = ControlsCreator()
controls.get_controls(game)

for player in game.players:
    print(player.controls.iloc[5000:6000].to_string())
    break
