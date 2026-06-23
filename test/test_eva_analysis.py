import pytest
from eva_data_analysis import text_to_duration

def test_text_to_duration_integer():
    input_value = "10:00"
    #test_result = text_to_duration(input_value) == 10    
    #print(f"text_to_duration('{input_value}') == 10 ? {test_result}")

    assert text_to_duration(input_value) == 10

def test_text_to_duration_float():
       """Test that function returns expected ground truth values witha non-zero minute value"""
       # assert text_to_duration("10:20") == 10.333333333333
       # assert abs(text_to_duration("10:20") - 10.333333333333) <1e-5
       assert text_to_duration("10:20") == pytest.approx(10.33333333, rel=1e-5)
