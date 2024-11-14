class ImageSearchApiError(Exception):
    def __init__(self, message: str = "Service is unavailable!"):
        self.message = message
        super().__init__(self.message)
