from app.functions.errorhandler import errorhandler

class validator:
    def __init__(self):
        self.errors = []
        pass

    def validate_email(self, email):
        if email.find('@') == -1:
            return False
        else:
            return True
        
    def validate_password(self, password):
        
        if not (8 <= len(password) <= 16):
            self.errors.append("Senha tem que ter entre 8 e 16 caracteres.")
        
        if not any(char.isdigit() for char in password):
            self.errors.append("Senha deve conter pelo menos um número.")
        
        if not any(char.isupper() for char in password):
            self.errors.append("Senha deve conter pelo menos uma letra maiúscula.")
        
        if not any(char in "!@#$%^&*()-_=+[]{}|;:',<.>/?`~" for char in password):
            self.errors.append("Senha deve conter pelo menos um caractere especial.")

        if self.errors:
            raise errorhandler(self.errors)
        
        return True
    
    def validate_telefone(self, telefone):
        if not telefone.isdigit() or len(telefone) != 11:
            self.errors.append("Telefone deve ser um número de 11 dígitos contando com o DDD.")
        
        if self.errors:
            raise errorhandler(self.errors)
        
        return True