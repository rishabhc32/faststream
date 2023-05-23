# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/005_Application_executors_export.ipynb.

# %% auto 0
__all__ = ['dummy']

# %% ../nbs/005_Application_executors_export.ipynb 1
from ._components.meta import export
from ._components.task_streaming import SequentialExecutor, DynamicTaskExecutor

__all__ = ["SequentialExecutor", "DynamicTaskExecutor"]

# %% ../nbs/005_Application_executors_export.ipynb 2
@export("_dummy")
def dummy() -> None:
    pass