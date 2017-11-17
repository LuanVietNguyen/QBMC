# Created by Hyst v1.18
# Hybrid Automaton in Python QBMC
# Converted from file: lynch_N_2_simplified_safe.xml
# Command Line arguments: lynch_N_2_simplified_safe.xml -qbmc -o lynch_N_2_simplified_safe.py


from z3 import *
from math import *

opt_debug = True

#Design Properties
k = 8
modeBitSize = int(ceil(log(82, 2)))
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
v = []
cur_v = Real('cur_v')
next_v = Real('next_v')
for i in range(0, k+1):
  v.append( Real('v_' + str(i)) )
  all_state_vars.append(v[i])
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
a = 1.0
cur_a = 1.0
b = 1.0
cur_b = 1.0
rate = 1.0
cur_rate = 1.0
true = True
false = False

rate = 1;
#Trajectories
Trajectories = And(next_mode == cur_mode, time >= 0, 
  And(
  Implies(cur_mode == 0,
    And(next_mode == cur_mode,
    #flow: [fischer_agent_1_x=0, fischer_agent_1_i=0, fischer_agent_2_x=0, fischer_agent_2_i=0, g=0, t=1, v=0]
    next_fischer_agent_1_x == cur_fischer_agent_1_x + time * (0),
    next_fischer_agent_1_i == cur_fischer_agent_1_i + time * (0),
    next_g == cur_g + time * (0),
    next_v == cur_v + time * (0),
    next_fischer_agent_2_x == cur_fischer_agent_2_x + time * (0),
    next_fischer_agent_2_i == cur_fischer_agent_2_i + time * (0),
    next_t == cur_t + time * (1),
    )),
  Implies(cur_mode == 1,
    And(next_mode == cur_mode,
    #flow: [fischer_agent_1_x=0, fischer_agent_1_i=0, fischer_agent_2_x=0, fischer_agent_2_i=0, g=0, t=1, v=0]
    next_fischer_agent_1_x == cur_fischer_agent_1_x + time * (0),
    next_fischer_agent_1_i == cur_fischer_agent_1_i + time * (0),
    next_g == cur_g + time * (0),
    next_v == cur_v + time * (0),
    next_fischer_agent_2_x == cur_fischer_agent_2_x + time * (0),
    next_fischer_agent_2_i == cur_fischer_agent_2_i + time * (0),
    next_t == cur_t + time * (1),
    )),
  Implies(cur_mode == 2,
    And(next_mode == cur_mode,
    #flow: [fischer_agent_1_x=0, fischer_agent_1_i=0, fischer_agent_2_x=0, fischer_agent_2_i=0, g=0, t=1, v=0]
    next_fischer_agent_1_x == cur_fischer_agent_1_x + time * (0),
    next_fischer_agent_1_i == cur_fischer_agent_1_i + time * (0),
    next_g == cur_g + time * (0),
    next_v == cur_v + time * (0),
    next_fischer_agent_2_x == cur_fischer_agent_2_x + time * (0),
    next_fischer_agent_2_i == cur_fischer_agent_2_i + time * (0),
    next_t == cur_t + time * (1),
    )),
  Implies(cur_mode == 3,
    And(next_mode == cur_mode,
    #invariant
    next_fischer_agent_2_x <= a, 
    cur_fischer_agent_2_x <= a, 
    #flow: [fischer_agent_1_x=0, fischer_agent_1_i=0, fischer_agent_2_x=rate, fischer_agent_2_i=0, g=0, t=1, v=0]
    next_fischer_agent_1_x == cur_fischer_agent_1_x + time * (0),
    next_fischer_agent_1_i == cur_fischer_agent_1_i + time * (0),
    next_g == cur_g + time * (0),
    next_v == cur_v + time * (0),
    next_fischer_agent_2_x == cur_fischer_agent_2_x + time * (rate),
    next_fischer_agent_2_i == cur_fischer_agent_2_i + time * (0),
    next_t == cur_t + time * (1),
    )),
  Implies(cur_mode == 4,
    And(next_mode == cur_mode,
    #invariant
    next_fischer_agent_2_x <= a, 
    cur_fischer_agent_2_x <= a, 
    #flow: [fischer_agent_1_x=0, fischer_agent_1_i=0, fischer_agent_2_x=rate, fischer_agent_2_i=0, g=0, t=1, v=0]
    next_fischer_agent_1_x == cur_fischer_agent_1_x + time * (0),
    next_fischer_agent_1_i == cur_fischer_agent_1_i + time * (0),
    next_g == cur_g + time * (0),
    next_v == cur_v + time * (0),
    next_fischer_agent_2_x == cur_fischer_agent_2_x + time * (rate),
    next_fischer_agent_2_i == cur_fischer_agent_2_i + time * (0),
    next_t == cur_t + time * (1),
    )),
  Implies(cur_mode == 5,
    And(next_mode == cur_mode,
    #invariant
    next_fischer_agent_2_x <= a, 
    cur_fischer_agent_2_x <= a, 
    #flow: [fischer_agent_1_x=0, fischer_agent_1_i=0, fischer_agent_2_x=rate, fischer_agent_2_i=0, g=0, t=1, v=0]
    next_fischer_agent_1_x == cur_fischer_agent_1_x + time * (0),
    next_fischer_agent_1_i == cur_fischer_agent_1_i + time * (0),
    next_g == cur_g + time * (0),
    next_v == cur_v + time * (0),
    next_fischer_agent_2_x == cur_fischer_agent_2_x + time * (rate),
    next_fischer_agent_2_i == cur_fischer_agent_2_i + time * (0),
    next_t == cur_t + time * (1),
    )),
  Implies(cur_mode == 6,
    And(next_mode == cur_mode,
    #invariant
    next_fischer_agent_2_x <= a, 
    cur_fischer_agent_2_x <= a, 
    #flow: [fischer_agent_1_x=0, fischer_agent_1_i=0, fischer_agent_2_x=rate, fischer_agent_2_i=0, g=0, t=1, v=0]
    next_fischer_agent_1_x == cur_fischer_agent_1_x + time * (0),
    next_fischer_agent_1_i == cur_fischer_agent_1_i + time * (0),
    next_g == cur_g + time * (0),
    next_v == cur_v + time * (0),
    next_fischer_agent_2_x == cur_fischer_agent_2_x + time * (rate),
    next_fischer_agent_2_i == cur_fischer_agent_2_i + time * (0),
    next_t == cur_t + time * (1),
    )),
  Implies(cur_mode == 7,
    And(next_mode == cur_mode,
    #flow: [fischer_agent_1_x=0, fischer_agent_1_i=0, fischer_agent_2_x=rate, fischer_agent_2_i=0, g=0, t=1, v=0]
    next_fischer_agent_1_x == cur_fischer_agent_1_x + time * (0),
    next_fischer_agent_1_i == cur_fischer_agent_1_i + time * (0),
    next_g == cur_g + time * (0),
    next_v == cur_v + time * (0),
    next_fischer_agent_2_x == cur_fischer_agent_2_x + time * (rate),
    next_fischer_agent_2_i == cur_fischer_agent_2_i + time * (0),
    next_t == cur_t + time * (1),
    )),
  Implies(cur_mode == 8,
    And(next_mode == cur_mode,
    #flow: [fischer_agent_1_x=0, fischer_agent_1_i=0, fischer_agent_2_x=rate, fischer_agent_2_i=0, g=0, t=1, v=0]
    next_fischer_agent_1_x == cur_fischer_agent_1_x + time * (0),
    next_fischer_agent_1_i == cur_fischer_agent_1_i + time * (0),
    next_g == cur_g + time * (0),
    next_v == cur_v + time * (0),
    next_fischer_agent_2_x == cur_fischer_agent_2_x + time * (rate),
    next_fischer_agent_2_i == cur_fischer_agent_2_i + time * (0),
    next_t == cur_t + time * (1),
    )),
  Implies(cur_mode == 9,
    And(next_mode == cur_mode,
    #flow: [fischer_agent_1_x=0, fischer_agent_1_i=0, fischer_agent_2_x=0, fischer_agent_2_i=0, g=0, t=1, v=0]
    next_fischer_agent_1_x == cur_fischer_agent_1_x + time * (0),
    next_fischer_agent_1_i == cur_fischer_agent_1_i + time * (0),
    next_g == cur_g + time * (0),
    next_v == cur_v + time * (0),
    next_fischer_agent_2_x == cur_fischer_agent_2_x + time * (0),
    next_fischer_agent_2_i == cur_fischer_agent_2_i + time * (0),
    next_t == cur_t + time * (1),
    )),
  Implies(cur_mode == 10,
    And(next_mode == cur_mode,
    #flow: [fischer_agent_1_x=0, fischer_agent_1_i=0, fischer_agent_2_x=0, fischer_agent_2_i=0, g=0, t=1, v=0]
    next_fischer_agent_1_x == cur_fischer_agent_1_x + time * (0),
    next_fischer_agent_1_i == cur_fischer_agent_1_i + time * (0),
    next_g == cur_g + time * (0),
    next_v == cur_v + time * (0),
    next_fischer_agent_2_x == cur_fischer_agent_2_x + time * (0),
    next_fischer_agent_2_i == cur_fischer_agent_2_i + time * (0),
    next_t == cur_t + time * (1),
    )),
  Implies(cur_mode == 11,
    And(next_mode == cur_mode,
    #flow: [fischer_agent_1_x=0, fischer_agent_1_i=0, fischer_agent_2_x=0, fischer_agent_2_i=0, g=0, t=1, v=0]
    next_fischer_agent_1_x == cur_fischer_agent_1_x + time * (0),
    next_fischer_agent_1_i == cur_fischer_agent_1_i + time * (0),
    next_g == cur_g + time * (0),
    next_v == cur_v + time * (0),
    next_fischer_agent_2_x == cur_fischer_agent_2_x + time * (0),
    next_fischer_agent_2_i == cur_fischer_agent_2_i + time * (0),
    next_t == cur_t + time * (1),
    )),
  Implies(cur_mode == 12,
    And(next_mode == cur_mode,
    #invariant
    next_fischer_agent_2_x <= a, 
    cur_fischer_agent_2_x <= a, 
    #flow: [fischer_agent_1_x=0, fischer_agent_1_i=0, fischer_agent_2_x=rate, fischer_agent_2_i=0, g=0, t=1, v=0]
    next_fischer_agent_1_x == cur_fischer_agent_1_x + time * (0),
    next_fischer_agent_1_i == cur_fischer_agent_1_i + time * (0),
    next_g == cur_g + time * (0),
    next_v == cur_v + time * (0),
    next_fischer_agent_2_x == cur_fischer_agent_2_x + time * (rate),
    next_fischer_agent_2_i == cur_fischer_agent_2_i + time * (0),
    next_t == cur_t + time * (1),
    )),
  Implies(cur_mode == 13,
    And(next_mode == cur_mode,
    #invariant
    next_fischer_agent_2_x <= a, 
    cur_fischer_agent_2_x <= a, 
    #flow: [fischer_agent_1_x=0, fischer_agent_1_i=0, fischer_agent_2_x=rate, fischer_agent_2_i=0, g=0, t=1, v=0]
    next_fischer_agent_1_x == cur_fischer_agent_1_x + time * (0),
    next_fischer_agent_1_i == cur_fischer_agent_1_i + time * (0),
    next_g == cur_g + time * (0),
    next_v == cur_v + time * (0),
    next_fischer_agent_2_x == cur_fischer_agent_2_x + time * (rate),
    next_fischer_agent_2_i == cur_fischer_agent_2_i + time * (0),
    next_t == cur_t + time * (1),
    )),
  Implies(cur_mode == 14,
    And(next_mode == cur_mode,
    #invariant
    next_fischer_agent_2_x <= a, 
    cur_fischer_agent_2_x <= a, 
    #flow: [fischer_agent_1_x=0, fischer_agent_1_i=0, fischer_agent_2_x=rate, fischer_agent_2_i=0, g=0, t=1, v=0]
    next_fischer_agent_1_x == cur_fischer_agent_1_x + time * (0),
    next_fischer_agent_1_i == cur_fischer_agent_1_i + time * (0),
    next_g == cur_g + time * (0),
    next_v == cur_v + time * (0),
    next_fischer_agent_2_x == cur_fischer_agent_2_x + time * (rate),
    next_fischer_agent_2_i == cur_fischer_agent_2_i + time * (0),
    next_t == cur_t + time * (1),
    )),
  Implies(cur_mode == 15,
    And(next_mode == cur_mode,
    #invariant
    next_fischer_agent_2_x <= a, 
    cur_fischer_agent_2_x <= a, 
    #flow: [fischer_agent_1_x=0, fischer_agent_1_i=0, fischer_agent_2_x=rate, fischer_agent_2_i=0, g=0, t=1, v=0]
    next_fischer_agent_1_x == cur_fischer_agent_1_x + time * (0),
    next_fischer_agent_1_i == cur_fischer_agent_1_i + time * (0),
    next_g == cur_g + time * (0),
    next_v == cur_v + time * (0),
    next_fischer_agent_2_x == cur_fischer_agent_2_x + time * (rate),
    next_fischer_agent_2_i == cur_fischer_agent_2_i + time * (0),
    next_t == cur_t + time * (1),
    )),
  Implies(cur_mode == 16,
    And(next_mode == cur_mode,
    #flow: [fischer_agent_1_x=0, fischer_agent_1_i=0, fischer_agent_2_x=rate, fischer_agent_2_i=0, g=0, t=1, v=0]
    next_fischer_agent_1_x == cur_fischer_agent_1_x + time * (0),
    next_fischer_agent_1_i == cur_fischer_agent_1_i + time * (0),
    next_g == cur_g + time * (0),
    next_v == cur_v + time * (0),
    next_fischer_agent_2_x == cur_fischer_agent_2_x + time * (rate),
    next_fischer_agent_2_i == cur_fischer_agent_2_i + time * (0),
    next_t == cur_t + time * (1),
    )),
  Implies(cur_mode == 17,
    And(next_mode == cur_mode,
    #flow: [fischer_agent_1_x=0, fischer_agent_1_i=0, fischer_agent_2_x=rate, fischer_agent_2_i=0, g=0, t=1, v=0]
    next_fischer_agent_1_x == cur_fischer_agent_1_x + time * (0),
    next_fischer_agent_1_i == cur_fischer_agent_1_i + time * (0),
    next_g == cur_g + time * (0),
    next_v == cur_v + time * (0),
    next_fischer_agent_2_x == cur_fischer_agent_2_x + time * (rate),
    next_fischer_agent_2_i == cur_fischer_agent_2_i + time * (0),
    next_t == cur_t + time * (1),
    )),
  Implies(cur_mode == 18,
    And(next_mode == cur_mode,
    #flow: [fischer_agent_1_x=0, fischer_agent_1_i=0, fischer_agent_2_x=0, fischer_agent_2_i=0, g=0, t=1, v=0]
    next_fischer_agent_1_x == cur_fischer_agent_1_x + time * (0),
    next_fischer_agent_1_i == cur_fischer_agent_1_i + time * (0),
    next_g == cur_g + time * (0),
    next_v == cur_v + time * (0),
    next_fischer_agent_2_x == cur_fischer_agent_2_x + time * (0),
    next_fischer_agent_2_i == cur_fischer_agent_2_i + time * (0),
    next_t == cur_t + time * (1),
    )),
  Implies(cur_mode == 19,
    And(next_mode == cur_mode,
    #flow: [fischer_agent_1_x=0, fischer_agent_1_i=0, fischer_agent_2_x=0, fischer_agent_2_i=0, g=0, t=1, v=0]
    next_fischer_agent_1_x == cur_fischer_agent_1_x + time * (0),
    next_fischer_agent_1_i == cur_fischer_agent_1_i + time * (0),
    next_g == cur_g + time * (0),
    next_v == cur_v + time * (0),
    next_fischer_agent_2_x == cur_fischer_agent_2_x + time * (0),
    next_fischer_agent_2_i == cur_fischer_agent_2_i + time * (0),
    next_t == cur_t + time * (1),
    )),
  Implies(cur_mode == 20,
    And(next_mode == cur_mode,
    #flow: [fischer_agent_1_x=0, fischer_agent_1_i=0, fischer_agent_2_x=0, fischer_agent_2_i=0, g=0, t=1, v=0]
    next_fischer_agent_1_x == cur_fischer_agent_1_x + time * (0),
    next_fischer_agent_1_i == cur_fischer_agent_1_i + time * (0),
    next_g == cur_g + time * (0),
    next_v == cur_v + time * (0),
    next_fischer_agent_2_x == cur_fischer_agent_2_x + time * (0),
    next_fischer_agent_2_i == cur_fischer_agent_2_i + time * (0),
    next_t == cur_t + time * (1),
    )),
  Implies(cur_mode == 21,
    And(next_mode == cur_mode,
    #invariant
    next_fischer_agent_2_x <= a, 
    cur_fischer_agent_2_x <= a, 
    #flow: [fischer_agent_1_x=0, fischer_agent_1_i=0, fischer_agent_2_x=rate, fischer_agent_2_i=0, g=0, t=1, v=0]
    next_fischer_agent_1_x == cur_fischer_agent_1_x + time * (0),
    next_fischer_agent_1_i == cur_fischer_agent_1_i + time * (0),
    next_g == cur_g + time * (0),
    next_v == cur_v + time * (0),
    next_fischer_agent_2_x == cur_fischer_agent_2_x + time * (rate),
    next_fischer_agent_2_i == cur_fischer_agent_2_i + time * (0),
    next_t == cur_t + time * (1),
    )),
  Implies(cur_mode == 22,
    And(next_mode == cur_mode,
    #invariant
    next_fischer_agent_2_x <= a, 
    cur_fischer_agent_2_x <= a, 
    #flow: [fischer_agent_1_x=0, fischer_agent_1_i=0, fischer_agent_2_x=rate, fischer_agent_2_i=0, g=0, t=1, v=0]
    next_fischer_agent_1_x == cur_fischer_agent_1_x + time * (0),
    next_fischer_agent_1_i == cur_fischer_agent_1_i + time * (0),
    next_g == cur_g + time * (0),
    next_v == cur_v + time * (0),
    next_fischer_agent_2_x == cur_fischer_agent_2_x + time * (rate),
    next_fischer_agent_2_i == cur_fischer_agent_2_i + time * (0),
    next_t == cur_t + time * (1),
    )),
  Implies(cur_mode == 23,
    And(next_mode == cur_mode,
    #invariant
    next_fischer_agent_2_x <= a, 
    cur_fischer_agent_2_x <= a, 
    #flow: [fischer_agent_1_x=0, fischer_agent_1_i=0, fischer_agent_2_x=rate, fischer_agent_2_i=0, g=0, t=1, v=0]
    next_fischer_agent_1_x == cur_fischer_agent_1_x + time * (0),
    next_fischer_agent_1_i == cur_fischer_agent_1_i + time * (0),
    next_g == cur_g + time * (0),
    next_v == cur_v + time * (0),
    next_fischer_agent_2_x == cur_fischer_agent_2_x + time * (rate),
    next_fischer_agent_2_i == cur_fischer_agent_2_i + time * (0),
    next_t == cur_t + time * (1),
    )),
  Implies(cur_mode == 24,
    And(next_mode == cur_mode,
    #invariant
    next_fischer_agent_2_x <= a, 
    cur_fischer_agent_2_x <= a, 
    #flow: [fischer_agent_1_x=0, fischer_agent_1_i=0, fischer_agent_2_x=rate, fischer_agent_2_i=0, g=0, t=1, v=0]
    next_fischer_agent_1_x == cur_fischer_agent_1_x + time * (0),
    next_fischer_agent_1_i == cur_fischer_agent_1_i + time * (0),
    next_g == cur_g + time * (0),
    next_v == cur_v + time * (0),
    next_fischer_agent_2_x == cur_fischer_agent_2_x + time * (rate),
    next_fischer_agent_2_i == cur_fischer_agent_2_i + time * (0),
    next_t == cur_t + time * (1),
    )),
  Implies(cur_mode == 25,
    And(next_mode == cur_mode,
    #flow: [fischer_agent_1_x=0, fischer_agent_1_i=0, fischer_agent_2_x=rate, fischer_agent_2_i=0, g=0, t=1, v=0]
    next_fischer_agent_1_x == cur_fischer_agent_1_x + time * (0),
    next_fischer_agent_1_i == cur_fischer_agent_1_i + time * (0),
    next_g == cur_g + time * (0),
    next_v == cur_v + time * (0),
    next_fischer_agent_2_x == cur_fischer_agent_2_x + time * (rate),
    next_fischer_agent_2_i == cur_fischer_agent_2_i + time * (0),
    next_t == cur_t + time * (1),
    )),
  Implies(cur_mode == 26,
    And(next_mode == cur_mode,
    #flow: [fischer_agent_1_x=0, fischer_agent_1_i=0, fischer_agent_2_x=rate, fischer_agent_2_i=0, g=0, t=1, v=0]
    next_fischer_agent_1_x == cur_fischer_agent_1_x + time * (0),
    next_fischer_agent_1_i == cur_fischer_agent_1_i + time * (0),
    next_g == cur_g + time * (0),
    next_v == cur_v + time * (0),
    next_fischer_agent_2_x == cur_fischer_agent_2_x + time * (rate),
    next_fischer_agent_2_i == cur_fischer_agent_2_i + time * (0),
    next_t == cur_t + time * (1),
    )),
  Implies(cur_mode == 27,
    And(next_mode == cur_mode,
    #invariant
    next_fischer_agent_1_x <= a, 
    cur_fischer_agent_1_x <= a, 
    #flow: [fischer_agent_1_x=rate, fischer_agent_1_i=0, fischer_agent_2_x=0, fischer_agent_2_i=0, g=0, t=1, v=0]
    next_fischer_agent_1_x == cur_fischer_agent_1_x + time * (rate),
    next_fischer_agent_1_i == cur_fischer_agent_1_i + time * (0),
    next_g == cur_g + time * (0),
    next_v == cur_v + time * (0),
    next_fischer_agent_2_x == cur_fischer_agent_2_x + time * (0),
    next_fischer_agent_2_i == cur_fischer_agent_2_i + time * (0),
    next_t == cur_t + time * (1),
    )),
  Implies(cur_mode == 28,
    And(next_mode == cur_mode,
    #invariant
    next_fischer_agent_1_x <= a, 
    cur_fischer_agent_1_x <= a, 
    #flow: [fischer_agent_1_x=rate, fischer_agent_1_i=0, fischer_agent_2_x=0, fischer_agent_2_i=0, g=0, t=1, v=0]
    next_fischer_agent_1_x == cur_fischer_agent_1_x + time * (rate),
    next_fischer_agent_1_i == cur_fischer_agent_1_i + time * (0),
    next_g == cur_g + time * (0),
    next_v == cur_v + time * (0),
    next_fischer_agent_2_x == cur_fischer_agent_2_x + time * (0),
    next_fischer_agent_2_i == cur_fischer_agent_2_i + time * (0),
    next_t == cur_t + time * (1),
    )),
  Implies(cur_mode == 29,
    And(next_mode == cur_mode,
    #invariant
    next_fischer_agent_1_x <= a, 
    cur_fischer_agent_1_x <= a, 
    #flow: [fischer_agent_1_x=rate, fischer_agent_1_i=0, fischer_agent_2_x=0, fischer_agent_2_i=0, g=0, t=1, v=0]
    next_fischer_agent_1_x == cur_fischer_agent_1_x + time * (rate),
    next_fischer_agent_1_i == cur_fischer_agent_1_i + time * (0),
    next_g == cur_g + time * (0),
    next_v == cur_v + time * (0),
    next_fischer_agent_2_x == cur_fischer_agent_2_x + time * (0),
    next_fischer_agent_2_i == cur_fischer_agent_2_i + time * (0),
    next_t == cur_t + time * (1),
    )),
  Implies(cur_mode == 30,
    And(next_mode == cur_mode,
    #invariant
    next_fischer_agent_1_x <= a , next_fischer_agent_2_x <= a, 
    cur_fischer_agent_1_x <= a , cur_fischer_agent_2_x <= a, 
    #flow: [fischer_agent_1_x=rate, fischer_agent_1_i=0, fischer_agent_2_x=rate, fischer_agent_2_i=0, g=0, t=1, v=0]
    next_fischer_agent_1_x == cur_fischer_agent_1_x + time * (rate),
    next_fischer_agent_1_i == cur_fischer_agent_1_i + time * (0),
    next_g == cur_g + time * (0),
    next_v == cur_v + time * (0),
    next_fischer_agent_2_x == cur_fischer_agent_2_x + time * (rate),
    next_fischer_agent_2_i == cur_fischer_agent_2_i + time * (0),
    next_t == cur_t + time * (1),
    )),
  Implies(cur_mode == 31,
    And(next_mode == cur_mode,
    #invariant
    next_fischer_agent_1_x <= a , next_fischer_agent_2_x <= a, 
    cur_fischer_agent_1_x <= a , cur_fischer_agent_2_x <= a, 
    #flow: [fischer_agent_1_x=rate, fischer_agent_1_i=0, fischer_agent_2_x=rate, fischer_agent_2_i=0, g=0, t=1, v=0]
    next_fischer_agent_1_x == cur_fischer_agent_1_x + time * (rate),
    next_fischer_agent_1_i == cur_fischer_agent_1_i + time * (0),
    next_g == cur_g + time * (0),
    next_v == cur_v + time * (0),
    next_fischer_agent_2_x == cur_fischer_agent_2_x + time * (rate),
    next_fischer_agent_2_i == cur_fischer_agent_2_i + time * (0),
    next_t == cur_t + time * (1),
    )),
  Implies(cur_mode == 32,
    And(next_mode == cur_mode,
    #invariant
    next_fischer_agent_1_x <= a , next_fischer_agent_2_x <= a, 
    cur_fischer_agent_1_x <= a , cur_fischer_agent_2_x <= a, 
    #flow: [fischer_agent_1_x=rate, fischer_agent_1_i=0, fischer_agent_2_x=rate, fischer_agent_2_i=0, g=0, t=1, v=0]
    next_fischer_agent_1_x == cur_fischer_agent_1_x + time * (rate),
    next_fischer_agent_1_i == cur_fischer_agent_1_i + time * (0),
    next_g == cur_g + time * (0),
    next_v == cur_v + time * (0),
    next_fischer_agent_2_x == cur_fischer_agent_2_x + time * (rate),
    next_fischer_agent_2_i == cur_fischer_agent_2_i + time * (0),
    next_t == cur_t + time * (1),
    )),
  Implies(cur_mode == 33,
    And(next_mode == cur_mode,
    #invariant
    next_fischer_agent_1_x <= a , next_fischer_agent_2_x <= a, 
    cur_fischer_agent_1_x <= a , cur_fischer_agent_2_x <= a, 
    #flow: [fischer_agent_1_x=rate, fischer_agent_1_i=0, fischer_agent_2_x=rate, fischer_agent_2_i=0, g=0, t=1, v=0]
    next_fischer_agent_1_x == cur_fischer_agent_1_x + time * (rate),
    next_fischer_agent_1_i == cur_fischer_agent_1_i + time * (0),
    next_g == cur_g + time * (0),
    next_v == cur_v + time * (0),
    next_fischer_agent_2_x == cur_fischer_agent_2_x + time * (rate),
    next_fischer_agent_2_i == cur_fischer_agent_2_i + time * (0),
    next_t == cur_t + time * (1),
    )),
  Implies(cur_mode == 34,
    And(next_mode == cur_mode,
    #invariant
    next_fischer_agent_1_x <= a, 
    cur_fischer_agent_1_x <= a, 
    #flow: [fischer_agent_1_x=rate, fischer_agent_1_i=0, fischer_agent_2_x=rate, fischer_agent_2_i=0, g=0, t=1, v=0]
    next_fischer_agent_1_x == cur_fischer_agent_1_x + time * (rate),
    next_fischer_agent_1_i == cur_fischer_agent_1_i + time * (0),
    next_g == cur_g + time * (0),
    next_v == cur_v + time * (0),
    next_fischer_agent_2_x == cur_fischer_agent_2_x + time * (rate),
    next_fischer_agent_2_i == cur_fischer_agent_2_i + time * (0),
    next_t == cur_t + time * (1),
    )),
  Implies(cur_mode == 35,
    And(next_mode == cur_mode,
    #invariant
    next_fischer_agent_1_x <= a, 
    cur_fischer_agent_1_x <= a, 
    #flow: [fischer_agent_1_x=rate, fischer_agent_1_i=0, fischer_agent_2_x=rate, fischer_agent_2_i=0, g=0, t=1, v=0]
    next_fischer_agent_1_x == cur_fischer_agent_1_x + time * (rate),
    next_fischer_agent_1_i == cur_fischer_agent_1_i + time * (0),
    next_g == cur_g + time * (0),
    next_v == cur_v + time * (0),
    next_fischer_agent_2_x == cur_fischer_agent_2_x + time * (rate),
    next_fischer_agent_2_i == cur_fischer_agent_2_i + time * (0),
    next_t == cur_t + time * (1),
    )),
  Implies(cur_mode == 36,
    And(next_mode == cur_mode,
    #invariant
    next_fischer_agent_1_x <= a, 
    cur_fischer_agent_1_x <= a, 
    #flow: [fischer_agent_1_x=rate, fischer_agent_1_i=0, fischer_agent_2_x=0, fischer_agent_2_i=0, g=0, t=1, v=0]
    next_fischer_agent_1_x == cur_fischer_agent_1_x + time * (rate),
    next_fischer_agent_1_i == cur_fischer_agent_1_i + time * (0),
    next_g == cur_g + time * (0),
    next_v == cur_v + time * (0),
    next_fischer_agent_2_x == cur_fischer_agent_2_x + time * (0),
    next_fischer_agent_2_i == cur_fischer_agent_2_i + time * (0),
    next_t == cur_t + time * (1),
    )),
  Implies(cur_mode == 37,
    And(next_mode == cur_mode,
    #invariant
    next_fischer_agent_1_x <= a, 
    cur_fischer_agent_1_x <= a, 
    #flow: [fischer_agent_1_x=rate, fischer_agent_1_i=0, fischer_agent_2_x=0, fischer_agent_2_i=0, g=0, t=1, v=0]
    next_fischer_agent_1_x == cur_fischer_agent_1_x + time * (rate),
    next_fischer_agent_1_i == cur_fischer_agent_1_i + time * (0),
    next_g == cur_g + time * (0),
    next_v == cur_v + time * (0),
    next_fischer_agent_2_x == cur_fischer_agent_2_x + time * (0),
    next_fischer_agent_2_i == cur_fischer_agent_2_i + time * (0),
    next_t == cur_t + time * (1),
    )),
  Implies(cur_mode == 38,
    And(next_mode == cur_mode,
    #invariant
    next_fischer_agent_1_x <= a, 
    cur_fischer_agent_1_x <= a, 
    #flow: [fischer_agent_1_x=rate, fischer_agent_1_i=0, fischer_agent_2_x=0, fischer_agent_2_i=0, g=0, t=1, v=0]
    next_fischer_agent_1_x == cur_fischer_agent_1_x + time * (rate),
    next_fischer_agent_1_i == cur_fischer_agent_1_i + time * (0),
    next_g == cur_g + time * (0),
    next_v == cur_v + time * (0),
    next_fischer_agent_2_x == cur_fischer_agent_2_x + time * (0),
    next_fischer_agent_2_i == cur_fischer_agent_2_i + time * (0),
    next_t == cur_t + time * (1),
    )),
  Implies(cur_mode == 39,
    And(next_mode == cur_mode,
    #invariant
    next_fischer_agent_1_x <= a , next_fischer_agent_2_x <= a, 
    cur_fischer_agent_1_x <= a , cur_fischer_agent_2_x <= a, 
    #flow: [fischer_agent_1_x=rate, fischer_agent_1_i=0, fischer_agent_2_x=rate, fischer_agent_2_i=0, g=0, t=1, v=0]
    next_fischer_agent_1_x == cur_fischer_agent_1_x + time * (rate),
    next_fischer_agent_1_i == cur_fischer_agent_1_i + time * (0),
    next_g == cur_g + time * (0),
    next_v == cur_v + time * (0),
    next_fischer_agent_2_x == cur_fischer_agent_2_x + time * (rate),
    next_fischer_agent_2_i == cur_fischer_agent_2_i + time * (0),
    next_t == cur_t + time * (1),
    )),
  Implies(cur_mode == 40,
    And(next_mode == cur_mode,
    #invariant
    next_fischer_agent_1_x <= a , next_fischer_agent_2_x <= a, 
    cur_fischer_agent_1_x <= a , cur_fischer_agent_2_x <= a, 
    #flow: [fischer_agent_1_x=rate, fischer_agent_1_i=0, fischer_agent_2_x=rate, fischer_agent_2_i=0, g=0, t=1, v=0]
    next_fischer_agent_1_x == cur_fischer_agent_1_x + time * (rate),
    next_fischer_agent_1_i == cur_fischer_agent_1_i + time * (0),
    next_g == cur_g + time * (0),
    next_v == cur_v + time * (0),
    next_fischer_agent_2_x == cur_fischer_agent_2_x + time * (rate),
    next_fischer_agent_2_i == cur_fischer_agent_2_i + time * (0),
    next_t == cur_t + time * (1),
    )),
  Implies(cur_mode == 41,
    And(next_mode == cur_mode,
    #invariant
    next_fischer_agent_1_x <= a , next_fischer_agent_2_x <= a, 
    cur_fischer_agent_1_x <= a , cur_fischer_agent_2_x <= a, 
    #flow: [fischer_agent_1_x=rate, fischer_agent_1_i=0, fischer_agent_2_x=rate, fischer_agent_2_i=0, g=0, t=1, v=0]
    next_fischer_agent_1_x == cur_fischer_agent_1_x + time * (rate),
    next_fischer_agent_1_i == cur_fischer_agent_1_i + time * (0),
    next_g == cur_g + time * (0),
    next_v == cur_v + time * (0),
    next_fischer_agent_2_x == cur_fischer_agent_2_x + time * (rate),
    next_fischer_agent_2_i == cur_fischer_agent_2_i + time * (0),
    next_t == cur_t + time * (1),
    )),
  Implies(cur_mode == 42,
    And(next_mode == cur_mode,
    #invariant
    next_fischer_agent_1_x <= a , next_fischer_agent_2_x <= a, 
    cur_fischer_agent_1_x <= a , cur_fischer_agent_2_x <= a, 
    #flow: [fischer_agent_1_x=rate, fischer_agent_1_i=0, fischer_agent_2_x=rate, fischer_agent_2_i=0, g=0, t=1, v=0]
    next_fischer_agent_1_x == cur_fischer_agent_1_x + time * (rate),
    next_fischer_agent_1_i == cur_fischer_agent_1_i + time * (0),
    next_g == cur_g + time * (0),
    next_v == cur_v + time * (0),
    next_fischer_agent_2_x == cur_fischer_agent_2_x + time * (rate),
    next_fischer_agent_2_i == cur_fischer_agent_2_i + time * (0),
    next_t == cur_t + time * (1),
    )),
  Implies(cur_mode == 43,
    And(next_mode == cur_mode,
    #invariant
    next_fischer_agent_1_x <= a, 
    cur_fischer_agent_1_x <= a, 
    #flow: [fischer_agent_1_x=rate, fischer_agent_1_i=0, fischer_agent_2_x=rate, fischer_agent_2_i=0, g=0, t=1, v=0]
    next_fischer_agent_1_x == cur_fischer_agent_1_x + time * (rate),
    next_fischer_agent_1_i == cur_fischer_agent_1_i + time * (0),
    next_g == cur_g + time * (0),
    next_v == cur_v + time * (0),
    next_fischer_agent_2_x == cur_fischer_agent_2_x + time * (rate),
    next_fischer_agent_2_i == cur_fischer_agent_2_i + time * (0),
    next_t == cur_t + time * (1),
    )),
  Implies(cur_mode == 44,
    And(next_mode == cur_mode,
    #invariant
    next_fischer_agent_1_x <= a, 
    cur_fischer_agent_1_x <= a, 
    #flow: [fischer_agent_1_x=rate, fischer_agent_1_i=0, fischer_agent_2_x=rate, fischer_agent_2_i=0, g=0, t=1, v=0]
    next_fischer_agent_1_x == cur_fischer_agent_1_x + time * (rate),
    next_fischer_agent_1_i == cur_fischer_agent_1_i + time * (0),
    next_g == cur_g + time * (0),
    next_v == cur_v + time * (0),
    next_fischer_agent_2_x == cur_fischer_agent_2_x + time * (rate),
    next_fischer_agent_2_i == cur_fischer_agent_2_i + time * (0),
    next_t == cur_t + time * (1),
    )),
  Implies(cur_mode == 45,
    And(next_mode == cur_mode,
    #invariant
    next_fischer_agent_1_x <= a, 
    cur_fischer_agent_1_x <= a, 
    #flow: [fischer_agent_1_x=rate, fischer_agent_1_i=0, fischer_agent_2_x=0, fischer_agent_2_i=0, g=0, t=1, v=0]
    next_fischer_agent_1_x == cur_fischer_agent_1_x + time * (rate),
    next_fischer_agent_1_i == cur_fischer_agent_1_i + time * (0),
    next_g == cur_g + time * (0),
    next_v == cur_v + time * (0),
    next_fischer_agent_2_x == cur_fischer_agent_2_x + time * (0),
    next_fischer_agent_2_i == cur_fischer_agent_2_i + time * (0),
    next_t == cur_t + time * (1),
    )),
  Implies(cur_mode == 46,
    And(next_mode == cur_mode,
    #invariant
    next_fischer_agent_1_x <= a, 
    cur_fischer_agent_1_x <= a, 
    #flow: [fischer_agent_1_x=rate, fischer_agent_1_i=0, fischer_agent_2_x=0, fischer_agent_2_i=0, g=0, t=1, v=0]
    next_fischer_agent_1_x == cur_fischer_agent_1_x + time * (rate),
    next_fischer_agent_1_i == cur_fischer_agent_1_i + time * (0),
    next_g == cur_g + time * (0),
    next_v == cur_v + time * (0),
    next_fischer_agent_2_x == cur_fischer_agent_2_x + time * (0),
    next_fischer_agent_2_i == cur_fischer_agent_2_i + time * (0),
    next_t == cur_t + time * (1),
    )),
  Implies(cur_mode == 47,
    And(next_mode == cur_mode,
    #invariant
    next_fischer_agent_1_x <= a, 
    cur_fischer_agent_1_x <= a, 
    #flow: [fischer_agent_1_x=rate, fischer_agent_1_i=0, fischer_agent_2_x=0, fischer_agent_2_i=0, g=0, t=1, v=0]
    next_fischer_agent_1_x == cur_fischer_agent_1_x + time * (rate),
    next_fischer_agent_1_i == cur_fischer_agent_1_i + time * (0),
    next_g == cur_g + time * (0),
    next_v == cur_v + time * (0),
    next_fischer_agent_2_x == cur_fischer_agent_2_x + time * (0),
    next_fischer_agent_2_i == cur_fischer_agent_2_i + time * (0),
    next_t == cur_t + time * (1),
    )),
  Implies(cur_mode == 48,
    And(next_mode == cur_mode,
    #invariant
    next_fischer_agent_1_x <= a , next_fischer_agent_2_x <= a, 
    cur_fischer_agent_1_x <= a , cur_fischer_agent_2_x <= a, 
    #flow: [fischer_agent_1_x=rate, fischer_agent_1_i=0, fischer_agent_2_x=rate, fischer_agent_2_i=0, g=0, t=1, v=0]
    next_fischer_agent_1_x == cur_fischer_agent_1_x + time * (rate),
    next_fischer_agent_1_i == cur_fischer_agent_1_i + time * (0),
    next_g == cur_g + time * (0),
    next_v == cur_v + time * (0),
    next_fischer_agent_2_x == cur_fischer_agent_2_x + time * (rate),
    next_fischer_agent_2_i == cur_fischer_agent_2_i + time * (0),
    next_t == cur_t + time * (1),
    )),
  Implies(cur_mode == 49,
    And(next_mode == cur_mode,
    #invariant
    next_fischer_agent_1_x <= a , next_fischer_agent_2_x <= a, 
    cur_fischer_agent_1_x <= a , cur_fischer_agent_2_x <= a, 
    #flow: [fischer_agent_1_x=rate, fischer_agent_1_i=0, fischer_agent_2_x=rate, fischer_agent_2_i=0, g=0, t=1, v=0]
    next_fischer_agent_1_x == cur_fischer_agent_1_x + time * (rate),
    next_fischer_agent_1_i == cur_fischer_agent_1_i + time * (0),
    next_g == cur_g + time * (0),
    next_v == cur_v + time * (0),
    next_fischer_agent_2_x == cur_fischer_agent_2_x + time * (rate),
    next_fischer_agent_2_i == cur_fischer_agent_2_i + time * (0),
    next_t == cur_t + time * (1),
    )),
  Implies(cur_mode == 50,
    And(next_mode == cur_mode,
    #invariant
    next_fischer_agent_1_x <= a , next_fischer_agent_2_x <= a, 
    cur_fischer_agent_1_x <= a , cur_fischer_agent_2_x <= a, 
    #flow: [fischer_agent_1_x=rate, fischer_agent_1_i=0, fischer_agent_2_x=rate, fischer_agent_2_i=0, g=0, t=1, v=0]
    next_fischer_agent_1_x == cur_fischer_agent_1_x + time * (rate),
    next_fischer_agent_1_i == cur_fischer_agent_1_i + time * (0),
    next_g == cur_g + time * (0),
    next_v == cur_v + time * (0),
    next_fischer_agent_2_x == cur_fischer_agent_2_x + time * (rate),
    next_fischer_agent_2_i == cur_fischer_agent_2_i + time * (0),
    next_t == cur_t + time * (1),
    )),
  Implies(cur_mode == 51,
    And(next_mode == cur_mode,
    #invariant
    next_fischer_agent_1_x <= a , next_fischer_agent_2_x <= a, 
    cur_fischer_agent_1_x <= a , cur_fischer_agent_2_x <= a, 
    #flow: [fischer_agent_1_x=rate, fischer_agent_1_i=0, fischer_agent_2_x=rate, fischer_agent_2_i=0, g=0, t=1, v=0]
    next_fischer_agent_1_x == cur_fischer_agent_1_x + time * (rate),
    next_fischer_agent_1_i == cur_fischer_agent_1_i + time * (0),
    next_g == cur_g + time * (0),
    next_v == cur_v + time * (0),
    next_fischer_agent_2_x == cur_fischer_agent_2_x + time * (rate),
    next_fischer_agent_2_i == cur_fischer_agent_2_i + time * (0),
    next_t == cur_t + time * (1),
    )),
  Implies(cur_mode == 52,
    And(next_mode == cur_mode,
    #invariant
    next_fischer_agent_1_x <= a, 
    cur_fischer_agent_1_x <= a, 
    #flow: [fischer_agent_1_x=rate, fischer_agent_1_i=0, fischer_agent_2_x=rate, fischer_agent_2_i=0, g=0, t=1, v=0]
    next_fischer_agent_1_x == cur_fischer_agent_1_x + time * (rate),
    next_fischer_agent_1_i == cur_fischer_agent_1_i + time * (0),
    next_g == cur_g + time * (0),
    next_v == cur_v + time * (0),
    next_fischer_agent_2_x == cur_fischer_agent_2_x + time * (rate),
    next_fischer_agent_2_i == cur_fischer_agent_2_i + time * (0),
    next_t == cur_t + time * (1),
    )),
  Implies(cur_mode == 53,
    And(next_mode == cur_mode,
    #invariant
    next_fischer_agent_1_x <= a, 
    cur_fischer_agent_1_x <= a, 
    #flow: [fischer_agent_1_x=rate, fischer_agent_1_i=0, fischer_agent_2_x=rate, fischer_agent_2_i=0, g=0, t=1, v=0]
    next_fischer_agent_1_x == cur_fischer_agent_1_x + time * (rate),
    next_fischer_agent_1_i == cur_fischer_agent_1_i + time * (0),
    next_g == cur_g + time * (0),
    next_v == cur_v + time * (0),
    next_fischer_agent_2_x == cur_fischer_agent_2_x + time * (rate),
    next_fischer_agent_2_i == cur_fischer_agent_2_i + time * (0),
    next_t == cur_t + time * (1),
    )),
  Implies(cur_mode == 54,
    And(next_mode == cur_mode,
    #invariant
    next_fischer_agent_1_x <= a, 
    cur_fischer_agent_1_x <= a, 
    #flow: [fischer_agent_1_x=rate, fischer_agent_1_i=0, fischer_agent_2_x=0, fischer_agent_2_i=0, g=0, t=1, v=0]
    next_fischer_agent_1_x == cur_fischer_agent_1_x + time * (rate),
    next_fischer_agent_1_i == cur_fischer_agent_1_i + time * (0),
    next_g == cur_g + time * (0),
    next_v == cur_v + time * (0),
    next_fischer_agent_2_x == cur_fischer_agent_2_x + time * (0),
    next_fischer_agent_2_i == cur_fischer_agent_2_i + time * (0),
    next_t == cur_t + time * (1),
    )),
  Implies(cur_mode == 55,
    And(next_mode == cur_mode,
    #invariant
    next_fischer_agent_1_x <= a, 
    cur_fischer_agent_1_x <= a, 
    #flow: [fischer_agent_1_x=rate, fischer_agent_1_i=0, fischer_agent_2_x=0, fischer_agent_2_i=0, g=0, t=1, v=0]
    next_fischer_agent_1_x == cur_fischer_agent_1_x + time * (rate),
    next_fischer_agent_1_i == cur_fischer_agent_1_i + time * (0),
    next_g == cur_g + time * (0),
    next_v == cur_v + time * (0),
    next_fischer_agent_2_x == cur_fischer_agent_2_x + time * (0),
    next_fischer_agent_2_i == cur_fischer_agent_2_i + time * (0),
    next_t == cur_t + time * (1),
    )),
  Implies(cur_mode == 56,
    And(next_mode == cur_mode,
    #invariant
    next_fischer_agent_1_x <= a, 
    cur_fischer_agent_1_x <= a, 
    #flow: [fischer_agent_1_x=rate, fischer_agent_1_i=0, fischer_agent_2_x=0, fischer_agent_2_i=0, g=0, t=1, v=0]
    next_fischer_agent_1_x == cur_fischer_agent_1_x + time * (rate),
    next_fischer_agent_1_i == cur_fischer_agent_1_i + time * (0),
    next_g == cur_g + time * (0),
    next_v == cur_v + time * (0),
    next_fischer_agent_2_x == cur_fischer_agent_2_x + time * (0),
    next_fischer_agent_2_i == cur_fischer_agent_2_i + time * (0),
    next_t == cur_t + time * (1),
    )),
  Implies(cur_mode == 57,
    And(next_mode == cur_mode,
    #invariant
    next_fischer_agent_1_x <= a , next_fischer_agent_2_x <= a, 
    cur_fischer_agent_1_x <= a , cur_fischer_agent_2_x <= a, 
    #flow: [fischer_agent_1_x=rate, fischer_agent_1_i=0, fischer_agent_2_x=rate, fischer_agent_2_i=0, g=0, t=1, v=0]
    next_fischer_agent_1_x == cur_fischer_agent_1_x + time * (rate),
    next_fischer_agent_1_i == cur_fischer_agent_1_i + time * (0),
    next_g == cur_g + time * (0),
    next_v == cur_v + time * (0),
    next_fischer_agent_2_x == cur_fischer_agent_2_x + time * (rate),
    next_fischer_agent_2_i == cur_fischer_agent_2_i + time * (0),
    next_t == cur_t + time * (1),
    )),
  Implies(cur_mode == 58,
    And(next_mode == cur_mode,
    #invariant
    next_fischer_agent_1_x <= a , next_fischer_agent_2_x <= a, 
    cur_fischer_agent_1_x <= a , cur_fischer_agent_2_x <= a, 
    #flow: [fischer_agent_1_x=rate, fischer_agent_1_i=0, fischer_agent_2_x=rate, fischer_agent_2_i=0, g=0, t=1, v=0]
    next_fischer_agent_1_x == cur_fischer_agent_1_x + time * (rate),
    next_fischer_agent_1_i == cur_fischer_agent_1_i + time * (0),
    next_g == cur_g + time * (0),
    next_v == cur_v + time * (0),
    next_fischer_agent_2_x == cur_fischer_agent_2_x + time * (rate),
    next_fischer_agent_2_i == cur_fischer_agent_2_i + time * (0),
    next_t == cur_t + time * (1),
    )),
  Implies(cur_mode == 59,
    And(next_mode == cur_mode,
    #invariant
    next_fischer_agent_1_x <= a , next_fischer_agent_2_x <= a, 
    cur_fischer_agent_1_x <= a , cur_fischer_agent_2_x <= a, 
    #flow: [fischer_agent_1_x=rate, fischer_agent_1_i=0, fischer_agent_2_x=rate, fischer_agent_2_i=0, g=0, t=1, v=0]
    next_fischer_agent_1_x == cur_fischer_agent_1_x + time * (rate),
    next_fischer_agent_1_i == cur_fischer_agent_1_i + time * (0),
    next_g == cur_g + time * (0),
    next_v == cur_v + time * (0),
    next_fischer_agent_2_x == cur_fischer_agent_2_x + time * (rate),
    next_fischer_agent_2_i == cur_fischer_agent_2_i + time * (0),
    next_t == cur_t + time * (1),
    )),
  Implies(cur_mode == 60,
    And(next_mode == cur_mode,
    #invariant
    next_fischer_agent_1_x <= a , next_fischer_agent_2_x <= a, 
    cur_fischer_agent_1_x <= a , cur_fischer_agent_2_x <= a, 
    #flow: [fischer_agent_1_x=rate, fischer_agent_1_i=0, fischer_agent_2_x=rate, fischer_agent_2_i=0, g=0, t=1, v=0]
    next_fischer_agent_1_x == cur_fischer_agent_1_x + time * (rate),
    next_fischer_agent_1_i == cur_fischer_agent_1_i + time * (0),
    next_g == cur_g + time * (0),
    next_v == cur_v + time * (0),
    next_fischer_agent_2_x == cur_fischer_agent_2_x + time * (rate),
    next_fischer_agent_2_i == cur_fischer_agent_2_i + time * (0),
    next_t == cur_t + time * (1),
    )),
  Implies(cur_mode == 61,
    And(next_mode == cur_mode,
    #invariant
    next_fischer_agent_1_x <= a, 
    cur_fischer_agent_1_x <= a, 
    #flow: [fischer_agent_1_x=rate, fischer_agent_1_i=0, fischer_agent_2_x=rate, fischer_agent_2_i=0, g=0, t=1, v=0]
    next_fischer_agent_1_x == cur_fischer_agent_1_x + time * (rate),
    next_fischer_agent_1_i == cur_fischer_agent_1_i + time * (0),
    next_g == cur_g + time * (0),
    next_v == cur_v + time * (0),
    next_fischer_agent_2_x == cur_fischer_agent_2_x + time * (rate),
    next_fischer_agent_2_i == cur_fischer_agent_2_i + time * (0),
    next_t == cur_t + time * (1),
    )),
  Implies(cur_mode == 62,
    And(next_mode == cur_mode,
    #invariant
    next_fischer_agent_1_x <= a, 
    cur_fischer_agent_1_x <= a, 
    #flow: [fischer_agent_1_x=rate, fischer_agent_1_i=0, fischer_agent_2_x=rate, fischer_agent_2_i=0, g=0, t=1, v=0]
    next_fischer_agent_1_x == cur_fischer_agent_1_x + time * (rate),
    next_fischer_agent_1_i == cur_fischer_agent_1_i + time * (0),
    next_g == cur_g + time * (0),
    next_v == cur_v + time * (0),
    next_fischer_agent_2_x == cur_fischer_agent_2_x + time * (rate),
    next_fischer_agent_2_i == cur_fischer_agent_2_i + time * (0),
    next_t == cur_t + time * (1),
    )),
  Implies(cur_mode == 63,
    And(next_mode == cur_mode,
    #flow: [fischer_agent_1_x=rate, fischer_agent_1_i=0, fischer_agent_2_x=0, fischer_agent_2_i=0, g=0, t=1, v=0]
    next_fischer_agent_1_x == cur_fischer_agent_1_x + time * (rate),
    next_fischer_agent_1_i == cur_fischer_agent_1_i + time * (0),
    next_g == cur_g + time * (0),
    next_v == cur_v + time * (0),
    next_fischer_agent_2_x == cur_fischer_agent_2_x + time * (0),
    next_fischer_agent_2_i == cur_fischer_agent_2_i + time * (0),
    next_t == cur_t + time * (1),
    )),
  Implies(cur_mode == 64,
    And(next_mode == cur_mode,
    #flow: [fischer_agent_1_x=rate, fischer_agent_1_i=0, fischer_agent_2_x=0, fischer_agent_2_i=0, g=0, t=1, v=0]
    next_fischer_agent_1_x == cur_fischer_agent_1_x + time * (rate),
    next_fischer_agent_1_i == cur_fischer_agent_1_i + time * (0),
    next_g == cur_g + time * (0),
    next_v == cur_v + time * (0),
    next_fischer_agent_2_x == cur_fischer_agent_2_x + time * (0),
    next_fischer_agent_2_i == cur_fischer_agent_2_i + time * (0),
    next_t == cur_t + time * (1),
    )),
  Implies(cur_mode == 65,
    And(next_mode == cur_mode,
    #flow: [fischer_agent_1_x=rate, fischer_agent_1_i=0, fischer_agent_2_x=0, fischer_agent_2_i=0, g=0, t=1, v=0]
    next_fischer_agent_1_x == cur_fischer_agent_1_x + time * (rate),
    next_fischer_agent_1_i == cur_fischer_agent_1_i + time * (0),
    next_g == cur_g + time * (0),
    next_v == cur_v + time * (0),
    next_fischer_agent_2_x == cur_fischer_agent_2_x + time * (0),
    next_fischer_agent_2_i == cur_fischer_agent_2_i + time * (0),
    next_t == cur_t + time * (1),
    )),
  Implies(cur_mode == 66,
    And(next_mode == cur_mode,
    #invariant
    next_fischer_agent_2_x <= a, 
    cur_fischer_agent_2_x <= a, 
    #flow: [fischer_agent_1_x=rate, fischer_agent_1_i=0, fischer_agent_2_x=rate, fischer_agent_2_i=0, g=0, t=1, v=0]
    next_fischer_agent_1_x == cur_fischer_agent_1_x + time * (rate),
    next_fischer_agent_1_i == cur_fischer_agent_1_i + time * (0),
    next_g == cur_g + time * (0),
    next_v == cur_v + time * (0),
    next_fischer_agent_2_x == cur_fischer_agent_2_x + time * (rate),
    next_fischer_agent_2_i == cur_fischer_agent_2_i + time * (0),
    next_t == cur_t + time * (1),
    )),
  Implies(cur_mode == 67,
    And(next_mode == cur_mode,
    #invariant
    next_fischer_agent_2_x <= a, 
    cur_fischer_agent_2_x <= a, 
    #flow: [fischer_agent_1_x=rate, fischer_agent_1_i=0, fischer_agent_2_x=rate, fischer_agent_2_i=0, g=0, t=1, v=0]
    next_fischer_agent_1_x == cur_fischer_agent_1_x + time * (rate),
    next_fischer_agent_1_i == cur_fischer_agent_1_i + time * (0),
    next_g == cur_g + time * (0),
    next_v == cur_v + time * (0),
    next_fischer_agent_2_x == cur_fischer_agent_2_x + time * (rate),
    next_fischer_agent_2_i == cur_fischer_agent_2_i + time * (0),
    next_t == cur_t + time * (1),
    )),
  Implies(cur_mode == 68,
    And(next_mode == cur_mode,
    #invariant
    next_fischer_agent_2_x <= a, 
    cur_fischer_agent_2_x <= a, 
    #flow: [fischer_agent_1_x=rate, fischer_agent_1_i=0, fischer_agent_2_x=rate, fischer_agent_2_i=0, g=0, t=1, v=0]
    next_fischer_agent_1_x == cur_fischer_agent_1_x + time * (rate),
    next_fischer_agent_1_i == cur_fischer_agent_1_i + time * (0),
    next_g == cur_g + time * (0),
    next_v == cur_v + time * (0),
    next_fischer_agent_2_x == cur_fischer_agent_2_x + time * (rate),
    next_fischer_agent_2_i == cur_fischer_agent_2_i + time * (0),
    next_t == cur_t + time * (1),
    )),
  Implies(cur_mode == 69,
    And(next_mode == cur_mode,
    #invariant
    next_fischer_agent_2_x <= a, 
    cur_fischer_agent_2_x <= a, 
    #flow: [fischer_agent_1_x=rate, fischer_agent_1_i=0, fischer_agent_2_x=rate, fischer_agent_2_i=0, g=0, t=1, v=0]
    next_fischer_agent_1_x == cur_fischer_agent_1_x + time * (rate),
    next_fischer_agent_1_i == cur_fischer_agent_1_i + time * (0),
    next_g == cur_g + time * (0),
    next_v == cur_v + time * (0),
    next_fischer_agent_2_x == cur_fischer_agent_2_x + time * (rate),
    next_fischer_agent_2_i == cur_fischer_agent_2_i + time * (0),
    next_t == cur_t + time * (1),
    )),
  Implies(cur_mode == 70,
    And(next_mode == cur_mode,
    #flow: [fischer_agent_1_x=rate, fischer_agent_1_i=0, fischer_agent_2_x=rate, fischer_agent_2_i=0, g=0, t=1, v=0]
    next_fischer_agent_1_x == cur_fischer_agent_1_x + time * (rate),
    next_fischer_agent_1_i == cur_fischer_agent_1_i + time * (0),
    next_g == cur_g + time * (0),
    next_v == cur_v + time * (0),
    next_fischer_agent_2_x == cur_fischer_agent_2_x + time * (rate),
    next_fischer_agent_2_i == cur_fischer_agent_2_i + time * (0),
    next_t == cur_t + time * (1),
    )),
  Implies(cur_mode == 71,
    And(next_mode == cur_mode,
    #flow: [fischer_agent_1_x=rate, fischer_agent_1_i=0, fischer_agent_2_x=rate, fischer_agent_2_i=0, g=0, t=1, v=0]
    next_fischer_agent_1_x == cur_fischer_agent_1_x + time * (rate),
    next_fischer_agent_1_i == cur_fischer_agent_1_i + time * (0),
    next_g == cur_g + time * (0),
    next_v == cur_v + time * (0),
    next_fischer_agent_2_x == cur_fischer_agent_2_x + time * (rate),
    next_fischer_agent_2_i == cur_fischer_agent_2_i + time * (0),
    next_t == cur_t + time * (1),
    )),
  Implies(cur_mode == 72,
    And(next_mode == cur_mode,
    #flow: [fischer_agent_1_x=rate, fischer_agent_1_i=0, fischer_agent_2_x=0, fischer_agent_2_i=0, g=0, t=1, v=0]
    next_fischer_agent_1_x == cur_fischer_agent_1_x + time * (rate),
    next_fischer_agent_1_i == cur_fischer_agent_1_i + time * (0),
    next_g == cur_g + time * (0),
    next_v == cur_v + time * (0),
    next_fischer_agent_2_x == cur_fischer_agent_2_x + time * (0),
    next_fischer_agent_2_i == cur_fischer_agent_2_i + time * (0),
    next_t == cur_t + time * (1),
    )),
  Implies(cur_mode == 73,
    And(next_mode == cur_mode,
    #flow: [fischer_agent_1_x=rate, fischer_agent_1_i=0, fischer_agent_2_x=0, fischer_agent_2_i=0, g=0, t=1, v=0]
    next_fischer_agent_1_x == cur_fischer_agent_1_x + time * (rate),
    next_fischer_agent_1_i == cur_fischer_agent_1_i + time * (0),
    next_g == cur_g + time * (0),
    next_v == cur_v + time * (0),
    next_fischer_agent_2_x == cur_fischer_agent_2_x + time * (0),
    next_fischer_agent_2_i == cur_fischer_agent_2_i + time * (0),
    next_t == cur_t + time * (1),
    )),
  Implies(cur_mode == 74,
    And(next_mode == cur_mode,
    #flow: [fischer_agent_1_x=rate, fischer_agent_1_i=0, fischer_agent_2_x=0, fischer_agent_2_i=0, g=0, t=1, v=0]
    next_fischer_agent_1_x == cur_fischer_agent_1_x + time * (rate),
    next_fischer_agent_1_i == cur_fischer_agent_1_i + time * (0),
    next_g == cur_g + time * (0),
    next_v == cur_v + time * (0),
    next_fischer_agent_2_x == cur_fischer_agent_2_x + time * (0),
    next_fischer_agent_2_i == cur_fischer_agent_2_i + time * (0),
    next_t == cur_t + time * (1),
    )),
  Implies(cur_mode == 75,
    And(next_mode == cur_mode,
    #invariant
    next_fischer_agent_2_x <= a, 
    cur_fischer_agent_2_x <= a, 
    #flow: [fischer_agent_1_x=rate, fischer_agent_1_i=0, fischer_agent_2_x=rate, fischer_agent_2_i=0, g=0, t=1, v=0]
    next_fischer_agent_1_x == cur_fischer_agent_1_x + time * (rate),
    next_fischer_agent_1_i == cur_fischer_agent_1_i + time * (0),
    next_g == cur_g + time * (0),
    next_v == cur_v + time * (0),
    next_fischer_agent_2_x == cur_fischer_agent_2_x + time * (rate),
    next_fischer_agent_2_i == cur_fischer_agent_2_i + time * (0),
    next_t == cur_t + time * (1),
    )),
  Implies(cur_mode == 76,
    And(next_mode == cur_mode,
    #invariant
    next_fischer_agent_2_x <= a, 
    cur_fischer_agent_2_x <= a, 
    #flow: [fischer_agent_1_x=rate, fischer_agent_1_i=0, fischer_agent_2_x=rate, fischer_agent_2_i=0, g=0, t=1, v=0]
    next_fischer_agent_1_x == cur_fischer_agent_1_x + time * (rate),
    next_fischer_agent_1_i == cur_fischer_agent_1_i + time * (0),
    next_g == cur_g + time * (0),
    next_v == cur_v + time * (0),
    next_fischer_agent_2_x == cur_fischer_agent_2_x + time * (rate),
    next_fischer_agent_2_i == cur_fischer_agent_2_i + time * (0),
    next_t == cur_t + time * (1),
    )),
  Implies(cur_mode == 77,
    And(next_mode == cur_mode,
    #invariant
    next_fischer_agent_2_x <= a, 
    cur_fischer_agent_2_x <= a, 
    #flow: [fischer_agent_1_x=rate, fischer_agent_1_i=0, fischer_agent_2_x=rate, fischer_agent_2_i=0, g=0, t=1, v=0]
    next_fischer_agent_1_x == cur_fischer_agent_1_x + time * (rate),
    next_fischer_agent_1_i == cur_fischer_agent_1_i + time * (0),
    next_g == cur_g + time * (0),
    next_v == cur_v + time * (0),
    next_fischer_agent_2_x == cur_fischer_agent_2_x + time * (rate),
    next_fischer_agent_2_i == cur_fischer_agent_2_i + time * (0),
    next_t == cur_t + time * (1),
    )),
  Implies(cur_mode == 78,
    And(next_mode == cur_mode,
    #invariant
    next_fischer_agent_2_x <= a, 
    cur_fischer_agent_2_x <= a, 
    #flow: [fischer_agent_1_x=rate, fischer_agent_1_i=0, fischer_agent_2_x=rate, fischer_agent_2_i=0, g=0, t=1, v=0]
    next_fischer_agent_1_x == cur_fischer_agent_1_x + time * (rate),
    next_fischer_agent_1_i == cur_fischer_agent_1_i + time * (0),
    next_g == cur_g + time * (0),
    next_v == cur_v + time * (0),
    next_fischer_agent_2_x == cur_fischer_agent_2_x + time * (rate),
    next_fischer_agent_2_i == cur_fischer_agent_2_i + time * (0),
    next_t == cur_t + time * (1),
    )),
  Implies(cur_mode == 79,
    And(next_mode == cur_mode,
    #flow: [fischer_agent_1_x=rate, fischer_agent_1_i=0, fischer_agent_2_x=rate, fischer_agent_2_i=0, g=0, t=1, v=0]
    next_fischer_agent_1_x == cur_fischer_agent_1_x + time * (rate),
    next_fischer_agent_1_i == cur_fischer_agent_1_i + time * (0),
    next_g == cur_g + time * (0),
    next_v == cur_v + time * (0),
    next_fischer_agent_2_x == cur_fischer_agent_2_x + time * (rate),
    next_fischer_agent_2_i == cur_fischer_agent_2_i + time * (0),
    next_t == cur_t + time * (1),
    )),
  Implies(cur_mode == 80,
    And(next_mode == cur_mode,
    #flow: [fischer_agent_1_x=rate, fischer_agent_1_i=0, fischer_agent_2_x=rate, fischer_agent_2_i=0, g=0, t=1, v=0]
    next_fischer_agent_1_x == cur_fischer_agent_1_x + time * (rate),
    next_fischer_agent_1_i == cur_fischer_agent_1_i + time * (0),
    next_g == cur_g + time * (0),
    next_v == cur_v + time * (0),
    next_fischer_agent_2_x == cur_fischer_agent_2_x + time * (rate),
    next_fischer_agent_2_i == cur_fischer_agent_2_i + time * (0),
    next_t == cur_t + time * (1),
    )),
  )
)

