# write tests for transcribe functions

from seqparser import (
        transcribe,
        reverse_transcribe)


def test_freebie_transcribe_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True


def test_freebie_transcribe_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_transcribe():
    """
    Write your unit test for the transcribe function here.
    """
    # Test basic transcription: DNA to RNA (T -> U)
    assert transcribe("ATGC") == "AUGC"
    assert transcribe("TTT") == "UUU"
    assert transcribe("ATATATTAT") == "AUAUAUUAU"
    
    # Test lowercase input
    assert transcribe("atgc") == "AUGC"
    
    # Test reverse transcription parameter
    assert transcribe("ATGC", reverse=False) == "AUGC"
    assert transcribe("ATGC", reverse=True) == "CGUA"
    
    # Test empty string
    assert transcribe("") == ""
    
    # Test single character
    assert transcribe("T") == "U"
    assert transcribe("A") == "A"


def test_reverse_transcribe():
    """
    Write your unit test for the reverse transcribe function here.
    """
    # Test reverse transcription
    assert reverse_transcribe("ATGC") == "CGUA"
    assert reverse_transcribe("TTT") == "UUU"
    assert reverse_transcribe("ATATATTAT") == "UAUUAUAUA"
    
    # Test lowercase input
    assert reverse_transcribe("atgc") == "CGUA"
    
    # Test empty string
    assert reverse_transcribe("") == ""
    
    # Test single character
    assert reverse_transcribe("T") == "U"
    assert reverse_transcribe("A") == "A"
    
    # Test that it reverses the sequence
    original = "ATGCTAGC"
    result = reverse_transcribe(original)
    assert result == transcribe(original, reverse=True)