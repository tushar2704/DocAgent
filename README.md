
# DocAgent - Intelligent Document Assistant

DocAgent is an intelligent document analysis system that combines the power of AI agents with RAG (Retrieval-Augmented Generation) capabilities. Built using CrewAI, this application allows users to upload PDFs and get intelligent responses to their questions about the document content.

## Features

- 📄 PDF document processing and analysis
- 🤖 Multiple specialized AI agents working together
- 💡 Intelligent question answering using RAG
- 🔍 Advanced semantic search using Nomic embeddings
- 🖥️ Clean and intuitive Streamlit interface

## Installation

1. Clone the repository:
```bash
git clone https://github.com/tushar2704/docagent.git
cd docagent
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Quick Start

1. Set up your environment variables:
```bash
export OPENAI_API_KEY="your-api-key"
```

2. Run the Streamlit application:
```bash
streamlit run ui/main.py
```

## Project Structure

```
docagent/
├── src/               # Core application code
│   ├── agents/        # CrewAI agents implementation
│   ├── core/          # Core functionality
│   └── utils/         # Utility functions
├── ui/                # Streamlit interface
└── tests/             # Test suite
```

## Usage

1. Launch the application using Streamlit
2. Upload your PDF document
3. Ask questions about the document content
4. Get intelligent responses from the AI agents

## Components

### AI Agents

- **Document Processor Agent**: Handles document ingestion and preprocessing
- **Query Agent**: Manages user queries and information retrieval
- **Research Agent**: Synthesizes information and generates responses

### Core Technologies

- **CrewAI**: Agent orchestration and task management
- **Nomic Embeddings**: Advanced text embedding generation
- **LlamaIndex**: Document processing and indexing
- **Streamlit**: User interface
- **LangChain**: Additional RAG capabilities

## Development

### Prerequisites

- Python 3.9+
- OpenAI API key
- Git

### Setting Up Development Environment

1. Install development dependencies:
```bash
pip install -r requirements-dev.txt
```

2. Run tests:
```bash
pytest tests/
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- CrewAI team for the amazing agent framework
- Nomic AI for their embedding model
- LlamaIndex team for document processing capabilities
- Streamlit team for the wonderful UI framework

## Support

For support, please open an issue in the GitHub repository or contact the maintainers.

## Roadmap

- [ ] Add support for more document formats
- [ ] Implement document comparison features
- [ ] Add memory capabilities to agents
- [ ] Enhance query processing with multi-hop reasoning
- [ ] Add document summarization features

## Citation

If you use this project in your research or work, please cite:

```bibtex
@software{docagent2024,
  author = {Your Name},
  title = {DocAgent: Intelligent Document Assistant},
  year = {2024},
  publisher = {GitHub},
  url = {https://github.com/tushar2704/docagent}
}