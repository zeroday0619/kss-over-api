from typing import List

from pydantic import BaseModel, Field


class Response(BaseModel):
    sentences: List[str]


class SPLIT_SENTENCES(BaseModel):
    text: str = Field(..., description="input texts")
    use_heuristic: bool = Field(True, description="use heuristic algorithms or not")
    use_quotes_brackets_processing: bool = Field(
        True, description="use quotes and brackets processing or not"
    )
    max_recover_step: int = Field(
        5, description="maximum step for quote and bracket misalignment recovering"
    )
    max_recover_length: int = Field(
        20000,
        description="maximum text length to recover when quote and bracket misaligned",
    )
    backend: str = Field(
        "pynori", description="max length of text to use morpheme feature"
    )
    num_workers: int = Field(
        -1,
        description="number of multiprocessing workers ('-1' means maximum processes)",
    )
    disable_gc: bool = Field(
        True, description="disable garbage collecting (It helps to improve speed)"
    )


class SPLIT_CHUNKS(BaseModel):
    text: str = Field(..., description="input texts")
    max_length: int = Field(..., description="max length of ecah chunk")
    overlap: bool = Field(False, description="whether allow duplicated sentence")
    use_heuristic: bool = Field(True, description="use heuristic algorithms or not")
    use_quotes_brackets_processing: bool = Field(
        True, description="use quotes and brackets processing or not"
    )
    max_recover_step: int = Field(
        5, description="maximum step for quote and bracket misalignment recovering"
    )
    max_recover_length: int = Field(
        20000,
        description="maximum text length to recover when quote and bracket misaligned",
    )
    backend: str = Field(
        "pynori", description="max length of text to use morpheme feature"
    )
    num_workers: int = Field(
        -1,
        description="number of multiprocessing workers ('-1' means maximum processes)",
    )
    disable_gc: bool = Field(
        True, description="disable garbage collecting (It helps to improve speed)"
    )
