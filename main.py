import kss
import uvicorn
from fastapi import FastAPI

from models import SPLIT_CHUNKS, SPLIT_SENTENCES, Response

server = FastAPI(
    title="KSS over API",
    description="KSS(A Toolkit for Korean sentence segmentation) over RESTFul API",
    version="0.1.0",
    debug=False,
)


@server.post("/api/v1/kss/split_sentences", response_model=Response)
async def split_sentences(sentence: SPLIT_SENTENCES):
    """Split document to sentences"""
    return {
        "sentences": kss.split_sentences(
            text=sentence.text,
            use_heuristic=sentence.use_heuristic,
            use_quotes_brackets_processing=sentence.use_quotes_brackets_processing,
            max_recover_step=sentence.max_recover_step,
            max_recover_length=sentence.max_recover_length,
            backend=sentence.backend,
            num_workers=sentence.num_workers,
            disable_gc=sentence.disable_gc,
        )
    }


@server.post("/api/v1/kss/split_chunks", response_model=Response)
async def split_chunks(sentence: SPLIT_CHUNKS):
    """Split chunks from input texts by max_length"""
    return {
        "sentences": kss.split_chunks(
            text=sentence.text,
            max_length=sentence.max_length,
            use_heuristic=sentence.use_heuristic,
            use_quotes_brackets_processing=sentence.use_quotes_brackets_processing,
            max_recover_step=sentence.max_recover_step,
            max_recover_length=sentence.max_recover_length,
            backend=sentence.backend,
            num_workers=sentence.num_workers,
            disable_gc=sentence.disable_gc,
        )
    }


if __name__ == "__main__":
    uvicorn.run(
        "main:server",
        host="127.0.0.1",
        port=20455,
    )
