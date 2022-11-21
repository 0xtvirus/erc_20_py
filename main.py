from ERC_20 import ERC_20_functions

USDT = '0xc7198437980c041c805A1EDcbA50c1Ce5db95118'
usdt_token = ERC_20_functions(USDT)
holder = '0x92f803fd6edffaf8c4e81bb73234f270711b63f8'  # 14,933.881087 USDT.e
spender = '0xed2a7edd7413021d440b09d654f3b87712abab66'

print(usdt_token.token)
print(usdt_token.get_balance(holder))
print(usdt_token.get_allowance(holder, spender))