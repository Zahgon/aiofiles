import asyncio
import sys
from functools import partial, singledispatch
from io import BufferedRandom, BufferedReader, BufferedWriter, FileIO, TextIOBase
from tempfile import NamedTemporaryFile as syncNamedTemporaryFile
from tempfile import SpooledTemporaryFile as syncSpooledTemporaryFile
from tempfile import TemporaryDirectory as syncTemporaryDirectory
from tempfile import TemporaryFile as syncTemporaryFile
from tempfile import _TemporaryFileWrapper as syncTemporaryFileWrapper

from ..base import AiofilesContextManager
from ..threadpool.binary import AsyncBufferedIOBase, AsyncBufferedReader, AsyncFileIO
from ..threadpool.text import AsyncTextIOWrapper
from .temptypes import AsyncSpooledTemporaryFile, AsyncTemporaryDirectory

__all__ = [
    "NamedTemporaryFile",
    "TemporaryFile",
    "SpooledTemporaryFile",
    "TemporaryDirectory",
]


# ================================================================
# Public methods for async open and return of temp file/directory
# objects with async interface
# ================================================================
if sys.version_info >= (3, 12):

    def NamedTemporaryFile(
        mode="w+b",
        buffering=-1,
        encoding=None,
        newline=None,
        suffix=None,
        prefix=None,
        dir=None,
        delete=True,
        delete_on_close=True,
        loop=None,
        executor=None,
    ):
        """Async open a named temporary file"""
        pass

else:

    def NamedTemporaryFile(
        mode="w+b",
        buffering=-1,
        encoding=None,
        newline=None,
        suffix=None,
        prefix=None,
        dir=None,
        delete=True,
        loop=None,
        executor=None,
    ):
        """Async open a named temporary file"""
        pass


def TemporaryFile(
    mode="w+b",
    buffering=-1,
    encoding=None,
    newline=None,
    suffix=None,
    prefix=None,
    dir=None,
    loop=None,
    executor=None,
):
    """Async open an unnamed temporary file"""
    pass


def SpooledTemporaryFile(
    max_size=0,
    mode="w+b",
    buffering=-1,
    encoding=None,
    newline=None,
    suffix=None,
    prefix=None,
    dir=None,
    loop=None,
    executor=None,
):
    """Async open a spooled temporary file"""
    pass


def TemporaryDirectory(suffix=None, prefix=None, dir=None, loop=None, executor=None):
    """Async open a temporary directory"""
    pass


# =========================================================
# Internal coroutines to open new temp files/directories
# =========================================================
if sys.version_info >= (3, 12):

    async def _temporary_file(
        named=True,
        mode="w+b",
        buffering=-1,
        encoding=None,
        newline=None,
        suffix=None,
        prefix=None,
        dir=None,
        delete=True,
        delete_on_close=True,
        loop=None,
        executor=None,
        max_size=0,
    ):
        """Async method to open a temporary file with async interface"""
        pass

else:

    async def _temporary_file(
        named=True,
        mode="w+b",
        buffering=-1,
        encoding=None,
        newline=None,
        suffix=None,
        prefix=None,
        dir=None,
        delete=True,
        loop=None,
        executor=None,
        max_size=0,
    ):
        """Async method to open a temporary file with async interface"""
        pass


async def _spooled_temporary_file(
    max_size=0,
    mode="w+b",
    buffering=-1,
    encoding=None,
    newline=None,
    suffix=None,
    prefix=None,
    dir=None,
    loop=None,
    executor=None,
):
    """Open a spooled temporary file with async interface"""
    pass


async def _temporary_directory(
    suffix=None, prefix=None, dir=None, loop=None, executor=None
):
    """Async method to open a temporary directory with async interface"""
    pass


class AiofilesContextManagerTempDir(AiofilesContextManager):
    """With returns the directory location, not the object (matching sync lib)"""

    async def __aenter__(self):
        self._obj = await self._coro
        return self._obj.name


@singledispatch
def wrap(base_io_obj, file, *, loop=None, executor=None):
    """Wrap the object with interface based on type of underlying IO"""
    pass


@wrap.register(TextIOBase)
def _(base_io_obj, file, *, loop=None, executor=None):
    pass


@wrap.register(BufferedWriter)
def _(base_io_obj, file, *, loop=None, executor=None):
    pass


@wrap.register(BufferedReader)
@wrap.register(BufferedRandom)
def _(base_io_obj, file, *, loop=None, executor=None):
    pass


@wrap.register(FileIO)
def _(base_io_obj, file, *, loop=None, executor=None):
    pass
