/*
 * Copyright 2011, Blender Foundation.
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
 */

#ifndef _COM_ColorCorrectionOperation_h
#define _COM_ColorCorrectionOperation_h
#include "COM_NodeOperation.h"


class ColorCorrectionOperation : public NodeOperation {
private:
	/**
	 * Cached reference to the inputProgram
	 */
	SocketReader *m_inputImage;
	SocketReader *m_inputMask;
	NodeColorCorrection *m_data;
	
	bool m_redChannelEnabled;
	bool m_greenChannelEnabled;
	bool m_blueChannelEnabled;

public:
	ColorCorrectionOperation();
	
	/**
	 * the inner loop of this program
	 */
	void executePixelSampled(float output[4], float x, float y, PixelSampler sampler);
	
	/**
	 * Initialize the execution
	 */
	void initExecution();
	
	/**
	 * Deinitialize the execution
	 */
	void deinitExecution();
	
	void setData(NodeColorCorrection *data) { this->m_data = data; }
	void setRedChannelEnabled(bool enabled) { this->m_redChannelEnabled = enabled; }
	void setGreenChannelEnabled(bool enabled) { this->m_greenChannelEnabled = enabled; }
	void setBlueChannelEnabled(bool enabled) { this->m_blueChannelEnabled = enabled; }
};
#endif
