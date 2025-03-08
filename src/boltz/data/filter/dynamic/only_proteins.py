from boltz.data.types import Record
from boltz.data.filter.dynamic.filter import DynamicFilter
from boltz.data import const


class OnlyProteinsFilter(DynamicFilter):
    def filter(self, record: Record) -> bool:
        for chain in record.chains:
            if chain.mol_type != const.chain_type_ids["PROTEIN"]:
                return False
        return True
