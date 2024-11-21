class errorhandler(Exception):
    def __init__(self, errors):
        self.errors = errors
        super().__init__(self._format_message)

    def _format_message(self):
        return f"A error occurred:\n" + "\n".join(f"    {error}" for error in self.errors)
    
    def __str__(self) -> str:
        return self._format_message()