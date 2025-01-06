from src import favorites
from moccasin.boa_tools import VyperContract
from moccasin.config import get_active_network

def deploy_favorites() -> VyperContract:
    favorites_contract: VyperContract = favorites.deploy()
    starting_number: int = favorites_contract.retrieve()
    print(f"The starting number is {starting_number}")
    
    favorites_contract.store(77)
    ending_number: int = favorites_contract.retrieve()
    print(f"The ending number is {ending_number}")
    
    active_network = get_active_network()

    if active_network.has_explorer():
        result = active_network.moccasin_verify(favorites_contract)
        result.wait_for_verification()
    return favorites_contract

    # factory_contract.store_from_factory(0,88)
    # print(f"New contract stored value is {new_favorites_contract.retrieve()}")
    # print(f"Original contract stored value is {favorites_contract.retrieve()}")

def deploy_five_more(favorites_contract):
    five_more_contract: VyperContract = five_more.deploy()
    five_more_contract.store(90)
    print(five_more_contract.retrieve())
    # print(five_more_contract.index())

def moccasin_main():
    favorites_contract = deploy_favorites()
    deploy_favorites(favorites_contract)
    return deploy_five_more()
    