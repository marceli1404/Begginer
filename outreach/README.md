# CV Outreach

A scheduled Claude routine that emails my CV to up to 10 local businesses between
Edinburgh and Tranent every weekday morning, asking about part-time work.

- **What it does, step by step:** [`PLAYBOOK.md`](./PLAYBOOK.md). Edit the Settings
  table there to change the area or volume, or to pause it.
- **Businesses to never email:** [`do-not-contact.txt`](./do-not-contact.txt)
- **CV:** put it at `outreach/cv.pdf` on `main`. The routine sends nothing until it
  is there.

Each business is only ever emailed once, because the routine checks Gmail Sent mail
before sending. Every outreach email gets the `CV Outreach` Gmail label. A summary
of each run, including any replies, is emailed back to me.

> ⚠️ This repository is **public**, so anyone can read `cv.pdf`, and it stays in git
> history even if you delete it later. Use a version without your home address,
> date of birth or personal phone number, or make the repo private first.
> Show replies to a parent or guardian before meeting anyone.
