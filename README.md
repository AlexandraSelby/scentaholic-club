## Development Progress (Day 1)

Today I focused on establishing a stable project foundation, ensuring the core structure was in place before building database-driven features.

### What I implemented

#### Global layout and navigation
- Created a global `base.html` template to provide a consistent layout across the entire site.
- Added a reusable navbar include to support clear navigation from the start.
- Set up a global templates directory so templates can be shared across multiple apps consistently.

#### Multiple apps scaffolded (reusable components)
I created the following apps at the start of development to ensure each domain area remains modular and reusable:
- `home` (landing and navigation entry point)
- `catalog` (fragrance and brand catalogue)
- `club` (community discussion features)
- `samples` (weekly sample packs and subscriptions)
- `polls` (Fragrance of the Week voting system)
- `checkout` (Stripe subscription flow)
- `profiles` (user profile / membership state)
- `quiz` (planned integration of my previous fragrance quiz project)

#### Placeholder pages (navigation-ready)
To ensure I could visually test routing and layout early, I implemented placeholder views and templates for:
- Home
- Catalog
- Club
- Weekly Packs
- Vote
- Membership

These placeholders act as a working navigation skeleton and will be expanded into database-driven pages in the next development phase.

### Git workflow (commit discipline)
I used a “one commit per meaningful change” approach. This allows an assessor to clearly track the development process feature-by-feature, rather than in large unclear commits.

### Security and housekeeping
- Added `.gitignore` early to prevent committing:
  - `db.sqlite3`
  - `.env`
  - `__pycache__` and compiled python files
  - local environment folders
- Confirmed `db.sqlite3` is not tracked by Git.

### Bugs Fixed (Day 1)

| Bug / Issue | Cause | Fix |
|------------|-------|-----|
| `TemplateDoesNotExist: home/home.html` | The home template did not exist in the global templates path expected by the view. | Created `templates/home/home.html` and confirmed the server rendered the Home page successfully. |
| `.pyc` / `__pycache__` files appearing in Git status | Compiled Python files were being tracked before `.gitignore` rules were applied. | Added ignore rules and removed compiled files from tracking. |
