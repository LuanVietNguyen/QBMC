# Hyst v1.17
# Hybrid Automaton in QBMC
# Converted from file: fischer_N_2_simplified.xml
# Command Line arguments: fischer_N_2_simplified.xml fischer_N_2_simplified_safe.cfg -qbmc -o fischer_N_2_simplified_safe.py


from z3 import *
from math import *

opt_debug = True

#Design Properties
k = 32
modeBitSize = int(ceil(log(17, 2)))
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
fischer_agent_1_x = []
cur_fischer_agent_1_x = Real('cur_fischer_agent_1_x')
next_fischer_agent_1_x = Real('next_fischer_agent_1_x')
for i in range(0, k+1):
  fischer_agent_1_x.append( Real('fischer_agent_1_x_' + str(i)) )
  all_state_vars.append(fischer_agent_1_x[i])
fischer_agent_1_i = []
cur_fischer_agent_1_i = Real('cur_fischer_agent_1_i')
next_fischer_agent_1_i = Real('next_fischer_agent_1_i')
for i in range(0, k+1):
  fischer_agent_1_i.append( Real('fischer_agent_1_i_' + str(i)) )
  all_state_vars.append(fischer_agent_1_i[i])
g = []
cur_g = Real('cur_g')
next_g = Real('next_g')
for i in range(0, k+1):
  g.append( Real('g_' + str(i)) )
  all_state_vars.append(g[i])
fischer_agent_2_x = []
cur_fischer_agent_2_x = Real('cur_fischer_agent_2_x')
next_fischer_agent_2_x = Real('next_fischer_agent_2_x')
for i in range(0, k+1):
  fischer_agent_2_x.append( Real('fischer_agent_2_x_' + str(i)) )
  all_state_vars.append(fischer_agent_2_x[i])
fischer_agent_2_i = []
cur_fischer_agent_2_i = Real('cur_fischer_agent_2_i')
next_fischer_agent_2_i = Real('next_fischer_agent_2_i')
for i in range(0, k+1):
  fischer_agent_2_i.append( Real('fischer_agent_2_i_' + str(i)) )
  all_state_vars.append(fischer_agent_2_i[i])
t = []
cur_t = Real('cur_t')
next_t = Real('next_t')
for i in range(0, k+1):
  t.append( Real('t_' + str(i)) )
  all_state_vars.append(t[i])

#Constant definitions
A = 5.0
cur_A = 5.0
B = 70.0
cur_B = 70.0
rate = 1.0
cur_rate = 1.0
true = True
false = False

