# Flyfood

Projeto PI2 - Curso de Sistemas de Informação - UFRPE
Este projeto foi desenvolvido para a disciplina de Programação de Inteligência 2 do curso de Sistemas de Informação da Universidade Federal Rural de Pernambuco (UFRPE).

## 🚀 Problema

O problema é definido por uma matriz onde os pontos de entrega são representados por valores diferentes de 0 e o ponto de origem e retorno (R) é sempre representado pelo valor 0. O drone só pode se mover na horizontal ou na vertical, e não pode se mover na diagonal.

Consulte **[Descrição](https://github.com/JoseEliodoro/Flyfood/blob/master/PISI2%20-%20Descri%C3%A7%C3%A3o%20do%20projeto%20-%20Flyfood.pdf)** para saber mais sobre o projeto.

## 📋 Entrada
A entrada é fornecida através de um arquivo texto onde cada linha representa uma linha da matriz.

O algoritmo lê uma matriz de entrada, representando a malha de entregas, onde cada posição representa um ponto de entrega ou não. Os pontos de entrega são representados por letras, enquanto os pontos não válidos são representados por zero. A origem e destino dos pedidos é representado pelo ponto R.

## 📋 Saída
O output é a ordem de entrega dos pacotes, representada por uma string, na qual a menor distância é percorrida.

## ⚙️ Testes


```
A B C D E
0 0 0 0 0
0 0 0 0 0
R 0 0 0 0
```
*Resultado: A menor rota é ['R', 'A', 'D', 'C', 'B', 'R'] com exatos 14 
dronômetros*

```
0 0 0 0 D
0 A 0 0 0
0 0 0 0 C
R 0 B 0 0
```
*Resultado: A menor rota é ['R', 'A', 'B', 'C', 'D', 'E', 'R'] com exatos 14 
dronômetros.*


## ✒️ Autores

Este projeto foi desenvolvido por mim.

## 📄 Licença

Este projeto está sob a licença (sua licença) - veja o arquivo [LICENSE.md](https://github.com/JoseEliodoro/Flyfood/blob/master/LICENSE) para detalhes.
