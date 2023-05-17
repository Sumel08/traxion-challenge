from abc import abstractmethod


class Converter:

    @abstractmethod
    def from_dto(self, dto):
        pass

    @abstractmethod
    def from_entity(self, entity):
        pass

    def from_dto_list(self, dto_array: list):
        return map(lambda dto: self.from_dto(dto), dto_array)

    def from_entity_list(self, entity_list: list):
        return map(lambda entity: self.from_entity(entity), entity_list)
