import contextlib
import io
import os
import tempfile

import pytest

import translator
import machine


@pytest.mark.golden_test("golden/*.yml")
def test_whole_by_golden(golden):
    with tempfile.TemporaryDirectory() as tmpdirname:
        source = os.path.join(tmpdirname, "program.q")
        input_stream = os.path.join(tmpdirname, "input")
        target = os.path.join(tmpdirname, "compile")
        tick = os.path.join(tmpdirname, "tick.txt")

        with open(source, "w", encoding="utf-8") as file:
            file.write(golden["in_source"])
        with open(input_stream, "w", encoding="utf-8") as file:
            file.write(golden["in_input"])

        with contextlib.redirect_stdout(io.StringIO()) as stdout:
            translator.main(source, target)
            machine.main(target, tick, input_stream)
        with open(target, encoding="utf-8", mode="r") as file:
            code = file.read()
        assert code == golden.out["out_code"]
        assert stdout.getvalue() == str(golden.out["out_output"])
        os.remove(tmpdirname)
