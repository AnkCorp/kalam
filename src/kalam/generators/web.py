"""Web generator class."""

from kalam.generators import Generator


class WebGenerator(Generator):
    """Web Generator class."""

    def __init__(self: "WebGenerator", filename_with_path: str = "") -> None:
        """Initialize instace of WebGenerator."""
        super().__init__("web")
        self.config_questions.extend(
            [
                {
                    "question": "Base URL",
                    "property": "baseURL",
                    "default": "http://localhost:8080",
                },
                {
                    "question": "Langauge Code",
                    "property": "langaugeCode",
                    "default": "en-US",
                },
            ]
        )

        if filename_with_path != "":
            self.setup(filename_with_path)
