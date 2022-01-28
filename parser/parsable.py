from abc import ABCMeta, abstractmethod, abstractproperty


class Parsable:

    @abstractmethod
    def parse(self):
        pass

    @abstractmethod
    def get_name(self):
        pass
