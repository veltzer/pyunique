# TOFIX

Findings from a code scan on 2026-10-04.

## High

- `src/pyunique/main.py:30-41` - `scan` runs the whole walk inside one LMDB write transaction and has no error handling: a broken symlink or unreadable file (`open` in `src/pyunique/digest.py:13`) or a non-UTF-8 filename (`encode` in `src/pyunique/archive.py:95`) raises, `end_write()` is never reached, and every digest computed so far is discarded; skip-and-log per-file errors (and/or commit periodically).

## Medium

- `src/pyunique/main.py:37` - cached digests are reused purely by path: a file whose content changed since the last scan keeps its stale digest, and running with a different `--digest` mixes algorithms in one DB because the algorithm is not stored; key the cache on (path, size, mtime) and record the algorithm in the DB.
- `src/pyunique/configs.py:26` - `choice_list=list(hashlib.algorithms_available)` offers `shake_128`/`shake_256`, whose `.digest()` requires a length argument, so `src/pyunique/digest.py:18` raises `TypeError` for them; filter variable-length algorithms out of the choice list (or pass a length).
- `pyproject.toml:15` - the description promises the tool "helps you get rid of duplicate files", but there is no duplicate-finding command (only `scan`, `clean_db`, `check_filenames`; see `doc/TODO.txt:5` "do the dup command"); implement it or describe what the tool actually does.
- `pyproject.toml:87` and `pyproject.toml:90` - mypy `ignore_missing_imports` for `lmdb.*` and `tqdm.*` is stale: `lmdb` ships `py.typed` and `types-tqdm` is already in the dev group (`pyproject.toml:105`); remove the two entries.
- `rsconstruct.toml:28` and `rsconstruct.toml:32` - `ruff` and `mypy` list `config` in `src_dirs`, but `config/` holds only `.lua` files; drop `config`.

## Low

- `src/pyunique/__init__.py:5` - `LOGGER_NAME` is duplicated by the generated `src/pyunique/static.py:5`; have `src/pyunique/utils.py:8` import it from `pyunique.static` and drop the copy in `__init__.py`.
- `doc/TODO.txt:1` - "add a "diff" command to show the diff in multiple repositories" has nothing to do with this tool (copied from a multi-repo project); delete it.
- `pyproject.toml:80` - `mypy_path = "src:python:scripts"` names `python/` and `scripts/`, which do not exist; reduce it to `src`.
