output a topics.toml for each domain batch in the list @valid-domains.txt 

e.g. in /tools/seeds/
statistics-seed-v1.toml  with 10 topics.
economics-seed-v1.toml  with 10 topics.
... etc so on so forth...

NB: Each topic can have between (1-3) domains from the list @valid-domains.txt  and 7-12 relevant tags. Observe the @meta folders subfiles @batch-workflow.md @domain-taxonomy.md @kdos-entry-standard.md @output-validation-and-lint-rules.md @tagging-rules.md  for more details

Example of a single topic item from inside a seed file:

[[topics]]
topic = "Variance"
difficulty = "beginner"
domains = ["Statistics", "Mathematics"]
tags = ["dispersion", "variability", "squared-deviation", "descriptive-statistics"]