import subprocess
import tempfile
import os
import sqlite3


TOOL_NAME = "inspect2hgdb"


def test_line_info():
    with tempfile.TemporaryDirectory() as temp:
        output_db = os.path.join(temp, "debug.db")
        subprocess.check_call([TOOL_NAME, output_db])

        with sqlite3.connect(output_db) as conn:
            c = conn.cursor()
            c.execute("SELECT filename, line_num, condition FROM breakpoint")
            res = c.fetchall()
            assert len(res) > 10
            filename, line, condition = res[0]
            assert filename == "/legup/examples/debug/qsort/qsort_labeled.c"
            assert line == 11
            for i in range(1, 6):
                cond_str = f"cur_state == {i}"
                assert cond_str in condition


if __name__ == "__main__":
    test_line_info()
