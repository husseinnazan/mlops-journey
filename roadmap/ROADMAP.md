# MLOps Engineering Roadmap — Full Reference

**Hussein Azan** — Nabatieh Governorate, Lebanon
**Goal:** Backend/cloud engineer first (Job #1), MLOps engineer after (Job #2/3)
**Started:** August 3, 2026 · **LU starts:** September 14, 2026 · **LU graduation:** ~mid-2029

**Standing rule:** Never self-study what LU is about to teach — this roadmap is sequenced to stay *ahead* of the degree, not duplicate it.

This version explains *why* each topic is here and what it actually covers — enough to study each one independently from its listed resource without needing anything clarified first. Treat it as the syllabus; the linked resources are the textbook.

---

## Timeline

Estimates, not commitments — LU exam periods and normal life will shift this right. Don't compress a later phase to "catch up."

| Phase | Duration | Rough window |
|---|---|---|
| Phase 1 — SWE Core | 6 wks | Aug 3 – ~mid Sep 2026 |
| Phase 1.5 — Frontend Basics | ~4–5 wks | mid Sep – late Oct 2026 |
| Phase 2 — Cloud & DevOps | ~10 wks | late Oct – early Jan 2027 |
| Phase 3 — Python for Data & ML | ~6 wks | early Jan – ~mid Feb 2027 |
| Phase 4 — AI Integration (RAG) | ~3–4 wks | ~mid Feb – ~mid Mar 2027 |
| **→ Job #1 application-ready** | | **~mid March 2027** |
| Phase 5 — ML Foundations | ~10–12 wks | Mar – ~Jun 2027 |
| Phase 6 — Deep Learning | ~10–12 wks | Jun – ~Sep 2027 |
| Phase 7 — Core MLOps Stack | ~12–14 wks | Sep – ~Dec 2027 |
| Phase 8 — Production ML Systems | ~10–12 wks | Dec 2027 – ~Mar 2028 |
| Phase 9 — Portfolio & Job Prep | ~8–10 wks | Mar – ~Jun 2028 |
| **→ Full MLOps readiness** | | **~Jun 2028** |

---

# Phase 1 — Software Engineering Core (6 weeks)

The goal of this phase isn't breadth for its own sake — every topic here is something StudyMind, the capstone, will actually use. If a topic doesn't show up in the capstone, it's not in Phase 1.

**1. Git & GitHub.** Version control — a record of every change ever made to a codebase, with the ability to branch off, experiment, and merge back without risking the working version. This isn't optional infrastructure; it's the thing every single job, every open-source contribution, and every collaboration runs on. What matters at this stage: committing in small logical chunks (not one giant commit per session), branching for anything experimental, and understanding merge vs. rebase well enough to not panic at a conflict.

**2. Bash.** Not a programming language you'll build apps in — a way to talk to the operating system and, critically, to *read* what other tools write. A Dockerfile's `RUN` lines are Bash. A GitHub Actions step is Bash. An AWS EC2 startup script is Bash. The goal isn't scripting mastery; it's fluency enough that none of those look like a black box.

**3. SQL window functions.** You already have SQL fundamentals — SELECT, joins, aggregates. Window functions are the next tier: `ROW_NUMBER()`, `RANK()`, running totals via `SUM() OVER (...)`, and `LAG()`/`LEAD()` for comparing a row to the one before or after it. This is the line between "can write a SELECT statement" and "can actually answer an analytical question with SQL" — and it shows up constantly in interviews.

**4. OOP (Object-Oriented Programming).** Structuring code around objects that bundle data and behavior together, instead of loose functions operating on loose variables. Matters here specifically because FastAPI, SQLAlchemy (the ORM you'll likely touch later), and most real Python codebases are built this way. Core ideas: classes, `__init__`, instance vs. class attributes, inheritance, and knowing when composition is the better choice over inheritance.

**5. Type hints.** Optional annotations (`def add(x: int, y: int) -> int:`) that don't change how Python runs but let your editor and tools like `mypy` catch a whole category of bugs before the code ever executes. Increasingly expected in professional Python codebases and required by FastAPI's own type-driven request/response validation.

**6. Foundational DSA.** Arrays, hash maps, linked lists, stacks/queues, trees, basic recursion. This isn't about becoming a competitive programmer — it's the shared vocabulary every technical interview assumes, and the daily NeetCode/Grind75 grind starting in Phase 1.5 builds directly on this foundation.

**7. Error handling (custom exceptions).** Real applications fail — a network call times out, a file doesn't exist, an API key is wrong. The difference between an amateur script and production code is whether failure is handled deliberately (specific exception types, meaningful messages, a decision about what happens next) or just crashes. StudyMind's retry logic on AI API calls depends directly on this.

**8. Context managers.** The `with` statement — `with open("file.txt") as f:` — and what it's actually doing: guaranteeing cleanup happens (closing a file, releasing a connection) even if an error occurs partway through. Writing your own via `__enter__`/`__exit__` or `contextlib` matters for anything that opens a resource and must reliably close it, including database connections.

**9. Decorators.** Functions that wrap other functions to add behavior without changing their code — logging, timing, authentication checks, and specifically the retry-on-failure decorator StudyMind uses around its AI API calls. Understanding `@decorator` syntax means understanding that functions are values in Python, passed around like any other object.

**10. JSON.** The universal data format for APIs. Every request StudyMind's frontend sends and every response the AI API returns is JSON. `json.dumps`/`json.loads`, nested structures, and the mapping between JSON types and Python types (this is where subtle bugs live — JSON has no tuple, no None vs. null confusion goes unnoticed).

**11. HTTP requests.** How to actually call an external API from Python — the `requests` library, status codes, headers, handling timeouts and failures. This is the mechanism behind calling the LLM API for StudyMind's summarization feature, and behind almost every backend service talking to another service.

**12. Unit testing.** Writing automated tests (`pytest`) that verify code behaves correctly — and specifically, mocking external calls (so tests don't actually hit the AI API every run) so StudyMind's test suite is fast, free, and doesn't depend on network access. This is also the literal gate that CI/CD in Phase 2 runs before allowing a deploy.

**Capstone — StudyMind:** AI-powered notes/study API. FastAPI + SQLite + LLM API integration (summarize notes, generate flashcards), custom exceptions, a retry decorator on AI calls, and pytest tests that mock the AI API. Every topic above maps directly onto a piece of this project — that's not a coincidence, it's the point.

---

# Phase 1.5 — Frontend Basics (~4–5 weeks)

Not a pivot to full-stack as the specialization — just enough breadth to also apply to full-stack junior postings, which are more numerous than backend-only roles at entry level. Basics only, on purpose.

**1. HTML.** The structure layer of every web page — semantic elements (`<header>`, `<nav>`, `<article>`, not just endless `<div>`s), forms, and how content is organized before any styling or behavior touches it.

**2. CSS.** The presentation layer — box model, flexbox and grid for layout, responsive design (so StudyMind's frontend works on a phone screen, not just a laptop). Not animation mastery, just competent, clean layout.

**3. JavaScript.** The behavior layer — how a page responds to clicks, fetches data, updates without a full reload. Core language fundamentals (variables, functions, arrays/objects, `fetch()` for calling an API) rather than framework-specific tricks yet.

**4. TypeScript.** JavaScript with type annotations layered on top — same relationship type hints have to Python. Catches a category of bugs (calling a function with the wrong shape of data) before the code runs, and is what StudyMind's actual frontend will be written in, not plain JS.

**5. React.** The framework that turns HTML/CSS/JS/TS into an actual interactive application — components, state, props, and how data flows from StudyMind's FastAPI backend into the UI. This is where the previous four topics stop being separate and start being one working frontend.

**Resources — one path, not a menu:** The Odin Project's Full Stack JavaScript path, but only three of its four courses: **Foundations → JavaScript → React**, in that order. Skip the **NodeJS/Databases** course inside that same path entirely — it's backend (Express, SQL), and Phase 1's FastAPI work already covers that ground; redoing it here in a different language would burn weeks for zero new skill.

TypeScript is the one real gap Odin leaves — its own TS coverage is thin. Pair it with the **official TypeScript Handbook** directly. That's a few hours of reading, not a course, so it doesn't turn this into a second parallel track — just a short detour partway through the React course, once components start needing typed props.

**Why not Full Stack Open instead:** it's a genuinely excellent course, but it assumes HTML/CSS/basic JS already, and its later parts (testing, GraphQL, CI/CD, containers) go well past "basics" and start duplicating Phase 2. Worth returning to later as an optional deep-dive on React specifically — not the right entry point for someone starting frontend from zero.

**Capstone:** React + TypeScript frontend for StudyMind — the actual interface a user would click through to add notes and get AI-generated summaries.

**DSA daily grind starts here** — 45–60 min/day, NeetCode 150 or Grind75, continues through Phase 2. Consistency over speed; this is a long parallel track, not a sprint.

---

# Phase 2 — Cloud & DevOps (~10 weeks)

Moved far forward from where a generic MLOps roadmap would put this, because deployment and cloud skills are exactly what Job #1 postings ask for — this phase is the single highest-leverage block in the whole roadmap for getting hired first.

**1. Docker.** Packaging an application and everything it needs to run (Python version, dependencies, system libraries) into a single portable image, so "works on my machine" stops being a real problem. Images, containers (a running instance of an image), Dockerfiles (the recipe for building an image), and docker-compose (running multiple containers — like StudyMind's API and its database — together). Non-negotiable; Kubernetes, CI/CD, and cloud deployment all assume you can already do this.

**2. Kubernetes fundamentals.** Once you have containers, you need something to actually run and manage many of them in production — restarting crashed ones, scaling up under load, routing traffic. Kubernetes is the industry-standard tool for that. Lightweight conceptual pass only here: pods (a running container or group of them), deployments (how many copies to keep running), services (how traffic reaches them). ~21.6% of real entry-level remote backend postings ask for it — conceptual fluency is the bar, not operational mastery.

**3. Go** (~2–3 weeks). Placed right after Docker/K8s while that context is fresh, because Kubernetes, Docker, Terraform, and Prometheus are all *written* in Go — reading their source or understanding their behavior gets meaningfully easier once Go syntax isn't foreign. A statically-typed, compiled language with a very different feel from Python (explicit error returns instead of exceptions, goroutines for concurrency). **Done-when:** rewrite one StudyMind endpoint in Go, just to prove the syntax has actually landed.

**4. CI/CD.** Continuous Integration / Continuous Deployment — automatically running tests and deploying code the moment it's pushed, instead of doing either by hand. GitHub Actions specifically: a YAML file that defines a pipeline (install dependencies → run pytest → build Docker image → deploy) that runs on every push. This is where Phase 1's unit tests stop being just "good practice" and become an actual gate nothing broken can pass through.

**5. AWS.** The cloud platform StudyMind actually deploys to. IAM (identity and access management — who/what can do what), EC2 (a virtual server to run things on), S3 (file/object storage), Lambda (running a function without managing a server at all). Stay inside the Free Tier throughout, and set a billing alarm on day one — this is the one place a mistake costs real money.

**6. AWS Certified Cloud Practitioner** (~$100, prep studied alongside the hands-on AWS work above). Not because certifications make careers on their own — because studying for it forces breadth across AWS services you'd otherwise skip entirely, and it's a genuine, checkable signal on an entry-level CV where you otherwise have little to prove cloud knowledge with.

**Resources — closest thing to a single source here:** TechWorld with Nana's YouTube channel covers Docker, Kubernetes, and CI/CD (GitHub Actions) as three separate but consistently-taught full courses — one instructor, not five disconnected tutorials. There's no true single mega-course for this phase the way Odin works for frontend, because Docker, Kubernetes, Go, and AWS are five unrelated vendor/language ecosystems, not one coherent stack. Go and AWS stay on their own dedicated sources regardless: *A Tour of Go* + *Learn Go with Tests* for Go, AWS Skill Builder's free tier for the Cloud Practitioner prep.

**Capstone:** Dockerize StudyMind, wire up GitHub Actions CI/CD, deploy live on AWS behind a real URL that redeploys automatically on every push.

---

# Phase 3 — Python for Data & ML (~6 weeks)

Sits after Phase 2 finishes, as its own full phase — not a side-track, not squeezed under another phase's hours. It's placed here rather than earlier because it has zero dependency on Phase 1.5 or Phase 2's tools, so nothing upstream needed to happen first; it's placed *before* Phase 4 specifically so RAG's embeddings and vector work in Phase 4 aren't hit cold.

**1. NumPy.** The foundational library for numerical computing in Python — arrays (fixed-type, far faster than Python lists for math), vectorized operations (applying an operation to a whole array at once instead of looping), and the underlying data structure that pandas, scikit-learn, and PyTorch are all built on top of. An embedding — the thing Phase 4's RAG pipeline is built around — is, mechanically, just a NumPy array.

**2. pandas.** The standard tool for working with tabular data in Python — DataFrames (think: a spreadsheet as a Python object), filtering, grouping, merging, handling missing data. This is what real-world "data cleaning" actually looks like in practice, and it's assumed knowledge the moment Phase 5's ML Foundations begins.

**3. Data cleaning.** Not a separate library, a skill: handling missing values, inconsistent formatting, duplicate records, and outliers before any model or analysis touches the data. In practice this is where most of the actual time in any real data task goes — models are the easy part.

**4. scikit-learn basics.** A first, real pass at the library Phase 5 goes deep on — fitting a simple model (like linear regression) on a real dataset, understanding the `.fit()` / `.predict()` pattern, and a first look at train/test splits, without yet covering the full evaluation and model-selection theory Phase 5 is dedicated to.

**Resources:** Kaggle Learn micro-courses (Python, Pandas, Intro to Machine Learning, Intermediate Machine Learning) for the core sequence, backed by a real dataset from Kaggle for the capstone below rather than each micro-course's toy examples alone.

**Capstone:** A small data-analysis notebook on StudyMind's own usage — clean and analyze real data the app generates (notes created over time, summary requests, flashcard generation counts) and answer 3–4 concrete questions about how it's actually being used. Same principle as every other phase's capstone: the skill gets applied to something real, not just exercises.

---

# Phase 4 — AI Integration for Backend (~3–4 weeks)

Sits directly after Phase 2 and 3 finish, and reuses tools from both — FastAPI/Docker/cloud deployment from Phase 2, vector/numerical intuition from Phase 3. This is a deliberately scoped, practical slice of "AI Engineering" — not the deeper agent-orchestration/evals stack that's genuinely senior-level territory, but the part that's now a real, current line item on backend job postings.

**1. LLM API basics.** Calling OpenAI's or Anthropic's API programmatically — authentication, structured outputs (getting the model to return data in a specific, parseable shape rather than free text), proper error handling and retry logic (reusing Phase 1's decorator pattern), and cost awareness (these calls cost real money per token, unlike a database query).

**2. RAG (Retrieval-Augmented Generation).** The pattern behind grounding an LLM's answers in your own data instead of just what it learned during training. Mechanically: turn documents into embeddings (numeric vectors capturing meaning), store them in a vector database, and when a question comes in, retrieve the most relevant chunks and hand them to the LLM as context before it answers. Chroma is the standard lightweight local-dev vector store to learn this with.

**3. Wrapping it as a real service.** Putting the RAG pipeline behind a FastAPI endpoint, containerizing it with Docker, and deploying it the exact same way Phase 2's project was — proving the RAG work isn't a one-off script but a properly deployed service like everything else.

**Milestone:** A small RAG-backed API — feed it a handful of documents, ask it questions, get grounded answers back — deployed live. A fourth, distinctly current portfolio piece.

---

## → By end of Phase 4, ready for:

Junior Backend/Full-Stack Engineer roles, cloud-leaning, remote — with StudyMind (FastAPI + React/TS + Docker + CI/CD + live on AWS + a RAG endpoint) as portfolio proof, plus the Cloud Practitioner cert as a signal.

**Not yet ready for:** MLOps roles specifically — no deep learning or model training yet. That's Phases 5–9.

---

# Phase 5 — ML Foundations (~10–12 weeks)

This is where the LU math (S1–S2 algebra, analysis, statistics) actually gets used for the first time — not abstractly, but as the literal mechanism behind the models being learned.

**1. Regression & classification.** Linear regression (predicting a number) and logistic regression (predicting a category) — the two simplest, most interpretable models, and the right place to build intuition for what "fitting a model" actually means before anything more complex.

**2. Tree-based models.** Decision trees, random forests, gradient boosting — a different family from regression, built on splitting data by rules rather than fitting a curve. Extremely common in real-world tabular-data jobs, often outperforming more complex models on exactly the kind of structured data a backend engineer would encounter.

**3. Model evaluation.** How to actually know if a model is good — train/test splits, cross-validation, and choosing the right metric for the problem (accuracy is often the wrong one; precision/recall, RMSE, and others matter depending on what's actually being predicted). Without this, a model's "it works" claim is unverifiable.

**4. Unsupervised learning basics.** Clustering (grouping similar data points without labeled answers) and dimensionality reduction — a smaller topic than the above, but necessary vocabulary for the field.

**Tooling:** scikit-learn end to end — this phase is where Phase 3's brief introduction to it becomes real fluency.

---

# Phase 6 — Deep Learning (~10–12 weeks)

Neural networks — the specific class of models behind essentially everything currently called "AI" in the news, and a genuinely different mental model from Phase 5's classical ML.

**1. Neural network fundamentals.** Layers, weights, activation functions, forward pass — what a network actually computes, mechanically, before any of the training machinery is layered on.

**2. Backpropagation & training loops.** How a network actually learns — computing gradients and adjusting weights to reduce error, iteration by iteration. This is the part that feels like magic until it's implemented once by hand.

**3. PyTorch.** The dominant deep learning framework in industry and research alike. Tensors (PyTorch's version of NumPy arrays, with GPU support and automatic differentiation built in), building a model as a class, the standard training loop pattern.

**4. Common architectures, at a survey level.** CNNs (image-oriented), RNNs/Transformers (sequence-oriented) — not deep expertise in any one, but enough to recognize which architecture a given problem calls for.

---

# Phase 7 — Core MLOps Stack (~12–14 weeks)

The actual center of the roadmap — everything before this was prerequisite. This is where "knows how to train a model" becomes "knows how to run models in production," which is the actual job.

**1. MLflow.** Experiment tracking — logging every training run's parameters, metrics, and resulting model, so "which version of the model is this, and how was it trained" always has a real answer instead of living in someone's memory.

**2. DVC (Data Version Control).** Git for datasets and models — the things Git itself handles badly because they're large binary files. Lets a specific model or dataset version be tied to a specific commit, the same way code is.

**3. Airflow.** Orchestrating pipelines — chains of steps (pull data → clean it → train a model → evaluate it → deploy it) that need to run on a schedule or in a specific order, with retries and monitoring if a step fails.

**4. Kubernetes, revisited at depth.** Phase 2 covered the lightweight conceptual pass; this is where it becomes operational — actually deploying and scaling ML workloads on it, not just being able to describe what a pod is.

**5. Terraform.** Infrastructure as Code — defining cloud infrastructure (servers, networking, databases) in version-controlled config files instead of clicking through a cloud console by hand, so infrastructure can be reproduced, reviewed, and rolled back like any other code.

---

# Phase 8 — Production ML Systems (~10–12 weeks)

The layer most self-taught paths skip entirely, and precisely the layer that separates "can build a model" from "can be trusted to run one in production."

**1. Monitoring.** Tracking a deployed model's real-world performance and behavior over time, not just its score on a test set at training time.

**2. Drift detection.** Recognizing when the real-world data a model sees in production has shifted away from what it was trained on — the single most common reason a previously-good model quietly gets worse.

**3. Scaling.** Handling more traffic and larger models without the system falling over — load balancing, caching, batching predictions.

**4. Retraining pipelines & CI/CD for ML.** Automating the loop of retraining a model on fresh data and redeploying it safely, applying Phase 2's CI/CD concepts specifically to models instead of just application code.

---

# Phase 9 — Portfolio & Job Prep (~8–10 weeks)

Same shape as the Job #1 prep at the end of Phase 4, but aimed at MLOps roles specifically this time, with the full stack behind it.

**1. Flagship MLOps projects.** Two or three complete, deployed projects that demonstrate the full pipeline — training, tracking, deployment, monitoring — not just a Jupyter notebook that ends at "the model works."

**2. Interview prep.** MLOps-specific interview patterns — system design questions about ML pipelines, not just generic DSA (though the daily grind from Phase 1.5 onward keeps that sharp too).

**3. Applications.** Targeting MLOps roles directly, with StudyMind's full evolution (backend → frontend → cloud-deployed → RAG-enabled) plus the Phase 9 flagship projects as the complete portfolio story.

---

## Job market data (target postings — Job #1)

AWS 33% · Python 26.4% · CI/CD 23.2% · SQL 21.6% · Kubernetes 21.6% · Docker 21.5% · Microservices 15.8% · JavaScript 15.5% · PostgreSQL 15.4%

**Java (23.2%) deliberately excluded** — enterprise/Java-shop roles are a different lane, not an oversight.