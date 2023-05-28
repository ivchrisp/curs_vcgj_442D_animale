<h1>Git</h1>
Am creat branch-ul de development devel/IonVlad_lenes.
<br>
<h1>Aplicatia WEB Flask</h1>
Am implementat codul de baza pentru biblioteca si aplicatia in sine, care returneaza informatiile unui lenes
Aplicatia ruleaza local la http://127.0.0.1:5002
Comenzile suportare / respectiv, URL-urile valide se gasesc in fisierul README.md
<h1>Teste</h1>
Am adaugat directorul de teste in /app/tests, care contine fisierul python de testare a functiilor din biblioteca
PATH = /app/lib/biblioteca_animale
<h1>Jenkins</h1>
Jenkins a fost instalat iar serverul ruleaza local pe portul 8080; localhost:8080; 
Jenkins este configurat sa instaleze automat python, flask, modulul pytest si sa configureze venv(virtual environment)
in cazul in care acestea nu sunt detectate. Jenkins ruleaza si testele gasite in app/tests
Toate aceste operatini sunt efectuate in baza Jenkinsfile, activeaza_venv si activeaza_venv_jenkins
