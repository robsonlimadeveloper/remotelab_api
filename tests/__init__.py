'''Init tests module'''
from injector import Module


class DependencyModule(Module):
    '''Init dependency module'''
    def __init__(self, service_class, repository_class):
        self.service_class = service_class
        self.repository_class = repository_class

    def configure(self, binder):
        '''Configure method'''
        if self.repository_class:
            binder.bind(self.repository_class, to=self.repository_class)

        binder.bind(self.service_class, to=self.service_class)