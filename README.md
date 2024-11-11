# 3-oji (papildoma) užduotis: Bitcoin transakcijų ir blokų analizė su Libbitcoin ir python-bitcoinlib
Šioje papildomoje užduotyje gilinsimės į Bitcoin transakcijų ir blokų struktūrą, panaudodami libbitcoin ir python-bitcoinlib bibliotekas.
## 1 dalis: Merkle medžio implementacija su Libbitcoin
Šioje dalyje susipažinsime su libbitcoin biblioteka ir ja pasinaudosime Merkle medžio implementacijai.

## 2 dalis: Pilno Bitcoin mazgo (Bitcoin Core) įdiegimas
Šiai užduočiai reikia įdiegti pilną Bitcoin mazgą (Bitcoin Core) savo kompiuteryje arba debesyje ir pasidalinti mazgo prieiga su kolegomis.

## 3 dalis: Bitcoin tinklo analizė su python-bitcoinlib
Šioje dalyje išmoksite naudotis python-bitcoinlib biblioteka ir Bitcoin Core mazgu, norint gauti ir analizuoti informaciją apie Bitcoin tinklą.

### Užduotis
1. Įdiekite python-bitcoinlib.
2. Išbandykite pateiktus pavyzdžius: Sukurkite ir paleiskite rpc_example.py , rpc_transaction.py ir rpc_block.py failus.
3. Apskaičiuokite transakcijos mokestį: Parašykite programą, kuri apskaičiuoja Bitcoin transakcijos mokestį pagal jos hash'ą. Išbandykite ją su šia 2019-09-06 įvykusia viena vertingiausių transakcijų.
4. Patikrinkite bloko hash'ą: Parašykite programą, kuri patikrina, ar bloko hash'as yra teisingai apskaičiuotas pagal bloko header'io informaciją. Šis šaltinis gali būti naudingas.

### Atliktos užduoties aprašymas
1. Užduočiai atlikti instaiavau PuTTY ir įvedžiau duotą ip ir portą tam, kad galėčiau prisijungti prie VU Bitcoin mazgo. Prisijungiau su vardu user17 ir slaptažodžiu bn17. Kai prisijungiau prie terminalo, parašiau komandą "pip install pythin-bitcoinlib" ir taip ją įdiegiau.
2. Išbandžiau visus tris kodus tokiu būdu:
   
   rpc_example.py
   
   * Terminale parašiau "nano rpc_example.py"
   * Įdėjau duotą kodą rpc_example.py
   * Paspaudžiau Ctrl + X, tada Y ir Enter
   * Paleidžiau kodą naudodama komandą "python3 rpc_example.py"
   * Gavau atsakymą: 869567
   * ![image](https://github.com/user-attachments/assets/3c4522ac-7f15-4512-8e13-8f0ad7de3322)

   rpc_transaction.py
   
   * Terminale parašiau "nano rpc_transaction.py"
   * Įdėjau duotą kodą rpc_transaction.py
   * Paspaudžiau Ctrl + X, tada Y ir Enter
   * Paleidžiau kodą naudodama komandą "python3 rpc_transaction.py"
   * Gavau atsakymą: 1GdK9UzpHBzqzX2A9JFP3Di4weBwqgmoQA 0.01500000 ir 1Cdid9KFAaatwczBwBttQcwXYCpvK8h7FK 0.08450000
   * ![image](https://github.com/user-attachments/assets/ff23df34-5e86-430e-bf2a-8a3e634a837f)

   rpc_block.py
   
   * Terminale parašiau "nano rpc_block.py"
   * Įdėjau duotą kodą rpc_block.py
   * Paspaudžiau Ctrl + X, tada Y ir Enter
   * Paleidžiau kodą naudodama komandą "python3 rpc_block.py"
   * Gavau atsakymą: Total output value (in BTC) in block #277316:  1.24369901
   * ![image](https://github.com/user-attachments/assets/c124594f-47c7-49c7-be1a-2a2e8b317553)

3. 2019-09-06 viena vertingiausiu transakciju buvo su hash 4410c8d14ff9f87ceeed1d65cb58e7c7b2422b2d7529afc675208ce2ce09ed7d. Mokestis buvo:

![image](https://github.com/user-attachments/assets/2c9e1576-15a2-4c3e-9685-c4f5943c69ef)

Tam tikslui, pamodifikavau vieną iš duotų kodų ir gavau tokį:

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

To kodo rezultatas:

![image](https://github.com/user-attachments/assets/528eb6e0-0f5f-4f5c-b292-a7cced474563)

Taigi, mokėstis buvo teisingai apskaičiuotas.


