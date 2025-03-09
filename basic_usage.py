from deep_creator import DeepCreator

def main():
    creator = DeepCreator(debug=True)
    
    # Активация ИИ (опционально)
    creator.enable_ai(api_key="your_api_key_here")
    
    project_structure = {
        "src": {
            "main.py": "# Основной код"
        },
        "README.md": "# Базовая документация"
    }
    
    creator.build_structure(project_structure)

if __name__ == "__main__":
    main()