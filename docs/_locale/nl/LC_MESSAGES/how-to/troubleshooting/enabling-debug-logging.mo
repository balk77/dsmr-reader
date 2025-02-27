��          �                 S        q  	   �     �  �   	  F   �  �   �     �  .   �  '   �  4     \   6  J   �  %   �  q     �  v  U   P  �   �     @     G  �   U  W   �  �   F	     �	  C   
  &   ]
  ,   �
  o   �
  M   !  -   o  t   �   :doc:`See here for where to find the log files </how-to/troubleshooting/logfiles>`. After editing the file, all processes need to be restarted to reflect the change. Go back to the **root user or sudoer** with:: All done! And restart:: DSMR-reader has DEBUG logging, which makes the system log very verbosely about what it's trying to do and **why** it executes or skips certain actions. Don't forget to disable DEBUG logging whenever you are done debugging. Errors are likely to be logged at all times, no matter the logging level used. DEBUG logging is only helpful to watch DSMR-reader's detailed behaviour, when debugging issues. It should now be:: Make sure you are ``dsmr`` user by executing:: Now remove the ``###`` from this line:: Open the ``.env`` file and look for the code below:: The DEBUG logging is **disabled by default**, to reduce the number writes on the filesystem. This applies **specifically** to the ``dsmr_backend`` process and its log. Troubleshooting: Enable DEBUG logging You can enable the DEBUG logging by setting the ``DSMRREADER_LOGLEVEL`` env var to ``DEBUG``. Follow these steps: Project-Id-Version: DSMR Reader
Report-Msgid-Bugs-To: Dennis Siemensma <github@dennissiemensma.nl>
POT-Creation-Date: 2021-04-03 00:06+0200
PO-Revision-Date: YEAR-MO-DA HO:MI+ZONE
Last-Translator: Dennis Siemensma <github@dennissiemensma.nl>
Language: nl
Language-Team: Dennis Siemensma <github@dennissiemensma.nl>
Plural-Forms: nplurals=2; plural=(n != 1)
MIME-Version: 1.0
Content-Type: text/plain; charset=utf-8
Content-Transfer-Encoding: 8bit
Generated-By: Babel 2.9.0
 :doc:`Bekijk hier waar je de logfiles kan vinden </how-to/troubleshooting/logfiles>`. Na het bewerken van het bestand zul je alle processen moeten herstarten om de wijziging door te voeren. Ga terug naar de **root of sudo-gebruiker** met:: Klaar! En herstart:: DSMR-reader heeft DEBUG-logging, waarmee het systeem heel letterlijk logt wat het aan het doen is en **waarom** het sommige acties wel of niet uitvoert. Vergeet niet om DEBUG-logging weer uit te schakelen wanneer je klaar bent met debuggen. Fouten worden doorgaans altijd gelogd, ongeacht het logging niveau. DEBUG-logging is alleen nuttig om het gedrag van DSMR-reader in meer detail te observeren, om issues te debuggen. Het zou nu dit moeten zijn:: Zorg ervoor dat je ``dsmr`` gebruiker bent door dit uit te voeren:: Verwijder nu de ``###`` uit de regel:: Open ``.env`` en zoek de onderstaande code:: De DEBUG-logging is **standaard uitgeschakeld** om het aantal schrijfacties op het bestandssysteem te beperken. Dit geldt **specifiek** voor het ``dsmr_backend`` proces en bijbehorende log. Hulp bij problemen: DEBUG-logging inschakelen Je kunt DEBUG-logging inschakelen door de ``DSMRREADER_LOGLEVEL`` env var op ``DEBUG`` te zetten. Volg deze stappen: 