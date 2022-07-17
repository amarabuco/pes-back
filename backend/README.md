# pes-back

1. Construir imagem
   docker build -t pes-back .

2. Montar container
   docker run -it --name pes-back -v "$PWD":/usr/src/myapp -w /usr/src/myapp -p 8000:8000 pes-back bash

3. Executar aplicação
   uvicorn main:app --reload --host 0.0.0.0
