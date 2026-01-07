# 🎮 Game Price Comparer

A Python CLI application for querying and comparing game and DLC prices across multiple digital storefronts using a public REST API.

---

## 🇺🇸 EN-US

## Overview

**Game Price Comparer** is a command-line application built with Python that enables users to search for a game or DLC and automatically identify the lowest available price across multiple digital stores.

The application consumes an external REST API to retrieve up-to-date pricing data and presents the results in a clear and structured CLI output.

---

## Features

- Search for games or DLCs by name  
- Automatic title normalization  
- Identification of the store with the lowest current price  
- Display of the regular (average market) price  
- Direct link to the product page on the selected store  
- Simple and efficient CLI-based interaction  

---

## Technologies

- **Python 3**
- **Requests** — HTTP communication and API consumption  
- **JSON** — data parsing and validation  
- **Pytest** — unit testing and functional validation  

---

## Architecture & Design

- Modular project structure  
- Object-Oriented Programming (OOP) principles  
- Clear separation of concerns:
  - API communication  
  - Business logic  
  - CLI interaction  
- Designed for readability, maintainability, and testability  

---

## Usage

1. Run the application from the command line  
2. Select whether the search is for a **game** or **DLC**  
3. Provide the product name  
4. Receive structured output containing pricing and store information  

---

## Learning Outcomes

- Consuming and processing data from an external REST API  
- Working with endpoints, HTTP methods, and structured JSON responses  
- Designing a CLI-based application with clear responsibilities  
- Writing clean, modular, and testable Python code  
- Solving a real-world problem through software automation  

---

## Motivation

Manually checking multiple digital stores to find the best price for a game is repetitive and inefficient.

By leveraging the **IsThereAnyDeal** public API, this project automates the comparison process and delivers objective pricing information through a lightweight and user-friendly command-line interface.

---

## Scope & Limitations

- Focused exclusively on price comparison  
- No purchasing, authentication, or user account management  
- Dependent on the availability and accuracy of the external API  

---

## 🇧🇷 PT-BR

## Visão Geral

**Game Price Comparer** é uma aplicação de linha de comando desenvolvida em Python que permite consultar e comparar preços de jogos e DLCs em múltiplas lojas digitais de forma automatizada.

A aplicação consome uma API REST externa para obter dados atualizados de preços e apresenta os resultados de maneira estruturada e objetiva no terminal.

---

## Funcionalidades

- Busca por jogos ou DLCs pelo nome  
- Normalização automática do título  
- Identificação da loja com o menor preço disponível  
- Exibição do preço regular (média de mercado)  
- Link direto para a página do produto na loja correspondente  
- Interface CLI simples e eficiente  

---

## Tecnologias

- **Python 3**
- **Requests** — comunicação HTTP e consumo de API  
- **JSON** — parsing, validação e manipulação de dados  
- **Pytest** — testes unitários e validação funcional  

---

## Arquitetura & Design

- Estrutura de projeto modular  
- Aplicação de conceitos de Programação Orientada a Objetos (OOP)  
- Separação clara entre:
  - Comunicação com a API  
  - Regras de negócio  
  - Interface de linha de comando  
- Código focado em legibilidade, manutenção e testabilidade  

---

## Motivação

O processo de consultar manualmente diversas lojas digitais para encontrar o menor preço de um jogo é repetitivo e pouco eficiente.

Utilizando a API pública do **IsThereAnyDeal**, esta aplicação automatiza a comparação de preços e fornece informações objetivas por meio de uma interface de linha de comando simples e direta.