# Transition Relation
Transitions = And(
  And(
  Implies(cur_mode == BitVecVal(0, modeBitSize), 
  Or(
    And(cur_g == 0, And(next_fischer_agent_1_x == 0, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(54, modeBitSize))),
    And(cur_g == 0, And(next_fischer_agent_2_x == 0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(6, modeBitSize))),
    And(true, And(next_g == 2, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(0, modeBitSize))))
  )
  ,
  Implies(cur_mode == BitVecVal(1, modeBitSize), 
  Or(
    And(cur_g == 0, And(next_fischer_agent_1_x == 0, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(55, modeBitSize))),
    And(cur_g == 0, And(next_fischer_agent_2_x == 0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(4, modeBitSize))),
    And(true, And(next_g == 2, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(1, modeBitSize))))
  )
  ,
  Implies(cur_mode == BitVecVal(2, modeBitSize), 
  Or(
    And(cur_g == 0, And(next_fischer_agent_1_x == 0, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(56, modeBitSize))),
    And(cur_v == 0, And(next_fischer_agent_2_x == 0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(5, modeBitSize))),
    And(cur_v == 1, And(next_fischer_agent_2_x == 0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(1, modeBitSize))),
    And(true, And(next_g == 2, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(2, modeBitSize))))
  )
  ,
  Implies(cur_mode == BitVecVal(3, modeBitSize), 
  Or(
    And(cur_g == 0, And(next_fischer_agent_1_x == 0, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(57, modeBitSize))),
    And(true, And(next_g == 2, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(3, modeBitSize))))
  )
  ,
  Implies(cur_mode == BitVecVal(4, modeBitSize), 
  Or(
    And(cur_g == 0, And(next_fischer_agent_1_x == 0, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(58, modeBitSize))),
    And(true, And(next_fischer_agent_2_x == 0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(7, modeBitSize))),
    And(true, And(next_g == 2, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(4, modeBitSize))))
  )
  ,
  Implies(cur_mode == BitVecVal(5, modeBitSize), 
  Or(
    And(cur_g == 0, And(next_fischer_agent_1_x == 0, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(59, modeBitSize))),
    And(true, And(next_fischer_agent_2_x == 0, next_v == 1, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(8, modeBitSize))),
    And(true, And(next_g == 2, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(5, modeBitSize))))
  )
  ,
  Implies(cur_mode == BitVecVal(6, modeBitSize), 
  Or(
    And(cur_g == 0, And(next_fischer_agent_1_x == 0, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(60, modeBitSize))),
    And(cur_fischer_agent_2_x >= cur_b, And(next_fischer_agent_2_x == 0, next_v == 0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(3, modeBitSize))),
    And(true, And(next_g == 2, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(6, modeBitSize))))
  )
  ,
  Implies(cur_mode == BitVecVal(7, modeBitSize), 
  Or(
    And(cur_g == 0, And(next_fischer_agent_1_x == 0, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(61, modeBitSize))),
    And(cur_g < cur_fischer_agent_2_i ,  cur_fischer_agent_2_x >= cur_b, And(next_fischer_agent_2_x == 0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(1, modeBitSize))),
    And(cur_g > cur_fischer_agent_2_i ,  cur_fischer_agent_2_x >= cur_b, And(next_fischer_agent_2_x == 0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(1, modeBitSize))),
    And(cur_g == cur_fischer_agent_2_i ,  cur_fischer_agent_2_x >= cur_b, And(next_fischer_agent_2_x == 0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(2, modeBitSize))),
    And(true, And(next_g == 2, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(7, modeBitSize))))
  )
  ,
  Implies(cur_mode == BitVecVal(8, modeBitSize), 
  Or(
    And(cur_g == 0, And(next_fischer_agent_1_x == 0, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(62, modeBitSize))),
    And(cur_g > cur_fischer_agent_2_i, And(next_fischer_agent_2_x == 0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(1, modeBitSize))),
    And(cur_g < cur_fischer_agent_2_i, And(next_fischer_agent_2_x == 0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(1, modeBitSize))),
    And(cur_g == cur_fischer_agent_2_i, And(next_fischer_agent_2_x == 0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(0, modeBitSize))),
    And(true, And(next_g == 2, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(8, modeBitSize))))
  )
  ,
  Implies(cur_mode == BitVecVal(9, modeBitSize), 
  Or(
    And(cur_g == 0, And(next_fischer_agent_1_x == 0, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(36, modeBitSize))),
    And(cur_g == 0, And(next_fischer_agent_2_x == 0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(15, modeBitSize))),
    And(true, And(next_g == 2, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(9, modeBitSize))))
  )
  ,
  Implies(cur_mode == BitVecVal(10, modeBitSize), 
  Or(
    And(cur_g == 0, And(next_fischer_agent_1_x == 0, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(37, modeBitSize))),
    And(cur_g == 0, And(next_fischer_agent_2_x == 0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(13, modeBitSize))),
    And(true, And(next_g == 2, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(10, modeBitSize))))
  )
  ,
  Implies(cur_mode == BitVecVal(11, modeBitSize), 
  Or(
    And(cur_g == 0, And(next_fischer_agent_1_x == 0, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(38, modeBitSize))),
    And(cur_v == 0, And(next_fischer_agent_2_x == 0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(14, modeBitSize))),
    And(cur_v == 1, And(next_fischer_agent_2_x == 0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(10, modeBitSize))),
    And(true, And(next_g == 2, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(11, modeBitSize))))
  )
  ,
  Implies(cur_mode == BitVecVal(12, modeBitSize), 
  Or(
    And(cur_g == 0, And(next_fischer_agent_1_x == 0, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(39, modeBitSize))),
    And(true, And(next_g == 2, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(12, modeBitSize))))
  )
  ,
  Implies(cur_mode == BitVecVal(13, modeBitSize), 
  Or(
    And(cur_g == 0, And(next_fischer_agent_1_x == 0, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(40, modeBitSize))),
    And(true, And(next_fischer_agent_2_x == 0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(16, modeBitSize))),
    And(true, And(next_g == 2, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(13, modeBitSize))))
  )
  ,
  Implies(cur_mode == BitVecVal(14, modeBitSize), 
  Or(
    And(cur_g == 0, And(next_fischer_agent_1_x == 0, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(41, modeBitSize))),
    And(true, And(next_fischer_agent_2_x == 0, next_v == 1, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(17, modeBitSize))),
    And(true, And(next_g == 2, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(14, modeBitSize))))
  )
  ,
  Implies(cur_mode == BitVecVal(15, modeBitSize), 
  Or(
    And(cur_g == 0, And(next_fischer_agent_1_x == 0, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(42, modeBitSize))),
    And(cur_fischer_agent_2_x >= cur_b, And(next_fischer_agent_2_x == 0, next_v == 0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(12, modeBitSize))),
    And(true, And(next_g == 2, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(15, modeBitSize))))
  )
  ,
  Implies(cur_mode == BitVecVal(16, modeBitSize), 
  Or(
    And(cur_g == 0, And(next_fischer_agent_1_x == 0, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(43, modeBitSize))),
    And(cur_g < cur_fischer_agent_2_i ,  cur_fischer_agent_2_x >= cur_b, And(next_fischer_agent_2_x == 0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(10, modeBitSize))),
    And(cur_g > cur_fischer_agent_2_i ,  cur_fischer_agent_2_x >= cur_b, And(next_fischer_agent_2_x == 0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(10, modeBitSize))),
    And(cur_g == cur_fischer_agent_2_i ,  cur_fischer_agent_2_x >= cur_b, And(next_fischer_agent_2_x == 0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(11, modeBitSize))),
    And(true, And(next_g == 2, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(16, modeBitSize))))
  )
  ,
  Implies(cur_mode == BitVecVal(17, modeBitSize), 
  Or(
    And(cur_g == 0, And(next_fischer_agent_1_x == 0, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(44, modeBitSize))),
    And(cur_g > cur_fischer_agent_2_i, And(next_fischer_agent_2_x == 0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(10, modeBitSize))),
    And(cur_g < cur_fischer_agent_2_i, And(next_fischer_agent_2_x == 0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(10, modeBitSize))),
    And(cur_g == cur_fischer_agent_2_i, And(next_fischer_agent_2_x == 0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(9, modeBitSize))),
    And(true, And(next_g == 2, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(17, modeBitSize))))
  )
  ,
  Implies(cur_mode == BitVecVal(18, modeBitSize), 
  Or(
    And(cur_v == 0, And(next_fischer_agent_1_x == 0, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(45, modeBitSize))),
    And(cur_v == 1, And(next_fischer_agent_1_x == 0, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(9, modeBitSize))),
    And(cur_g == 0, And(next_fischer_agent_2_x == 0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(24, modeBitSize))),
    And(true, And(next_g == 2, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(18, modeBitSize))))
  )
  ,
  Implies(cur_mode == BitVecVal(19, modeBitSize), 
  Or(
    And(cur_v == 0, And(next_fischer_agent_1_x == 0, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(46, modeBitSize))),
    And(cur_v == 1, And(next_fischer_agent_1_x == 0, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(10, modeBitSize))),
    And(cur_g == 0, And(next_fischer_agent_2_x == 0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(22, modeBitSize))),
    And(true, And(next_g == 2, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(19, modeBitSize))))
  )
  ,
  Implies(cur_mode == BitVecVal(20, modeBitSize), 
  Or(
    And(cur_v == 0, And(next_fischer_agent_1_x == 0, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(47, modeBitSize))),
    And(cur_v == 1, And(next_fischer_agent_1_x == 0, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(11, modeBitSize))),
    And(cur_v == 0, And(next_fischer_agent_2_x == 0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(23, modeBitSize))),
    And(cur_v == 1, And(next_fischer_agent_2_x == 0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(19, modeBitSize))),
    And(true, And(next_g == 2, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(20, modeBitSize))))
  )
  ,
  Implies(cur_mode == BitVecVal(21, modeBitSize), 
  Or(
    And(cur_v == 0, And(next_fischer_agent_1_x == 0, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(48, modeBitSize))),
    And(cur_v == 1, And(next_fischer_agent_1_x == 0, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(12, modeBitSize))),
    And(true, And(next_g == 2, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(21, modeBitSize))))
  )
  ,
  Implies(cur_mode == BitVecVal(22, modeBitSize), 
  Or(
    And(cur_v == 0, And(next_fischer_agent_1_x == 0, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(49, modeBitSize))),
    And(cur_v == 1, And(next_fischer_agent_1_x == 0, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(13, modeBitSize))),
    And(true, And(next_fischer_agent_2_x == 0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(25, modeBitSize))),
    And(true, And(next_g == 2, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(22, modeBitSize))))
  )
  ,
  Implies(cur_mode == BitVecVal(23, modeBitSize), 
  Or(
    And(cur_v == 0, And(next_fischer_agent_1_x == 0, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(50, modeBitSize))),
    And(cur_v == 1, And(next_fischer_agent_1_x == 0, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(14, modeBitSize))),
    And(true, And(next_fischer_agent_2_x == 0, next_v == 1, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(26, modeBitSize))),
    And(true, And(next_g == 2, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(23, modeBitSize))))
  )
  ,
  Implies(cur_mode == BitVecVal(24, modeBitSize), 
  Or(
    And(cur_v == 0, And(next_fischer_agent_1_x == 0, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(51, modeBitSize))),
    And(cur_v == 1, And(next_fischer_agent_1_x == 0, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(15, modeBitSize))),
    And(cur_fischer_agent_2_x >= cur_b, And(next_fischer_agent_2_x == 0, next_v == 0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(21, modeBitSize))),
    And(true, And(next_g == 2, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(24, modeBitSize))))
  )
  ,
  Implies(cur_mode == BitVecVal(25, modeBitSize), 
  Or(
    And(cur_v == 0, And(next_fischer_agent_1_x == 0, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(52, modeBitSize))),
    And(cur_v == 1, And(next_fischer_agent_1_x == 0, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(16, modeBitSize))),
    And(cur_g < cur_fischer_agent_2_i ,  cur_fischer_agent_2_x >= cur_b, And(next_fischer_agent_2_x == 0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(19, modeBitSize))),
    And(cur_g > cur_fischer_agent_2_i ,  cur_fischer_agent_2_x >= cur_b, And(next_fischer_agent_2_x == 0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(19, modeBitSize))),
    And(cur_g == cur_fischer_agent_2_i ,  cur_fischer_agent_2_x >= cur_b, And(next_fischer_agent_2_x == 0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(20, modeBitSize))),
    And(true, And(next_g == 2, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(25, modeBitSize))))
  )
  ,
  Implies(cur_mode == BitVecVal(26, modeBitSize), 
  Or(
    And(cur_v == 0, And(next_fischer_agent_1_x == 0, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(53, modeBitSize))),
    And(cur_v == 1, And(next_fischer_agent_1_x == 0, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(17, modeBitSize))),
    And(cur_g > cur_fischer_agent_2_i, And(next_fischer_agent_2_x == 0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(19, modeBitSize))),
    And(cur_g < cur_fischer_agent_2_i, And(next_fischer_agent_2_x == 0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(19, modeBitSize))),
    And(cur_g == cur_fischer_agent_2_i, And(next_fischer_agent_2_x == 0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(18, modeBitSize))),
    And(true, And(next_g == 2, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(26, modeBitSize))))
  )
  ,
  Implies(cur_mode == BitVecVal(27, modeBitSize), 
  Or(
    And(cur_g == 0, And(next_fischer_agent_2_x == 0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(33, modeBitSize))),
    And(true, And(next_g == 2, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(27, modeBitSize))))
  )
  ,
  Implies(cur_mode == BitVecVal(28, modeBitSize), 
  Or(
    And(cur_g == 0, And(next_fischer_agent_2_x == 0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(31, modeBitSize))),
    And(true, And(next_g == 2, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(28, modeBitSize))))
  )
  ,
  Implies(cur_mode == BitVecVal(29, modeBitSize), 
  Or(
    And(cur_v == 0, And(next_fischer_agent_2_x == 0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(32, modeBitSize))),
    And(cur_v == 1, And(next_fischer_agent_2_x == 0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(28, modeBitSize))),
    And(true, And(next_g == 2, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(29, modeBitSize))))
  )
  ,
  Implies(cur_mode == BitVecVal(30, modeBitSize), 
  Or(
    And(true, And(next_g == 2, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(30, modeBitSize))),
    And(cur_fischer_agent_1_x >= cur_b ,  cur_fischer_agent_2_x >= cur_b, And(next_fischer_agent_2_x == 0, next_fischer_agent_1_x == 0, next_g == 0, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_v == cur_v, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(10, modeBitSize))))
  )
  ,
  Implies(cur_mode == BitVecVal(31, modeBitSize), 
  Or(
    And(true, And(next_fischer_agent_2_x == 0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(34, modeBitSize))),
    And(true, And(next_g == 2, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(31, modeBitSize))))
  )
  ,
  Implies(cur_mode == BitVecVal(32, modeBitSize), 
  Or(
    And(true, And(next_fischer_agent_2_x == 0, next_v == 1, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(35, modeBitSize))),
    And(true, And(next_g == 2, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(32, modeBitSize))))
  )
  ,
  Implies(cur_mode == BitVecVal(33, modeBitSize), 
  Or(
    And(cur_fischer_agent_2_x >= cur_b, And(next_fischer_agent_2_x == 0, next_v == 0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(30, modeBitSize))),
    And(true, And(next_g == 2, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(33, modeBitSize))))
  )
  ,
  Implies(cur_mode == BitVecVal(34, modeBitSize), 
  Or(
    And(cur_g < cur_fischer_agent_2_i ,  cur_fischer_agent_2_x >= cur_b, And(next_fischer_agent_2_x == 0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(28, modeBitSize))),
    And(cur_g > cur_fischer_agent_2_i ,  cur_fischer_agent_2_x >= cur_b, And(next_fischer_agent_2_x == 0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(28, modeBitSize))),
    And(cur_g == cur_fischer_agent_2_i ,  cur_fischer_agent_2_x >= cur_b, And(next_fischer_agent_2_x == 0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(29, modeBitSize))),
    And(true, And(next_g == 2, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(34, modeBitSize))))
  )
  ,
  Implies(cur_mode == BitVecVal(35, modeBitSize), 
  Or(
    And(cur_g > cur_fischer_agent_2_i, And(next_fischer_agent_2_x == 0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(28, modeBitSize))),
    And(cur_g < cur_fischer_agent_2_i, And(next_fischer_agent_2_x == 0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(28, modeBitSize))),
    And(cur_g == cur_fischer_agent_2_i, And(next_fischer_agent_2_x == 0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(27, modeBitSize))),
    And(true, And(next_g == 2, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(35, modeBitSize))))
  )
  ,
  Implies(cur_mode == BitVecVal(36, modeBitSize), 
  Or(
    And(cur_g == 0, And(next_fischer_agent_2_x == 0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(42, modeBitSize))),
    And(true, And(next_g == 2, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(36, modeBitSize))),
    And(true, And(next_fischer_agent_1_x == 0, next_g == 1, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(63, modeBitSize))))
  )
  ,
  Implies(cur_mode == BitVecVal(37, modeBitSize), 
  Or(
    And(cur_g == 0, And(next_fischer_agent_2_x == 0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(40, modeBitSize))),
    And(true, And(next_g == 2, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(37, modeBitSize))),
    And(true, And(next_fischer_agent_1_x == 0, next_g == 1, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(64, modeBitSize))))
  )
  ,
  Implies(cur_mode == BitVecVal(38, modeBitSize), 
  Or(
    And(cur_v == 0, And(next_fischer_agent_2_x == 0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(41, modeBitSize))),
    And(cur_v == 1, And(next_fischer_agent_2_x == 0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(37, modeBitSize))),
    And(true, And(next_g == 2, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(38, modeBitSize))),
    And(true, And(next_fischer_agent_1_x == 0, next_g == 1, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(65, modeBitSize))))
  )
  ,
  Implies(cur_mode == BitVecVal(39, modeBitSize), 
  Or(
    And(true, And(next_g == 2, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(39, modeBitSize))),
    And(true, And(next_fischer_agent_1_x == 0, next_g == 1, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(66, modeBitSize))))
  )
  ,
  Implies(cur_mode == BitVecVal(40, modeBitSize), 
  Or(
    And(true, And(next_fischer_agent_2_x == 0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(43, modeBitSize))),
    And(true, And(next_g == 2, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(40, modeBitSize))),
    And(true, And(next_fischer_agent_1_x == 0, next_g == 1, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(67, modeBitSize))))
  )
  ,
  Implies(cur_mode == BitVecVal(41, modeBitSize), 
  Or(
    And(true, And(next_fischer_agent_2_x == 0, next_v == 1, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(44, modeBitSize))),
    And(true, And(next_g == 2, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(41, modeBitSize))),
    And(true, And(next_fischer_agent_1_x == 0, next_g == 1, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(68, modeBitSize))))
  )
  ,
  Implies(cur_mode == BitVecVal(42, modeBitSize), 
  Or(
    And(cur_fischer_agent_2_x >= cur_b, And(next_fischer_agent_2_x == 0, next_v == 0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(39, modeBitSize))),
    And(true, And(next_g == 2, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(42, modeBitSize))),
    And(true, And(next_fischer_agent_1_x == 0, next_g == 1, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(69, modeBitSize))))
  )
  ,
  Implies(cur_mode == BitVecVal(43, modeBitSize), 
  Or(
    And(cur_g < cur_fischer_agent_2_i ,  cur_fischer_agent_2_x >= cur_b, And(next_fischer_agent_2_x == 0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(37, modeBitSize))),
    And(cur_g > cur_fischer_agent_2_i ,  cur_fischer_agent_2_x >= cur_b, And(next_fischer_agent_2_x == 0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(37, modeBitSize))),
    And(cur_g == cur_fischer_agent_2_i ,  cur_fischer_agent_2_x >= cur_b, And(next_fischer_agent_2_x == 0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(38, modeBitSize))),
    And(true, And(next_g == 2, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(43, modeBitSize))),
    And(true, And(next_fischer_agent_1_x == 0, next_g == 1, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(70, modeBitSize))))
  )
  ,
  Implies(cur_mode == BitVecVal(44, modeBitSize), 
  Or(
    And(cur_g > cur_fischer_agent_2_i, And(next_fischer_agent_2_x == 0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(37, modeBitSize))),
    And(cur_g < cur_fischer_agent_2_i, And(next_fischer_agent_2_x == 0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(37, modeBitSize))),
    And(cur_g == cur_fischer_agent_2_i, And(next_fischer_agent_2_x == 0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(36, modeBitSize))),
    And(true, And(next_g == 2, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(44, modeBitSize))),
    And(true, And(next_fischer_agent_1_x == 0, next_g == 1, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(71, modeBitSize))))
  )
  ,
  Implies(cur_mode == BitVecVal(45, modeBitSize), 
  Or(
    And(true, And(next_fischer_agent_1_x == 0, next_v == 1, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(72, modeBitSize))),
    And(cur_g == 0, And(next_fischer_agent_2_x == 0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(51, modeBitSize))),
    And(true, And(next_g == 2, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(45, modeBitSize))))
  )
  ,
  Implies(cur_mode == BitVecVal(46, modeBitSize), 
  Or(
    And(true, And(next_fischer_agent_1_x == 0, next_v == 1, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(73, modeBitSize))),
    And(cur_g == 0, And(next_fischer_agent_2_x == 0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(49, modeBitSize))),
    And(true, And(next_g == 2, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(46, modeBitSize))))
  )
  ,
  Implies(cur_mode == BitVecVal(47, modeBitSize), 
  Or(
    And(true, And(next_fischer_agent_1_x == 0, next_v == 1, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(74, modeBitSize))),
    And(cur_v == 0, And(next_fischer_agent_2_x == 0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(50, modeBitSize))),
    And(cur_v == 1, And(next_fischer_agent_2_x == 0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(46, modeBitSize))),
    And(true, And(next_g == 2, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(47, modeBitSize))))
  )
  ,
  Implies(cur_mode == BitVecVal(48, modeBitSize), 
  Or(
    And(true, And(next_fischer_agent_1_x == 0, next_v == 1, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(75, modeBitSize))),
    And(true, And(next_g == 2, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(48, modeBitSize))))
  )
  ,
  Implies(cur_mode == BitVecVal(49, modeBitSize), 
  Or(
    And(true, And(next_fischer_agent_1_x == 0, next_v == 1, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(76, modeBitSize))),
    And(true, And(next_fischer_agent_2_x == 0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(52, modeBitSize))),
    And(true, And(next_g == 2, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(49, modeBitSize))))
  )
  ,
  Implies(cur_mode == BitVecVal(50, modeBitSize), 
  Or(
    And(true, And(next_fischer_agent_1_x == 0, next_v == 1, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(77, modeBitSize))),
    And(true, And(next_fischer_agent_2_x == 0, next_v == 1, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(53, modeBitSize))),
    And(true, And(next_g == 2, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(50, modeBitSize))))
  )
  ,
  Implies(cur_mode == BitVecVal(51, modeBitSize), 
  Or(
    And(true, And(next_fischer_agent_1_x == 0, next_v == 1, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(78, modeBitSize))),
    And(cur_fischer_agent_2_x >= cur_b, And(next_fischer_agent_2_x == 0, next_v == 0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(48, modeBitSize))),
    And(true, And(next_g == 2, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(51, modeBitSize))))
  )
  ,
  Implies(cur_mode == BitVecVal(52, modeBitSize), 
  Or(
    And(true, And(next_fischer_agent_1_x == 0, next_v == 1, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(79, modeBitSize))),
    And(cur_g < cur_fischer_agent_2_i ,  cur_fischer_agent_2_x >= cur_b, And(next_fischer_agent_2_x == 0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(46, modeBitSize))),
    And(cur_g > cur_fischer_agent_2_i ,  cur_fischer_agent_2_x >= cur_b, And(next_fischer_agent_2_x == 0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(46, modeBitSize))),
    And(cur_g == cur_fischer_agent_2_i ,  cur_fischer_agent_2_x >= cur_b, And(next_fischer_agent_2_x == 0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(47, modeBitSize))),
    And(true, And(next_g == 2, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(52, modeBitSize))))
  )
  ,
  Implies(cur_mode == BitVecVal(53, modeBitSize), 
  Or(
    And(true, And(next_fischer_agent_1_x == 0, next_v == 1, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(80, modeBitSize))),
    And(cur_g > cur_fischer_agent_2_i, And(next_fischer_agent_2_x == 0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(46, modeBitSize))),
    And(cur_g < cur_fischer_agent_2_i, And(next_fischer_agent_2_x == 0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(46, modeBitSize))),
    And(cur_g == cur_fischer_agent_2_i, And(next_fischer_agent_2_x == 0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(45, modeBitSize))),
    And(true, And(next_g == 2, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(53, modeBitSize))))
  )
  ,
  Implies(cur_mode == BitVecVal(54, modeBitSize), 
  Or(
    And(cur_fischer_agent_1_x >= cur_b, And(next_fischer_agent_1_x == 0, next_v == 0, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(27, modeBitSize))),
    And(cur_g == 0, And(next_fischer_agent_2_x == 0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(60, modeBitSize))),
    And(true, And(next_g == 2, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(54, modeBitSize))))
  )
  ,
  Implies(cur_mode == BitVecVal(55, modeBitSize), 
  Or(
    And(cur_fischer_agent_1_x >= cur_b, And(next_fischer_agent_1_x == 0, next_v == 0, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(28, modeBitSize))),
    And(cur_g == 0, And(next_fischer_agent_2_x == 0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(58, modeBitSize))),
    And(true, And(next_g == 2, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(55, modeBitSize))))
  )
  ,
  Implies(cur_mode == BitVecVal(56, modeBitSize), 
  Or(
    And(cur_fischer_agent_1_x >= cur_b, And(next_fischer_agent_1_x == 0, next_v == 0, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(29, modeBitSize))),
    And(cur_v == 0, And(next_fischer_agent_2_x == 0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(59, modeBitSize))),
    And(cur_v == 1, And(next_fischer_agent_2_x == 0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(55, modeBitSize))),
    And(true, And(next_g == 2, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(56, modeBitSize))))
  )
  ,
  Implies(cur_mode == BitVecVal(57, modeBitSize), 
  Or(
    And(cur_fischer_agent_1_x >= cur_b, And(next_fischer_agent_1_x == 0, next_v == 0, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(30, modeBitSize))),
    And(true, And(next_g == 2, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(57, modeBitSize))))
  )
  ,
  Implies(cur_mode == BitVecVal(58, modeBitSize), 
  Or(
    And(cur_fischer_agent_1_x >= cur_b, And(next_fischer_agent_1_x == 0, next_v == 0, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(31, modeBitSize))),
    And(true, And(next_fischer_agent_2_x == 0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(61, modeBitSize))),
    And(true, And(next_g == 2, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(58, modeBitSize))))
  )
  ,
  Implies(cur_mode == BitVecVal(59, modeBitSize), 
  Or(
    And(cur_fischer_agent_1_x >= cur_b, And(next_fischer_agent_1_x == 0, next_v == 0, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(32, modeBitSize))),
    And(true, And(next_fischer_agent_2_x == 0, next_v == 1, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(62, modeBitSize))),
    And(true, And(next_g == 2, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(59, modeBitSize))))
  )
  ,
  Implies(cur_mode == BitVecVal(60, modeBitSize), 
  Or(
    And(cur_fischer_agent_1_x >= cur_b, And(next_fischer_agent_1_x == 0, next_v == 0, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(33, modeBitSize))),
    And(cur_fischer_agent_2_x >= cur_b, And(next_fischer_agent_2_x == 0, next_v == 0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(57, modeBitSize))),
    And(true, And(next_g == 2, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(60, modeBitSize))))
  )
  ,
  Implies(cur_mode == BitVecVal(61, modeBitSize), 
  Or(
    And(cur_fischer_agent_1_x >= cur_b, And(next_fischer_agent_1_x == 0, next_v == 0, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(34, modeBitSize))),
    And(cur_g < cur_fischer_agent_2_i ,  cur_fischer_agent_2_x >= cur_b, And(next_fischer_agent_2_x == 0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(55, modeBitSize))),
    And(cur_g > cur_fischer_agent_2_i ,  cur_fischer_agent_2_x >= cur_b, And(next_fischer_agent_2_x == 0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(55, modeBitSize))),
    And(cur_g == cur_fischer_agent_2_i ,  cur_fischer_agent_2_x >= cur_b, And(next_fischer_agent_2_x == 0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(56, modeBitSize))),
    And(true, And(next_g == 2, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(61, modeBitSize))))
  )
  ,
  Implies(cur_mode == BitVecVal(62, modeBitSize), 
  Or(
    And(cur_fischer_agent_1_x >= cur_b, And(next_fischer_agent_1_x == 0, next_v == 0, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(35, modeBitSize))),
    And(cur_g > cur_fischer_agent_2_i, And(next_fischer_agent_2_x == 0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(55, modeBitSize))),
    And(cur_g < cur_fischer_agent_2_i, And(next_fischer_agent_2_x == 0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(55, modeBitSize))),
    And(cur_g == cur_fischer_agent_2_i, And(next_fischer_agent_2_x == 0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(54, modeBitSize))),
    And(true, And(next_g == 2, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(62, modeBitSize))))
  )
  ,
  Implies(cur_mode == BitVecVal(63, modeBitSize), 
  Or(
    And(cur_g < cur_fischer_agent_1_i ,  cur_fischer_agent_1_x >= cur_b, And(next_fischer_agent_1_x == 0, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(9, modeBitSize))),
    And(cur_g > cur_fischer_agent_1_i ,  cur_fischer_agent_1_x >= cur_b, And(next_fischer_agent_1_x == 0, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(9, modeBitSize))),
    And(cur_g == cur_fischer_agent_1_i ,  cur_fischer_agent_1_x >= cur_b, And(next_fischer_agent_1_x == 0, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(18, modeBitSize))),
    And(cur_g == 0, And(next_fischer_agent_2_x == 0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(69, modeBitSize))),
    And(true, And(next_g == 2, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(63, modeBitSize))))
  )
  ,
  Implies(cur_mode == BitVecVal(64, modeBitSize), 
  Or(
    And(cur_g < cur_fischer_agent_1_i ,  cur_fischer_agent_1_x >= cur_b, And(next_fischer_agent_1_x == 0, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(10, modeBitSize))),
    And(cur_g > cur_fischer_agent_1_i ,  cur_fischer_agent_1_x >= cur_b, And(next_fischer_agent_1_x == 0, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(10, modeBitSize))),
    And(cur_g == cur_fischer_agent_1_i ,  cur_fischer_agent_1_x >= cur_b, And(next_fischer_agent_1_x == 0, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(19, modeBitSize))),
    And(cur_g == 0, And(next_fischer_agent_2_x == 0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(67, modeBitSize))),
    And(true, And(next_g == 2, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(64, modeBitSize))))
  )
  ,
  Implies(cur_mode == BitVecVal(65, modeBitSize), 
  Or(
    And(cur_g < cur_fischer_agent_1_i ,  cur_fischer_agent_1_x >= cur_b, And(next_fischer_agent_1_x == 0, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(11, modeBitSize))),
    And(cur_g > cur_fischer_agent_1_i ,  cur_fischer_agent_1_x >= cur_b, And(next_fischer_agent_1_x == 0, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(11, modeBitSize))),
    And(cur_g == cur_fischer_agent_1_i ,  cur_fischer_agent_1_x >= cur_b, And(next_fischer_agent_1_x == 0, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(20, modeBitSize))),
    And(cur_v == 0, And(next_fischer_agent_2_x == 0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(68, modeBitSize))),
    And(cur_v == 1, And(next_fischer_agent_2_x == 0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(64, modeBitSize))),
    And(true, And(next_g == 2, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(65, modeBitSize))))
  )
  ,
  Implies(cur_mode == BitVecVal(66, modeBitSize), 
  Or(
    And(cur_g < cur_fischer_agent_1_i ,  cur_fischer_agent_1_x >= cur_b, And(next_fischer_agent_1_x == 0, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(12, modeBitSize))),
    And(cur_g > cur_fischer_agent_1_i ,  cur_fischer_agent_1_x >= cur_b, And(next_fischer_agent_1_x == 0, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(12, modeBitSize))),
    And(cur_g == cur_fischer_agent_1_i ,  cur_fischer_agent_1_x >= cur_b, And(next_fischer_agent_1_x == 0, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(21, modeBitSize))),
    And(true, And(next_g == 2, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(66, modeBitSize))))
  )
  ,
  Implies(cur_mode == BitVecVal(67, modeBitSize), 
  Or(
    And(cur_g < cur_fischer_agent_1_i ,  cur_fischer_agent_1_x >= cur_b, And(next_fischer_agent_1_x == 0, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(13, modeBitSize))),
    And(cur_g > cur_fischer_agent_1_i ,  cur_fischer_agent_1_x >= cur_b, And(next_fischer_agent_1_x == 0, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(13, modeBitSize))),
    And(cur_g == cur_fischer_agent_1_i ,  cur_fischer_agent_1_x >= cur_b, And(next_fischer_agent_1_x == 0, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(22, modeBitSize))),
    And(true, And(next_fischer_agent_2_x == 0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(70, modeBitSize))),
    And(true, And(next_g == 2, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(67, modeBitSize))))
  )
  ,
  Implies(cur_mode == BitVecVal(68, modeBitSize), 
  Or(
    And(cur_g < cur_fischer_agent_1_i ,  cur_fischer_agent_1_x >= cur_b, And(next_fischer_agent_1_x == 0, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(14, modeBitSize))),
    And(cur_g > cur_fischer_agent_1_i ,  cur_fischer_agent_1_x >= cur_b, And(next_fischer_agent_1_x == 0, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(14, modeBitSize))),
    And(cur_g == cur_fischer_agent_1_i ,  cur_fischer_agent_1_x >= cur_b, And(next_fischer_agent_1_x == 0, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(23, modeBitSize))),
    And(true, And(next_fischer_agent_2_x == 0, next_v == 1, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(71, modeBitSize))),
    And(true, And(next_g == 2, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(68, modeBitSize))))
  )
  ,
  Implies(cur_mode == BitVecVal(69, modeBitSize), 
  Or(
    And(cur_g < cur_fischer_agent_1_i ,  cur_fischer_agent_1_x >= cur_b, And(next_fischer_agent_1_x == 0, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(15, modeBitSize))),
    And(cur_g > cur_fischer_agent_1_i ,  cur_fischer_agent_1_x >= cur_b, And(next_fischer_agent_1_x == 0, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(15, modeBitSize))),
    And(cur_g == cur_fischer_agent_1_i ,  cur_fischer_agent_1_x >= cur_b, And(next_fischer_agent_1_x == 0, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(24, modeBitSize))),
    And(cur_fischer_agent_2_x >= cur_b, And(next_fischer_agent_2_x == 0, next_v == 0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(66, modeBitSize))),
    And(true, And(next_g == 2, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(69, modeBitSize))))
  )
  ,
  Implies(cur_mode == BitVecVal(70, modeBitSize), 
  Or(
    And(cur_g < cur_fischer_agent_1_i ,  cur_fischer_agent_1_x >= cur_b, And(next_fischer_agent_1_x == 0, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(16, modeBitSize))),
    And(cur_g > cur_fischer_agent_1_i ,  cur_fischer_agent_1_x >= cur_b, And(next_fischer_agent_1_x == 0, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(16, modeBitSize))),
    And(cur_g == cur_fischer_agent_1_i ,  cur_fischer_agent_1_x >= cur_b, And(next_fischer_agent_1_x == 0, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(25, modeBitSize))),
    And(cur_g < cur_fischer_agent_2_i ,  cur_fischer_agent_2_x >= cur_b, And(next_fischer_agent_2_x == 0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(64, modeBitSize))),
    And(cur_g > cur_fischer_agent_2_i ,  cur_fischer_agent_2_x >= cur_b, And(next_fischer_agent_2_x == 0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(64, modeBitSize))),
    And(cur_g == cur_fischer_agent_2_i ,  cur_fischer_agent_2_x >= cur_b, And(next_fischer_agent_2_x == 0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(65, modeBitSize))),
    And(true, And(next_g == 2, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(70, modeBitSize))))
  )
  ,
  Implies(cur_mode == BitVecVal(71, modeBitSize), 
  Or(
    And(cur_g < cur_fischer_agent_1_i ,  cur_fischer_agent_1_x >= cur_b, And(next_fischer_agent_1_x == 0, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(17, modeBitSize))),
    And(cur_g > cur_fischer_agent_1_i ,  cur_fischer_agent_1_x >= cur_b, And(next_fischer_agent_1_x == 0, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(17, modeBitSize))),
    And(cur_g == cur_fischer_agent_1_i ,  cur_fischer_agent_1_x >= cur_b, And(next_fischer_agent_1_x == 0, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(26, modeBitSize))),
    And(cur_g > cur_fischer_agent_2_i, And(next_fischer_agent_2_x == 0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(64, modeBitSize))),
    And(cur_g < cur_fischer_agent_2_i, And(next_fischer_agent_2_x == 0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(64, modeBitSize))),
    And(cur_g == cur_fischer_agent_2_i, And(next_fischer_agent_2_x == 0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(63, modeBitSize))),
    And(true, And(next_g == 2, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(71, modeBitSize))))
  )
  ,
  Implies(cur_mode == BitVecVal(72, modeBitSize), 
  Or(
    And(cur_g > cur_fischer_agent_1_i, And(next_fischer_agent_1_x == 0, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(9, modeBitSize))),
    And(cur_g < cur_fischer_agent_1_i, And(next_fischer_agent_1_x == 0, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(9, modeBitSize))),
    And(cur_g == cur_fischer_agent_1_i, And(next_fischer_agent_1_x == 0, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(0, modeBitSize))),
    And(cur_g == 0, And(next_fischer_agent_2_x == 0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(78, modeBitSize))),
    And(true, And(next_g == 2, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(72, modeBitSize))))
  )
  ,
  Implies(cur_mode == BitVecVal(73, modeBitSize), 
  Or(
    And(cur_g > cur_fischer_agent_1_i, And(next_fischer_agent_1_x == 0, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(10, modeBitSize))),
    And(cur_g < cur_fischer_agent_1_i, And(next_fischer_agent_1_x == 0, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(10, modeBitSize))),
    And(cur_g == cur_fischer_agent_1_i, And(next_fischer_agent_1_x == 0, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(1, modeBitSize))),
    And(cur_g == 0, And(next_fischer_agent_2_x == 0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(76, modeBitSize))),
    And(true, And(next_g == 2, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(73, modeBitSize))))
  )
  ,
  Implies(cur_mode == BitVecVal(74, modeBitSize), 
  Or(
    And(cur_g > cur_fischer_agent_1_i, And(next_fischer_agent_1_x == 0, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(11, modeBitSize))),
    And(cur_g < cur_fischer_agent_1_i, And(next_fischer_agent_1_x == 0, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(11, modeBitSize))),
    And(cur_g == cur_fischer_agent_1_i, And(next_fischer_agent_1_x == 0, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(2, modeBitSize))),
    And(cur_v == 0, And(next_fischer_agent_2_x == 0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(77, modeBitSize))),
    And(cur_v == 1, And(next_fischer_agent_2_x == 0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(73, modeBitSize))),
    And(true, And(next_g == 2, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(74, modeBitSize))))
  )
  ,
  Implies(cur_mode == BitVecVal(75, modeBitSize), 
  Or(
    And(cur_g > cur_fischer_agent_1_i, And(next_fischer_agent_1_x == 0, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(12, modeBitSize))),
    And(cur_g < cur_fischer_agent_1_i, And(next_fischer_agent_1_x == 0, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(12, modeBitSize))),
    And(cur_g == cur_fischer_agent_1_i, And(next_fischer_agent_1_x == 0, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(3, modeBitSize))),
    And(true, And(next_g == 2, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(75, modeBitSize))))
  )
  ,
  Implies(cur_mode == BitVecVal(76, modeBitSize), 
  Or(
    And(cur_g > cur_fischer_agent_1_i, And(next_fischer_agent_1_x == 0, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(13, modeBitSize))),
    And(cur_g < cur_fischer_agent_1_i, And(next_fischer_agent_1_x == 0, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(13, modeBitSize))),
    And(cur_g == cur_fischer_agent_1_i, And(next_fischer_agent_1_x == 0, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(4, modeBitSize))),
    And(true, And(next_fischer_agent_2_x == 0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(79, modeBitSize))),
    And(true, And(next_g == 2, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(76, modeBitSize))))
  )
  ,
  Implies(cur_mode == BitVecVal(77, modeBitSize), 
  Or(
    And(cur_g > cur_fischer_agent_1_i, And(next_fischer_agent_1_x == 0, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(14, modeBitSize))),
    And(cur_g < cur_fischer_agent_1_i, And(next_fischer_agent_1_x == 0, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(14, modeBitSize))),
    And(cur_g == cur_fischer_agent_1_i, And(next_fischer_agent_1_x == 0, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(5, modeBitSize))),
    And(true, And(next_fischer_agent_2_x == 0, next_v == 1, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(80, modeBitSize))),
    And(true, And(next_g == 2, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(77, modeBitSize))))
  )
  ,
  Implies(cur_mode == BitVecVal(78, modeBitSize), 
  Or(
    And(cur_g > cur_fischer_agent_1_i, And(next_fischer_agent_1_x == 0, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(15, modeBitSize))),
    And(cur_g < cur_fischer_agent_1_i, And(next_fischer_agent_1_x == 0, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(15, modeBitSize))),
    And(cur_g == cur_fischer_agent_1_i, And(next_fischer_agent_1_x == 0, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(6, modeBitSize))),
    And(cur_fischer_agent_2_x >= cur_b, And(next_fischer_agent_2_x == 0, next_v == 0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(75, modeBitSize))),
    And(true, And(next_g == 2, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(78, modeBitSize))))
  )
  ,
  Implies(cur_mode == BitVecVal(79, modeBitSize), 
  Or(
    And(cur_g > cur_fischer_agent_1_i, And(next_fischer_agent_1_x == 0, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(16, modeBitSize))),
    And(cur_g < cur_fischer_agent_1_i, And(next_fischer_agent_1_x == 0, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(16, modeBitSize))),
    And(cur_g == cur_fischer_agent_1_i, And(next_fischer_agent_1_x == 0, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(7, modeBitSize))),
    And(cur_g < cur_fischer_agent_2_i ,  cur_fischer_agent_2_x >= cur_b, And(next_fischer_agent_2_x == 0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(73, modeBitSize))),
    And(cur_g > cur_fischer_agent_2_i ,  cur_fischer_agent_2_x >= cur_b, And(next_fischer_agent_2_x == 0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(73, modeBitSize))),
    And(cur_g == cur_fischer_agent_2_i ,  cur_fischer_agent_2_x >= cur_b, And(next_fischer_agent_2_x == 0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(74, modeBitSize))),
    And(true, And(next_g == 2, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(79, modeBitSize))))
  )
  ,
  Implies(cur_mode == BitVecVal(80, modeBitSize), 
  Or(
    And(cur_g > cur_fischer_agent_1_i, And(next_fischer_agent_1_x == 0, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(17, modeBitSize))),
    And(cur_g < cur_fischer_agent_1_i, And(next_fischer_agent_1_x == 0, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(17, modeBitSize))),
    And(cur_g == cur_fischer_agent_1_i, And(next_fischer_agent_1_x == 0, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(8, modeBitSize))),
    And(cur_g > cur_fischer_agent_2_i, And(next_fischer_agent_2_x == 0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(73, modeBitSize))),
    And(cur_g < cur_fischer_agent_2_i, And(next_fischer_agent_2_x == 0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(73, modeBitSize))),
    And(cur_g == cur_fischer_agent_2_i, And(next_fischer_agent_2_x == 0, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_g == cur_g, next_v == cur_v, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(72, modeBitSize))),
    And(true, And(next_g == 2, next_fischer_agent_1_x == cur_fischer_agent_1_x, next_fischer_agent_1_i == cur_fischer_agent_1_i, next_v == cur_v, next_fischer_agent_2_x == cur_fischer_agent_2_x, next_fischer_agent_2_i == cur_fischer_agent_2_i, next_t == cur_t, next_mode == BitVecVal(80, modeBitSize))))
  )
  )

  )

