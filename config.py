#### SELF PLAY
# EPISODES = 30
EPISODES = 1
# MCTS_SIMS = 50
MCTS_SIMS = 10
# MEMORY_SIZE = 30000
MEMORY_SIZE = 5
# TURNS_UNTIL_TAU0 = 10 # turn on which it starts playing deterministically
TURNS_UNTIL_TAU0 = 5 # turn on which it starts playing deterministically
CPUCT = 1
EPSILON = 0.2
ALPHA = 0.8
LOOP = 1


#### RETRAINING
BATCH_SIZE = 256
EPOCHS = 1
REG_CONST = 0.0001
LEARNING_RATE = 0.1
MOMENTUM = 0.9
TRAINING_LOOPS = 10

HIDDEN_CNN_LAYERS = [
	{'filters':75, 'kernel_size': (4,4)}
	 , {'filters':75, 'kernel_size': (4,4)}
	 , {'filters':75, 'kernel_size': (4,4)}
	 , {'filters':75, 'kernel_size': (4,4)}
	 , {'filters':75, 'kernel_size': (4,4)}
	 , {'filters':75, 'kernel_size': (4,4)}
	]

#### EVALUATION
EVAL_EPISODES = 20
SCORING_THRESHOLD = 1.3