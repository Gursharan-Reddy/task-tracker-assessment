# AI Guidance Rules (AGENTS.md)
1. [cite_start]**Validation First**: All incoming payloads must be validated against the schema before processing[cite: 101, 302].
2. [cite_start]**Business Logic**: Keep logic in the `services/` layer, not in routes[cite: 129, 157, 330, 358].
3. [cite_start]**Immutability**: Archived tasks cannot be modified or moved back to active without a "restore" action[cite: 42, 243].
4. [cite_start]**Consistency**: Use enums for `status` (todo, in_progress, done, archived) and `priority` (low, medium, high)[cite: 40, 41, 104, 241, 242, 305].