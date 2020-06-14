## 1 - Escreva um script em Python que recebe a URL de uma imagem, aplica um filtro de sua escolha (por exemplo: blur, enhance, etc), salva a imagem e a mostra pro usuário

- Importei e instalei as bibliotecas os, OpenCV e Numpy.

- Fiz a função download_image para realizar o download da imagem

- Abri a imagem com a função open_image utilizando a biblioteca cv2

- Procurei na internet como aplicar o filtro. Verifiquei que precisava entender o conceito de kernels que é uma estrutura para usar filtros de imagens que trabalha com pixels, assim consegue percorrer toda a imagem e aplicar operações. Bom, peguei os valores do kernel no site https://image4.io/en/blog/how-to-apply-filters-to-images-using-python-and-opencv/ porque não compreende totalmente como posso fazer a definição deste valor. E criei a função apply_filter_blur. Fiz essa função para aplicar apenas o filtro blur. Então repensando como melhorar a escrita do código e para pode reutilizar novamente a função caso deseja-se utilizar um outro filtro. Criei a função apply_filter que poderia substituir a outra função, mas o objetivo é mostrar que poderia criar uma função para aplicar qualquer filtro na imagem e quando fosse chamar a função poderia definir o filtro desejado.

- Criei uma função para mostrar a imagem após a execução do código. Irá mostrar a imagem e clicando o 0 para a execução.

- Por último realizei a chamada das funções e salvei a imagem no formato original como image_antiga e a imagem com o filtro como image_com_filtro.

- Criei um arquivo ex01.py para executar o script das chamadas das funções para fazer download a img e aplicar o filtro

## 2. (Bônus) Faça um servidor, também em Python, que, recebendo a url de uma imagem, chama o script desenvolvido em (1)

- Importe o Flask e o json

- Criei uma rota com o método Post para o download de imagem. Eu mandei um json com uma chave url e a url no valor da chave.
  Para chamar a rota:

```
python3 sever.py

POST {"url": "url_image"} http://127.0.0.1:5000/download-image

```

- Fiz uma função no arquivo url_image chamada get_image_name para retornar o nome da imagem.

- Criei uma rota para mostrar a imagem na tela chamada show_image.
  Para chamar a rota:

```
python3 sever.py
name_image.jpg é retornado na rota de download
GET http://127.0.0.1:5000/name_image.jpg

```

- Criei um arquivo chamado index.html para redenrizar a imagem para o usuário.

- Criei outra função para fazer download da imagem utilizando a biblioteca urllib no lugar da chamada de sistema wget.

- Criei uma rota para mostrar a imagem com o filtro paa o usuário chamada apply_filter.

```
python3 sever.py
name_image.jpg é retornado na rota de download
GET http://127.0.0.1:5000/blur/name_image.jpg

```

## 3. (Bônus) Desenvolva um client em React que recebe uma url de input do usuário, faz requisições para o servidor (2), e mostra a imagem final. Se o seu filtro é parametrizável, deixe o usuário escolher esses parâmetros no front antes de aplicar o filtro

- Criei um App react utilizando o npx create-react-app my-app, assim apenas adicionei um component chamado UrlButton que irá receber uma url e ao clicar no botão ele irá enviar para o backend pela função callApiBluFilter que irá retornar a img com o filtro blur aplicado.

## Como executar

Para executar o frontend:

```bash
cd front-app
npm i
npm start

```

Você deve inserir uma url de imagem no formato jpg

Para executar o backend

```bash
pip3 install flask
pip3 install Pillow
pip3 install opencv-python
pip3 install numpy

python3 server.py
```

## O que pode ser melhorado no código

- Nos códigos python

```python
# Na função usada para pegar o nome da imagem esta apenas para jpg
# podendo ser uma lista ['jpg', 'png', 'jpeg',...] assim funcionará para
# todos os formatos
def get_image_name(url):
    url_splited = url.split('/')
    for item in url_splited:
        if '.jpg' in item:
            return item

## também na funcao de download se colocarmos
## um try catch irá evitar erro de url que não são imagem ou
## erros no download
def download_image2(url):
    try:
      name_image = get_image_name(url)
      urlretrieve(url, f"static/{name_image}")
    except Exception as err:
      return err

# No servidor flask podemos criar algumas funções para reutilizar código
# que estão muito repetitivos
```

- No front end podemos separar melhor os components em mais componentes com responsabilidades únicas

## Referências utilizadas:

https://docs.gimp.org/2.10/en/filters.html

https://flask.palletsprojects.com/en/1.1.x/

https://stackoverflow.com/questions/46785507/python-flask-display-image-on-a-html-page

https://image4.io/en/blog/how-to-apply-filters-to-images-using-python-and-opencv/

https://pt-br.reactjs.org/docs/create-a-new-react-app.html
