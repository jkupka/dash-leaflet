import React, {Component} from 'react';
import PropTypes from 'prop-types';

import { GeoJSON as GeoJSONLeaflet } from 'react-leaflet';

export default class GeoJSON extends Component {
    render() {
        // We need to use the non-JSX syntax to avoid having to list all props
        const el = React.createElement(
            GeoJSONLeaflet,
            this.props,
            this.props.children
        )

        return el
    }
}

GeoJSON.propTypes = {
	data: PropTypes.object,
}
