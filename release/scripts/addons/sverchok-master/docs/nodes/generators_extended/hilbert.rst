Hilbert 2D
=======================

Functionality
-------------

Hilbert field generator. this is concept of dence flooding of space by continuous line, that achived with division and special knotting. Hilbert space can be only square, because of his nature.

Inputs
------

All inputs are not vectorized and they will accept single value.
There is two inputs:

- **level**
- **size**

Parameters
----------

All parameters can be given by the node or an external input.


+-------------+---------------+-------------+------------------------------------------+
| Param       |  Type         |   Default   |    Description                           |
+=============+===============+=============+==========================================+
| **level**   |  Int          |   2         |    level of division of hilbert square   |                   
+-------------+---------------+-------------+------------------------------------------+
| **size**    |  float        |   1.0       |    scale of hilbert mesh                 |           
+-------------+---------------+-------------+------------------------------------------+

Outputs
-------

**Vertices**, **Edges**.


Example of usage
----------------

.. image:: https://cloud.githubusercontent.com/assets/5783432/4380966/a5d73b7c-436f-11e4-89e0-5a4be8f130aa.png
  :alt: hilbert.PNG

Smooth labirynth
