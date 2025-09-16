from langchain_google_genai import ChatGoogleGenerativeAI

from crewai import Agent, Task, Crew, Process, LLM

import os 
os.environ["GOOGLE_API_KEY"] = "AIzaSyB5GbFHmmGrVjo35T5rm6MQ2Ghu1ZD9Vz8"
print("funcionou")

llm =  LLM(model='gemini/gemini-2.0-flash-lite', verbose=True, temperature=0.4, api_key = os.environ["GOOGLE_API_KEY"])

especialista_imagem = Agent(
    role = "Diretor de Arte",
    goal = "Analisar aparência estética do filme: maguaigem, fotografia, cores, figurino",
    backstory = "Especialista na parte estética de cinema",
    verbose = True,
    llm = llm
)

especialista_som = Agent(
    role = "Designer de Som",
    goal = "Analisar todos os aspectos sonoros do filme: trilha sonora, mixagem de áudio, efeitos sonoros, dialogos, dublagem(se for o caso)",
    backstory = "Especialista em áudio cinematrográfico",
    verbose = True,
    llm = llm
)

especialista_roteiro = Agent(
    role = "Crítico de Cinema",
    goal = "Avaliar qualidade das atuações dos atores, roteiro, enredo proposto, desenvolvimento dos arcos dramáticos, coerencia da narrativa",
    backstory = "Profissional especialista em crítica de cinema",
    verbose = True,
    llm = llm
)

especialista_redator = Agent(
    role = "Redator Chefe",
    goal = "Reunir todas as informações anteriores e escrever uma crítica de um filme de cinema. Escrever de forma clara e fluida de forma que pessoas num geral que não sejam grandes especialistas na área do cinema possam compreender o texto",
    backstory = "Profissional especialista em crítica de cinema",
    verbose = True,
    llm = llm
)

tarefa_critica_visual = Task(
    description = "Reunir informações sobre a qualidade dos aspectos visuais do filme Ressaca de Amor",
    expected_output = "Um resumo detalhado em português sobre os aspectos do visual do filme.",
    agent = especialista_imagem

)

tarefa_critica_audio = Task(
    description = "Reunir informações sobre a qualidade dos aspectos sonoros do filme Ressaca de Amor",
    expected_output = "Um resumo detalhado em português sobre os aspectos do audio do filme.",
    agent = especialista_som
)

tarefa_critica_atuacao = Task(
    description = "Reunir informações sobre a qualidade dos aspectos relacionados a atuação dos atores, enredo, desenvolvimento da narrativa, roteiro do filme Ressaca de Amor",
    expected_output= "Um resumo detalhado em português sobre os aspectos do roteiro do filme.",
    agent = especialista_roteiro
)

tarefa_redacao = Task(
    description = "Reunir as informações anteriores e gerar um texto crítico sobre o filme Ressaca de Amor",
    expected_output= "Um texto escrito em português contendo uma crítica cinematrográfica sobre o filme Ressaca de Amor.",
    agent = especialista_redator
)


crew = Crew(
    agents = [especialista_imagem, especialista_som, especialista_roteiro, especialista_redator],
    tasks = [tarefa_critica_visual, tarefa_critica_audio, tarefa_critica_atuacao, tarefa_redacao],
    process = Process.sequential,
    verboose = True
)

resultado = crew.kickoff()

print(resultado)