rate = 1;
#Trajectories
Trajectories = And(next_mode == cur_mode, time >= 0, 
  Implies(cur_mode == 0,
    And(next_mode == cur_mode, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t)),
  Implies(cur_mode == 1,
    And(next_mode == cur_mode, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t)),
  Implies(cur_mode == 2,
    #invariant
    And(
    next_fischer_agent_2_x <= A, 
    cur_fischer_agent_2_x <= A, 
    next_fischer_agent_1_x == cur_fischer_agent_1_x, 
    next_fischer_agent_1_i == cur_fischer_agent_1_i, 
    next_g == cur_g,
    next_fischer_agent_2_x == cur_fischer_agent_2_x + time * rate,
    next_fischer_agent_2_i == cur_fischer_agent_2_i,
    next_t == cur_t, 
    next_mode == cur_mode)),
  Implies(cur_mode == 3,
    And(next_mode == cur_mode, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_fischer_agent_2_x == cur_fischer_agent_2_x + time * rate, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t)),
  Implies(cur_mode == 4,
    And(next_mode == cur_mode, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t)),
  Implies(cur_mode == 5,
    And(next_mode == cur_mode, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t)),
  Implies(cur_mode == 6,
    #invariant
    And(
    next_fischer_agent_2_x <= A, 
    cur_fischer_agent_2_x <= A, 
    next_fischer_agent_1_x == cur_fischer_agent_1_x, 
    next_fischer_agent_1_i == cur_fischer_agent_1_i, 
    next_g == cur_g, 
    next_fischer_agent_2_x == cur_fischer_agent_2_x + time * rate,
    next_fischer_agent_2_i == cur_fischer_agent_2_i, 
    next_t == cur_t,
    next_mode == cur_mode)),
  Implies(cur_mode == 7,
    And(next_mode == cur_mode, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_fischer_agent_2_x == cur_fischer_agent_2_x + time * rate, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t)),
  Implies(cur_mode == 8,
    #invariant
    And(
    next_fischer_agent_1_x <= A, 
    cur_fischer_agent_1_x <= A, 
    next_fischer_agent_1_x == cur_fischer_agent_1_x + time * rate,
    next_fischer_agent_1_i == cur_fischer_agent_1_i,
    next_g == cur_g, 
    next_fischer_agent_2_x == cur_fischer_agent_2_x, 
    next_fischer_agent_2_i == cur_fischer_agent_2_i,
    next_t == cur_t, 
    next_mode == cur_mode)),
  Implies(cur_mode == 9,
    #invariant
    And(
    next_fischer_agent_1_x <= A, 
    cur_fischer_agent_1_x <= A, 
    next_fischer_agent_1_x == cur_fischer_agent_1_x + time * rate, 
    next_fischer_agent_1_i == cur_fischer_agent_1_i,
    next_g == cur_g,
    next_fischer_agent_2_x == cur_fischer_agent_2_x, 
    next_fischer_agent_2_i == cur_fischer_agent_2_i, 
    next_t == cur_t, 
    next_mode == cur_mode)),
  Implies(cur_mode == 10,
    #invariant
    And(
    next_fischer_agent_1_x <= A , next_fischer_agent_2_x <= A, 
    cur_fischer_agent_1_x <= A , cur_fischer_agent_2_x <= A, 
    next_fischer_agent_1_x == cur_fischer_agent_1_x + time * rate,
    next_fischer_agent_1_i == cur_fischer_agent_1_i,
    next_g == cur_g, 
    next_fischer_agent_2_x == cur_fischer_agent_2_x + time * rate,
    next_fischer_agent_2_i == cur_fischer_agent_2_i,
    next_t == cur_t, 
    next_mode == cur_mode)),
  Implies(cur_mode == 11,
    #invariant
    And(
    next_fischer_agent_1_x <= A, 
    cur_fischer_agent_1_x <= A, 
    next_fischer_agent_1_x == cur_fischer_agent_1_x + time * rate,
    next_fischer_agent_1_i == cur_fischer_agent_1_i,
    next_g == cur_g, 
    next_fischer_agent_2_x == cur_fischer_agent_2_x + time * rate, 
    next_fischer_agent_2_i == cur_fischer_agent_2_i, 
    next_t == cur_t, 
    next_mode == cur_mode)),
  Implies(cur_mode == 12,
    And(next_mode == cur_mode, next_fischer_agent_1_x == cur_fischer_agent_1_x + time * rate, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t)),
  Implies(cur_mode == 13,
    And(next_mode == cur_mode, next_fischer_agent_1_x == cur_fischer_agent_1_x + time * rate, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t)),
  Implies(cur_mode == 14,
    #invariant
    And(
    next_fischer_agent_2_x <= A, 
    cur_fischer_agent_2_x <= A, 
    next_fischer_agent_1_x == cur_fischer_agent_1_x + time * rate, 
    next_fischer_agent_1_i == cur_fischer_agent_1_i, 
    next_g == cur_g, 
    next_fischer_agent_2_x == cur_fischer_agent_2_x + time * rate,
    next_fischer_agent_2_i == cur_fischer_agent_2_i,
    next_t == cur_t, 
    next_mode == cur_mode)),
  Implies(cur_mode == 15,
    And(next_mode == cur_mode, next_fischer_agent_1_x == cur_fischer_agent_1_x + time * rate, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_fischer_agent_2_x == cur_fischer_agent_2_x + time * rate, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t)),
)

