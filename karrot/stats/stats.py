from influxdb_metrics.loader import write_points


def convert_stat(stat):
    tags = dict(stat)
    ms = tags.pop('ms')
    ms_resources = tags.pop('ms_resources')
    route_params = tags.pop('route_params')
    for key, value in route_params.items():
        tags['route_params__{}'.format(key)] = value
    return {
        'measurement': 'karrot.stats.frontend',
        'fields': {
            'ms': ms,
            'ms_resources': ms_resources,
        },
        'tags': tags,
    }


def received_stats(stats):
    write_points([convert_stat(stat) for stat in stats])
