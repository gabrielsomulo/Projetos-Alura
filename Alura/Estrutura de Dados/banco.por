programa {
  real reais, dolar, taxa_de_cambio

  funcao inicio() {
    escreva("\n Insira o valor em real R$: \n")
    leia(reais)
    escreva("\n Insira o valor da taxa: \n")
    leia(taxa_de_cambio)

    dolar = converter_real(reais, taxa_de_cambio)
    
    escreva("Com a taxa atual, o valor em dólares é: " + dolar)

  }

  funcao real converter_real(real reais, real taxa_de_cambio){
    real resultado = reais/taxa_de_cambio
    retorne resultado
  }
}