# Transition Relation
Transitions = And(
  Implies(cur_mode == BitVecVal(0, modeBitSize), 
  Or(
    And(true, And(next_fischer_agent_2_x == 0.0, next_fischer_agent_1_x == 0.0, next_g == 0.0, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(5, modeBitSize))))
  )
  ,
  Implies(cur_mode == BitVecVal(1, modeBitSize), 
  Or(
    And(cur_g == 0.0, And(next_fischer_agent_2_x == 0.0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(2, modeBitSize))))
  )
  ,
  Implies(cur_mode == BitVecVal(2, modeBitSize), 
  Or(
    And(true, And(next_fischer_agent_2_x == 0.0, next_g == 2.0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(3, modeBitSize))))
  )
  ,
  Implies(cur_mode == BitVecVal(3, modeBitSize), 
  Or(
    And(cur_g == cur_fischer_agent_2_i ,  cur_fischer_agent_2_x >= cur_B, And(next_fischer_agent_2_x == 0.0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(0, modeBitSize))),
    And(cur_g < cur_fischer_agent_2_i ,  cur_fischer_agent_2_x >= cur_B, And(next_fischer_agent_2_x == 0.0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(1, modeBitSize))),
    And(cur_g > cur_fischer_agent_2_i ,  cur_fischer_agent_2_x >= cur_B, And(next_fischer_agent_2_x == 0.0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(1, modeBitSize))))
  )
  ,
  Implies(cur_mode == BitVecVal(4, modeBitSize), 
  Or(
    And(cur_g == 0.0, And(next_fischer_agent_1_x == 0.0, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(8, modeBitSize))))
  )
  ,
  Implies(cur_mode == BitVecVal(5, modeBitSize), 
  Or(
    And(cur_g == 0.0, And(next_fischer_agent_1_x == 0.0, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(9, modeBitSize))),
    And(cur_g == 0.0, And(next_fischer_agent_2_x == 0.0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(6, modeBitSize))))
  )
  ,
  Implies(cur_mode == BitVecVal(6, modeBitSize), 
  Or(
    And(cur_g == 0.0, And(next_fischer_agent_1_x == 0.0, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(10, modeBitSize))),
    And(true, And(next_fischer_agent_2_x == 0.0, next_g == 2.0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(7, modeBitSize))))
  )
  ,
  Implies(cur_mode == BitVecVal(7, modeBitSize), 
  Or(
    And(cur_g == 0.0, And(next_fischer_agent_1_x == 0.0, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(11, modeBitSize))),
    And(cur_g == cur_fischer_agent_2_i ,  cur_fischer_agent_2_x >= cur_B, And(next_fischer_agent_2_x == 0.0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(4, modeBitSize))),
    And(cur_g < cur_fischer_agent_2_i ,  cur_fischer_agent_2_x >= cur_B, And(next_fischer_agent_2_x == 0.0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(5, modeBitSize))),
    And(cur_g > cur_fischer_agent_2_i ,  cur_fischer_agent_2_x >= cur_B, And(next_fischer_agent_2_x == 0.0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(5, modeBitSize))))
  )
  ,
  Implies(cur_mode == BitVecVal(8, modeBitSize), 
  Or(
    And(true, And(next_fischer_agent_1_x == 0.0, next_g == 1.0, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(12, modeBitSize))))
  )
  ,
  Implies(cur_mode == BitVecVal(9, modeBitSize), 
  Or(
    And(cur_g == 0.0, And(next_fischer_agent_2_x == 0.0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(10, modeBitSize))),
    And(true, And(next_fischer_agent_1_x == 0.0, next_g == 1.0, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(13, modeBitSize))))
  )
  ,
  Implies(cur_mode == BitVecVal(10, modeBitSize), 
  Or(
    And(true, And(next_fischer_agent_1_x == 0.0, next_g == 1.0, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(14, modeBitSize))),
    And(true, And(next_fischer_agent_2_x == 0.0, next_g == 2.0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(11, modeBitSize))))
  )
  ,
  Implies(cur_mode == BitVecVal(11, modeBitSize), 
  Or(
    And(cur_g == cur_fischer_agent_2_i ,  cur_fischer_agent_2_x >= cur_B, And(next_fischer_agent_2_x == 0.0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(8, modeBitSize))),
    And(cur_g < cur_fischer_agent_2_i ,  cur_fischer_agent_2_x >= cur_B, And(next_fischer_agent_2_x == 0.0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(9, modeBitSize))),
    And(cur_g > cur_fischer_agent_2_i ,  cur_fischer_agent_2_x >= cur_B, And(next_fischer_agent_2_x == 0.0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(9, modeBitSize))),
    And(true, And(next_fischer_agent_1_x == 0.0, next_g == 1.0, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(15, modeBitSize))))
  )
  ,
  Implies(cur_mode == BitVecVal(12, modeBitSize), 
  Or(
    And(cur_g == cur_fischer_agent_1_i ,  cur_fischer_agent_1_x >= cur_B, And(next_fischer_agent_1_x == 0.0, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(0, modeBitSize))),
    And(cur_g < cur_fischer_agent_1_i ,  cur_fischer_agent_1_x >= cur_B, And(next_fischer_agent_1_x == 0.0, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(4, modeBitSize))),
    And(cur_g > cur_fischer_agent_1_i ,  cur_fischer_agent_1_x >= cur_B, And(next_fischer_agent_1_x == 0.0, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(4, modeBitSize))))
  )
  ,
  Implies(cur_mode == BitVecVal(13, modeBitSize), 
  Or(
    And(cur_g == cur_fischer_agent_1_i ,  cur_fischer_agent_1_x >= cur_B, And(next_fischer_agent_1_x == 0.0, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(1, modeBitSize))),
    And(cur_g < cur_fischer_agent_1_i ,  cur_fischer_agent_1_x >= cur_B, And(next_fischer_agent_1_x == 0.0, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(5, modeBitSize))),
    And(cur_g > cur_fischer_agent_1_i ,  cur_fischer_agent_1_x >= cur_B, And(next_fischer_agent_1_x == 0.0, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(5, modeBitSize))),
    And(cur_g == 0.0, And(next_fischer_agent_2_x == 0.0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(14, modeBitSize))))
  )
  ,
  Implies(cur_mode == BitVecVal(14, modeBitSize), 
  Or(
    And(cur_g == cur_fischer_agent_1_i ,  cur_fischer_agent_1_x >= cur_B, And(next_fischer_agent_1_x == 0.0, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(2, modeBitSize))),
    And(cur_g < cur_fischer_agent_1_i ,  cur_fischer_agent_1_x >= cur_B, And(next_fischer_agent_1_x == 0.0, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(6, modeBitSize))),
    And(cur_g > cur_fischer_agent_1_i ,  cur_fischer_agent_1_x >= cur_B, And(next_fischer_agent_1_x == 0.0, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(6, modeBitSize))),
    And(true, And(next_fischer_agent_2_x == 0.0, next_g == 2.0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(15, modeBitSize))))
  )
  ,
  Implies(cur_mode == BitVecVal(15, modeBitSize), 
  Or(
    And(cur_g == cur_fischer_agent_1_i ,  cur_fischer_agent_1_x >= cur_B, And(next_fischer_agent_1_x == 0.0, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(3, modeBitSize))),
    And(cur_g < cur_fischer_agent_1_i ,  cur_fischer_agent_1_x >= cur_B, And(next_fischer_agent_1_x == 0.0, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(7, modeBitSize))),
    And(cur_g > cur_fischer_agent_1_i ,  cur_fischer_agent_1_x >= cur_B, And(next_fischer_agent_1_x == 0.0, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(7, modeBitSize))),
    And(cur_g == cur_fischer_agent_2_i ,  cur_fischer_agent_2_x >= cur_B, And(next_fischer_agent_2_x == 0.0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(12, modeBitSize))),
    And(cur_g < cur_fischer_agent_2_i ,  cur_fischer_agent_2_x >= cur_B, And(next_fischer_agent_2_x == 0.0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(13, modeBitSize))),
    And(cur_g > cur_fischer_agent_2_i ,  cur_fischer_agent_2_x >= cur_B, And(next_fischer_agent_2_x == 0.0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(13, modeBitSize))))
  )

  )

