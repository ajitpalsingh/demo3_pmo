import openai

def prompt_engine(use_case, csv_text):
    prompt_templates = {
        "Financials": f'''
You are a financial analyst. Based on this Earned Value data, compute EAC for each project.
Highlight any budget breaches >5% and summarize in 3 bullet points for a steering committee.
Data:\n{csv_text}
''',
        "Timeline": f'''
You are a PMO analyst. Generate a traffic-light report identifying schedule slippage based on these dates and statuses.
Add a short summary for executive presentation.
Data:\n{csv_text}
''',
        "Resources": f'''
You are a resource planner. Based on this allocation data, suggest a 2-week reallocation plan that removes overloads on critical-path tasks without adding headcount.
Respect skillsets and PTO dates.
Data:\n{csv_text}
''',
        "Risks": f'''
You are a risk consultant. From this register, list the top 3 risks scored >7 with mitigation steps.
Also identify one systemic risk across the portfolio.
Data:\n{csv_text}
''',
        "RAID_Jira": f'''
You are a Gen AI risk advisor. From the RAID log and issue descriptions, infer 3 emerging risks that haven’t been logged but are likely.
Include probability, impact, and mitigation.
Data:\n{csv_text}
''',
        "Survey": f'''
You are a change manager. Based on this team survey data, write tailored communications:
1. VP-level summary (100 words, strategic)
2. PM update (bullet-style, actionable)
3. Analyst message (reassuring, informal tone)
Data:\n{csv_text}
'''
    }

    prompt = prompt_templates.get(use_case, "No prompt found.")
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']