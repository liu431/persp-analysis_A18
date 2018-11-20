import p3
import pytest
def test_operate():
    assert p3.operate(2,3,'+')==5
    assert p3.operate(2,3,'-')==-1
    assert p3.operate(2,3,'*')==6
    assert p3.operate(2,3,'/')==2/3
    with pytest.raises(ZeroDivisionError) as err:
        p3.operate(2,0,'/')
    assert err.value.args[0]=="division by zero is undefined"

    with pytest.raises(TypeError) as err2:
        p3.operate(2,0,0)
    assert err2.value.args[0]=="oper must be a string"

    with pytest.raises(ValueError) as err3:
        p3.operate(2,0,'>')
    assert err3.value.args[0]=="oper must be one of '+', '/', '-', or '*'"