TransitionRelation = Or(Transitions, Trajectories)
#TransitionRelation = Transitions
#TransitionRelation = True

#initial states
initStates = And(
  fischer_agent_1_x[0] == 0.0 ,  fischer_agent_1_i[0] == 1.0 ,  g[0] == 0.0 ,  fischer_agent_2_x[0] == 0.0 ,  fischer_agent_2_i[0] == 2.0 ,  t[0] == 0.0, v_time[0] == 0, mode[0] == BitVecVal(5, modeBitSize)
  )

#bad states
badStates = []
for i in range(1, k+1): 
  #unsat: cs_cs_default bit0, cs_try_defaults bit2; try_cs_defaults bit8;
  badStates.append(mode[i] == BitVecVal(0, modeBitSize))
badStates = And(Or(
  badStates
  ))

# Outer Multiplexers
muxes = []
for i in range(0, k):
  if i == 0:
    mux_i = Implies(tbv == i,
    And(
    cur_fischer_agent_1_x == fischer_agent_1_x[i],
    next_fischer_agent_1_x == fischer_agent_1_x[i+1],
    cur_fischer_agent_1_i == fischer_agent_1_i[i],
    next_fischer_agent_1_i == fischer_agent_1_i[i+1],
    cur_g == g[i],
    next_g == g[i+1],
    cur_fischer_agent_2_x == fischer_agent_2_x[i],
    next_fischer_agent_2_x == fischer_agent_2_x[i+1],
    cur_fischer_agent_2_i == fischer_agent_2_i[i],
    next_fischer_agent_2_i == fischer_agent_2_i[i+1],
    cur_t == t[i],
    next_t == t[i+1],
    time == v_time[i],
    v_time[i+1] >= v_time[i],
    cur_mode == mode[i],
    next_mode == mode[i+1]
    ) )
  else:
    mux_i = Implies(tbv == i,
    And(
    cur_fischer_agent_1_x == fischer_agent_1_x[i],
    next_fischer_agent_1_x == fischer_agent_1_x[i+1],
    cur_fischer_agent_1_i == fischer_agent_1_i[i],
    next_fischer_agent_1_i == fischer_agent_1_i[i+1],
    cur_g == g[i],
    next_g == g[i+1],
    cur_fischer_agent_2_x == fischer_agent_2_x[i],
    next_fischer_agent_2_x == fischer_agent_2_x[i+1],
    cur_fischer_agent_2_i == fischer_agent_2_i[i],
    next_fischer_agent_2_i == fischer_agent_2_i[i+1],
    cur_t == t[i],
    next_t == t[i+1],
    time == v_time[i],
    v_time[i] > v_time[i-1],
    cur_mode == mode[i],
    next_mode == mode[i+1]
    ) )
  muxes.append( mux_i )
mux = And(muxes)

# Finilize QBF formulation
inner = And(initStates, TransitionRelation, badStates, mux)
qbf_bmc_inner = Exists([cur_fischer_agent_1_x, next_fischer_agent_1_x, cur_fischer_agent_1_i, next_fischer_agent_1_i, cur_g, next_g, cur_fischer_agent_2_x, next_fischer_agent_2_x, cur_fischer_agent_2_i, next_fischer_agent_2_i, cur_t, next_t, cur_mode, next_mode, time], inner)
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
    print "fischer_agent_1_x: " + str(model[fischer_agent_1_x[i]])
    print "fischer_agent_1_i: " + str(model[fischer_agent_1_i[i]])
    print "g: " + str(model[g[i]])
    print "fischer_agent_2_x: " + str(model[fischer_agent_2_x[i]])
    print "fischer_agent_2_i: " + str(model[fischer_agent_2_i[i]])
    print "t: " + str(model[t[i]])
