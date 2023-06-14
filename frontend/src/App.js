import React, { useState } from 'react';
import {Container,
        Form,
        FormText,
        FormGroup, 
        Label, 
        Input, 
        Button,
       } from 'reactstrap';
import axios from 'axios';

function App() {

  const serverUrl = 'http://0.0.0.0:8000';

  const [formData, setFormData] = useState({
    name: '',
    cpf: '',
    address: '',
    loan_value: '',
  });

  const [message, setMessage] = useState('');

  const handleInputChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleMessage = (e) => {
    setMessage(e);
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    axios.post(`${serverUrl}/api/personal_loan/`, formData)
      .then(response => {
        setFormData({
          name: '',
          cpf: '',
          address: '',
          loan_value: '',
        });
        setMessage('Proposta enviada com sucesso.')
      })

      .catch(error => {
        setMessage('Algo deu errado.')
      });
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1 style={{textAlign: 'center'}}>
          Formulário de Empréstimo
        </h1>
      </header>
        <div className="centered-form-container">
          <Container>
            <Form onSubmit={handleSubmit}>
              <FormGroup>
                <Label for="name">
                  <h4>Nome:</h4>
                </Label>
                <Input id="name" name="name" placeholder="Insira o nome." value={formData.name} onChange={handleInputChange}/>
                <Label for="cpf">
                  <h4>Número de CPF:</h4>
                </Label>
                <Input id="cpf" name="cpf" placeholder="000.000.000-00." value={formData.cpf} onChange={handleInputChange}/>
                <Label for="address">
                  <h4>Endereço:</h4>
                </Label>
                <Input id="address" name="address" placeholder="Rua anonima, numero x, bairro y, UF." type="textarea" value={formData.address} onChange={handleInputChange}/>
                <Label for="loan_value">
                  <h4>Valor do Empréstimo: </h4>
                </Label>
                <Input id="loan_value" name="loan_value" placeholder="1000.00" type='number' value={formData.loan_value} onChange={handleInputChange}/>
              </FormGroup>
              <Button color="primary" >Enviar</Button>
              <FormText>
                {message}
              </FormText>
            </Form>
          </Container>
        </div>
    </div>
  );
}

export default App;
