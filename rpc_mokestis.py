from bitcoin.rpc import RawProxy
# Create a connection to local Bitcoin Core node
p = RawProxy()
# 2019-09-06 transaction ID
txid = "4410c8d14ff9f87ceeed1d65cb58e7c7b2422b2d7529afc675208ce2ce09ed7d"
# First, retrieve the raw transaction in hex
raw_tx = p.getrawtransaction(txid)
# Decode the transaction hex into a JSON object
decoded_tx = p.decoderawtransaction(raw_tx)

# Apskaiciuojama iejimu verte
total_input = 0
for vin in decoded_tx['vin']:
    input_txid = vin['txid']
    input_vout = vin['vout']
    
    # Gaunama pradine transakcija, is kur buvo iejimas
    raw_input_tx = p.getrawtransaction(input_txid)
    decoded_input_tx = p.decoderawtransaction(raw_input_tx)
    
    # Iejimo verte pridedama prie bendros sumos
    total_input += decoded_input_tx['vout'][input_vout]['value']

# Apskaiciuojama isejimu verte
total_output = sum(output['value'] for output in decoded_tx['vout'])

# Transakcijos mokestis
tx_mokestis = total_input - total_output
print(f"Transakcijos mokestis: {tx_mokestis} BTC")