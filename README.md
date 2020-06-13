## 1 - Escreva um script em Python que recebe a URL de uma imagem, aplica um filtro de sua escolha (por exemplo: blur, enhance, etc), salva a imagem e a mostra pro usuário

- Importei e instalei as bibliotecas os, OpenCV e Numpy.

- Fiz a função download_image para realizar o download da imagem

-Abri a imagem com a função open_image utilizando a biblioteca cv2

- Procurei na internet como aplicar o filtro. Verifiquei que precisava entender o conceito de kernels é a estrutura para filtrar de imagens que trabalha com pixels, assim consegue percorrer toda a imagem e aplicar operações. Bom, peguei os valores do kernel no site https://image4.io/en/blog/how-to-apply-filters-to-images-using-python-and-opencv/ porque não compreende totalmente como posso fazer a definição deste valor. E criei a função apply_filter_blur. Fiz essa função para aplicar apenas o filtro blur. Então repensando como melhorar a escrita do código e para pode reutilizar novamente a função caso deseja-se utilizar um outro filtro. Criei a função apply_filter que poderia substituir a outra função, mas o objetivo é mostrar que poderia criar uma função para aplicar qualquer filtro na imagem e quando fosse chamar a função poderia definir o filtro desejado.

- Criei uma função para mostrar a imagem após a execução do código. Irá mostrar a imagem e clicando o 0 para a execução.

- Por último realizei a chamada das funções e salvei a imagem no formato original como image_antiga e a imagem com o filtro como image_com_filtro.

2. (Bônus) Faça um servidor, também em Python, que, recebendo a url de uma imagem, chama o script desenvolvido em (1)

3. (Bônus) Desenvolva um client em React que recebe uma url de input do usuário, faz requisições para o servidor (2), e mostra a imagem final. Se o seu filtro é parametrizável, deixe o usuário escolher esses parâmetros no front antes de aplicar o filtro

Referências:
https://docs.gimp.org/2.10/en/filters.html
https://flask.palletsprojects.com/en/1.1.x/

Entregue o código via repositórios Git (não esqueça de deixar público!)
