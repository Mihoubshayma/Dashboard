{
 "cells": [
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Il linguaggio Python\n",
    "\n",
    "## Perché?\n",
    "- Facile da usare, possibile usarlo per scripting (linguaggio interpretato)\n",
    "- Presenta una console interattiva, e alcune interfacce interattive come Jupyter\n",
    "- Provvisto di strutture dati native pronte all'uso (dizionari, liste...)\n",
    "- Linguaggio a oggetti\n",
    "- Attualmente il più usato per il *machine learning* e l'*intelligenza artificiale* in genere\n",
    "\n",
    "### Nota sulle versioni\n",
    "Useremo Python 3.x che *non* è compatibile con Python 2.x. Si tratta di versioni portate avanti in parallelo, con idee e paradigmi differenti. \n",
    "Le differenze principali riguardano la gestione delle stringhe e delle strutture dati iterabili. La versione 2.x pian piano sta venendo abbandonata: è meglio iniziare con Python 3.x."
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Console interattiva e scripting\n",
    "\n",
    "Il modo più semplice di usare Python è installarlo sul proprio PC e lanciare il comando\n",
    "`python` o `python3`. Si aprirà una shell interattiva con cui \"dialogare\".\n",
    "\n",
    "In alternativa, si può creare un file con estensione `.py`, ad esempio `miofile.py`, riempirlo con una sequenza di istruzioni e lanciarlo da riga di comando con `python miofile.py`.  \n",
    "Questo è possibile perché Python è un linguaggio *interpretato*.\n",
    "\n",
    "È anche possibile *importare* altri script personali dentro a `miofile.py`. Ad esempio ipotizziamo di avere un file `mioscript.py` nella stessa cartella di `miofile.py`.  \n",
    "Questo può essere importato tramite il comando `import mioscript`.\n",
    "\n",
    "#### <span style=\"color:tomato\">Attenzione </span>\n",
    "**Tutte** le istruzioni presenti dentro a `mioscript` vengono eseguite durante la import."
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Inoltre  \n",
    "> <span style=\"color:orange\">In Python, ogni cosa è un **oggetto**</span>\n",
    "\n",
    "... quindi anche il mio script.\n",
    "Per controllare quali sono le proprietà e i metodi di un qualsiasi elemento (oggetto) python, si utilizza la funzione built-in `dir(mioscript)`."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<span style=\"color:dodgerblue\">Si provi a creare il file `mioscript.py` ed eseguire i seguenti comandi nella shell interattiva:</span>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import mioscript\n",
    "\n",
    "dir(mioscript)\n",
    "\n",
    "mioscript.__name__"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Quando viene importato, l'attributo `__name__` dell'oggetto `mioscript` coincide con il suo nome.  \n",
    "Invece, quando viene lanciato tramite il comando `python mioscript.py`, il suo nome coincide con `__main__`."
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Buone pratiche\n",
    "\n",
    "Visto il funzionamento dell'attributo `__name__`, è buona norma creare un main program che venga eseguito *solo* quando lo script viene lanciato direttamente, usando il costrutto if:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "if __name__ == \"__main__\":\n",
    "    pass # ... or do something"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Le istruzioni dentro a questo if verranno ignorate dalla import."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<span style=\"color:dodgerblue\">Creare un main dentro a `mioscript.py` ed eseguirlo solo se lanciato da console. Poi creare una funzione che wrappa il main per eseguirlo qui.</span>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Grazie al modulo built-in `sys`, possiamo controllare gli argomenti passati al nostro script da linea di comando. Il modulo infatti ci fornisce la lista `sys.argv`.  \n",
    "\n",
    "<span style=\"color:dodgerblue\">Modificare `mioscript.py` per passare al main gli argomenti della linea di comando.</span>"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Jupyter\n",
    "\n",
    "Una interfaccia interattiva molto comoda è quella di Jupyter: si tratta di uno strumento che consente di scrivere *notebook* che consistono di varie *celle*.  \n",
    "Le celle più usate sono quelle che contengono codice (python) e markdown.  \n",
    "**Attenzione**: Ogni cella viene eseguita solo su esplicito comando dell'utente, *non* necessariamente nell'ordine in cui si presenta!\n",
    "\n",
    "La documentazione è presente al seguente link: https://jupyter.org/\n",
    "\n",
    "Per usare Jupyter, si può installare JupyterLab oppure l'opportuno plugin per VSCode. Altri sistemi, come ad esempio Google Colab, fanno uso di notebook Jupyter. "
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Funzioni di input/output su console\n",
    "\n",
    "Alcune funzioni utili per lo scripting vengono fornite direttamente dal linguaggio, e vengono chiamate funzioni built-in.  \n",
    "L'elenco completo è presente al seguente link: https://docs.python.org/3/library/functions.html\n",
    "\n",
    "Tra queste, notiamo la funzione `print()`, per stampare su standard output:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "print(\"ciao mondo\")"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "La funzione `input()`, per leggere da standard input:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "a = input(\"inserisci il valore di a: \")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<span style=\"color:dodgerblue\">Chiedere all'utente l'anno di nascita e stampare la sua età.</span>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Attenzione**: i valori letti da standard input sono sempre stringhe."
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Variabili\n",
    "\n",
    "Le variabili sono rappresentate da letterali del linguaggio che consistono di caratteri alfanumerici e devono iniziare con una lettera (maiuscola o minuscola) o un underscore.  \n",
    "Una variabile viene dichiarata e immediatamente istanziata mediante assegnamento, tale operazione *inferisce* anche il suo **tipo**.  \n",
    "\n",
    "Sono possibili assegnamenti multipli:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "x, y, z = 1, 2, 3\n",
    "\n",
    "print(x)\n",
    "print(y)\n",
    "print(z)"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Anche le variabili sono oggetti. La classe è determinata dal loro tipo."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "a = 65\n",
    "\n",
    "print(type(a))\n",
    "\n",
    "print(dir(a))"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "\n",
    "In sintesi:\n",
    "> <span style=\"color:orange\">Python è un linguaggio *strongly and dynamically typed*</span>\n",
    "\n",
    "Con questo si intende che il controllo sul tipo di una variabile avviene a *runtime* (il che ci permette l'inferenza durante l'assegnamento) --> tipizzazione dinamica  \n",
    "ma allo stesso tempo, il tipo di una variabile non può cambiare in modo inaspettato (è necessario un cast) --> tipizzazione forte\n",
    "\n",
    "Il codice successivo genererà una eccezione:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "a = 65\n",
    "b = \"Z\"\n",
    "\n",
    "c = a + b"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<span style=\"color:dodgerblue\">Correggere il codice di cui sopra.</span>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Ecco un elenco dei principali tipi di variabile:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "a = 50\n",
    "\n",
    "int(a)\n",
    "float(a)\n",
    "\n",
    "chr(a) # ord(a)\n",
    "str(a)\n",
    "\n",
    "bool(a)\n",
    "complex(a)"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Ogni tipo attribuisce alla variabile una serie di proprietà e metodi, che si possono visualizzare con la funzione built-in `dir()`. Ad esempio:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "a = 27\n",
    "\n",
    "print(dir(a))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<span style=\"color:dodgerblue\">Ispezionare proprietà e metodi dei principali tipi di variabile.</span>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Operatori\n",
    "\n",
    "### Operatori numerici\n",
    "\n",
    "- Classici operatori aritmetici: `+`, `-`, `*`, `/`\n",
    "- Operatore di modulo o remainder: `%`, il risultato è il resto della divisione intera\n",
    "- Operatore di divisione intera: `//`, il risultato è il quoziente della divisione intera\n",
    "- Operatore di elevamento a potenza: `**` (per ragioni di efficienza, talvolta si usa la funzione built-in `pow`)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Altri operatori sono presenti nei moduli built-in `math` e `cmath`."
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Operatori bitwise\n",
    "\n",
    "- Bitwise AND: `&`\n",
    "- Bitwise OR: `|`\n",
    "- Bitwise XOR: `^`\n",
    "- Bitwise NOT: `~`\n",
    "- Shift destro: `>>`\n",
    "- Shift sinistro: `<<`\n"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Operatori di assegnamento"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "e = 1\n",
    "\n",
    "e += 1   # e = e + 1\n",
    "e -= 1   # e = e - 1\n",
    "e *= 5   # e = e * 5\n",
    "e /= 3   # e = e / 3\n",
    "e **= 2  # e = e ** 2\n",
    "\n",
    "print(e) # e = (((e + 1) - 1) * 5) / 3) ** 2"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<span style=\"color:dodgerblue\">Dati i coefficienti di una equazione di secondo grado </span> $ax^2 + bx + c = 0$ <span style=\"color:dodgerblue\">, stampare le soluzioni.</span>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "a, b, c = 1, 1, 1\n",
    "\n",
    "x1 = 0 # edit here\n",
    "\n",
    "x2 = 0 # edit here\n",
    "\n",
    "print(x1, x2)\n"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Operatori booleani\n",
    "\n",
    "I valori booleani sono `True` e `False`.\n",
    "\n",
    "- Congiunzione: `and`\n",
    "- Disgiunzione: `or`\n",
    "- Negazione: `not`\n",
    "\n",
    "<span style=\"color:orange\">In Python, qualsiasi variabile di qualsiasi tipo ha un valore di verità. Questo valore può essere *truthy* o *falsy*.</span>  \n",
    "\n",
    "Di norma, tutti gli oggetti, se testati da una condizione booleana, sono truthy, ovvero ritornano il valore di verità `True`, ad **eccezione** di:\n",
    "- costanti definite false: `False` e `None`\n",
    "- zeri dei tipi numerici: `0`, `0.0`, `0j`, ecc.\n",
    "- stringhe, sequenze e strutture dati vuote: `''`, `[]`, ecc."
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Operatori di confronto\n",
    "\n",
    "- Uguaglianza: `==`\n",
    "- Diverso: `!=`\n",
    "- Confronto sull'ordine: `<`, `>`, `<=`, `>=` (anche ordine lessicografico)"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Operatori di identità\n",
    "\n",
    "L'identità di un oggetto si può ottenere tramite la funzione di built-in `id()`: questa funzione ritorna il puntatore (ovvero l'indirizzo fisico di memoria) di quell'oggetto.\n",
    "\n",
    "- Confronto tra identità di oggetti: `is`, `is not`"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<span style=\"color:dodgerblue\">Ispezionare le identità delle variabili date e confrontarle.</span>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "a = 1\n",
    "b = a\n",
    "\n",
    "# insert comparison\n",
    "\n",
    "b += 1\n",
    "\n",
    "# insert comparison\n",
    "\n",
    "c = \"1\"\n",
    "\n",
    "# insert comparison"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Stringhe"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Una stringa in Python si definisce mediante apici o doppie virgolette. In più, è possibile definire stringhe multilinea, come nell'esempio seguente:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "a = \"ciao\"\n",
    "b = ' mondo'\n",
    "\n",
    "c = \"\"\" \n",
    "questa è una stringa\n",
    "multilinea\"\"\"\n",
    "\n",
    "d = \"qui posso usare gli apici ' \"\n",
    "e = 'qui posso usare le virgolette \" '\n",
    "\n",
    "d < e # confronto lessicografico"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Operatori su stringhe\n",
    "\n",
    "- Somma: `+`, concatena due stringhe date\n",
    "- Prodotto per un numero: `*` $n$, concatena $n$ volte la stringa con sé stessa"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "a = \"ciao\"\n",
    "b = ' mondo'\n",
    "\n",
    "concat = a + b\n",
    "\n",
    "print(concat)\n",
    "\n",
    "concat2 = a * 7\n",
    "\n",
    "print(concat2)\n",
    "\n",
    "concat3 = 3 * (a + b + ' ')\n",
    "\n",
    "print(concat3)"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Stringhe come sequenze\n",
    "\n",
    "In Python, le stringhe sono sequenze *ordinate* di caratteri. Grazie alla funzione built-in `len()`, definita su sequenze, è possibile conoscere la lunghezza di una stringa.  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "c = \"\"\" \n",
    "questa è una stringa\n",
    "multilinea\"\"\"\n",
    "\n",
    "len(c)"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Si può accedere a una precisa locazione della sequenza tramite l'operatore `[`$i$`]`, dove $i$ è la posizione desiderata.  \n",
    "L'operatore di *slicing* `[:]` permette di ottenere sotto-sequenze, in questo caso sotto-stringhe. Si veda l'esempio seguente:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "c = \"\"\" \n",
    "questa è una stringa\n",
    "multilinea\"\"\"\n",
    "\n",
    "print(c[3]) # accesso alla posizione 3\n",
    "\n",
    "print(c[1:5]) # sottostringa dalla posizione 1 (inclusa) alla posizione 5 (esclusa) -- si noti che è presente un a-capo\n",
    "\n",
    "print(c[2:16:3]) # sottostringa dalla posizione 2 (inclusa) alla posizione 16 (esclusa), con passo 3\n",
    "\n",
    "print(c[-1]) # accesso all'ultima posizione, shortcut per c[len(c) - 1]\n",
    "\n",
    "print(c[:]) # tutta la stringa\n",
    "\n",
    "print(c[::2]) # sottostringa dalla posizione 0 a len(c), con passo 2\n",
    "\n",
    "print(c[::-1]) # lettura della stringa con passo -1, cioè al contrario"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<span style=\"color:orange\">**Attenzione**: le stringhe in Python sono oggetti *immutabili*, cioè il loro contenuto non può essere modificato.</span>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<span style=\"color:dodgerblue\">Verificare quest'ultima affermazione confrontando tra loro gli `id` delle due stringhe date. Poi provare a modificare un singolo carattere.</span>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "c = \"\"\" \n",
    "questa è una stringa\n",
    "multilinea\"\"\"\n",
    "\n",
    "# here\n",
    "\n",
    "c = \"anche\" + c\n",
    "\n",
    "# here\n",
    "\n",
    "# direct edit:\n",
    "# c[5] = \"A\""
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Proprietà e metodi degli oggetti `str`"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "c = \"\"\" \n",
    "questa è una stringa\n",
    "multilinea\"\"\"\n",
    "\n",
    "print(dir(c))"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Per modificare il valore della stringa, ci sono vari metodi a seconda del risultato che si vuole ottenere.  \n",
    "I più comuni sono:\n",
    "- `strip()`, che elimina gli spazi \"dietro\" e \"davanti\" alla stringa (in altri linguaggi, questa operazione è nota come `trim`)\n",
    "- `replace(`*sub*`, `*new*`)`, che rimpiazza tutte le occorrenze della sottostringa *sub* con la stringa *new* specificata dall'utente\n",
    "- `upper()`, che converte ogni carattere alfabetico nell'equivalente maiuscolo\n",
    "- `lower()`, che converte ogni carattere alfabetico nell'equivalente minuscolo"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "stringa = \"    Stringa di Prova  12345  \"\n",
    "\n",
    "s2 = stringa.strip()\n",
    "s3 = stringa.upper()\n",
    "s4 = stringa.lower()\n",
    "stringa = stringa.replace(\" \", \"\")\n",
    "\n",
    "print(stringa)\n",
    "print(s2)\n",
    "print(s3)\n",
    "print(s4)\n",
    "# print(s5)\n",
    "print(stringa)\n"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Si noti che, trattandosi di metodi dell'oggetto `stringa`, vi si accede con l'operatore punto: `.`  \n",
    "Inoltre, questi metodi non modificano la stringa chiamante, bensì restituiscono una nuova stringa."
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Si possono fare alcune interrogazioni sulla stringa. Anche questi sono metodi dell'oggetto stringa.\n",
    "- `startswith(`*sub*`)` controlla se *sub* è un prefisso della stringa, restituendo `True` in caso affermativo, `False` altrimenti\n",
    "- `endswith(`*sub*`)` controlla se *sub* è un suffisso della stringa, restituendo `True` in caso affermativo, `False` altrimenti\n",
    "- `count(`*sub*`)` restituisce il numero di occorrenze della sottostringa *sub*\n",
    "- `find(`*sub*`)` restituisce la più piccola posizione in cui occorre la sottostringa *sub*, -1 se non viene trovata\n",
    "- `index(`*sub*`)` come `find`, ma lancia una eccezione se la sottostringa non viene trovata --> `index` è infatti un metodo comune a tutte le sequenze in Pyhton, non solo stringhe"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "stringa = \"stringa di di prova\"\n",
    "\n",
    "print(stringa.startswith(\"stri\"))\n",
    "\n",
    "print(stringa.endswith(\"OVA\"))\n",
    "\n",
    "print(stringa.count(\"di\"))\n",
    "print(stringa.count(\"ciao\"))\n",
    "\n",
    "print(stringa.find(\"di\"))\n",
    "print(stringa.find(\"ciao\"))\n",
    "\n",
    "print(stringa.index(\"di\"))\n",
    "print(stringa.index(\"ciao\"))\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Infine, il modulo built-in `re` permette di cercare pattern nelle stringhe con l'uso di *espressioni regolari*. Molto utile per il preprocessing di dati testuali."
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Costrutti"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "In Python, i blocchi di codice non sono delimitati da parentesi, ma il corpo di un costrutto è identificato tramite indentazione.\n",
    "\n",
    "### `if`-`elif`-`else`\n",
    "\n",
    "Il costrutto di selezione `if` ha la sintassi esplicitata nell'esempio seguente:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "a = 5\n",
    "b = 7\n",
    "\n",
    "if a < b:\n",
    "    print(a)\n",
    "else:\n",
    "    print(b)"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Gli if possono essere annidati, oppure si può utilizzare la parola chiave `elif`, per annidare un altro if nel ramo dell'else."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "a, b, c = 5, 7, 7\n",
    "\n",
    "if a == b:\n",
    "    print(\"primo if\")\n",
    "elif a == c:\n",
    "    print(\"secondo if\")\n",
    "elif b == c:\n",
    "    print(\"terzo if\")\n",
    "else:\n",
    "    pass"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "La parola chiave `pass` corrisponde a un blocco di codice vuoto."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<span style=\"color:dodgerblue\">Trovare il minimo tra i tre valori dati con il minor numero di condizioni `if`.</span>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "a, b, c = 5, 7, 3\n",
    "\n"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### `while`-`else`\n",
    "\n",
    "Il costrutto di iterazione while esegue il suo corpo quando la condizione booleana specificata è `True`. Non appena la condizione diventa `False`, viene eseguito il blocco `else` del while."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "a, b = 2, 3\n",
    "\n",
    "while a != b:\n",
    "    print(a)\n",
    "else:\n",
    "    print(\"ho finito\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<span style=\"color:dodgerblue\">Fare in modo di non eseguire il ramo `else` del costrutto while di cui sopra.</span>"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Soluzione: Il blocco `else` viene eseguito ogni qual volta il ciclo finisce, con una sola eccezione: uscendo dal corpo del while con una interruzione del flusso del programma, non viene valutata la condizione del while, dunque il corpo dell'else viene ignorato."
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### `for`-`in`-`else`"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Il costrutto di iterazione for permette di ciclare su un oggetto *iterabile*. Gli iterabili sono collezioni di vario tipo (si veda il paragrafo sulle strutture dati), oppure stringhe (come già visto).  \n",
    "La sintassi prevede di specificare una variabile che assumerà il valore dell'elemento della collezione da iterare: `for object in list`  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "print(range(15))\n",
    "\n",
    "for i in range(15): # for object in list\n",
    "    print(i)\n",
    "else:\n",
    "    print(\"ho finito\")\n",
    "\n",
    "print(type(range(15)))"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Anche per quanto riguarda il for, è possibile specificare un blocco `else`, il cui corpo verrà eseguito non appena la condizione `object in list` diventerà `False`. Se si esce dal for con una interruzione, il corpo dell'else non viene eseguito."
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Strutture dati"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "In Python sono presenti alcune strutture dati built-in che vengono messe a disposizione del programmatore senza il bisogno di caricare librerie aggiuntive.  \n",
    "Le più importanti sono le liste (di classe `list`), le tuple (`tuple`), i dizionari (`dict`) e gli insiemi (`set` e `frozenset`).\n",
    "\n",
    "Come per i tipi primitivi, è possibile effettuare il cast tramite apposite funzioni, quando possibile:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "a = list([1, 2, 3, 4])\n",
    "\n",
    "b = tuple([10, 20, 30, 40])\n",
    "\n",
    "a = dict(lista=a, tupla=b)\n",
    "\n",
    "a = set(a)\n",
    "\n",
    "a = frozenset(a)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<span style=\"color:dodgerblue\">Ispezionare le proprietà e i metodi degli oggetti che hanno come tipo le principali strutture dati.</span>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Liste e tuple\n",
    "\n",
    "Liste e tuple sono sequenze **ordinate** di oggetti *eterogenei*, ovvero gli oggetti della sequenza possono avere tipi diversi."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "lista = [0, 1, 2, \"ciao\", \"mondo\"]\n",
    "\n",
    "print(type(lista))\n",
    "\n",
    "tupla = (0, 1, 2, \"ciao\", \"mondo\")\n",
    "\n",
    "print(type(tupla))\n",
    "\n",
    "print(dir(lista))\n",
    "print(dir(tupla))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Nota bene: la variabile cui è assegnata la lista o tupla è un riferimento a una locazione di memoria contenente la lista o tupla reale."
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Liste e tuple sono indicizzate con indici numerici. Quindi è possibile accedere all'elemento $i$-esimo della sequenza tramite l'operatore di slicing `[`$i$`]`. L'utilizzo dell'operatore di slicing è lo stesso rispetto a quanto visto sulle stringhe. Ogni operazione di slicing crea una nuova copia della lista o tupla, perciò non modifica la sequenza stessa.\n",
    "\n",
    "Come per le stringhe, la lunghezza di una lista o tupla si può ottenere grazie alla funzione built-in `len()`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "lista = [0, 1, 2, \"ciao\", \"mondo\"]\n",
    "\n",
    "print(len(lista))\n",
    "\n",
    "print(lista[1:4:2])\n",
    "print(lista[3])\n",
    "print(lista[-1])\n",
    "print(lista[:])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "tupla = (0, 1, 2, \"ciao\", \"mondo\")\n",
    "\n",
    "print(tupla[0:4:2])\n",
    "print(tupla[-1])"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<span style=\"color:orange\">**Attenzione**: le liste sono strutture dati *mutabili*, mentre le tuple sono *immutabili*.</span>\n",
    "\n",
    "Questo significa che gli elementi di una tupla non possono essere modificati, tuttavia è possibile sovrascrivere completamente l'oggetto tupla, mediante assegnamento."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<span style=\"color:dodgerblue\">Sostituire un valore della tupla seguente.</span>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "tupla = (0, 1, 2, \"ciao\", \"mondo\")\n",
    "\n",
    "# questo lancerà una eccezione\n",
    "#tupla[0] = 5"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "La lista è invece mutabile, quindi è possibile modificare l'elemento alla posizione $i$ mediante assegnamento.  \n",
    "Come per le stringhe, è possibile concatenare liste con liste e tuple con tuple (non liste con tuple), mediante l'operatore `+`. Tramite l'operatore `*` invece, è possibile concatenare una lista (o una tupla) più volte con sé stessa."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<span style=\"color:dodgerblue\">Concatenare le due liste date ottenendo come risultato una lista e ottenendo come risultato una tupla.</span>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "lista1 = [0, 1, 2, \"ciao\", \"mondo\"]\n",
    "\n",
    "lista1[2] = 7 # esempio\n",
    "\n",
    "lista2 = [True, None, 'a']"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<span style=\"color:dodgerblue\">Creare una lista di 10 zeri e una tupla di 10 zeri, usando l'operatore `*`</span>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Per capire se un elemento è contenuto o meno in una lista o in una tupla, è possibile usare le parole chiave `in` e `not in`. Il risultato di queste espressioni è un valore booleano."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<span style=\"color:dodgerblue\">Verificare se i due valori dati sono nella lista specificata, poi iterare la lista usando la parola chiave `in`.</span>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "lista = [0, 1, 2, \"ciao\", \"mondo\"]\n",
    "\n",
    "a = 0\n",
    "\n",
    "b = \"gatto\""
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Per modificare una lista in-place, vengono forniti alcuni metodi dalla classe `list`.\n",
    "- `append(`*elem*`)` permette di aggiungere l'elemento *elem* in coda alla lista\n",
    "- `insert(`*pos*, *elem*`)` permette di aggiungere l'elemento *elem* alla posizione *pos*\n",
    "- `remove(`*elem*`)` permette di rimuovere l'elemento *elem*\n",
    "- `pop()` elimina l'elemento in coda alla lista e lo restituisce come output\n",
    "- `reverse()` inverte l'ordine degli elementi della lista\n",
    "- `clear()` pulisce la lista eliminando tutti gli elementi"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "lista = [0, 1, 2, \"ciao\", \"mondo\"]\n",
    "\n",
    "lista.append(\"aggiunto\") # in place\n",
    "\n",
    "print(lista)\n",
    "\n",
    "lista.insert(4, \"elemento\") # in place\n",
    "\n",
    "print(lista)\n",
    "\n",
    "lista.remove(\"elemento\") # in place\n",
    "\n",
    "print(lista)\n",
    "\n",
    "elem = lista.pop()\n",
    "\n",
    "print(lista)\n",
    "print(elem)\n",
    "\n",
    "lista.reverse()\n",
    "\n",
    "print(lista)\n",
    "\n",
    "lista.clear()\n",
    "\n",
    "print(lista)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Innestare liste e tuple è naturalmente possibile:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "b = [(1, 2), (3, 4), (5, 6)]\n",
    "\n",
    "c = ([1, 2], [3, 4], [5, 6])"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Copiare liste\n",
    "\n",
    "Come detto poco sopra, la variabile cui è assegnata la lista è un riferimento alla locazione di memoria in cui la lista risiede (lo stesso si può dire delle tuple).  \n",
    "\n",
    "Quando assegno questa variabile ad un'altra, sto facendo puntare entrambe le variabili alla stessa locazione, dunque modificare la lista può avvenire tramite l'una e l'altra.\n",
    "\n",
    "Si veda l'esempio seguente con liste innestate."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "a = [1, 2]\n",
    "b = a # assegno un puntatore\n",
    "\n",
    "c = [a, [3, 4]]\n",
    "d = [b, [5, 6]]\n",
    "\n",
    "print(c)\n",
    "print(d)\n",
    "\n",
    "a.append(7) # modifico a\n",
    "print(b) # b è stata modificata\n",
    "\n",
    "# entrambe c e d sono state modificate\n",
    "print(c)\n",
    "print(d)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Per evitare questo comportamento, si può utilizzare il metodo `copy()`.\n",
    "\n",
    "<span style=\"color:dodgerblue\">Risolvere i problemi dell'esempio precedente, tramite il metodo `copy()`.</span>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Nel caso in cui però la lista copiata con `copy()` abbia dentro di sé il riferimento a un'altra lista, quest'ultimo verrà copiato come riferimento. L'operazione di copia per questo motivo si chiama *shallow copy*.\n",
    "\n",
    "Si veda l'esempio seguente:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "a = [8, 9]\n",
    "\n",
    "b = [a, 1, 2]\n",
    "\n",
    "c = [a.copy(), [3, 4]]\n",
    "\n",
    "d = [b.copy(), [5, 6]]\n",
    "\n",
    "print(c)\n",
    "print(d)\n",
    "\n",
    "a.insert(0, 7) # modifico a\n",
    "\n",
    "print(b) # b è stata modificata\n",
    "print(c) # c non è stata modificata\n",
    "print(d) # d è stata modificata\n"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Per copiare in modo ricorsivo (profondo, non shallow) tutte le liste innestate, si fa uso della funzione `deepcopy` messa a disposizione dalla libreria `copy`."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<span style=\"color:dodgerblue\">Importare `deepcopy` dal modulo `copy` e risolvere il problema dell'esempio precedente.</span>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from copy import deepcopy\n",
    "\n",
    "# import copy\n",
    "# copy.deepcopy()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Ordinamento"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Un metodo molto utile della classe `list` è quello di ordinamento: `sort()`.\n",
    "L'ordinamento avviene in-place, ovvero modifica direttamente la lista su cui il metodo viene chiamato."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "lista2 = [0, 0.5, 7, 1, 1.43]\n",
    "\n",
    "lista2.sort() # in place\n",
    "\n",
    "print(lista2)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Se non si vuole modificare la lista originale, è possibile usare la funzione built-in `sorted(lista)`, che restituisce una nuova lista ordinata (utile per utilizzare l'iterabile dentro un `for`)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "a = [5, 2, 3, 4, 1, 1, 10]\n",
    "\n",
    "print(sorted(a))\n",
    "\n",
    "print(type(sorted(a)))\n",
    "\n",
    "for _ in sorted(a):\n",
    "    pass\n",
    "\n",
    "print(a)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Non è possibile ordinare una tupla, essendo immutabile. Si può però usare `sorted(tupla)` per ottenere una lista ordinata di elementi della tupla."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "a = (5, 2, 3, 4, 1, 1, 10)\n",
    "\n",
    "print(sorted(a))\n",
    "\n",
    "print(type(sorted(a)))\n",
    "\n",
    "print(a)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "La funzione built-in `sorted` ha alcuni parametri opzionali:  \n",
    "`sorted(iterable, key=key, reverse=reverse)`  \n",
    "dove `key` è una funzione che può essere usata per stabilire l'ordine, mentre `reverse` è un booleano che indica se utilizzare un ordinamento discendente. "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<span style=\"color:dodgerblue\">Ordinare la seguente tupla in base alla lunghezza delle stringhe elencate.</span>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "tupla = (\"gatto\", \"ciao\", \"a\", \"qualsiasi\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Creare stringhe da liste"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "La funzione `join` è un metodo della classe `string`.\n",
    "La `join` prende in ingresso una lista o una tupla di valori di tipo stringa e li concatena, utilizzando come separatore la stringa su cui si è chiamata la `join`.  \n",
    "**Attenzione**: tutti gli elementi della lista o tupla devono essere stringhe."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "a = (\"0\", \"1\", \"2\", \"3\")\n",
    "\n",
    "c = \"; \".join(a)\n",
    "\n",
    "print(type(c))\n",
    "print(c)\n",
    "\n",
    "b = [\"3\", \"2\", \"1\", 0]\n",
    "d = \"-\".join(b)\n",
    "\n",
    "print(d)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<span style=\"color:dodgerblue\">Modificare un singolo carattere della stringa data, usando il metodo `join`.</span>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "stringa = \"ciao mondi\"\n",
    "\n",
    "# risultato finale: stringa == \"ciao mondo\""
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### La funzione `zip`"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "La funzione built-in `zip` prende in ingresso due iterabili e restituisce un nuovo iterabile, i cui elementi sono coppie ordinate. Il primo elemento della prima collezione viene associato con il primo della seconda collezione, il secondo elemento della prima collezione con il secondo della seconda collezione e così via.\n",
    "\n",
    "I valori delle coppie ordinate si possono spacchettare utilizzando la sintassi nell'esempio."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "l1 = (1, 2, 3)\n",
    "l2 = [10, 20, 30]\n",
    "\n",
    "print(type(zip(l1, l2)))\n",
    "\n",
    "for couple in zip(l1, l2):\n",
    "    print(couple)\n",
    "\n",
    "for x, y in zip(l1, l2):\n",
    "    print(x, y)"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Insiemi\n",
    "\n",
    "Un insieme `set` è una collezione **non** ordinata di elementi *eterogenei*, che non ammette duplicati.  \n",
    "\n",
    "Un insieme `frozenset` è una collezione *immutabile* e **non** ordinata di elementi eterogenei, che non ammette duplicati.\n",
    "\n",
    "Gli insiemi si dichiarano utilizzando le funzioni built-in `set()` e `frozenset()`. In alternativa, con le parentesi graffe è possibile dichiarare un set.  \n",
    "\n",
    "<span style=\"color:orange\">**Attenzione**: in Python, le parentesi graffe aperte e chiuse `{}` non rappresentano un insieme vuoto bensì un dizionario vuoto.</span>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<span style=\"color:dodgerblue\">Usare la funzione built-in `set` per convertire una lista data in un insieme. Cosa si verifica?</span>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "lista = [0, 0.0, \"ciao\", 1, 0.5, \"ciao\", \"mondo\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "s2 = {1, 1, 1, 7, 14, 21}\n",
    "\n",
    "print(s2)\n",
    "\n",
    "s3 = frozenset(s2)\n",
    "\n",
    "print(s3)\n",
    "\n",
    "print(dir(s2))\n",
    "print(dir(s3))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "La classe `set` fornisce alcuni metodi per la modifica in-place di un insieme:\n",
    "- `add(`*elem*`)` permette di aggiungere l'elemento *elem* all'insieme, se già presente **non** viene duplicato\n",
    "- `remove(`*elem*`)` permette di rimuovere l'elemento *elem* dall'insieme\n",
    "- `clear()` restituisce l'insieme vuoto"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "s2 = {1, 1, 1, 7, 14, 21}\n",
    "s3 = frozenset(s2)\n",
    "\n",
    "print(s2)\n",
    "\n",
    "s2.add(3)\n",
    "\n",
    "print(s2)\n",
    "\n",
    "s2.remove(1)\n",
    "print(s2)\n",
    "\n",
    "s2.clear()\n",
    "print(s2)\n",
    "\n",
    "print(s3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "s = set()\n",
    "\n",
    "s.add(True)\n",
    "s.add(True)\n",
    "s.add(True)\n",
    "\n",
    "print(s)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<span style=\"color:dodgerblue\">Copiare gli elementi di un insieme dato in un altro e modificare quest'ultimo. Cosa si verifica?</span>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "s1 = {1, 1, 1, 7, 14, 21}"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Sugli insiemi si possono usare le classiche operazioni insiemistiche. Python fornisce i seguenti operatori:\n",
    "- `|`, `|=`: unione\n",
    "- `&`, `&=`: intersezione\n",
    "- `-`, `-=`: differenza insiemistica (attenzione: non è simmetrica)\n",
    "- `^`, `^=`: differenza simmetrica tra insiemi\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "a = {1, 2, 3}\n",
    "b = {1, 3, 6}\n",
    "\n",
    "print(\"a unito b:\", a | b)\n",
    "\n",
    "a |= {2, 7}\n",
    "\n",
    "print(\"a unito {2, 7}:\", a)\n",
    "\n",
    "print(\"a intesecato b:\", a & b)\n",
    "\n",
    "a &= {1, 2, 4} # a = a & {1, 2, 4}\n",
    "\n",
    "print(\"a intersecato {1, 2, 4}:\", a)\n",
    "\n",
    "a -= {2, 7}\n",
    "\n",
    "print(\"a meno {2, 7}:\", a)\n",
    "\n",
    "print(\"a meno b:\", a - b)\n",
    "\n",
    "print(\"b meno a:\", b - a)\n",
    "\n",
    "print(\"(a - b) | (b - a):\", a ^ b)\n",
    "\n",
    "a ^= b\n",
    "\n",
    "print(\"a = (a - b) | (b - a):\", a)\n"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Gli insiemi si possono confrontare con gli operatori di uguaglianza `==`, di inclusione `<=`, `>=`, e di inclusione stretta `<`, `>`.  \n",
    "Come per le liste e tuple, per capire se un elemento è contenuto o meno in un insieme o frozenset, è possibile usare le parole chiave `in` e `not in`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "s = {1, 2, 3}\n",
    "\n",
    "if 0 not in s:\n",
    "    print(\"no\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "N.B.: gli insiemi sono utili per \"pulire\" una lista da eventuali duplicati. Attenzione però che si perde l'ordinamento degli elementi."
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Dizionari"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Un dizionario `dict` è una collezione *eterogenea* di elementi chiave-valore **non** ordinati. Non ammette chiavi duplicate, ma gli elementi possono esserlo.  \n",
    "<span style=\"color:orange\">Le chiavi devono necessariamente essere oggetti *immutabili*.</span>\n",
    "\n",
    "Un dizionario si dichiara usando la funzione built-in `dict()` oppure usando le parentesi graffe, con i due punti a separazione di chiave e valore: `key : value`.\n",
    "\n",
    "La classe `dict` offre alcuni metodi per poter iterare sulle chiavi, sui valori, e sugli elementi del dizionario:\n",
    "- `keys()`\n",
    "- `values()`\n",
    "- `items()`"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<span style=\"color:dodgerblue\">Creare un dizionario eterogeneo in cui le chiavi spaziano tra gli oggetti immutabili visti precedentemente. Iterare poi sugli elementi e stamparli in forma chiave : valore.</span>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Come per liste, tuple, insiemi e frozenset, per capire se un elemento è contenuto o meno in un dizionario, è possibile usare le parole chiave `in` e `not in`.  \n",
    "<span style=\"color:orange\">**Attenzione**: `object in dictionary` restituisce `True` se `object` è una *chiave* di quel dizionario.</span>\n",
    "\n",
    "Siccome le collezioni di chiavi, valori ed elementi del dizionario sono iterabili, è possibile usare `in` e `not in` anche su queste."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "dizion = { 0 : \"ciao\", \"mondo\" : [2, 4], (0, 1) : 6 }\n",
    "\n",
    "print(0 in dizion)\n",
    "print(\"ciao\" in dizion)\n",
    "\n",
    "print(\"ciao\" in dizion.values())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "I valori di un dizionario si accedono interrogando la rispettiva chiave, per fare questo si usa l'operatore `[`$k$`]`, dove $k$ è una chiave.  \n",
    "In lettura, se la chiave non viene trovata, il codice genererà un'eccezione.  \n",
    "In scrittura, se la chiave non viene trovata, verrà creata una nuova entrata nel dizionario."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "dizion = { 0 : \"ciao\", \"mondo\" : [2, 4], (0, 1) : 6 }\n",
    "\n",
    "dizion[0] = \"altro\"\n",
    "dizion[\"mondo\"].append(6)\n",
    "\n",
    "print(dizion)\n",
    "\n",
    "dizion[2] = \"altro\"\n",
    "\n",
    "print(dizion)\n",
    "\n",
    "if 3 in dizion:\n",
    "    print(dizion[3])\n",
    "else:\n",
    "    print(dizion[3]) # dà eccezione"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### List comprehension\n",
    "\n",
    "La *list comprehension* (in italiano, comprensione di lista) è un metodo per creare liste, tuple, o insiemi, in modo dichiarativo.  \n",
    "\n",
    "Si definisce perciò una lista indicando innanzi tutto la \"forma\" dei valori che si vogliono ottenere, andando a specificare poi con un `for` da quale sovra-insieme prenderli, ed eventualmente aggiungendo condizioni con `if`.  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "lista3 = [True for x in range(6)] # list comprehension\n",
    "\n",
    "lista3 = []\n",
    "for x in range(6):\n",
    "    lista3.append(True)\n",
    "\n",
    "print(lista3)\n",
    "\n",
    "lista4 = [x // 2 for x in range(20) if x % 2 == 0]\n",
    "\n",
    "print(lista4)\n",
    "\n",
    "set2 = {i for i in range(3)}\n",
    "\n",
    "print(set2)\n",
    "\n",
    "dict2 = { i : i+1 for i in range(3) }\n",
    "\n",
    "print(dict2)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Le list comprehension possono essere annidate, in modo da creare liste di liste."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<span style=\"color:dodgerblue\">Usare una list comprehension per calcolare le tabelline dall'1 al 10, restituendole in una matrice (lista di liste).</span>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Questo modo di definire liste (ma anche tuple, insiemi, dizionari), è molto vicino al paradigma funzionale.\n",
    "\n",
    "Si possono usare le funzione built-in `filter` e la funzione built-in `map`, con una funzione $\\lambda$ appropriata per ricreare l'effetto di una list comprehension. \n",
    "\n",
    "Tuttavia `filter` restituisce un oggetto filter e `map` un oggetto map, che seppur iterabili, non sono liste. Si tratta di generatori, e una volta \"consumati\" non sono più utilizzabili."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "f = filter(lambda x: x % 2, range(10))\n",
    "\n",
    "print(f)\n",
    "\n",
    "m = map(lambda x: x * 3, range(10))\n",
    "\n",
    "print(m)\n",
    "\n",
    "mf = map(lambda x: x * 3, filter(lambda y: y % 2, range(10)))\n",
    "\n",
    "for x in mf:\n",
    "    print(x)\n",
    "\n",
    "lista = list(mf)\n",
    "\n",
    "print(lista)\n",
    "\n",
    "lista = list(filter(lambda x: x % 2, range(10)))\n",
    "print(lista)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<span style=\"color:dodgerblue\">Usare `map` e/o `filter` per creare la matrice di tabelline.</span>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Alcune utilità del modulo `random`"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "`random` è un modulo Python che fornisce utilità per generare numeri pseudo-random, secondo varie distribuzioni.  \n",
    "\n",
    "Fornisce inoltre una serie di funzioni definite su sequenze:  \n",
    "- `shuffle(`lista`)` mescola gli elementi della lista,\n",
    "- `choice(`lista`)` pesca un elemento dalla lista,\n",
    "- `sample(`lista, $k$`)` estrae un campione di $k$ elementi dalla lista."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from random import *\n",
    "# import random\n",
    "# random.shuffle(...)\n",
    "\n",
    "lista = [0, 0.0, \"ciao\", 1, 0.5, \"ciao\", \"mondo\"]\n",
    "\n",
    "seed(55) # random.seed\n",
    "\n",
    "print(randint(1, 5))\n",
    "\n",
    "shuffle(lista)\n",
    "\n",
    "print(lista)\n",
    "\n",
    "print(choice(lista))\n",
    "print(choice(lista))\n",
    "print(choice(lista))\n",
    "print(choice(lista))\n",
    "print(choice(lista))\n",
    "print(choice(lista))\n",
    "\n",
    "print(sample(lista, 2))\n",
    "\n",
    "print(lista)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<span style=\"color:dodgerblue\">Generare una lista di 10 codici fiscali pseudo-casuali, usando `randint` e `choice`. Poi estrarre un campione di due codici a caso tra quelli generati.</span>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import random\n",
    "\n",
    "# formato:\n",
    "# CCCCCCnnCnnCnnnC"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<span style=\"color:dodgerblue\">Rendere l'esercizio precedente replicabile.</span>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Funzioni"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Si può definire una funzione in Python usando la parola chiave `def` seguita dal nome della funzione e da un elenco di parametri."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Con la funzione di built-in `help`, possiamo visualizzare la documentazione della funzione."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def foo(par1, par2):\n",
    "    \"\"\"docs-\n",
    "    parameters:\n",
    "    (str) par1, (iterable) par2\n",
    "\n",
    "    returns\n",
    "    a tuple par1, par2\n",
    "    \"\"\"\n",
    "    par1 = par1.replace(\"a\", \"A\")\n",
    "    par2.remove(2)\n",
    "\n",
    "    return par1, par2\n",
    "\n",
    "help(foo)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<span style=\"color:dodgerblue\">Ispezionare il tipo della funzione e le sue proprietà e metodi.</span>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Il passaggio dei parametri è detto \"per oggetto\".  \n",
    "Se l'oggetto passato è immutabile, la funzione manipolerà una *copia* di quel parametro.  \n",
    "Se l'oggetto passato è mutabile, la funzione riceve un puntatore a quell'oggetto (come nel passaggio per riferimento), dunque potrà modificare l'oggetto."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "a = \"stringa\"\n",
    "b = [1, 2]\n",
    "\n",
    "print(a, b)\n",
    "\n",
    "# passaggio per oggetto\n",
    "res1, res2 = foo(a, b)\n",
    "\n",
    "print(a, b)\n",
    "print(res1, res2)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Liste di argomenti e dizionari di argomenti"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Gli operatori `*` e `**` servono a \"spacchettare\" liste e dizionari. Possono essere usati in combinazione con le funzioni per ottenere un numero variabile di parametri e di parametri chiave-valore."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def mia_funzione(*args, **kwargs):\n",
    "    print(\"Args:\", args)\n",
    "    print(\"Keyword args:\", kwargs)\n",
    "\n",
    "mia_funzione(0, [1, 2], \"tre\", 4, primo=\"ciao\", secondo=\"mondo\")\n",
    "\n",
    "print(\"-\" * 10)\n",
    "mia_funzione(0, *[1, 2], \"tre\", 4, primo=\"ciao\", secondo=\"mondo\")\n",
    "\n",
    "print(\"-\" * 10)\n",
    "mia_funzione(0, *[1, 2], \"tre\", 4, {\"primo\" : \"ciao\", \"secondo\" : \"mondo\"})\n",
    "\n",
    "print(\"-\" * 10)\n",
    "mia_funzione(0, *[1, 2], \"tre\", 4, **{\"primo\" : \"ciao\", \"secondo\" : \"mondo\"})"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Closure\n",
    "\n",
    "Le closure sono funzioni particolari che sono definite dentro altre funzioni. In questo modo possono accedere alle variabili dello scope \"padre\", anche dopo che quello scope è stato \"chiuso\"."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def closure():\n",
    "    GLOBAL = 2\n",
    "\n",
    "    def foo():\n",
    "        local = 1\n",
    "        print(local, GLOBAL)\n",
    "    \n",
    "    return foo\n",
    "\n",
    "my_function = closure()\n",
    "print(my_function)\n",
    "print(dir(my_function))\n",
    "\n",
    "my_function()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Le closure sono usate per creare dei decoratori da associare alle funzioni. In Python, un decoratore si associa a una funzione con l'operatore `@`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import time\n",
    "\n",
    "def eta(func):\n",
    "\n",
    "    def wrapper(*args):\n",
    "\n",
    "        start = time.time() * 1000\n",
    "\n",
    "        res = func(*args)\n",
    "\n",
    "        end = time.time() * 1000 - start\n",
    "\n",
    "        print(func.__name__, end)\n",
    "\n",
    "        return res\n",
    "\n",
    "    return wrapper\n",
    "\n",
    "@eta\n",
    "def foo(x):\n",
    "    time.sleep(x)\n",
    "    return 0\n",
    "\n",
    "result = foo(2)\n",
    "\n",
    "print(result)\n",
    "\n",
    "print(foo.__name__)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<span style=\"color:dodgerblue\">Creare un decoratore per effettuare la \"memoization\" dei risultati di una funzione (https://en.wikipedia.org/wiki/Memoization).</span>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Gestione eccezioni"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Per gestire le eccezioni, Python fornisce il costrutto `try-except-else-finally`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "try:\n",
    "    print(\"Codice che può generare eccezione\")\n",
    "    c = 10 + \"a\"\n",
    "except TypeError as t:\n",
    "    print(type(t))\n",
    "    print(dir(t))\n",
    "    print(t)\n",
    "except Exception:\n",
    "    print(\"altra eccezione\")\n",
    "else:\n",
    "    print(\"non ci sono state eccezioni\")\n",
    "finally:\n",
    "    print(\"codice che viene eseguito in ogni caso\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "I `try` possono essere annidati opportunamente."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "try:\n",
    "    f = open(\"mio_file\", \"r\")\n",
    "\n",
    "    try:\n",
    "        f.write(\"mia_stringa\")\n",
    "    except:\n",
    "        print(\"non riesco a scrivere\")\n",
    "    else:\n",
    "        print(\"sono riuscita a scrivere\")\n",
    "    finally:\n",
    "        f.close()\n",
    "\n",
    "except IOError as e: # e = IOError()\n",
    "    print(e)"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## OOP\n",
    "\n",
    "Le classi in Python derivano tutte da `object` e si definiscono usando la parola chiave `class`. Anche le classi sono oggetti."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Il metodo `__init__` è il costruttore della classe. Ogni metodo della classe prende come primo argomento obbligatoriamente un riferimento alla classe stessa, in genere chiamato `self`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "class MiaClasse(object):\n",
    "\n",
    "    par1 = 0\n",
    "    par3 = 10\n",
    "\n",
    "    def __init__(self, par1, par2):\n",
    "        self.par1 = par1\n",
    "        self._par2 = par2\n",
    "\n",
    "    def metodo(self, lista):\n",
    "        lista.append(self._par2)\n",
    "\n",
    "oggetto = MiaClasse(1, 2)\n",
    "\n",
    "lista = [10, 20, 30]\n",
    "oggetto.metodo(lista)\n",
    "\n",
    "print(lista)\n",
    "\n",
    "print(oggetto.par3)\n",
    "\n",
    "MiaClasse.par3 = 100\n",
    "\n",
    "print(oggetto.par3)\n",
    "\n",
    "oggetto2 = MiaClasse(3, 4)\n",
    "\n",
    "print(oggetto2.par3)\n",
    "\n",
    "oggetto3 = oggetto2\n",
    "\n",
    "oggetto2.par1 = 1\n",
    "\n",
    "print(oggetto2.par1)\n",
    "print(oggetto3.par1)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<span style=\"color:dodgerblue\">Ispezionare il tipo, le proprietà e i metodi della classe MiaClasse.</span>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Metaclassi\n",
    "\n",
    "Siccome in Python una classe è, a sua volta, un oggetto, ha un tipo. Il suo tipo è definito dalla sua metaclasse."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "class MetaClasse(type):\n",
    "    pass\n",
    "\n",
    "class MiaClasse(metaclass=MetaClasse):\n",
    "    pass\n",
    "\n",
    "print(type(MiaClasse))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Ereditarietà\n",
    "\n",
    "Si può definire una classe derivata specificando tra parentesi il nome della classe base.\n",
    "\n",
    "Per richiamare il costruttore della classe base, si usa `super().__init__`."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<span style=\"color:dodgerblue\">Estendere opportunamente i metodi della classe base `Human` alle classi derivate di esempio</span>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "class Human(object):\n",
    "    \n",
    "    hp = 10\n",
    "    faction = \"neutral\"\n",
    "\n",
    "    def __init__(self):\n",
    "        self.inventory = [\"food\"]\n",
    "\n",
    "    def eat(self):\n",
    "        if \"food\" in self.inventory:\n",
    "            self.hp += 5\n",
    "            self.inventory.remove(\"food\")\n",
    "\n",
    "    def attack(self, target):\n",
    "        target.hp -= 3\n",
    "\n",
    "    def __str__(self):\n",
    "        return f\"\"\"\n",
    "        Type: {self.__class__.__name__}\n",
    "        Faction: {self.faction}\n",
    "        Hit Points: {self.hp}\n",
    "        Inventory: {self.inventory}\n",
    "        \"\"\"\n",
    "\n",
    "class Paesant(Human):\n",
    "    pass\n",
    "\n",
    "class Ninja(Human):\n",
    "    pass\n",
    "\n",
    "class Samurai(Human):\n",
    "    pass\n",
    "\n",
    "\n",
    "# pippo = Paesant()\n",
    "# pluto = Ninja()\n",
    "# paperino = Samurai()\n",
    "# print(pippo, pluto, paperino)\n",
    "# pippo.eat()\n",
    "# pluto.attack(paperino)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Creare iterabili"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "I metodi `__iter__` e `__next__` sono usati per definire degli oggetti iterabili personalizzati.\n",
    "- `__iter__` restituisce l'iteratore stesso,\n",
    "- `__next__` restituisce l'elemento successivo della sequenza."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "class my_range_int(object):\n",
    "\n",
    "    def __init__(self, end, start=0):\n",
    "        self.end = end\n",
    "        self.current = start\n",
    "\n",
    "    def __iter__(self):\n",
    "        # return my_range_int(self.end, self.current)\n",
    "        return self\n",
    "\n",
    "    def __next__(self):\n",
    "        self.current += 1\n",
    "        if self.current >= self.end:\n",
    "            raise StopIteration\n",
    "        else:\n",
    "            return self.current\n",
    "\n",
    "\n",
    "oggetto = my_range_int(10)\n",
    "\n",
    "next(oggetto)\n",
    "next(oggetto)\n",
    "for x in oggetto:\n",
    "    print(x)\n",
    "\n",
    "# la seguente istruzione genererà una StopIteration exception\n",
    "# next(oggetto)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<span style=\"color:dodgerblue\">Creare un iterabile che restituisce i quadrati dei numeri fino a un limite specificato dall'utente.</span>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Python Standard Library\n",
    "\n",
    "https://docs.python.org/3/library/"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import sys\n",
    "\n",
    "def main(ARGS):\n",
    "\n",
    "    try:\n",
    "        primo = ARGS[0]\n",
    "    except:\n",
    "        print(\"il primo argomento non è stato trovato\")\n",
    "        return 1\n",
    "\n",
    "    return 0\n",
    "\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    ARGS = sys.argv[1:]\n",
    "\n",
    "    RETCODE = main(ARGS)\n",
    "\n",
    "    sys.exit(RETCODE)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# NumPy"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "NumPy è la libreria di Python per il calcolo numerico, ottimizzata per il calcolo matriciale.\n",
    "\n",
    "https://numpy.org/doc/stable/user/index.html"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "\n",
    "print(np.__version__)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Gli oggetti di base di NumPy sono gli array, i quali possono essere multi-dimensionali."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "a = np.array(42)\n",
    "b = np.array([1, 2, 3, 4, 5])\n",
    "c = np.array([[1, 2, 3], [4, 5, 6]])\n",
    "d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])\n",
    "\n",
    "print(a.ndim)\n",
    "print(b.ndim)\n",
    "print(c.ndim)\n",
    "print(d.ndim)\n",
    "\n",
    "print(a.shape)\n",
    "print(b.shape)\n",
    "print(c.shape)\n",
    "print(d.shape)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Il numero di dimensioni, così come la shape, possono essere forzati. Attenzione che la forma di un array deve combaciare con il numero dei suoi elementi."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "arr = np.array([1, 2, 3, 4], ndmin=3)\n",
    "\n",
    "print(arr)\n",
    "print(arr.ndim) \n",
    "print(arr.shape) \n",
    "\n",
    "arr = arr.reshape(2, 2) # non è inline\n",
    "\n",
    "print(arr)\n",
    "print(arr.ndim) \n",
    "print(arr.shape) \n",
    "\n",
    "# la seguente istruzione genererà una eccezione. perché?\n",
    "#arr = arr.reshape(1, 3)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Tramite l'operatore di slicing, si può accedere agli elementi dei NumPy array.  \n",
    "Attenzione: in questo caso, possono essere presenti più dimensioni, perciò è necessario specificare un indice per ciascuna di esse. \n",
    "\n",
    "Gli indici delle dimensioni sono separati da virgole: `[i, j, k]`"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<span style=\"color:dodgerblue\">Restituire il quinto elemento, da sinistra verso destra e dall'alto verso il basso, di ciascuno dei seguenti array.</span>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "b = np.array([1, 2, 3, 4, 5])\n",
    "c = np.array([[1, 2, 3], [4, 5, 6]])\n",
    "d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "L'assegnamento è sempre per riferimento, quindi è definito un metodo `copy` per copiare i dati in un nuovo array."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "a = np.zeros((2, 2))\n",
    "\n",
    "b = a\n",
    "\n",
    "b[0, 1] = 1\n",
    "\n",
    "print(a)\n",
    "print(b)\n",
    "\n",
    "c = a.copy()\n",
    "\n",
    "c[0, 1] = 17\n",
    "\n",
    "print(a)\n",
    "print(c)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Ci sono diversi modi di creare array in NumPy, con valori già inizializati."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Ad esempio, si possono creare array di zeri e array di uni, come in Matlab, specificandone la shape."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "a = np.zeros((2, 2, 2))\n",
    "\n",
    "print(a)\n",
    "\n",
    "b = np.ones((10, ))\n",
    "\n",
    "print(b)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Una versione ottimizzata di `range(n)` è presente in NumPy, con il nome di `arange(n)`:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "a = np.arange(10)\n",
    "\n",
    "print(a)\n",
    "\n",
    "a = np.arange(0, 1, 0.1)\n",
    "\n",
    "print(a)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Per creare array con uno specifico numero di elementi equispaziati in un determinato range, come in Matlab, è presente il metodo `linspace`. Il numero di elementi di default è 50."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "a = np.linspace(1, 10)\n",
    "\n",
    "print(a)\n",
    "\n",
    "a = np.linspace(0, 1, 5)\n",
    "\n",
    "print(a)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.1"
  },
  "orig_nbformat": 4
 },
 "nbformat": 4,
 "nbformat_minor": 2
}