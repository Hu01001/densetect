# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.10
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.



from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            # fp, pathname, description = imp.find_module('_polyiou', [dirname(__file__)])
            fp, pathname, description = imp.find_module('_polyiou', ['/home/hufan/pyprj/s2anet/DOTA_devkit'])

        except ImportError:
            import _polyiou
            return _polyiou
        if fp is not None:
            try:
                _mod = imp.load_module('_polyiou', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _polyiou = swig_import_helper()
    del swig_import_helper
else:
    import _polyiou
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


class SwigPyIterator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SwigPyIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SwigPyIterator, name)
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _polyiou.delete_SwigPyIterator
    __del__ = lambda self : None;
    def value(self): return _polyiou.SwigPyIterator_value(self)
    def incr(self, n=1): return _polyiou.SwigPyIterator_incr(self, n)
    def decr(self, n=1): return _polyiou.SwigPyIterator_decr(self, n)
    def distance(self, *args): return _polyiou.SwigPyIterator_distance(self, *args)
    def equal(self, *args): return _polyiou.SwigPyIterator_equal(self, *args)
    def copy(self): return _polyiou.SwigPyIterator_copy(self)
    def next(self): return _polyiou.SwigPyIterator_next(self)
    def __next__(self): return _polyiou.SwigPyIterator___next__(self)
    def previous(self): return _polyiou.SwigPyIterator_previous(self)
    def advance(self, *args): return _polyiou.SwigPyIterator_advance(self, *args)
    def __eq__(self, *args): return _polyiou.SwigPyIterator___eq__(self, *args)
    def __ne__(self, *args): return _polyiou.SwigPyIterator___ne__(self, *args)
    def __iadd__(self, *args): return _polyiou.SwigPyIterator___iadd__(self, *args)
    def __isub__(self, *args): return _polyiou.SwigPyIterator___isub__(self, *args)
    def __add__(self, *args): return _polyiou.SwigPyIterator___add__(self, *args)
    def __sub__(self, *args): return _polyiou.SwigPyIterator___sub__(self, *args)
    def __iter__(self): return self
SwigPyIterator_swigregister = _polyiou.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

class VectorDouble(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, VectorDouble, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, VectorDouble, name)
    __repr__ = _swig_repr
    def iterator(self): return _polyiou.VectorDouble_iterator(self)
    def __iter__(self): return self.iterator()
    def __nonzero__(self): return _polyiou.VectorDouble___nonzero__(self)
    def __bool__(self): return _polyiou.VectorDouble___bool__(self)
    def __len__(self): return _polyiou.VectorDouble___len__(self)
    def pop(self): return _polyiou.VectorDouble_pop(self)
    def __getslice__(self, *args): return _polyiou.VectorDouble___getslice__(self, *args)
    def __setslice__(self, *args): return _polyiou.VectorDouble___setslice__(self, *args)
    def __delslice__(self, *args): return _polyiou.VectorDouble___delslice__(self, *args)
    def __delitem__(self, *args): return _polyiou.VectorDouble___delitem__(self, *args)
    def __getitem__(self, *args): return _polyiou.VectorDouble___getitem__(self, *args)
    def __setitem__(self, *args): return _polyiou.VectorDouble___setitem__(self, *args)
    def append(self, *args): return _polyiou.VectorDouble_append(self, *args)
    def empty(self): return _polyiou.VectorDouble_empty(self)
    def size(self): return _polyiou.VectorDouble_size(self)
    def clear(self): return _polyiou.VectorDouble_clear(self)
    def swap(self, *args): return _polyiou.VectorDouble_swap(self, *args)
    def get_allocator(self): return _polyiou.VectorDouble_get_allocator(self)
    def begin(self): return _polyiou.VectorDouble_begin(self)
    def end(self): return _polyiou.VectorDouble_end(self)
    def rbegin(self): return _polyiou.VectorDouble_rbegin(self)
    def rend(self): return _polyiou.VectorDouble_rend(self)
    def pop_back(self): return _polyiou.VectorDouble_pop_back(self)
    def erase(self, *args): return _polyiou.VectorDouble_erase(self, *args)
    def __init__(self, *args): 
        this = _polyiou.new_VectorDouble(*args)
        try: self.this.append(this)
        except: self.this = this
    def push_back(self, *args): return _polyiou.VectorDouble_push_back(self, *args)
    def front(self): return _polyiou.VectorDouble_front(self)
    def back(self): return _polyiou.VectorDouble_back(self)
    def assign(self, *args): return _polyiou.VectorDouble_assign(self, *args)
    def resize(self, *args): return _polyiou.VectorDouble_resize(self, *args)
    def insert(self, *args): return _polyiou.VectorDouble_insert(self, *args)
    def reserve(self, *args): return _polyiou.VectorDouble_reserve(self, *args)
    def capacity(self): return _polyiou.VectorDouble_capacity(self)
    __swig_destroy__ = _polyiou.delete_VectorDouble
    __del__ = lambda self : None;
VectorDouble_swigregister = _polyiou.VectorDouble_swigregister
VectorDouble_swigregister(VectorDouble)


def iou_poly(*args):
  return _polyiou.iou_poly(*args)
iou_poly = _polyiou.iou_poly
# This file is compatible with both classic and new-style classes.


