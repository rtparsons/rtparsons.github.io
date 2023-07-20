---
layout: post
title:  "What does good code look like?"
date:   2023-07-17 20:00:00 +0000
categories: python
permalink: /what-is-good-code/
---

"Good code is thoughtful and written to achieve a specific goal"

I feel like all developers should have an answer to this question so this is mine (for now).

As I progress through my career the answer to this question has changed considerably. Early on it was likely a few pages of notes about how functions should be named, the max line length of functions, etc. Later, it may have referenced Uncle Bob or some coding philosophy, maybe even tests! More recently, it focuses on being able to pick up some existing code and work with it. Maybe in the future I will shorten it to simply "code".

You'll notice that as time goes on, my definition has become more terse. Good code comes in many shapes and sizes. It's often none of the things traditionally associated with clean code such as good naming or concise functions. It might be a messy 500-line function with 3-letter variable acronyms everywhere. The shared thread for me in all good code is that it was written with some thought and written to achieve a goal.

### Thoughtful

The first part of my definition is that whoever wrote it should have put some amount of thought and care into writing it. What I mean by thought is some consideration into how this code might fit into the code base, and how it might be used or expanded on in the future. 

This does not mean that the code needs to be covered by tests, follow any specific principles, or even be easy to understand. 

Consider a sorting algorithm. The code here is typically very nested with single letter variable names. This is fine here as the focus of these functions is performance. It is also unlikely to be modified heavily in the future so doesn't need to be easy to pick up and is best in its raw form.

Then consider some central business logic for choosing which customers should receive which marketing emails on a schedule. This code should hold very different properties from the sorting algorithm as it is highly likely to change in a variety of ways. Maybe in the future, it will need additional email providers, maybe it will need to include SMS, or maybe it will have to pass additional data. This code should be easy to understand and modify, with consideration paid to how those changes might look and be implemented.

### A specific goal

Here are some example goals:

- This code should be easily expandable to add extra reports in the future
- This code should have a clean interface and be hidden away so as not to detract from the rest of the system
- This code should be as thoroughly tested as possible as it cannot fail
- This code should allow us to move quickly and test this feature in production as quickly as possible

All of those are good goals. Where the trouble lies is if you try to target conflicting goals in one swoop, e.g. the classic this needs to be fast AND well tested AND extensible. Building real quality takes time so by moving quickly we comprimise the code and mix the meaning of what we produce.
This always leads to terrible code.
