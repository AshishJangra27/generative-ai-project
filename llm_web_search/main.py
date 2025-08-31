from get_links import get_links
from scrape import scrape_links, initialize_logs
from cleaning import combine_logs
from llm import call_gemini, context_combine_prompt

topic = 'latest ai news for today'
links = get_links(topic)
log_folder = initialize_logs(topic)

scrape_links(links, save_logs=True, log_folder=log_folder)

context_from_logs = combine_logs(log_folder)

final_prompt = context_combine_prompt(context_from_logs, topic)

answer = call_gemini(final_prompt)

print(answer)




