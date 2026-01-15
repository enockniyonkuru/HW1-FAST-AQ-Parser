# write tests for parsers

from seqparser import (
        FastaParser,
        FastqParser)

import pytest


def test_freebie_parser_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True # things after the assert are true statements


def test_freebie_parser_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_FastaParser():
    """
    Write your unit test for your FastaParser class here. You should generate
    an instance of your FastaParser class and assert that it properly reads in
    the example Fasta File.

    Some example of "good" test cases might be handling edge cases, like Fasta
    files that are blank or corrupted in some way. Two example Fasta files are
    provided in /tests/bad.fa and /tests/empty.fa
    """
    # Test parsing a valid FASTA file
    parser = FastaParser("data/test.fa")
    records = list(parser)
    assert len(records) > 0, "FastaParser should return records"
    assert len(records[0]) == 2, "FASTA records should have 2 elements (header, sequence)"
    assert records[0][0] == "seq0", "First record header should be 'seq0'"
    assert len(records[0][1]) > 0, "Sequence should not be empty"
    
    # Test that blank file raises ValueError
    with pytest.raises(ValueError):
        parser = FastaParser("tests/blank.fa")
        list(parser)
    
    # Test that bad FASTA file with empty lines raises ValueError
    with pytest.raises(ValueError):
        parser = FastaParser("tests/bad.fa")
        list(parser)


def test_FastaFormat():
    """
    Test to make sure that a fasta file is being read in if a fastq file is
    read, the first item is None
    """
    parser = FastaParser("data/test.fa")
    for header, sequence in parser:
        # FASTA should only have header and sequence (2 elements)
        assert header is not None, "Header should not be None"
        assert sequence is not None, "Sequence should not be None"
        assert isinstance(header, str), "Header should be a string"
        assert isinstance(sequence, str), "Sequence should be a string"


def test_FastqParser():
    """
    Write your unit test for your FastqParser class here. You should generate
    an instance of your FastqParser class and assert that it properly reads 
    in the example Fastq File.
    """
    # Test parsing a valid FASTQ file
    parser = FastqParser("data/test.fq")
    records = list(parser)
    assert len(records) > 0, "FastqParser should return records"
    assert len(records[0]) == 3, "FASTQ records should have 3 elements (header, sequence, quality)"
    assert records[0][0] == "seq0", "First record header should be 'seq0'"
    assert len(records[0][1]) > 0, "Sequence should not be empty"
    assert len(records[0][2]) > 0, "Quality should not be empty"
    assert len(records[0][1]) == len(records[0][2]), "Sequence and quality should have same length"

def test_FastqFormat():
    """
    Test to make sure fastq file is being read in. If this is a fasta file, the
    first line is None
    """
    parser = FastqParser("data/test.fq")
    for header, sequence, quality in parser:
        # FASTQ should have header, sequence, and quality (3 elements)
        assert header is not None, "Header should not be None"
        assert sequence is not None, "Sequence should not be None"
        assert quality is not None, "Quality should not be None"
        assert isinstance(header, str), "Header should be a string"
        assert isinstance(sequence, str), "Sequence should be a string"
        assert isinstance(quality, str), "Quality should be a string"
        assert len(sequence) == len(quality), "Sequence and quality should have equal length"