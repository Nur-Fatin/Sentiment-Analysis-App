"""
Package initializer for the sentiment analysis module.

This module imports and exposes the 'sentiment_analysis' submodule
to make it accessible when the package is imported.

__all__ defines the public interface of this package,
indicating that 'sentiment_analysis' is part of the package's API.
"""

from . import sentiment_analysis

__all__ = ["sentiment_analysis"]
