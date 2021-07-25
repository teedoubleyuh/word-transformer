import wordTransformer
import pytest

def test_wrong_size_dictionary_removal():
    dictionary = ['sta', 'slackkkkk', '', 'black', 'blank', 'bland', 'brand', 'braid']
    start = 'smart'
    goal = 'brain'
    dictionary = wordTransformer.__clean_dictionary(dictionary, start, goal)
    # The original dictionary is 8, so we expect the incorrectly sized words to be removed leaving 5
    # however start and goal are added so the count is 7
    assert len(dictionary) == 7

def test_duplicate_dictionary_removal():
    dictionary = ['start', 'start', 'start', 'slack', 'slack', 'black', 'blank', 'bland', 'brand', 'braid']
    start = 'smart'
    goal = 'brain'
    dictionary = wordTransformer.__clean_dictionary(dictionary, start, goal)
    # The original dictionary is 10, so we expect the duplicate to be removed leaving 7
    # however start and goal are added so the count is 9
    assert len(dictionary) == 9

@pytest.mark.parametrize('func', [wordTransformer.BFS_Parallel, wordTransformer.BFS_Iterative])
def test_happy_path(func):
    dictionary = ['start', 'stack', 'stark', 'slack', 'black', 'blank', 'bland', 'brand', 'braid']
    start = 'smart'
    goal = 'brain'
    result = func(dictionary, start, goal)
    assert len(result) == 11
    assert result[0] == start
    assert result[-1] == goal
    #Try it backwards
    result = func(dictionary, goal, start)
    assert len(result) == 11
    assert result[0] == goal
    assert result[-1] == start

@pytest.mark.parametrize('func', [wordTransformer.BFS_Parallel, wordTransformer.BFS_Iterative])
def test_start_equals_goal(func):
    dictionary = ['start', 'stack', 'stark', 'slack', 'black', 'blank', 'bland', 'brand', 'braid']
    start = 'smart'
    goal = 'smart'
    result = func(dictionary, start, goal)
    assert len(result) == 2
    assert result[0] == start
    assert result[-1] == goal

@pytest.mark.parametrize('func', [wordTransformer.BFS_Parallel, wordTransformer.BFS_Iterative])
def test_no_solution(func):
    dictionary = ['start', 'stack', 'slack', 'black', 'blank', 'bland', 'brand', 'braid']
    start = 'smart'
    goal = 'brain'
    result = func(dictionary, start, goal)
    assert result is None

@pytest.mark.parametrize('func', [wordTransformer.BFS_Parallel, wordTransformer.BFS_Iterative])
def test_no_connections(func):
    dictionary = ['fghij', 'klmnop']
    start = 'abcde'
    goal = 'vwxyz'
    result = func(dictionary, start, goal)
    assert result is None

@pytest.mark.parametrize('func', [wordTransformer.BFS_Parallel, wordTransformer.BFS_Iterative])
def test_loops_and_dead_ends(func):
    dictionary = ['awxyz', 'abcdz','abxyz', 'amxyz', 'amrrr', 'abcyz', 'amcyz', 'amcii', 'atxyz', 'atcyz', 'atdyz']
    start = 'vwxyz'
    goal = 'abcde'
    result = func(dictionary, start, goal)
    assert len(result) == 6
    assert result[0] == start
    assert result[-1] == goal
    #Try it backwards
    result = func(dictionary, goal, start)
    assert len(result) == 6
    assert result[0] == goal
    assert result[-1] == start

@pytest.mark.parametrize('func', [wordTransformer.BFS_Parallel, wordTransformer.BFS_Iterative])
def test_run_twice(func):
    dictionary = ['start', 'stack', 'stark', 'slack', 'black', 'blank', 'bland', 'brand', 'braid']
    start = 'smart'
    goal = 'brain'
    result = func(dictionary, start, goal)
    assert len(result) == 11
    assert result[0] == start
    assert result[-1] == goal
    result = func(dictionary, start, goal)
    assert len(result) == 11
    assert result[0] == start
    assert result[-1] == goal

@pytest.mark.parametrize('func', [wordTransformer.BFS_Parallel, wordTransformer.BFS_Iterative])
def test_goal_wrong_size(func):
    dictionary = ['start', 'stack', 'stark', 'slack', 'black', 'blank', 'bland', 'brand', 'braid']
    start = 'smart'
    goal = 'brains'
    result = func(dictionary, start, goal)
    assert result == None
    goal = 'brai'
    result = func(dictionary, start, goal)
    assert result == None

@pytest.mark.parametrize('func', [wordTransformer.BFS_Parallel, wordTransformer.BFS_Iterative])
def test_start_wrong_size(func):
    dictionary = ['start', 'stack', 'stark', 'slack', 'black', 'blank', 'bland', 'brand', 'braid']
    start = 'smarts'
    goal = 'brain'
    result = func(dictionary, start, goal)
    assert result == None
    start = 'smar'
    result = func(dictionary, start, goal)
    assert result == None

@pytest.mark.parametrize('func', [wordTransformer.BFS_Parallel, wordTransformer.BFS_Iterative])
def test_dictionary_capitals(func):
    dictionary = ['START', 'STACK', 'stark', 'slack', 'black', 'blank', 'bland', 'brand', 'braid']
    start = 'smart'
    goal = 'brain'
    result = func(dictionary, start, goal)
    assert len(result) == 11
    assert result[0] == start
    assert result[-1] == goal

@pytest.mark.parametrize('func', [wordTransformer.BFS_Parallel, wordTransformer.BFS_Iterative])
def test_start_capitals(func):
    dictionary = ['start', 'stack', 'stark', 'slack', 'black', 'blank', 'bland', 'brand', 'braid']
    start = 'SMART'
    goal = 'brain'
    result = func(dictionary, start, goal)
    assert len(result) == 11
    assert result[0] == 'smart'
    assert result[-1] == goal

@pytest.mark.parametrize('func', [wordTransformer.BFS_Parallel, wordTransformer.BFS_Iterative])
def test_goal_capitals(func):
    dictionary = ['start', 'stack', 'stark', 'slack', 'black', 'blank', 'bland', 'brand', 'braid']
    start = 'smart'
    goal = 'BRAIN'
    result = func(dictionary, start, goal)
    assert len(result) == 11
    assert result[0] == start
    assert result[-1] == 'brain'

@pytest.mark.parametrize('func', [wordTransformer.BFS_Parallel, wordTransformer.BFS_Iterative])
def test_dictionary_empty(func):
    dictionary = []
    start = 'smart'
    goal = 'brain'
    result = func(dictionary, start, goal)
    assert result == None