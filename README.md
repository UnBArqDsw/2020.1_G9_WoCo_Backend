<h1 align="center">
    WoCo - Workout Controller
</h1>

**Número do Grupo**: 09<br>
**Código da Disciplina**: FGA0208-T01<br>

## Alunos
|Matrícula | Aluno |
| -- | -- |
| 17/0138551  | Bruno Henrique Sousa Duarte |
| 15/0122837  |  Davi Alves Bezerra |
| 17/0033112  |  Eugenio Sales Siqueira |
| 16/0151732  |  Ernando da Silva Braga |
| 13/0137995  |  Weiller Fernandes Pereira |

## Sobre 
Tendo em vista a dificuldade de gestão de treino por parte de praticamentes, principalmente, de musculação quanto a gestão da ficha de treinos, periodização e controla da evolução de cargas e métricas do corpo. O WoKo propõe-se a centralizar essas informações e disponibilizar um controle pleno e integral do treino dos usuários de musculação. A oportunidade de negócio encontra-se em tornar a percepção subjetica de esforço em um processo controlado e centralizado. 

A aplicação permite a adição de treinos categorizados por grupamentos muscular de acordo a necessidade/prescrição de um profisional. Também é possível realizar agendamentos para delinear períodos de determinadas variações de treino, bem como, registrar medidas para acompanhamento de evolução.

## Screenshots
Adicione 3 ou mais screenshots do projeto em termos de interface e funcionamento.

## Instalação 
**Linguagens**: Python<br>
**Tecnologias**: SQLAlchemy, Flask, SQLite3<br>
Descreva os pré-requisitos para rodar o seu projeto e os comandos necessários.
Insira um manual ou um script para auxiliar ainda mais.

### Como rodar o projeto
Na pasta Woco:
```Bash
docker-compose up --build
```

## Uso 
Acessar os endpoints da API a partir da porta 5000.

1. Instale o Docker.
2. Entre na pasta onde esta o projeto e rode ```docker-compose up```.
3. Abra localhost:5000 no seu navegador.

## Observações
1. O Flask é executado no modo de desenvolvimento e será recarregado automaticamente nas alterações do arquivo.
2. Use o requirements.txt para instalar bibliotecas no Python.
3. Rode ```docker exec -it flask-woco bash``` para entrar no contêiner do Docker.
4. Rode ```docker start|stop|logs -f flask-woco``` para controlar o contêiner do Docker e ver o log.
