from abc import ABC, abstractmethod


class Algorithm(ABC):
    @abstractmethod
    def execute(self, *args, **kwargs):
        pass

    @abstractmethod
    def get_documentation(self):
        pass

    @abstractmethod
    def run_test(self):
        pass

    @abstractmethod
    def get_test_cases(self):
        pass

    @abstractmethod
    def get_source_code(self):
        pass
