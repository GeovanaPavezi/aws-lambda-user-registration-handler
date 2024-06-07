import json
import re

def lambda_handler(event, context):
    try:
        body = json.loads(event['body'])
        
        required_fields = ['name', 'email', 'age']
        for field in required_fields:
            if field not in body:
                return {
                    'statusCode': 400,
                    'body': json.dumps({
                        'message': f'Campos Faltandod: {field}'
                    })
                }
        
        name = body['name']
        email = body['email']
        age = body['age']
        
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return {
                'statusCode': 400,
                'body': json.dumps({
                    'message': 'Formato de email inválido'
                })
            }
        
        if not isinstance(age, int) or age <= 0 or age > 120:
            return {
                'statusCode': 400,
                'body': json.dumps({
                    'message': 'A idade precisa ser um número inteiro positivo menor ou igual a 120'
                })
            }
        
        age_in_days = age * 365
        
        response = {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Usuário cadastrado com sucesso',
                'user': {
                    'name': name,
                    'email': email,
                    'age': age,
                    'age_in_days': age_in_days
                }
            })
        }
    except ValueError as ve:
        return {
            'statusCode': 400,
            'body': json.dumps({
                'message': 'Formato de dados inválidot',
                'error': str(ve)
            })
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({
                'message': 'Erro do Servidor Interno',
                'error': str(e)
            })
        }
    
    return response
