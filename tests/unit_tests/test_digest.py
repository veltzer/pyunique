"""Behavioural tests for pyunique's pure helpers."""

import hashlib
import os
import tempfile
import unittest

from pyunique import digest, utils
from pyunique.configs import ConfigAlgo


class DigestTests(unittest.TestCase):
    def test_digest_file_bytes_matches_hashlib(self):
        data = b"hello pyunique\n" * 1000
        with tempfile.NamedTemporaryFile(delete=False) as fh:
            fh.write(data)
            name = fh.name
        try:
            got = digest.digest_file_bytes(name)
            want = hashlib.new(ConfigAlgo.digest, data).digest()
            self.assertEqual(got, want)
        finally:
            os.unlink(name)

    def test_digest_file_bytes_empty_file(self):
        with tempfile.NamedTemporaryFile(delete=False) as fh:
            name = fh.name
        try:
            got = digest.digest_file_bytes(name)
            want = hashlib.new(ConfigAlgo.digest, b"").digest()
            self.assertEqual(got, want)
        finally:
            os.unlink(name)

    def test_identical_content_same_digest(self):
        payload = os.urandom(200000)  # larger than the 65536 read block
        names = []
        try:
            for _ in range(2):
                with tempfile.NamedTemporaryFile(delete=False) as fh:
                    fh.write(payload)
                    names.append(fh.name)
            self.assertEqual(digest.digest_file_bytes(names[0]), digest.digest_file_bytes(names[1]))
        finally:
            for n in names:
                os.unlink(n)


class FileCountTests(unittest.TestCase):
    @staticmethod
    def _touch(path: str) -> None:
        with open(path, "w", encoding="utf-8"):
            pass

    def test_counts_files_recursively(self):
        with tempfile.TemporaryDirectory() as d:
            self._touch(os.path.join(d, "a"))
            sub = os.path.join(d, "sub")
            os.mkdir(sub)
            self._touch(os.path.join(sub, "b"))
            self._touch(os.path.join(sub, "c"))
            self.assertEqual(utils.get_number_of_files(d), 3)

    def test_empty_folder_is_zero(self):
        with tempfile.TemporaryDirectory() as d:
            self.assertEqual(utils.get_number_of_files(d), 0)
