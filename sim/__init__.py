

# rewrite that whole thing from scratch
# app usage:
# define architecture (walls, obsticals, spawners, doors)
# define init board (agent pos)
# give rules for SF and DF
# give agent update rules
# from all that create Board instance
# use board instance to calculate info of interest (concurrent with mp)
# (monte carlo density over time, monte carlo average time that amount x gets through doors, SF, DF)
# Board instance creates timeline data
# use timeline data to visualize through renderer
# compare timeline data of different board instances