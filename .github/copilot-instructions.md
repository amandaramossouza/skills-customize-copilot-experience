# Descrição do Projeto

Este projeto é um site educacional para compartilhar tarefas de casa e exercícios de programação com estudantes. Os estudantes podem navegar, visualizar e baixar tarefas diretamente do portal.

## Estrutura do Projeto

- [`assignments/`](../assignments/) Cada tarefa de casa é armazenada em sua própria subpasta com uma estrutura consistente.
- [`templates/`](../templates/) Templates reutilizáveis para novo conteúdo
- [`assets/`](../assets/) Contém os recursos do site incluindo CSS, JavaScript, imagens e arquivos de configuração
- [`index.html`](../index.html) A página principal do site que serve como um portal estático para navegar e visualizar tarefas. O conteúdo é configurável através do arquivo [`config.json`](../config.json) para gerar dinamicamente listas e detalhes de tarefas.

## Diretrizes do Projeto

- Manter estilo consistente em todas as páginas
- Manter nomes de arquivos e pastas descritivos e organizados

## Padrões Educacionais

Ao gerar conteúdo para este projeto:

- **Focado em aprendizado**: Todo conteúdo deve ser projetado com objetivos de aprendizado claros e níveis de dificuldade apropriados
- **Amigável para estudantes**: Use linguagem clara e encorajadora que motiva os estudantes

## Conventional Commits

Este projeto segue a especificação de [Conventional Commits](https://www.conventionalcommits.org/) para manter um histórico de commits organizado e legível.

### Formato
`<type>(<scope>): <subject>`

### Tipos

- **feat**: Nova funcionalidade
- **fix**: Correção de bug
- **docs**: Mudanças na documentação
- **style**: Formatação, sem mudanças de código
- **refactor**: Refatoração de código
- **test**: Adição ou modificação de testes
- **chore**: Tarefas de manutenção, dependências

### Exemplos

- `feat(assignments): add new Python classes assignment`
- `fix(script): correct assignment sorting by due date`
- `docs(readme): update project structure documentation`
- `style(css): improve header styling consistency`
- `refactor(script): simplify assignment loading logic`
- `test(assignments): add tests for date filtering`
- `chore(deps): update Node.js dependencies`