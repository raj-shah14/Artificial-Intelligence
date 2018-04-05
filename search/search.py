# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

class Node(object):
    
    def __init__(self, state, action, cost, parent, accumulated, heuristic):
        self.state = state
        self.action = action
        self.cost = cost
        self.parent = parent
        self.accumulated = accumulated
        self.heuristic = heuristic

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    #print "Start:", problem.getStartState()
    #print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    #print "Start's successors:", problem.getSuccessors(problem.getStartState())
    
    fringe=util.Stack()				    #Initializing a Stack
    snode=[problem.getStartState(),None,0,None]	    #Start Node: [Start State,action,cost,parent]
    fringe.push(snode)				    #Pushing the content to fringe
    actions=[]
    visited=[]
    while not fringe.isEmpty():
	current=fringe.pop()
	#print current[0]
	if problem.isGoalState(current[0]):	    #Checking if Goal State is reached
		while current[3]!=None:
			actions.append(current[1])
			current=current[3]
		actions.reverse()		    #Since actions are saved from goal to source,we need to reverse.
		#print actions
		return actions
	if current[0] not in visited:
		visited.append(current[0])	    #Appending the node if not visited
		for child in problem.getSuccessors(current[0]):
			nnode=[child[0],child[1],child[2],current]
			fringe.push(nnode)	
    
    util.raiseNotDefined()
	
def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    fringe=util.Queue()				    #Initializing a Queue
    snode=[problem.getStartState(),None,0,None]    #Start Node: [Start State,action,cost,parent]
    fringe.push(snode)				    #Pushing the content to fringe
    actions=[]
    visited=[]
    while not fringe.isEmpty():
	current=fringe.pop()
	#print current[0]
	if problem.isGoalState(current[0]):	    #Checking if Goal State is reached
		while current[3]!=None:
			actions.append(current[1])
			current=current[3]
		actions.reverse()		    #Since actions are saved from goal to source,we need to reverse.
		#print actions
		return actions
	if current[0] not in visited:
		visited.append(current[0])	    #Appending the node if not visited
		for child in problem.getSuccessors(current[0]):
			nnode=[child[0],child[1],child[2],current]
			if child[0] not in visited:
				fringe.push(nnode)
    	
    
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    fringe=util.PriorityQueue()				    #Initializing a Priority Queue
    snode=[problem.getStartState(),None,0,None,0]	    #Start Node: [Start State,action,cost,parent,accumulated cost]
    fringe.push(snode,0)				    #Pushing the content to fringe
    actions=[]
    visited=[]
    while not fringe.isEmpty():
	current=fringe.pop()
	#print current	
	if problem.isGoalState(current[0]):	    #Checking if Goal State is reached
		while current[3]!=None:
			actions.append(current[1])
			current=current[3]
		actions.reverse()		    #Since actions are saved from goal to source,we need to reverse.
		#print actions
		return actions
	if current[0] not in visited:
		visited.append(current[0])	    #Appending the node if not visited
		for child in problem.getSuccessors(current[0]):
			nnode=[child[0],child[1],child[2],current,current[4]+child[2]]
			if child[0] not in visited:
				fringe.update(nnode,nnode[4])	
    	
    
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    fringe=util.PriorityQueue()				    #Initializing a Priority Queue
    snode=[problem.getStartState(),None,0,None,0]	    #Start Node: [Start State,action,cost,parent,accumulated cost]
    fringe.push(snode,0)				    #Pushing the content to fringe
    actions=[]
    visited=[]
    while not fringe.isEmpty():
	current=fringe.pop()
	#print current	
	if problem.isGoalState(current[0]):	    #Checking if Goal State is reached
		while current[3]!=None:
			actions.append(current[1])
			current=current[3]
		actions.reverse()		    #Since actions are saved from goal to source,we need to reverse.
		#print actions
		return actions
	if current[0] not in visited:
		visited.append(current[0])	    #Appending the node if not visited
		for child in problem.getSuccessors(current[0]):
			nnode=[child[0],child[1],child[2],current,current[4]+child[2],heuristic(child[0],problem)]
			if child[0] not in visited:
				fringe.update(nnode,nnode[4]+nnode[5])	

    
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
