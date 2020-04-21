from my_code import make_change

def test_make_change():
    assert make_change(.00, .00) == "No change returned."
    assert make_change(.01, .01) == "No change returned."
    assert make_change(.01, .02) == "Your change will be: 1 $.01"
    assert make_change(.00, .10) == "Your change will be: 1 $.10"
    assert make_change(.01, .10) == "Your change will be: 1 $.05, 4 $.01"
    assert make_change(60.00, 117.24) == "Your change will be: 2 $20, 1 $10, 1 $5, 2 $1, 2 $.10, 4 $.01"
    assert make_change(10.00, 118.23) == "Your change will be: 5 $20, 1 $5, 3 $1, 2 $.10, 3 $.01"
    assert make_change(.01, 35.42) == "Your change will be: 1 $20, 1 $10, 1 $5, 1 $.25, 1 $.10, 1 $.05, 1 $.01"