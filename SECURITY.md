# Security

This repository is markdown files and three Python scripts. It has no server, no network calls, no
dependencies, no telemetry, and no build step. Most of what follows is therefore about **what you put
into it**, which is the actual risk surface.

---

## What never goes in these files

The practice folder describes *your business*, not *your deals*. Keep it that way.

**Never write into any file here:**

- A client's name, address, phone, or email
- A property address, listing number, or transaction identifier
- Anyone's financial detail — loan amounts, account numbers, pre-approval figures, proceeds
- A specific inspection report's contents attached to an identifiable property
- Anything you'd need someone's permission to repeat

**Instead, write patterns.** *"Entry-band buyers here are usually tight on cash at closing"* is the
useful form and carries nothing. *"The Hendersons at 14 Oak had $3k left after down payment"* is a
privacy problem sitting in a text file, and it is not more useful.

## Before you fork or publish

The `reference/your-practice/` files ship with `[PLACEHOLDER]` markers **on purpose** — the shipped
versions are meant to be public; your filled-in versions are not. Your fee, your floor, your flex
positions, and your read of your market are competitive information.

Check before you push:

    python3 reference/checks/practice-state.py

Every file reading `BLANK` means nothing of yours is in there. If any reads `ON FILE`, you are about
to publish your own positions — decide that deliberately. [`.gitignore`](.gitignore) carries commented
lines you can uncomment to keep a filled copy untracked in your working tree.

## What you paste into an AI assistant

Loading these files into a Claude Project, or any assistant, means your conversation goes to that
provider. That's true of every AI tool and it isn't specific to this repo, but two things follow:

- **Client detail you paste into the chat is client detail you've sent to a third party.** Anonymize.
  "My buyer" and "the ranch" work fine — every worked example in [`examples.md`](examples.md) is
  written that way deliberately.
- **Check your brokerage's policy.** Some have rules about AI tools and client information. That
  policy outranks anything here.

## Inspection reports and client documents

Job 5 runs on your client's inspection report. The report belongs to your client. Confirm you may
share its contents with a third-party service before you paste it, strip identifying detail when you
do, and prefer describing the findings over uploading the document.

## The scripts

Three, in `reference/checks/`. Python 3, standard library only. They read files in the repository and
print results — no network, no writes, no subprocesses, no installs. Read them before you run them;
they're short, and you should not take a stranger's word for that.

`practice-state.py` reads your filled-in position files in order to count placeholders. It prints
counts and filenames only, never contents.

## Reporting a problem

Open a GitHub issue. If it involves a real person's data, **do not put that data in the issue** —
describe the shape of the problem and leave the specifics out.

Realistic issues for a repo like this one: a rule that contradicts another rule, a check that passes
something it should catch, a claim in the README that
[`VERIFY.md`](VERIFY.md) can't substantiate, or a boundary in a skill file that has drifted toward
something an agent shouldn't say. All four are welcome, and the third and fourth are the valuable ones.
