import re


def _filter_dist(arg):
    """dist filter retrieves dist name from version string"""
    dist = re.match('[^\d]+', arg)
    return 'unknown' if not dist else dist.group(0)


def _filter_id(arg):
    """id filter retrieves version id version string"""
    vid = re.search('\d+$', arg)
    return 'unknown' if not vid else vid.group(0)
