"""
The :mod:`voxel_model.regressors.nonnegative_linear` module implements linear
models subject to the nonnegativity constraint. It includes Nonnegative linear
regression and Nonnegative linear regression with L2 (Ridge) regularization.
"""

# Authors: Joseph Knox <josephk@alleninstitute.org>
# License: BSD 3

from .base import nonnegative_regression, NonnegativeLinear
from .ridge import nonnegative_ridge_regression, NonnegativeRidge

__all__ = ['NonnegativeLinear',
           'NonnegativeRidge',
           'nonnegative_regression',
           'nonnegative_ridge_regression']
