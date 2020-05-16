# leetcode_answers

Compilation of all algorithm correct answers I have submitted to leetcode.

I used [leetcode-cli](https://github.com/leetcode-tools/leetcode-cli) to consume from leetcode's API, with this cookie trick [here](https://github.com/jdneo/vscode-leetcode/issues/478).

I also had to write my own script to get past the new throttling restrictions on the API (If you reader are a leetcode dev: Sorry for the nuisance).

## How to run

1. `npm install -g leetcode-tools/leetcode-cli`

2. `python get_all_questions.py -l python`

Note: To download 300 questions it will take around 15 minutes due to pause to avoid throttling.

## Stats

As of May 14th 2020:

```
$ leetcode stat -t -l algorithms

 Easy	119/353 ( 33.71 %)  ███████████░░░░░░░░░░░░░░░░░░░
 Medium	151/684 ( 22.08 %)  ███████░░░░░░░░░░░░░░░░░░░░░░░
 Hard	 30/285 ( 10.53 %)  ████░░░░░░░░░░░░░░░░░░░░░░░░░░
```