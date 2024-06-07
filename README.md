# AWS Lambda - Registro de Usuário

Este projeto implementa uma função AWS Lambda para processar o registro de usuário através de uma solicitação POST. A função valida os dados recebidos, calcula a idade do usuário em dias e retorna uma resposta personalizada.

## Funcionalidades

- **Processamento de Solicitação POST:** A função Lambda processa os dados enviados através de uma solicitação POST.
- **Validação de Dados:** São validados os campos obrigatórios: nome, e-mail e idade.
- **Cálculo de Idade em Dias:** A idade fornecida é convertida em dias para fins informativos.
- **Resposta Personalizada:** Retorna uma resposta JSON com uma mensagem de sucesso e os dados do usuário registrados.
- **Tratamento de Erros:** Captura exceções para lidar com erros de validação de dados e erros internos do servidor.

## Como usar 

```json
{
  "name": "João da Silva",
  "email": "joao.silva@example.com",
  "age": 25
}
```
## Exemplo de resposta
```json
{
  "message": "Usuário registrado com sucesso",
  "user": {
    "nome": "João da Silva",
    "email": "joao.silva@example.com",
    "idade": 25,
    "idade_em_dias": 9125
  }
}
```

## Testar no Postman:

- Abra o Postman e crie uma nova solicitação POST.
- Insira o seguinte URL no campo de URL da solicitação: https://fsek3bntggjarycqernr4df36a0tjzrx.lambda-url.us-east-2.amazonaws.com/.
- Cole o payload JSON acima no corpo da solicitação.
- Envie a solicitação e verifique a resposta.

