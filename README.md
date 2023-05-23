Proiect site cu animale - exemplu personal Pantera

Am instalat toate librariile necesare(git,gedit,pytest,pip,jenkins,docker,etc) si am creat un director "Git" in care am lucrat la proiect. Continutul acestuia l-am pus intr-un repository pe GitHub(https://github.com/ivchrisp/curs_vcgj_442D_animale/edit/devel/AndreiBoro_animale). Am ales animalul "Pantera" si am completat toate functiile si fisierele cu trasaturile specifice acesteia(culoare(), hrana(), invelis corp() si biblioteca_animale, 442D_animale, etc). Am creat un host local pe 127.0.0.1:5001 unde pentru afisarea programului 442D_animale.py, iar cu extensia /pantera ni se vor afisare si trasaturile acestui animal. Pentru a testa ca nu sunt erori, am creat programul biblioteca_animale care prin intermediul pytest verifica daca fisierele sunt completate bine. Dupa ce am verificat ca totul este in regula, am conectat GitHub si am dat push documentelor updatate. In continuare am instalat Jenkins pentru testare. Am facut cont pe site-ul acestuia si am instalat Blue Ocean. Pentru testare in pipeline Jenkins am folosit un mediu virtual(venv) si flask. Pentru containerizarea cu Docker am instalat libraria si am creat un dockerfile pentru rulare.

Poze pentru a demonstra functionarea proiectului :

Pentru a crea acest proiect am avut nevoie de un director pe Ubuntu : $mkdir Git.
In acest director vom trage de pe GitHub un repository creat de noi. Mergem pe GitHub, intram pe contul personal, creem un repository gol in care includem un fisier README.md si un .gitignore cu template de Python. In CLI, dam un git status pentru a vedea daca directorul git este supervizat de git : $git status

$git clone https://github.com/andrei162/curs_vcgj_442D_animale.git $cd curs_vcgj_442D_animale $ls -la – pentru a vedea daca s-au clonat de pe GitHub fisierele necesare pentru acest repository – README.md si .gitignore. In .gitignore am comentat linia care exclude /lib de la adaugare in git. Acum putem crea fisierele necesare proiectului, cel mai important fiind 442D_animale.py care va face rutele si in el vom apela functiile necesare.
![image](https://github.com/ivchrisp/curs_vcgj_442D_animale/assets/132371318/609c813c-4996-4c80-bab5-08d787a53037)
![image](https://github.com/ivchrisp/curs_vcgj_442D_animale/assets/132371318/a810f4d6-0ecf-46e0-a116-d5493ef61b75)
![image](https://github.com/ivchrisp/curs_vcgj_442D_animale/assets/132371318/7045c98a-dace-4084-afc9-a9f52c257fb8)
In acest moment avem totul pregatit pentru a urca pe repository-ul remote, dar git-ul nu va sti unde sa incarce si nici nu cunoaste branch-ul creat de noi, deci va trebui sa configuram git-ul astfel :
$git config –global user.email(mail@domain.x) $git config –global user.name(name) $git config –credentials.helper store $git push – moment in care CLI ne va cere username-ul de pe git : AndreiBoro in cazul meu, si parola care consista intr-un token pe care il obtinem astfel : Intram pe GitHub, la setari , developer options, create token (classic) , token-ul este de tip hash – il salvam undeva secret si il introducem la parola in CLI, iar credentialele noastre vor fi salvate pentru acest repository.
![image](https://github.com/ivchrisp/curs_vcgj_442D_animale/assets/132371318/851663c7-5081-4033-94de-8c9d398d567a)


Aici vom scrie functii ca in exemplul de mai jos :
![image](https://github.com/ivchrisp/curs_vcgj_442D_animale/assets/132371318/4f2689e4-f059-4ef6-81a3-cf31c69f3b05)
Pentru fiecare route folosim : @app.route Exemple de rute + functie pentru a crea un link :
![image](https://github.com/ivchrisp/curs_vcgj_442D_animale/assets/132371318/e448f9b0-9dd9-46b2-acaa-082b8c51f37e)
La sfarsitul codului in Python, pentru a rula site-ul pe localhost, vom folosi :
app.run(host = "127.0.0.1", port = 5001). Acum vom putea porni programul 444D_flori.py din directorul /app astfel: $python3 444D_flori.py Programul va porni pe masina locala, putem accesa link-ul 127.0.0.1 :5001 SAU localhost :5001 si ne va duce pe o pagina simpla, cu un text, iar dac ape langa acest link mai punem si /lalea ne va duce catre alta pagina unde avem toate functiile cu return-urile respective.
![image](https://github.com/ivchrisp/curs_vcgj_442D_animale/assets/132371318/ad04c84e-4851-4df3-9650-e814a5fc08d3)
![image](https://github.com/ivchrisp/curs_vcgj_442D_animale/assets/132371318/c35d132b-ac5d-45ad-8099-e57a2092701c)
![image](https://github.com/ivchrisp/curs_vcgj_442D_animale/assets/132371318/6a4553a1-bbb3-4516-99fa-2985542887cb)
![image](https://github.com/ivchrisp/curs_vcgj_442D_animale/assets/132371318/7ee76542-1975-4587-b19a-f77154cfdc73)

In acest moment, branch-ul nostrum va fi urcat pe GitHub cu tot proiectul nostrum si putem trece la partea de testare.
Vom avea 6 teste in fisierul test_biblioteca_animale.py – culoare caine,pantera – hrana caine,pantera – invelis caine,pantera.
Alte comenzi utile pentru git : $git config –global alias.hist “log –oneline –graph –decorate –all” – ne creeaza o noua comanda pe care o apelam astfel : $git hist ; - ne va afisa istoricul branch-urilor si al commit-urilor. $git config –global --list

Testare Jenkins

Acum avem nevoie de testare cu Jenkins. Pentru a instala Jenkins trebuie sa urmam niste pasi : 
1.Verificare daca este instalat java : $java -version 
2.Instalare Java : $sudo apt install java 
3.$sudo apt install openjdk-11-jdk - pentru JavaJDK 11 
4.$sudo apt install curl 
5.$curl -fsSl | sudo tee /usr/share/keyrings/jenkins-keyring.asc > /dev/null 
6.$echo deb [signed-by=/usr/share/keyrings/Jenkins-keyring.asc] binary | sudo tee /etc/apt/source.list.d/Jenkins.list > dev/null 
7.$sudo apt-get update 
8.$sudo apt install jenkins -y 
9.$sudo systemctl status Jenkins
![image](https://github.com/ivchrisp/curs_vcgj_442D_animale/assets/132371318/f23e3228-23d7-4c67-bcc8-78f7a2d369b1)

Accesam localhost:8080 pe browser.
De aici va porni sistemul Jenkins – Prima data ne va cere Administrator password.Pentru aceasta va trebui sa accesam un fisier secret din calea urmatoare : 

$sudo cat /var/lib/Jenkins/secrets/initialAdminPassword – ne va da in consola CLI parola de tip hash pe care o introducem in Jenkins. De aici vom configura contul de Jenkins care se ocupa de acest repository si de aici putem crea teste pentru script-uri – Freestyle,Pipeline Install suggested Plugins Create account -> user = admin ; password = admin -> Save and Continue -> Manage Jenkins -> Install Plugins -> Available Plugins -> Search Blue Ocean -> Install
![Jenlins](https://github.com/ivchrisp/curs_vcgj_442D_animale/assets/132371318/9ff1f4ee-5fcc-4b23-8e81-16eba5aea680)

In browser, pe Jenkins – configuram Jenkins-ul astfel incat sa folosim un plugin – Blue Ocean care ne creaza o interfata unde vedem o diagrama cu toate stage-urile aplicatiei de test si astfel vedem eventuale erori – Jenkins-ul ne va spune unde si ce anume a picat si mesajele noastre din fisierul Jenkinsfile(daca exista).

Pentru a rula testarea automata cu Jenkins trebuie sa dam New Build, ii dam un nume,selectam Pipeline, selectam la Script -> Script from SCM - > Select SCM -> GitHub -> GitHub Repository URL -> Select branch -> /devel/andrei162_flori – selectam branch-ul pe care am lucrat -> Save.
![image](https://github.com/ivchrisp/curs_vcgj_442D_animale/assets/132371318/515591e4-a5d8-4f29-900e-ed2a0cb2ea9e)

![Jenkins Build](https://github.com/ivchrisp/curs_vcgj_442D_animale/assets/132371318/28c3896a-9f0e-4043-8d9e-5ff952cf6e94)

![Blue Ocean](https://github.com/ivchrisp/curs_vcgj_442D_animale/assets/132371318/b00ef5c3-0717-4061-a343-2dd259956740)

Daca modificam ceva in cod sau stergem/adaugam/modificam fisiere, va trebui urcat pe git astfel : 
$git status $git add SAU $git add . SAU $git add * $git commit -m “message” $git push
Astfel, cand dam iar Build in Jenkins, va lua iar repository-ul de pe GitHub si va rula cu noile modificari aduse in repository.

Containerizare cu Docker
Pentru containerizare folosim serviciile Docker – punem aplicatia cu toate dependintele si virtual environment pentru a putea rula intr-o « cutie » si nu pe masina noastra locala.
Pentru inceput, instalam docker :
1.sudo apt-get update 
2.sudo apt-get install ca-certificates curl gnupg lsb-release 
3.sudo mkdir -p /etc/apy/keyrings 
4.curl -fsSL | sudo gpg –dearmor -o /etc/apy/keyrings/docker.gpg 
5.echo “deb [arch=$(dpkg –print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] $(lsb_release -cs) stable”| sudo tee /etc/apt/sources.list.d/docker.list > /dev/null 6.sudo apt-get update 
7.sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin docker-compose 
Pentru a face acest lucru avem nevoie de un Dockerfile, o imagine cu nume – 442D_animale, un fisier pentru a porni serviciul docker – dockerstart.sh Continut repository :
![image](https://github.com/ivchrisp/curs_vcgj_442D_animale/assets/132371318/c8276db7-5d73-42c4-9b9d-1e76d331cbf5)

Dockerfile pentru aplicatie Flask in Python 3 :
![image](https://github.com/ivchrisp/curs_vcgj_442D_animale/assets/132371318/1d500ae4-d66b-4947-8734-4e729137e829)

Dockerstart.sh :
![image](https://github.com/ivchrisp/curs_vcgj_442D_animale/assets/132371318/9a174fcb-dce6-4a8a-9377-e02fea7aa62a)

Pentru a vedea imaginea de docker folosim: $sudo docker images
![image](https://github.com/ivchrisp/curs_vcgj_442D_animale/assets/132371318/99e7e5bd-bc1b-4141-8010-5ebff0a39170)

Pentru a rula in background containerul – adaugam -d in comanda de rulare a containerului.

Comenzi utile :

$sudo docker ps -a – Arata toate imaginile create si repository
![image](https://github.com/ivchrisp/curs_vcgj_442D_animale/assets/132371318/5d4bfbb3-3e6c-4a2b-b654-33ee9dc3140b)

$sudo docker start - comanda de start a unui container $sudo docker stop - comanda de stop a unui container
$sudo docker rm - comanda de stergere a unui container $sudo docker rmi <id_imagine> - comanda de stergere a unei imagini
$sudo docker export > <arhiva.tgz> - export imagine pe DockerHub $sudo docker import ) – import imagine de pe DockerHub
$docker login – ne conecteaza la contul de DockerHub 
$docker tag nume_docker_tag /<nume_imagine> - adaugare tag pentru o imagine 
$docker push /<nume_imagine> - incarcare container pe DockerHub 
$sudo docker attach – dupa run – ne activeaza request-urile pentru containerul care ruleaza – de exemplu accesam site-ul de flori – ne va afisa in consola request-ul

