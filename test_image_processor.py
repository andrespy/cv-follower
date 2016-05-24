import pytest

from image_processor import ImageProcessor


class TestImageProcessor:
    def test_init(self):
        """
        Just after instantiating the class, a matcher is not set and thus,
        an exception should be raised if matcher method was to be invoked.
        """

        processor = ImageProcessor()

        with pytest.raises(Exception):
            processor.matcher()

    def set_matcher_test(self):
        # assert that after setting a matcher it is available.
        pass
