This is an implementation of [GCRA](https://en.wikipedia.org/wiki/Generic_cell_rate_algorithm) for rate limiting based on Redis.

The code requires Redis version 3.2 or newer since it relies on [replicate_commands](https://redis.io/commands/eval/#replicating-commands-instead-of-scripts) feature.
