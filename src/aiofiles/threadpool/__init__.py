"""Handle files using a thread pool executor."""

import asyncio
import sys
from functools import partial, singledispatch
from io import (
    BufferedIOBase,
    BufferedRandom,
    BufferedReader,
    BufferedWriter,
    FileIO,
    TextIOBase,
)

from ..base import AiofilesContextManager
from .binary import (
    AsyncBufferedIOBase,
    AsyncBufferedReader,
    AsyncFileIO,
    AsyncIndirectBufferedIOBase,
)
from .text import AsyncTextIndirectIOWrapper, AsyncTextIOWrapper

sync_open = open

__all__ = (
    "open",
    "stdin",
    "stdout",
    "stderr",
    "stdin_bytes",
    "stdout_bytes",
    "stderr_bytes",
)


def open(
    file,
    mode="r",
    buffering=-1,
    encoding=None,
    errors=None,
    newline=None,
    closefd=True,
    opener=None,
    *,
    loop=None,
    executor=None,
):
    pass


async def _open(
    file,
    mode="r",
    buffering=-1,
    encoding=None,
    errors=None,
    newline=None,
    closefd=True,
    opener=None,
    *,
    loop=None,
    executor=None,
):
    """Open an asyncio file."""
    pass


@singledispatch
def wrap(file, *, loop=None, executor=None):
    pass


@wrap.register(TextIOBase)
def _(file, *, loop=None, executor=None):
    pass


@wrap.register(BufferedWriter)
@wrap.register(BufferedIOBase)
def _(file, *, loop=None, executor=None):
    pass


@wrap.register(BufferedReader)
@wrap.register(BufferedRandom)
def _(file, *, loop=None, executor=None):
    pass


@wrap.register(FileIO)
def _(file, *, loop=None, executor=None):
    pass


stdin = AsyncTextIndirectIOWrapper("sys.stdin", None, None, indirect=lambda: sys.stdin)
stdout = AsyncTextIndirectIOWrapper(
    "sys.stdout", None, None, indirect=lambda: sys.stdout
)
stderr = AsyncTextIndirectIOWrapper(
    "sys.stderr", None, None, indirect=lambda: sys.stderr
)
stdin_bytes = AsyncIndirectBufferedIOBase(
    "sys.stdin.buffer", None, None, indirect=lambda: sys.stdin.buffer
)
stdout_bytes = AsyncIndirectBufferedIOBase(
    "sys.stdout.buffer", None, None, indirect=lambda: sys.stdout.buffer
)
stderr_bytes = AsyncIndirectBufferedIOBase(
    "sys.stderr.buffer", None, None, indirect=lambda: sys.stderr.buffer
)
