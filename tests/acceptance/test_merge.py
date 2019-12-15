import io

from approvaltests.approvals import verify

from asciicast.stream import AsciicastStream


def test_merge_two_streams():
    string_stream1 = io.StringIO(
        """{"version": 2, "width": 1, "height": 2}
            [1, "o", "x"]
            [2, "i", "y"]""")

    string_stream2 = io.StringIO(
        """{"version": 2, "width": 2, "height": 3}
            [0.1, "o", "a"]
            [1.2, "i", "b"]""")

    string_stream = io.StringIO()
    asciicast_stream = AsciicastStream(width=60, height=21, stream=string_stream)

    asciicast_stream.write_from_input_stream(string_stream1)
    asciicast_stream.write_from_input_stream(string_stream2)

    verify(string_stream.getvalue())
