- [Topics](#topics)
  - [Search](#search)
    - [Terminology](#terminology)
    - [Search Problems](#search-problems)
    - [Approach](#approach)
    - [Revised Approach](#revised-approach)
    - [Search Algorithms](#search-algorithms)
    - [Search Strategies](#search-strategies)
    - [Heuristic Functions](#heuristic-functions)
    - [Adverserial Search Problems](#adverserial-search-problems)
      - [Game](#game)
      - [Minimax Pseudocode](#minimax-pseudocode)
- [Projects](#projects)

# Topics

- Search

## Search

### Terminology

- __agent__: entity that perceives its environment and acts upon that environment
- __state__: a configuration of the agent and its environment
- __inital state__: the state in which the agent begins
- __actions__: choices that can be made in a state. 
    - __actions(s)__ returns the set of actions that can be executed in state _s_
- __transition model__: a description of what state returns from performing any applicable action in any state
    - __result(s,a)__ returns the state resulting from performing action _a_ in state _s_
- __state space__: the set of all states reachable from the inital state by any sequence of actions
- __goal test__: a way to determine whether a given state is a goal state
- __path cost__: numerical cost associated with a given path
- __solution__: a sequence of actions that leads from the initial state to a goal state
- __optimal solution__: a solution that has the lowest path cost among all solutions
- __node__: a data structure that keeps track of
    - a state
    - a parent (node that generated this node)
    - an action (action applied to parent to get node)
    - a path cost (from inital state to node)
- __Expanding a node__: to look at all of the neighbors of that node. Considering all possible actions that AI could take from the state that the node is representing and what nodes could it get to from there.
- __stack__: last-in first-out data type
- __depth-first search__: search algorithm that always expands the deepest node in the frontier
- __breadth-first search__: search algorithm that always expands the shallowest node in the frontier
- __queue__: first-in first-out data type
- __uninformed search__: search strategy that uses no problem-specific knowledge (DFS, BFS)
- __informed search__: search strategy that uses problem-specific knowledge to find solutions more efficiently
- __greedy best-first search__: search algorithm that expands the node that is closest to the goal, as estimated by a heuristic function __h(n)__
- __A * search__: search algorithm that expands node with lowest value of __g(n) + h(n)__
  - __g(n)__ = cost to reach node
  - __h(n)__ = estimated cost to goal
- __evaluation function__: function that estimates the expected utility of the game from a given state

### Search Problems

- initial state
- actions
- transition model
- goal test
- path cost function

### Approach

- Start with a frontier that contains the initial state
- Repeat:
    - If the frontier is empty, there nothing left to explore and there is no solution.
    - Else, remove a node from the frontier
    - If node contains goal state, return the solution.
    - Else, expand node, add resulting nodes to the frontier.

### Revised Approach

- Start with a frontier that contains the initial state
- Start with an empty explored set
- Repeat:
    - If the frontier is empty, there nothing left to explore and there is no solution.
    - Else, remove a node from the frontier
    - If node contains goal state, return the solution.
    - Add the node to the explored set
    - Else, expand node, add resulting nodes to the frontierif they aren't already in the frontier or the explored set

### Search Algorithms

- [Depth-First Search](#terminology)
- [Breath-First Search](#terminology)
- [Greedy Best-First Search](#terminology)
- [A * search](#terminology)
  - optimal if:
    - __h(n)__ is admissible (never overestimates the true cost), and
    - __h(n)__ is consistent (for every node _n_ and successor _n'_ with step cost _c, h(n) less or equal to h(n') + c_)
  - This algo uses quite a bit of memory, there are some other versions that use less memory.

### Search Strategies

- [Uninformed Search](#terminology)
- [Informed Search](#terminology)

### Heuristic Functions

- Manhattan distance heuristic

### Adverserial Search Problems

- Minimax Algorithm (Tic-Tac Toe example)
  - MAX (X player) aims to maximize score
  - MIN (O player) aims to minimize score
- Alpha-Beta Pruning (optimization of Minimax)
- Depth-Limited Minimax
  - Uses an [evaluation function](#terminology)


#### Game

- __S<sub>0</sub>__: initial state
- __Player(s)__: returns which player to mov in state _s_
- __Actions(s)__: returns legal moves in state _s_
- __Result(s, a)__: returns state after action _a_ taken in state _s_
- __Terminal(s)__: checks if state _s_ is a terminal state
- __Utility(s)__: final numerical value for terminal state _s_


#### Minimax Pseudocode

- Given a state _s_:
  - __MAX__ picks action _a_ in _actions(s)_ that produces the highest value of __Min-value(result(s,a))__
  - __MIN__ picks action _a_ in _actions(s) that produces the smallest value of __Max-value(result(s,a))__

- function __Max-value(state)__:
  - if _Terminal(state)_:
    - return _Utility(state)_
  - v = negative infinity
  - for _action_ in _actions(state)_:
    - v = max(v, min-value(result(state, action)))
  - return v

- function __Min-value(state)__:
  - if _Terminal(state)_:
    - return _Utility(state)_
  - v = infinity
  - for _action_ in _actions(state)_:
    - v = min(v, max-value(result(state, action)))
  - return v

# Projects

[Project 0](./project_0)
