# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.1
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _roadBuilder
else:
    import _roadBuilder

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


class city(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        _roadBuilder.city_swiginit(self, _roadBuilder.new_city(*args))
    coordX = property(_roadBuilder.city_coordX_get, _roadBuilder.city_coordX_set)
    coordY = property(_roadBuilder.city_coordY_get, _roadBuilder.city_coordY_set)
    nombre = property(_roadBuilder.city_nombre_get, _roadBuilder.city_nombre_set)
    __swig_destroy__ = _roadBuilder.delete_city

# Register city in _roadBuilder:
_roadBuilder.city_swigregister(city)

class pais(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self):
        _roadBuilder.pais_swiginit(self, _roadBuilder.new_pais())
    ciudades = property(_roadBuilder.pais_ciudades_get, _roadBuilder.pais_ciudades_set)
    n = property(_roadBuilder.pais_n_get, _roadBuilder.pais_n_set)
    edges = property(_roadBuilder.pais_edges_get, _roadBuilder.pais_edges_set)

    def agregar_ciudad(self, arg2, arg3):
        return _roadBuilder.pais_agregar_ciudad(self, arg2, arg3)

    def calcular(self):
        return _roadBuilder.pais_calcular(self)

    def distancia_edge(self, arg2, arg3, arg4, arg5):
        return _roadBuilder.pais_distancia_edge(self, arg2, arg3, arg4, arg5)

    def distancia(self, arg2, arg3):
        return _roadBuilder.pais_distancia(self, arg2, arg3)
    __swig_destroy__ = _roadBuilder.delete_pais

# Register pais in _roadBuilder:
_roadBuilder.pais_swigregister(pais)

class SwigPyIterator(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _roadBuilder.delete_SwigPyIterator

    def value(self):
        return _roadBuilder.SwigPyIterator_value(self)

    def incr(self, n=1):
        return _roadBuilder.SwigPyIterator_incr(self, n)

    def decr(self, n=1):
        return _roadBuilder.SwigPyIterator_decr(self, n)

    def distance(self, x):
        return _roadBuilder.SwigPyIterator_distance(self, x)

    def equal(self, x):
        return _roadBuilder.SwigPyIterator_equal(self, x)

    def copy(self):
        return _roadBuilder.SwigPyIterator_copy(self)

    def next(self):
        return _roadBuilder.SwigPyIterator_next(self)

    def __next__(self):
        return _roadBuilder.SwigPyIterator___next__(self)

    def previous(self):
        return _roadBuilder.SwigPyIterator_previous(self)

    def advance(self, n):
        return _roadBuilder.SwigPyIterator_advance(self, n)

    def __eq__(self, x):
        return _roadBuilder.SwigPyIterator___eq__(self, x)

    def __ne__(self, x):
        return _roadBuilder.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n):
        return _roadBuilder.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n):
        return _roadBuilder.SwigPyIterator___isub__(self, n)

    def __add__(self, n):
        return _roadBuilder.SwigPyIterator___add__(self, n)

    def __sub__(self, *args):
        return _roadBuilder.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self

# Register SwigPyIterator in _roadBuilder:
_roadBuilder.SwigPyIterator_swigregister(SwigPyIterator)


def cos(x):
    return _roadBuilder.cos(x)

def sin(x):
    return _roadBuilder.sin(x)

def tan(x):
    return _roadBuilder.tan(x)

def acos(x):
    return _roadBuilder.acos(x)

def asin(x):
    return _roadBuilder.asin(x)

def atan(x):
    return _roadBuilder.atan(x)

def atan2(y, x):
    return _roadBuilder.atan2(y, x)

def cosh(x):
    return _roadBuilder.cosh(x)

def sinh(x):
    return _roadBuilder.sinh(x)

def tanh(x):
    return _roadBuilder.tanh(x)

def exp(x):
    return _roadBuilder.exp(x)

def log(x):
    return _roadBuilder.log(x)

