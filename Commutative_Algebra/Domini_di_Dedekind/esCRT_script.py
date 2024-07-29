'''
Windows: Utilizzo di Task Scheduler
Apri il Task Scheduler.
Crea una nuova attività.
Imposta il trigger per eseguire l'operazione ogni 15 secondi.
Configura l'azione per eseguire il comando desiderato.
Linux: Utilizzo di Cron
Apri il crontab con crontab -e.
Aggiungi una nuova linea per eseguire l'operazione ogni 20 secondi:

* * * * * /path/to/script.sh
script.sh
#!/bin/bash
while true; do
  # Comando da eseguire
  echo "Esecuzione comando"
  sleep 20
done


Per assicurarti che le operazioni rimangano sincronizzate, puoi utilizzare un server centralizzato che invia segnali di sincronizzazione o utilizza NTP (Network Time Protocol) per sincronizzare gli orologi delle macchine.
'''
