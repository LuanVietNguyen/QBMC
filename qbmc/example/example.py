# Created by Hyst v1.2
# Hybrid Automaton in Python QBMC
# Converted from file: example_paper.xml
# Command Line arguments: example_paper.xml -qbmc -o example_paper.py


from z3 import *
from math import *

opt_debug = True

#Design Properties
k = 8
modeBitSize = int(ceil(log(3, 2)))
klog = int(ceil(log(k, 2)))

#Variable definitions
tbv = BitVec('tbv', klog)
all_state_vars = []
v_time = []
mode = []
time = Real('time')
cur_mode = BitVec('cur_mode', modeBitSize)
next_mode = BitVec('next_mode', modeBitSize)
for i in range(0, k+1):
  mode.append( BitVec('mode_' + str(i), modeBitSize) )
  v_time.append( Real('time_' + str(i)))
  all_state_vars.append(mode[i])
  all_state_vars.append(v_time[i])
x = []
cur_x = Real('cur_x')
next_x = Real('next_x')
for i in range(0, k+1):
  x.append( Real('x_' + str(i)) )
  all_state_vars.append(x[i])

#Constant definitions
a1 = 0;
b1 = 1;
a2 = 0;
b2 = 2;
#rate1 = 2.0
#rate2 = 1.0
true = True
false = False



#rate = 1;
#Trajectories
Trajectories = And(next_mode == cur_mode, time >= 0, 
  And(
  Implies(cur_mode == 0,
    And(next_mode == cur_mode,
    #invariant
    next_x <= 5, 
    cur_x <= 5, 
    #flow: 
    next_x >= cur_x + time * (a1),
	next_x <= cur_x + time * (b1),
    )),
  Implies(cur_mode == 1,
    And(next_mode == cur_mode,
    #invariant
    next_x <= 10, 
    cur_x <= 10, 
    #flow: 
	next_x >= cur_x + time * (a2),
	next_x <= cur_x + time * (b2),
    )),
  )
)

# Transition Relation
Transitions = And(
  And(
  Implies(cur_mode == BitVecVal(0, modeBitSize), 
  Or(
    And(cur_x >= 2.5, And(next_x == cur_x, next_mode == BitVecVal(1, modeBitSize))))
  )
  ,
  Implies(cur_mode == BitVecVal(1, modeBitSize), 
  Or(
    And(cur_x >= 10, And(next_x == 0, next_mode == BitVecVal(0, modeBitSize))))
  )
  )

  )

TransitionRelation = Or(Transitions, Trajectories)

#initial states
initStates = And(
  x[0] == 0 , v_time[0] == 0, mode[0] == BitVecVal(0, modeBitSize)
  )

#bad states
badStates = []
for i in range(1, k+1): 
  badStates.append(And(mode[i] == BitVecVal(1, modeBitSize), x[i] < 2.5))
badStates = And(Or(
  badStates
  ))

# Outer Multiplexers
muxes = []
for i in range(0, k):
  if i == 0:
    mux_i = Implies(tbv == i,
    And(
    cur_x == x[i],
    next_x == x[i+1],
    time == v_time[i],
    v_time[i+1] >= v_time[i],
    cur_mode == mode[i],
    next_mode == mode[i+1]
    ) )
  else:
    mux_i = Implies(tbv == i,
    And(
    cur_x == x[i],
    next_x == x[i+1],
    time == v_time[i],
    v_time[i] > v_time[i-1],
    cur_mode == mode[i],
    next_mode == mode[i+1]
    ) )
  muxes.append( mux_i )
mux = And(muxes)

# Finilize QBF formulation
inner = And(initStates, TransitionRelation, badStates, mux)
qbf_bmc_inner = Exists([cur_x, next_x, cur_mode, next_mode, time], inner)
qbf_bmc_middle = ForAll(tbv, qbf_bmc_inner)
qbf_bmc_outer = qbf_bmc_middle
# Run z3
z3_solver = Solver()

if opt_debug:
  print qbf_bmc_outer

z3_solver.add( qbf_bmc_outer )
result = z3_solver.check()
print result

if result == sat:
  model = z3_solver.model()

  print model

  #print counterexample in execution order
  for i in range(0, k):
    print os.linesep
    print "step " + str(i) + "/" + str(k) + " state:"
    print "mode: " + str(model[mode[i]])
    print "time: " + str(model[v_time[i]])
    print "x: " + str(model[x[i]])
