для github
создаем ключи

<ПРЕДПОЧТИТЕЛЬНО более новый вариант ключей>
<НО НЕ РАБОТАЕТ В УБУНТЕ и много где еще>
ssh-keygen -t ed25519-sk -C "your_email@example.com" -f key_file_name

<ИСПОЛЬЗУЕМ>
///<старый вариант>
///ssh-keygen -t rsa -b 4096 -C "your_email@gmail.com" -f kts_python_rsa.key

будут созданы 2 файла
с открытым ключем (заканчивается на .pub)
и закрытый - как указали в опции <-f>

чтобы ходить на гитхаб по ssh и git работал через ssh добавляем алиасы
настройки для ssh по хостам 
(значки $ и пробелы после него -  в файл помещать не надо, это просто копия из теринала)
$ cd ~/.ssh/config
$ cat ./config 
$ Host wcdi
$     Hostname github.com
$     IdentityFile=/opt/users/wcdi/keys/key_wcdi_rsa.key
!!!обратите внимание, на своей машине работаем с приватным ключом

таким образом можно работать с несколькими репами в github, прописав алиасы и ключи


закачиваем публичный ключ на гитхаб, в соответствующий репозиторий (можно создать репу wcdi_*)
Your repo/Settings/Deploy keys
!!! Заливается все, что есть в публичном ключе, т.е. все что выдает 
$cat key_file_name.key.pub
не забываем поставить галочку на право писать в репу.


далее можно клонировать репу и работать нормально

git clone git@<ALIAS_FROM_SSH_CONFIG>:<GITHUB_USER_NAME>/<REPO_NAME>.git
пример для моего аккаунта на обучение
git clone git@wcdi:sirif/wcdi-school-backend.git
