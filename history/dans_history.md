
# Pre-AI setup
I set up an Obsidian folder / vault specific for the campaign so I could track my ideas. All the files are markdown `_.md` files, so basically linkable plain text. 

As I worked on various mechanics, I found myself using ChatGPT to see if things were balanced, or what kind of plot hooks I could make. This involved having a `project` in ChatGPT with common instructions. However, ChatGPT didn't have access to the folder / files i was working in, and couldn't directly read or write files (I was copy/pasting back and forth). That got pretty annoying. 
# Local AI Setup
So I decided to start using Claude Code locally. I created a `claude.md` file and that was very useful at directly writing/iterating on files. It also nudged me to organize my file system better, creating ideas/, sessions/, npcs/ etc. But over time disliked having to sit with my laptop open babysitting an AI and approving every interaction. 
It did prompt me to optimize my agents.md into sub-folder-files, so that I wasn't loading all the context even when it wasn't relevant. 
## Using a repo with Github Cloud Agent
That's when I decided to switch to using github copilots cloud agent. I initialized my Obsidian folder into a git repo, and pushed it up to github. I then migrated `claude.md`   to `AGENTS.md` file. This is when things really took off. I was able to open a github issue with what I wanted done ("create 3 ideas for sessions where the players have to protect something to win"), assign it to copilot, and just wait. Usually in about 10 minutes a github PR was opened with exactly what I wanted. 

# And what did it cost you? 
$1.46. Almost nothing. 
