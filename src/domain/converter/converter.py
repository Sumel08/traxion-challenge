from abc import abstractmethod


class Converter:
    """
    Basic structure that will help us to convert between entitities and dto objects
    """

    @abstractmethod
    def from_dto(self, dto):
        pass

    @abstractmethod
    def from_entity(self, entity):
        pass

    def from_dto_list(self, dto_array: list):
        return list(map(lambda dto: self.from_dto(dto), dto_array))

    def from_entity_list(self, entity_list: list):
        return list(map(lambda entity: self.from_entity(entity), entity_list))
