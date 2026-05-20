class BinanceAPIError(Exception):
    """Raised when the Binance API returns an error."""


class ValidationError(Exception):
    """Raised when user input validation fails."""


class ConfigurationError(Exception):
    """Raised when required configuration is missing or invalid."""
