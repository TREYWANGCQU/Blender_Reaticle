/*
 * Copyright 2012, Blender Foundation.
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
 * Contributor:
 *		Jeroen Bakker
 *		Monique Dewanchand
 *		Sergey Sharybin
 */

#ifndef __COM_MASKNODE_H__
#define __COM_MASKNODE_H__

#include "COM_Node.h"
#include "DNA_node_types.h"

/**
 * @brief MaskNode
 * @ingroup Node
 */
class MaskNode : public Node {
public:
	MaskNode(bNode *editorNode);
	void convertToOperations(NodeConverter &converter, const CompositorContext &context) const;

};

#endif  /* __COM_MASKNODE_H__ */
