# 🐞 Bug Bounty Hunt: Debugging Challenge

Unlock a secret reward by fixing intentional bugs in this Python project! Perfect for team competitions.

![Tests](https://github.com/yourusername/bug-bounty-event/actions/workflows/tests.yml/badge.svg)

## 👥 Team Workflow

### For Participants

1. **Fork the Repository**  
   Click "Fork" at top-right of this repo to create your team's copy

2. **Clone Your Fork**

```bash
git clone https://github.com/YOUR-USERNAME/bug_bouty_event.git
cd bug-bounty-event
```

3. **Create Team Branch**

```bash
git checkout -b team-awesome-name  # Replace with your team name
```

4. **Fix Bugs & Commit**

```bash
# Make changes in src/ and tests/
git add .
git commit -m "fix: corrected prime number logic"
```

5. **Push to Your Fork**

```bash
git push origin team-awesome-name
```

6. **Create Pull Request**
   - Go to **Pull Requests** tab in original repository
   - Select:  
     `base: main` ← `compare: team-awesome-name`
   - Add description of your fixes

### For Event Organizers

1. **Setup Protected Branch**

   - Require PRs to `main` branch
   - Enable "Require status checks to pass"

2. **Track Team Progress**
   - Label PRs with team names
   - Use GitHub Projects for tracking

## 🏆 Success Criteria

- Passing CI Tests (required for merge)
- Clean commit history
- PR description explaining fixes
- Secret gift revealed in final test run

## 🔍 How to Participate

```bash

# Fix code in src/magic_calculator.py and tests/test_magic.py
# Test iteratively:
python tests/test_magic.py

# When tests pass locally:
git push origin your-team-branch
```

## 📜 Rules

1. All work must be in team-named branches
2. No direct pushes to `main`
3. PRs must reference team members
4. Merge conflicts resolved via rebase

---

**Happy Team Debugging!** 👨💻👩💻✨
