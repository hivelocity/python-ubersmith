"""Order call classes.

These classes implement any response cleaning and validation needed.  If a
call class isn't defined for a given method then one is created using
ubersmith.calls.BaseCall.

"""

from ubersmith.calls import BaseCall, GroupCall
from ubersmith.utils import prepend_base

__all__ = [
    'GetCall',
    'ListCall',
]

_ = prepend_base(__name__.split('.')[-1])


class GetCall(BaseCall):
    method = _('get')
    required_fields = [('order_id', 'hash')]


class ListCall(GroupCall):
    method = _('list')


class QueueListCall(GroupCall):
    method = _('queue_list')
