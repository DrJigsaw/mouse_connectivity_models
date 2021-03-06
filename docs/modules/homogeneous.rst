.. _homogeneous:

.. currentmodule:: mcmodels.models

==============================================
:class:`HomogeneousModel` similar to [Oh2014]_
==============================================

The homogeneous model we implement is similar to [Oh2014]_, and is a linear
connectivity model via constrained optimization and linear regression of the form:

.. math::
        \underset{w_{x, y} \geq 0 }{\text{min}} \sum_{i=1}^{|S_E|}
        \sqrt{( \sum_{x \in S_x} w_{x, y} PV(x \cap E_i) - PV(y) )^2}

that best fits the data given by the injections in the set :math:`S_E`.

This is perhaps more clearly represented as a :ref:`nonnegative least squares
regression problem <nonnegative_linear>`:

.. math::
        \underset{x}{\text{argmin}} \| Ax - b \|_2^2, \quad \text{subject to} \quad x \geq 0

This model seeks set of positive linear weight coefficients :math:`w_{x,y}` that
minimize the :term:`L2` prediction error. Because many injections overlap several regions,
the model attempts to assign credit to each of the source regions by relying on
multiple non-overlapping injections.


Assumptions
-----------
- :term:`Homogeneity`: two injections of identical volume into region X result in the
  same fluorescence in a target region, irrespective of the exact position of
  the injection within the source area
- :term:`Additivity`: the fluorescence observed in a target region can be explained by
  a linear sum of appropriately weighted sources.


Region selection criteria
-------------------------

This model only fits a connectivity matrix over a subset of the 292
:term:`summary structures`. First, a region is only included if for at least
one injection experiment the injection infected at least 50 voxels in the region.
Additionally, since the injection matrix :math:`x` is poorly conditioned using
all of the remaining regions, regions were heuristically removed one-by-one to
reduce the condition number :math:`\kappa` to a predefined threshold of 1000.

Conditioning
~~~~~~~~~~~~

.. currentmodule:: mcmodels

The :term:`conditioning` algorithm is implemented in
:func:`models.homogeneous.backward_subset_selection_conditioning`,
and utilizes a :term:`singular value decomposition`
based technique to remove a set of columns that heuristically decreases the
:term:`condition number`.


.. topic:: References

        .. [Oh2014] "A mesoscale connectome of the mouse brain", Oh et al,
          Nature. 2014. https://www.nature.com/articles/nature13186
