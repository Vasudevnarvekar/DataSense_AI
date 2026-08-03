"""
Base Tool

Abstract base class for all AI tools.
"""

from abc import ABC, abstractmethod


class BaseTool(ABC):

    @property
    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def execute(self, df, **kwargs):
        pass