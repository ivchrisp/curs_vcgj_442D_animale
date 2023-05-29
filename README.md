Proiect site cu animale - exemplu personal Tigru

Am instalat librariile necesare(git,gedit,pytest,pip,jenkins,docker) si am creat un director "git" in care am lucrat la proiect. Continutul acestuia l-am pus intr-un repository pe GitHub(https://github.com/ivchrisp/curs_vcgj_442D_animale/edit/devel/alexnic2000_animale). Am ales animalul "Tigru" si am completat toate functiile si fisierele cu trasaturile specifice acesteia(culoare(), hrana(), invelis corp() si biblioteca_animale, 442D_animale, etc). Am creat un host local pe 127.0.0.1:5001 unde pentru afisarea programului 442D_animale.py, iar cu extensia /tigru ni se vor afisa si trasaturile acestui animal. Pentru a testa ca nu sunt erori, am creat programul biblioteca_animale care prin intermediul pytest verifica daca fisierele sunt completate bine. Dupa ce am verificat ca totul este in regula, am conectat GitHub si am dat push documentelor updatate. In continuare am instalat Jenkins pentru testare. Am facut cont pe site-ul acestuia si am instalat Blue Ocean. Pentru testare in pipeline Jenkins am folosit un mediu virtual(venv) si flask. Pentru containerizarea cu Docker am instalat libraria si am creat un dockerfile pentru rulare.

Poze pentru a demonstra functionarea proiectului :

Pentru a crea acest proiect am avut nevoie de un director pe Ubuntu : $mkdir git. In acest director vom trage de pe GitHub un repository creat de noi. Mergem pe GitHub, intram pe contul personal, creem un repository gol in care includem un fisier README.md si un .gitignore cu template de Python. In CLI, dam un git status pentru a vedea daca directorul git este supervizat de git : $git status

$git clone https://github.com/andrei162/curs_vcgj_442D_animale.git $cd curs_vcgj_442D_animale $ls -la – pentru a vedea daca s-au clonat de pe GitHub fisierele necesare pentru acest repository – README.md si .gitignore. In .gitignore am comentat linia care exclude /lib de la adaugare in git. Acum putem crea fisierele necesare proiectului, cel mai important fiind 442D_animale.py care va face rutele si in el vom apela functiile necesare.

![image](https://github.com/ivchrisp/curs_vcgj_442D_animale/assets/128916149/c2016c36-7432-4c7f-8178-db57b3ec9448)

![image](https://github.com/ivchrisp/curs_vcgj_442D_animale/assets/128916149/cd113e91-38b9-44b2-99bc-13698c9aef77)


![image](https://github.com/ivchrisp/curs_vcgj_442D_animale/assets/128916149/04415b1d-e15b-437d-b475-b399d2ff608f)


![image](https://github.com/ivchrisp/curs_vcgj_442D_animale/assets/128916149/8877f1ef-dc38-4612-b852-8f89372beed3)



![image](https://github.com/ivchrisp/curs_vcgj_442D_animale/assets/128916149/618dc15d-d782-48c3-aad5-30155de18333)


![image](https://github.com/ivchrisp/curs_vcgj_442D_animale/assets/128916149/d6847b72-2f94-4a15-8b40-6b2aa1225029)


![image](https://github.com/ivchrisp/curs_vcgj_442D_animale/assets/128916149/725bd120-c0e2-4d86-9244-e9f3c133cc26)

![image](https://github.com/ivchrisp/curs_vcgj_442D_animale/assets/128916149/bd23305b-dc3a-4ce0-972d-5a78dbd9894d)



![image](https://github.com/ivchrisp/curs_vcgj_442D_animale/assets/128916149/8ac21ec7-8d50-468e-ba10-a70ef39c2288)


![image](https://github.com/ivchrisp/curs_vcgj_442D_animale/assets/128916149/bd9240a2-d072-4c74-a484-dbf512c09b16)



![image](https://github.com/ivchrisp/curs_vcgj_442D_animale/assets/128916149/62b27aa2-8b73-488b-bcb6-35364859caa6)




![image](https://github.com/ivchrisp/curs_vcgj_442D_animale/assets/128916149/3ac4b0e0-e507-41c3-ba89-73471de4c114)


![image](https://github.com/ivchrisp/curs_vcgj_442D_animale/assets/128916149/12525c56-be8a-493f-8583-2defd58128b1)


![image](https://github.com/ivchrisp/curs_vcgj_442D_animale/assets/128916149/5dfa9e2d-a82a-428d-89b0-731ad6dbfff4)



![image](https://github.com/ivchrisp/curs_vcgj_442D_animale/assets/128916149/e80ce896-9bab-48dc-9809-bdae6a5f00c7)



![image](https://github.com/ivchrisp/curs_vcgj_442D_animale/assets/128916149/f548dc46-5af2-4724-aa0a-1a4d942ce860)



![image](https://github.com/ivchrisp/curs_vcgj_442D_animale/assets/128916149/273be29f-8781-4ec4-a101-82e33c93b5dd)


![image](https://github.com/ivchrisp/curs_vcgj_442D_animale/assets/128916149/15ec3084-a808-44ae-a27c-776548f3ac12)


![image](https://github.com/ivchrisp/curs_vcgj_442D_animale/assets/128916149/804639e0-1fe5-47f0-a1e5-d6edda8446da)

![image](https://github.com/ivchrisp/curs_vcgj_442D_animale/assets/128916149/50bb2e14-d4d3-45f6-b0e4-021b0f3f45df)


![image](https://github.com/ivchrisp/curs_vcgj_442D_animale/assets/128916149/ae34f1fb-3ca6-42af-8fcd-abb27462dfc4)


![image](https://github.com/ivchrisp/curs_vcgj_442D_animale/assets/128916149/0a39b543-19f5-410f-b1fc-2df540a2141c)



Daca modificam ceva in cod sau stergem/adaugam/modificam fisiere, va trebui urcat pe git astfel : $git status $git add SAU $git add . SAU $git add * $git commit -m “message” $git push Astfel, cand dam iar Build in Jenkins, va lua iar repository-ul de pe GitHub si va rula cu noile modificari aduse in repository.

Containerizare cu Docker Pentru containerizare folosim serviciile Docker – punem aplicatia cu toate dependintele si virtual environment pentru a putea rula intr-o « cutie » si nu pe masina noastra locala. Pentru inceput, instalam docker : 1.sudo apt-get update 2.sudo apt-get install ca-certificates curl gnupg lsb-release 3.sudo mkdir -p /etc/apy/keyrings 4.curl -fsSL | sudo gpg –dearmor -o /etc/apy/keyrings/docker.gpg 5.echo “deb [arch=$(dpkg –print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] $(lsb_release -cs) stable”| sudo tee /etc/apt/sources.list.d/docker.list > /dev/null 6.sudo apt-get update 7.sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin docker-compose Pentru a face acest lucru avem nevoie de un Dockerfile, o imagine cu nume – 442D_animale, un fisier pentru a porni serviciul docker – dockerstart.sh Continut repository :


![image](https://github.com/ivchrisp/curs_vcgj_442D_animale/assets/128916149/e9eb2317-738e-4bfa-a151-b2a1be9996a8)



![image](https://github.com/ivchrisp/curs_vcgj_442D_animale/assets/128916149/0316c734-62f8-40db-9d81-b7ea4e49881e)



![image](https://github.com/ivchrisp/curs_vcgj_442D_animale/assets/128916149/7a64bae3-0e10-4000-a0ea-a7d4063431be)



![image](https://github.com/ivchrisp/curs_vcgj_442D_animale/assets/128916149/8e3c258a-c002-49fd-b067-da64c8534f41)


Comenzi utile :

$sudo docker ps -a – Arata toate imaginile create si repository
$sudo docker start - comanda de start a unui container
$sudo docker stop - comanda de stop a unui container 
$sudo docker rm - comanda de stergere a unui container 
$sudo docker rmi <id_imagine> - comanda de stergere a unei imagini 
$sudo docker export > <arhiva.tgz> - export imagine pe DockerHub $sudo docker import ) – import imagine de pe DockerHub $docker login – ne conecteaza la contul de DockerHub 
$docker tag nume_docker_tag /<nume_imagine> - adaugare tag pentru o imagine
$docker push /<nume_imagine> - incarcare container pe DockerHub $sudo docker attach – dupa run – ne activeaza request-urile pentru containerul care ruleaza – de exemplu accesam site-ul de flori – ne va afisa in consola request-ul






