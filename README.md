# 3-oji (papildoma) užduotis: Bitcoin transakcijų ir blokų analizė su Libbitcoin ir python-bitcoinlib
Šioje papildomoje užduotyje gilinsimės į Bitcoin transakcijų ir blokų struktūrą, panaudodami libbitcoin ir python-bitcoinlib bibliotekas.
## 1 dalis: Merkle medžio implementacija su Libbitcoin
Šioje dalyje susipažinsime su libbitcoin biblioteka ir ja pasinaudosime Merkle medžio implementacijai.

_Užduoties padaryti nepavyko, tačiau pateiksiu bandymų procesą._

1. Bandžiau padaryti WSL, parašiau komandas į PowerShell ir atsirado:

   ![изображение](https://github.com/user-attachments/assets/ffb00195-df39-43fa-b479-a988b36e8362).

   Tačiau jis neatsidarinėjo. Tada bandžiau instaliuoti Ubuntu, tačiau visą laiką rodė tik tai:

   ![изображение](https://github.com/user-attachments/assets/2cd710b1-e584-4e7b-8df2-5196b7a042ed)

   ir daugiau nieko nesidarė.
3. Pabandžiau tada instaliuoti libbitcoin ir paleisti kodą per Miscrosoft Visual Studio 2022. Tam tikslui instaliavau Visual Studio 2017 Redistribution (nepavyko rasti Visual Studio 2017). Kodas neveikė, rodė 22 klaidas. Keletas iš jų buvo, kad reikia naujesnės versijos.
4. Pabandžiau su Visual Studio Code. Rodė vieną klaidą - su <bitcoin/bitcoin.hpp> - negalėjo rasti failo.
5. Kadangi nepavyko su WSL, pabandžiau su Ubuntu virtualėje mašinoje. Instaliavau Oracle VM Virtual Box, ten įdiegiau Ubuntu, VSCode. Bandžiau atkartoti tą patį procesą, kurį bandžiau daryti savo kompiuteryje, tačiau vis tiek rodė klaidą.
6. Klausiau ChatGPT, žiūrėjau libbitcoin instaliavimo instrukciją, bandžiau viska įdiegti per terminalą - gavau 20GB failų, kuriuose vis teik nebuvo <bitcoin/bitcoin.hpp>.
7. Paklausiau kursiokų, ką galėtų parekomenduoti, jei jiems pavyko. Man patarė pakeisti <bitcoin/bitcoin.hpp> į <system.hpp>. Neveikė.
8. Pabandžiau pakeisti <bitcoin/bitcoin.hpp> į <system.hpp> ir mano kompiuterio Visual Studio, VSCode - vis tiek neveikė.
9. Bandymų buvo labai daug ir tam skirta net ne vieną dieną, bet rezultatai nebuvo tenkinami ir iki galo padaryti nesigavo.

## 2 dalis: Pilno Bitcoin mazgo (Bitcoin Core) įdiegimas
Šiai užduočiai reikia įdiegti pilną Bitcoin mazgą (Bitcoin Core) savo kompiuteryje arba debesyje ir pasidalinti mazgo prieiga su kolegomis.

_Užduoties padaryti nepavyko, tačiau pateiksiu bandymų procesą._

Bitcoin Core diegimas:

![image](https://github.com/user-attachments/assets/0ff0e286-a5ae-4e45-a69e-184c6e2c025a)

1. Pirmi kartai nepavyko, nes pasirodė, kad instaliavosi ne pilnos versijos.
2. Pabandžiau atsiųsti pilną Bitcoin Core versiją, tačiau instaliavosi į kompiuterį.
3. Modifikavau bitcoin.config failą, bet keletą kartų vis tiek instaliavo į kompiuterį.
4. Modifikavau bitcoin.conf failą - nustačiau, kad failai būtų įrašomi tam tikru keliu: datadir=C:\Users\acer\OneDrive - Vilnius University\BitcoinData. Tačiau jis vis tiek siųntė failus į kompiuterį ir iš kompiuterio į OneDrive. Tada iš kompiuterio šalino duomenis. Tačiau vienu momentu jis man neužteko vietos kompiuteryje, viskas užsidarė ir pradėjo rodyti error'us.
5. Pabandžiau dar kartą padaryti, bet praėjus 3 dienoms, į OneDrive atsisuntė tik 174 GB:

![изображение](https://github.com/user-attachments/assets/60ba700a-9ce5-4373-9310-821d6cd06c20)

Dažnai man užsidaro Bitcoin Core diegimo langas. Kada jį atidarau, rodo "Loading block index...", tačiau daugiau nieko nevyksta.

Taigi, atlikti šiai užduočiau buvo padaryta daug bandymų, laukta daug laiko, bet vis nepasisekė padaryti iki galo.

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

4. Šiai užduočiai bandžiau sukurti savo kodą, tačiau nepavyko - blogai skaičiaviavo hash. Todėl pasinaudojau rastu kodu iš https://stackoverflow.com/questions/66944273/bitcoin-verify-a-single-block-in-python. Kodas patikrina 620954 bloko hash. Kodą paleidžiau taip, kaip 2 ir 3 užduotyse:

   rpc_hash.py
   
   * Terminale parašiau "nano rpc_hash.py"
   * Įdėjau duotą kodą rpc_hash.py
   * Paspaudžiau Ctrl + X, tada Y ir Enter
   * Paleidžiau kodą naudodama komandą "python3 rpc_hash.py"
   * Gavau atsakymą: 
   * ![image](https://github.com/user-attachments/assets/84450e0e-a0d2-46d8-bf31-4b75d951785d)

