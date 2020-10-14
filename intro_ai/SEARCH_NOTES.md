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