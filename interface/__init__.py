import pkgutil

__all__ = []

def reversed_iterator(iter):
    return reversed(list(iter))

rev_packages = reversed_iterator(pkgutil.walk_packages(__path__))
for loader, module_name, is_pkg in rev_packages:
    __all__.append(module_name)
    _module = loader.find_module(module_name).load_module(module_name)
    globals()[module_name] = _module
