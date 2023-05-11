from pathlib import Path

from staticfg import CFGBuilder


FILEPATH = Path(__file__).parent.joinpath("syntax_tree.py")


cfg = CFGBuilder().build_from_file("test", FILEPATH)
cfg.build_visual("test", "png")