def log10(x):
    return _roadBuilder.log10(x)

def pow(x, y):
    return _roadBuilder.pow(x, y)

def sqrt(x):
    return _roadBuilder.sqrt(x)

def fabs(x):
    return _roadBuilder.fabs(x)

def ceil(x):
    return _roadBuilder.ceil(x)

def floor(x):
    return _roadBuilder.floor(x)

def fmod(x, y):
    return _roadBuilder.fmod(x, y)
M_E = _roadBuilder.M_E
M_LOG2E = _roadBuilder.M_LOG2E
M_LOG10E = _roadBuilder.M_LOG10E
M_LN2 = _roadBuilder.M_LN2
M_LN10 = _roadBuilder.M_LN10
M_PI = _roadBuilder.M_PI
M_PI_2 = _roadBuilder.M_PI_2
M_PI_4 = _roadBuilder.M_PI_4
M_1_PI = _roadBuilder.M_1_PI
M_2_PI = _roadBuilder.M_2_PI
M_2_SQRTPI = _roadBuilder.M_2_SQRTPI
M_SQRT2 = _roadBuilder.M_SQRT2
M_SQRT1_2 = _roadBuilder.M_SQRT1_2
class vectorCity(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def iterator(self):
        return _roadBuilder.vectorCity_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _roadBuilder.vectorCity___nonzero__(self)

    def __bool__(self):
        return _roadBuilder.vectorCity___bool__(self)

    def __len__(self):
        return _roadBuilder.vectorCity___len__(self)

    def __getslice__(self, i, j):
        return _roadBuilder.vectorCity___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _roadBuilder.vectorCity___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _roadBuilder.vectorCity___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _roadBuilder.vectorCity___delitem__(self, *args)

    def __getitem__(self, *args):
        return _roadBuilder.vectorCity___getitem__(self, *args)

    def __setitem__(self, *args):
        return _roadBuilder.vectorCity___setitem__(self, *args)

    def pop(self):
        return _roadBuilder.vectorCity_pop(self)

    def append(self, x):
        return _roadBuilder.vectorCity_append(self, x)

    def empty(self):
        return _roadBuilder.vectorCity_empty(self)

    def size(self):
        return _roadBuilder.vectorCity_size(self)

    def swap(self, v):
        return _roadBuilder.vectorCity_swap(self, v)

    def begin(self):
        return _roadBuilder.vectorCity_begin(self)

    def end(self):
        return _roadBuilder.vectorCity_end(self)

    def rbegin(self):
        return _roadBuilder.vectorCity_rbegin(self)

    def rend(self):
        return _roadBuilder.vectorCity_rend(self)

    def clear(self):
        return _roadBuilder.vectorCity_clear(self)

    def get_allocator(self):
        return _roadBuilder.vectorCity_get_allocator(self)

    def pop_back(self):
        return _roadBuilder.vectorCity_pop_back(self)

    def erase(self, *args):
        return _roadBuilder.vectorCity_erase(self, *args)

    def __init__(self, *args):
        _roadBuilder.vectorCity_swiginit(self, _roadBuilder.new_vectorCity(*args))

    def push_back(self, x):
        return _roadBuilder.vectorCity_push_back(self, x)

    def front(self):
        return _roadBuilder.vectorCity_front(self)

    def back(self):
        return _roadBuilder.vectorCity_back(self)

    def assign(self, n, x):
        return _roadBuilder.vectorCity_assign(self, n, x)

    def resize(self, *args):
        return _roadBuilder.vectorCity_resize(self, *args)

    def insert(self, *args):
        return _roadBuilder.vectorCity_insert(self, *args)

    def reserve(self, n):
        return _roadBuilder.vectorCity_reserve(self, n)

    def capacity(self):
        return _roadBuilder.vectorCity_capacity(self)
    __swig_destroy__ = _roadBuilder.delete_vectorCity

# Register vectorCity in _roadBuilder:
_roadBuilder.vectorCity_swigregister(vectorCity)



