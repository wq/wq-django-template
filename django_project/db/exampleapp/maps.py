place_map = {
    'list': {'autoLayers': True},
    'detail': {'autoLayers': True},
    'edit': {
        'layers': [{
            'name': 'Place Location(s)',
            'type': 'geojson',
            'url': 'places/{% templatetag openvariable %}id{% templatetag closevariable %}/edit.geojson',
            'geometryField': 'locations',

            # Leaflet.draw options
            'draw': {
                'circle': False,
                'marker': {},
                'polygon': {},
                'polyline': False,
                'rectangle': {},
            }
        }]
    }
}

index_map = {
    'defaults': {
        'layers': [{
            'name': 'Places',
            'type': 'geojson',
            'url': 'places.geojson',
            'popup': 'place',
        }]
    }
}
