#### Project architecture

I structured the project as a multi-app Django application so that each core area of functionality remains modular, reusable, and easier to maintain as development progresses.

Each app has a clearly defined responsibility:

- `home` handles landing pages and shared entry-point views
- `catalog` manages fragrance-related data such as brands and fragrances
- `club` is intended for discussion and community interaction
- `samples` manages weekly sample pack functionality
- `polls` supports fragrance voting logic
- `checkout` will manage Stripe subscription flow
- `profiles` will support user-specific account and membership information
- `quiz` is reserved for integrating and adapting previous quiz work into this project

This structure makes the project easier to scale, test, and document, while also meeting the requirement for multiple reusable apps within a Django full-stack project.

## Development Progress
First I focused on establishing a stable project foundation, ensuring the core structure was in place before building database-driven features.
---

## Continuing Development

After establishing the core project structure and navigation system, the next stage of development focused on introducing user authentication and preparing the platform for user-specific functionality.

Authentication is an essential requirement for the project because future features depend on identifying users. These include membership subscriptions, voting eligibility for fragrance polls, and personalised user profiles.

### Authentication Integration

Django’s built-in authentication framework (`django.contrib.auth`) was integrated to provide secure login and logout functionality.

Authentication routes were enabled by including Django’s authentication URL configuration within the project routing system:

`path("accounts/", include("django.contrib.auth.urls"))`

A custom login template was created to integrate the authentication form with the existing site layout:

`templates/registration/login.html`

This template extends the global `base.html` layout and renders Django’s authentication form.

### Navigation authentication logic

The navigation bar was updated to display login or logout options depending on whether the user is authenticated.

This behaviour is implemented using Django template logic:

`{% if user.is_authenticated %}`

Authenticated users see a **Logout** option, while unauthenticated users see a **Login** link.

### Authentication fixes

During testing several authentication-related issues were discovered and resolved:

- Django redirected users to `/accounts/profile/` after login, which caused a 404 error.  
  This was fixed by adding:

`LOGIN_REDIRECT_URL = "/"`

`LOGOUT_REDIRECT_URL = "/"`

- Logout initially produced an HTTP **405 Method Not Allowed** error because Django requires logout requests to use **POST** rather than **GET**.  
  The logout navigation element was therefore converted into a POST form submission.


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

## Weekly Pack Feature Development
### Weekly pack database structure

The first database-driven feature implemented in the project was the Weekly Packs system.

Two related models were created inside the `samples` app:

- `WeeklyPack` – represents a weekly fragrance discovery pack and stores the pack title, date range, publication status, and creation timestamp.
- `PackItem` – links individual fragrances to a weekly pack and stores the sample size for each item.

This relationship allows each pack to contain multiple fragrances while preventing the same fragrance from being added twice to the same pack.

### Admin management

Both models were registered within the Django admin interface so that pack content can be created and managed without requiring custom forms.

Using the admin panel, it became possible to:

- create a new weekly pack
- set the pack publication status
- define the week start and end dates
- add multiple fragrances to the pack using inline pack items

This approach allowed the database structure to be tested early before building user-facing interfaces.

### Public display of packs

Once the models were confirmed to work in the admin panel, the `/packs/` page was connected to the database.

The corresponding view retrieves all published weekly packs and passes them to the template using Django’s ORM:

`WeeklyPack.objects.filter(is_published=True)`

The template was then updated to dynamically render:

- the pack title
- the weekly date range
- the fragrances included in the pack
- the sample size for each fragrance

This replaced the original placeholder page with dynamic content rendered from the database.

### Navigation Evidence

The following screenshots confirm that the navigation system renders correctly across all placeholder pages:

- `docs/screenshots/nav-home.png`
- `docs/screenshots/nav-catalog.png`
- `docs/screenshots/nav-club.png`
- `docs/screenshots/nav-weekly-packs.png`
- `docs/screenshots/nav-vote.png`
- `docs/screenshots/nav-membership.png`

### Git workflow (commit discipline)
I used a “one commit per meaningful change” approach. This allows an assessor to clearly track the development process feature-by-feature, rather than in large unclear commits.

### Security and housekeeping
- Added `.gitignore` early to prevent committing:
  - `db.sqlite3`
  - `.env`
  - `__pycache__` and compiled python files
  - local environment folders
- Confirmed `db.sqlite3` is not tracked by Git.

### Bugs Fixed 

| Bug / Issue | Cause | Fix |
|------------|-------|-----|
| `TemplateDoesNotExist: home/home.html` | The home template did not exist in the global templates path expected by the view. | Created `templates/home/home.html` and confirmed the server rendered the Home page successfully. |
| `.pyc` / `__pycache__` files appearing in Git status | Compiled Python files were being tracked before `.gitignore` rules were applied. | Added ignore rules and removed compiled files from tracking. |

| `/accounts/profile/` redirect after login | Django redirects authenticated users to `/accounts/profile/` by default when no redirect is configured. | Added `LOGIN_REDIRECT_URL = "/"` and `LOGOUT_REDIRECT_URL = "/"` in `settings.py` to redirect users to the homepage. |
| Logout returned HTTP 405 Method Not Allowed | Django's logout view requires a POST request for security, but the navigation initially attempted to log out using a GET link. | Replaced the logout navigation link with a POST form submission in the navbar. |
| Login page rendering incorrectly | The login template initially contained misplaced navigation markup rather than the authentication form. | Recreated `templates/registration/login.html` using Django's authentication form structure. |

| Weekly packs did not render correctly on the public page | The template content block was closed before the pack loop, preventing the pack items from being rendered inside the layout. | The `{% endblock %}` tag was moved to the bottom of the template so the pack loop rendered correctly within the page content block. |