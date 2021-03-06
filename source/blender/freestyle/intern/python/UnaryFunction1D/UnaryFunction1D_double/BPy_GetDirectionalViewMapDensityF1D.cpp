/*
 * ***** BEGIN GPL LICENSE BLOCK *****
 *
 * This program is free software; you can redistribute it and/or
 * modify it under the terms of the GNU General Public License
 * as published by the Free Software Foundation; either version 2
 * of the License, or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software Foundation,
 * Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
 *
 * ***** END GPL LICENSE BLOCK *****
 */

/** \file source/blender/freestyle/intern/python/UnaryFunction1D/UnaryFunction1D_double/BPy_GetDirectionalViewMapDensityF1D.cpp
 *  \ingroup freestyle
 */

#include "BPy_GetDirectionalViewMapDensityF1D.h"

#include "../../../stroke/AdvancedFunctions1D.h"
#include "../../BPy_Convert.h"
#include "../../BPy_IntegrationType.h"

#ifdef __cplusplus
extern "C" {
#endif

///////////////////////////////////////////////////////////////////////////////////////////

//------------------------INSTANCE METHODS ----------------------------------

static char GetDirectionalViewMapDensityF1D___doc__[] =
"Class hierarchy: :class:`freestyle.types.UnaryFunction1D` > :class:`freestyle.types.UnaryFunction1DDouble` "
"> :class:`GetDirectionalViewMapDensityF1D`\n"
"\n"
".. method:: __init__(orientation, level, integration_type=IntegrationType.MEAN, sampling=2.0)\n"
"\n"
"   Builds a GetDirectionalViewMapDensityF1D object.\n"
"\n"
"   :arg orientation: The number of the directional map we must work\n"
"      with.\n"
"   :type orientation: int\n"
"   :arg level: The level of the pyramid from which the pixel must be\n"
"      read.\n"
"   :type level: int\n"
"   :arg integration_type: The integration method used to compute a single value\n"
"      from a set of values.\n"
"   :type integration_type: :class:`freestyle.types.IntegrationType`\n"
"   :arg sampling: The resolution used to sample the chain: the\n"
"      corresponding 0D function is evaluated at each sample point and\n"
"      the result is obtained by combining the resulting values into a\n"
"      single one, following the method specified by integration_type.\n"
"   :type sampling: float\n"
"\n"
".. method:: __call__(inter)\n"
"\n"
"   Returns the density evaluated for an Interface1D in of the steerable\n"
"   viewmaps image.  The direction telling which Directional map to choose\n"
"   is explicitly specified by the user.  The density is evaluated for a\n"
"   set of points along the Interface1D (using the\n"
"   :class:`freestyle.functions.ReadSteerableViewMapPixelF0D` functor) and\n"
"   then integrated into a single value using a user-defined integration\n"
"   method.\n"
"\n"
"   :arg inter: An Interface1D object.\n"
"   :type inter: :class:`freestyle.types.Interface1D`\n"
"   :return: the density evaluated for an Interface1D in of the\n"
"      steerable viewmaps image.\n"
"   :rtype: float\n";

static int GetDirectionalViewMapDensityF1D___init__(BPy_GetDirectionalViewMapDensityF1D *self,
                                                    PyObject *args, PyObject *kwds)
{
	static const char *kwlist[] = {"orientation", "level", "integration_type", "sampling", NULL};
	PyObject *obj = 0;
	unsigned int u1, u2;
	float f = 2.0;

	if (!PyArg_ParseTupleAndKeywords(args, kwds, "II|O!f", (char **)kwlist, &u1, &u2, &IntegrationType_Type, &obj, &f))
		return -1;
	IntegrationType t = (obj) ? IntegrationType_from_BPy_IntegrationType(obj) : MEAN;
	self->py_uf1D_double.uf1D_double = new Functions1D::GetDirectionalViewMapDensityF1D(u1, u2, t, f);
	return 0;
}

/*-----------------------BPy_GetDirectionalViewMapDensityF1D type definition ------------------------------*/

PyTypeObject GetDirectionalViewMapDensityF1D_Type = {
	PyVarObject_HEAD_INIT(NULL, 0)
	"GetDirectionalViewMapDensityF1D", /* tp_name */
	sizeof(BPy_GetDirectionalViewMapDensityF1D), /* tp_basicsize */
	0,                              /* tp_itemsize */
	0,                              /* tp_dealloc */
	0,                              /* tp_print */
	0,                              /* tp_getattr */
	0,                              /* tp_setattr */
	0,                              /* tp_reserved */
	0,                              /* tp_repr */
	0,                              /* tp_as_number */
	0,                              /* tp_as_sequence */
	0,                              /* tp_as_mapping */
	0,                              /* tp_hash  */
	0,                              /* tp_call */
	0,                              /* tp_str */
	0,                              /* tp_getattro */
	0,                              /* tp_setattro */
	0,                              /* tp_as_buffer */
	Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE, /* tp_flags */
	GetDirectionalViewMapDensityF1D___doc__, /* tp_doc */
	0,                              /* tp_traverse */
	0,                              /* tp_clear */
	0,                              /* tp_richcompare */
	0,                              /* tp_weaklistoffset */
	0,                              /* tp_iter */
	0,                              /* tp_iternext */
	0,                              /* tp_methods */
	0,                              /* tp_members */
	0,                              /* tp_getset */
	&UnaryFunction1DDouble_Type,    /* tp_base */
	0,                              /* tp_dict */
	0,                              /* tp_descr_get */
	0,                              /* tp_descr_set */
	0,                              /* tp_dictoffset */
	(initproc)GetDirectionalViewMapDensityF1D___init__, /* tp_init */
	0,                              /* tp_alloc */
	0,                              /* tp_new */
};

///////////////////////////////////////////////////////////////////////////////////////////

#ifdef __cplusplus
}
#endif
