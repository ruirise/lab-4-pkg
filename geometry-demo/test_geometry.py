from geometry import Shape, Circle, Square, area_stats
import pytest
def test_square_area_zero_and_positive():
    assert pytest.approx(Circle(0).area())==0
    assert pytest.approx(Square(0).area()) == 0 
    with pytest.raises(ValueError): 
        Circle(-1).area()
        Square(-1).area()
def test_stats_keys_and_values():
    temp = [Circle(4), Square(7), Square(8), Circle(3), Square(9), Square(4), Circle(1)]
    temp2 = area_stats(temp)
    assert len(temp2) == 5
    assert type(temp2) == dict
    sets = {"mean", "total", "n", "min", "max"}
    for i in temp2:
        assert i in sets
        assert type(temp2[i]) == float or type(temp2[i]) == int
        sets.remove(i)
def  test_stats_raises_without_shapes():
    with pytest.raises(ValueError):
        area_stats([])
