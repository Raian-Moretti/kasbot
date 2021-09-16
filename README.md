# KasBot
## Bot do Kasino para o Discord.

## Executar
1. Tenha `python3` e `pip3` instalado.
2. `git checkout https://github.com/ivanch/kasbot`
3. `pip3 install -r requirements.txt`
3. Exporte o token do seu bot com `export token=[token]`
4. `python main.py`

#### Keepalive
Para executar com *keepalive* (manter o servidor vivo com um servidor web):
1. Instale o flask utilizando `pip3 install flask`
2. Defina uma variável de ambiente *alive* com `export alive`
3. Execute os [passos acima](#executar).

## Comandos
* `kasino`
    * Toca o famoso SABADAÇO.
* `shake it`
    * Toca o hit SHAKE IT.
* `jet music`
    * NAS PISTAS DO JET MUSIC!
* `pare`
    * Para de tocar e desconecta.
* `companhia`
    * Entra no canal e te faz companhia, sem falar nem ouvir nada, apenas o doce som do silêncio.
