import React, {Component} from 'react';
import PropTypes from 'prop-types';

import { GeoJSON as GeoJSONLeaflet } from 'react-leaflet';
import { Circle } from 'react-leaflet';

export default class GeoJSON extends Component {
    render() {
        // We need to use the non-JSX syntax to avoid having to list all props
	let circles = []
	let data = JSON.parse(this.props.data)
	for(const obj of data){
		if (obj.properties.hasOwnProperty("radius")){
			circles.push(
				React.createElement(
					Circle,
					{center: obj.geometry.coordinates, radius: obj.properties.radius}
				)
			)
		}
	}

        return circles 
    }
}

GeoJSON.propTypes = {
	data: PropTypes.string
}
