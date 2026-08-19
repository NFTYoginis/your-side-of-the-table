# Your practice

Three position files, plus this one. Your positions, in your words. Nothing in this folder ships
filled in, and nothing in it leaves your machine.

---

## Why this folder exists

Jobs 2, 3, and 4 are unrunnable without your actual positions. A fee brief written around a fee the
tool guessed is worse than no fee brief — you won't notice the guess, and you may repeat it out loud.

So the rule ([`../../rules.md`](../../rules.md) § Empty-practice handling) is: while a file here is
still marked `[PLACEHOLDER]`, any job that needs it either **asks you the one question that fills it**
or **labels its output framework-only**. It never fills the blank itself.

## The three files

| File | Feeds | Fill it before |
|---|---|---|
| [`fee-position.md`](fee-position.md) | Jobs 1, 2, 4 | Any fee conversation |
| [`agreement-terms.md`](agreement-terms.md) | Jobs 1, 4 | Any buyer consult |
| [`what-i-see-locally.md`](what-i-see-locally.md) | Jobs 2, 3 | Any seller compensation conversation |

## How to fill them

**Ten minutes, once.** Open each, replace the `[PLACEHOLDER]` markers, delete the guidance comments if
they annoy you. Prose is fine. These are read by a model that will quote them back to you, not parsed
by a script.

**Answer as you actually are, not as you intend to be.** If you've been discounting to 2% whenever
anyone pushes, write 2%, not 2.5%. The gap between the number you say and the number you take is the
single most useful thing in this folder, and a file that records your aspiration hides it.

**Revisit quarterly, or after anything that changes your mind.** Date your edits. A position from
eighteen months ago that you've silently drifted from is worse than a blank.

## Check what's still empty

    python3 ../checks/practice-state.py

Prints which files are filled and which still carry placeholders. Exit 0 either way — an empty practice
folder is a normal day-one state, not a failure.

## Privacy

These files contain your business terms and your read of your market. They are not secrets, but they
are yours.

- **Don't commit filled-in versions to a public fork.** The shipped `[PLACEHOLDER]` versions are meant
  to be public; your filled versions are not.
- **Never put a client's name, address, or financial detail in here.** These files describe *your*
  practice, not your deals. See [`../../SECURITY.md`](../../SECURITY.md).
