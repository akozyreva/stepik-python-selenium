import pytest


@pytest.fixture(scope="class")
def prepare_faces():
    print("beginning of prepare_faces", "\n")
    yield
    print("end of prepare_faces", "\n")


@pytest.fixture()
def very_important_fixture():
    print("important fixture", "\n")


@pytest.fixture(autouse=True)
def print_smiling_faces():
    print("smiling faces", "\n")


class TestPrintSmilingFaces():
    def test_first_smiling_faces(self, prepare_faces, very_important_fixture):
        pass

    def test_second_smiling_faces(self, prepare_faces):
        pass