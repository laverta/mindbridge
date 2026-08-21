# Compact State Schema

Use only the fields needed for the current interaction:

```json
{
  "state": "overloaded|stuck|activated|low_energy|reflective|stable|safety_review",
  "user_goal": "understand|calm|prioritize|start|finish|sleep|reflect",
  "pressure": "low|medium|high|unknown",
  "energy": "low|medium|high|unknown",
  "lens": "general|audhd_optional|three_layer_optional|plain_language",
  "primary_action": "one reversible next step",
  "completion_signal": "visible sign of completion",
  "safety_flag": false,
  "confidence": "low|medium|high",
  "updated_at": "ISO-8601 timestamp",
  "consent_scope": "session_only|user_approved_local|user_approved_shared",
  "retention": "session|until_user_deletes|unknown"
}
```

Do not treat this schema as a diagnostic score. `confidence` describes the assistant's understanding of the conversation, not the person's health.
Do not persist a state summary beyond the recorded `retention` scope. `user_approved_shared` is required before any summary can enter federation bridge traffic.