TransitionRelation = Or(Transitions, Trajectories)

#initial states
initStates = And(
  fischer_agent_1_x[0] == 0 ,  fischer_agent_1_i[0] == 1 ,  g[0] == 0 ,  cur_a == 1 ,  cur_b == 1 ,  cur_rate == 1 ,  fischer_agent_2_x[0] == 0 ,  fischer_agent_2_i[0] == 2 ,  v[0] == 0 ,  t[0] == 0, v_time[0] == 0, mode[0] == BitVecVal(10, modeBitSize)
  )

#bad states
badStates = []
for i in range(1, k+1): 
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
    cur_v == v[i],
    next_v == v[i+1],
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
    cur_v == v[i],
    next_v == v[i+1],
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
qbf_bmc_inner = Exists([cur_fischer_agent_1_x, next_fischer_agent_1_x, cur_fischer_agent_1_i, next_fischer_agent_1_i, cur_g, next_g, cur_v, next_v, cur_fischer_agent_2_x, next_fischer_agent_2_x, cur_fischer_agent_2_i, next_fischer_agent_2_i, cur_t, next_t, cur_mode, next_mode, time], inner)
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
    print "v: " + str(model[v[i]])
    print "fischer_agent_2_x: " + str(model[fischer_agent_2_x[i]])
    print "fischer_agent_2_i: " + str(model[fischer_agent_2_i[i]])
    print "t: " + str(model[t[i]])
