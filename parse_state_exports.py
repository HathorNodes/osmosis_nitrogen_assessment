"""Parse state exportrs from upgrade height and halt height."""
import json

import pandas as pd
from typing import Mapping, Text

class StateExportParser():
    """Parses state_export to get relevant accounts, balances, authorizations and locks."""
    def __init__(self, height: Text):
        self.height = height
        self.base_account = '/cosmos.auth.v1beta1.BaseAccount'
        self.module_account = '/cosmos.auth.v1beta1.ModuleAccount'
        self.delayed_vesting = '/cosmos.vesting.v1beta1.DelayedVestingAccount'
        self.continuous_vesting = '/cosmos.vesting.v1beta1.ContinuousVestingAccount'

        # Create DataFrames of
        self.balances = self._parse_balances()
        self.locks = self._parse_locks()

    def _parse_balances(self, balances: Mapping) -> pd.DataFrame:
        """Formats and writes balances data to DB table."""
        count = 0
        for balance in balances:
            coins = balance.get('coins', [])
            count += len(coins)

        bal_info = [None] * count
        idx = 0
        for balance in balances:
            coins = balance.get('coins', [])
            address = balance.get('address')
            for coin in coins:
                amount = int(coin.get('amount'), 0)
                denom = coin.get('denom')
                bal_info[idx] = {
                    'height' : self.height,
                    'address' : address,
                    'amount' : amount,
                    'denom' : denom
                }
                idx += 1
        return pd.DataFrame(bal_info)

    def _parse_locks(self, locks: Mapping) -> pd.DataFrame:
        """Formats and writes locks data to DB table."""
        count = 0
        for lock in locks:
            coins = lock.get('coins')
            denom = coins[0].get('denom')
            if not denom.startswith("gamm/pool"):
                continue
            count += 1

        lock_info = [None] * count
        idx = 0
        for lock in locks:
            coins = lock.get('coins')
            denom = coins[0].get('denom')
            if not denom.startswith("gamm/pool"):
                continue
            lock_id = int(lock.get('ID'))
            duration = lock.get('duration')
            end_time = lock.get('end_time')
            status = "BONDED" if end_time.startswith("0001") else "UNBONDED"
            end_time = dateutil.parser.isoparse(end_time)
            lock_info[idx] = {
                'height': self.height,
                '`id`' : lock_id,
                'pool' : denom,
                'duration' : duration,
                'end_time' : end_time,
                'status' : status
            }
            idx += 1
        return pd.DataFrame(lock_info)

    def parse_export(self, json_file):
        """Extracts accounts, authorizations, balances and locks from state export file."""
        state_export = json.loads(json_file)
        balances = state_export['app_state']['bank']['balances']
        locks = state_export['app_state']['lockup']['locks']
        self._parse_balances(balances)
        self._parse_locks(locks)

if __name__ == '__main__':
    with open("data/state_export_upgrade_height_4707300.json", "rb") as upgrade_export_file:
        upgrade_export_state = json.load(upgrade_export_file)
        
    with open("data/state_export_halt_height_4713064.json", "rb") as halt_export_file:
        halt_export_state = json.load(halt_export_file)
          
    
    upgrade_export_data = StateExportParser(upgrade_export_state)
    upgrade_export_data.balances.to_csv("data/halt_balances.csv", index=False)
    upgrade_export_data.locks.to_csv("data/halt_locks.csv", index=False)

    halt_export_data = StateExportParser(halt_export_state)  
    halt_export_data.balances.to_csv("data/halt_balances.csv", index=False)
    halt_export_data.locks.to_csv("data/halt_locks.csv", index=False)
