from github import Github

g = Github()
repo = g.get_repo("mqttjs/MQTT.js")

open_issues = repo.get_issues(state='open')
titles = [issue.title for issue in open_issues]
titles_text = '\n'.join(titles)

with open('issues.txt', 'w') as text_file:
  text_file.write(titles_text)