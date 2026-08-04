#!/usr/bin/env python3
"""
Redemption waterfall timeline builder.
Takes counterparty steps as input, produces formatted waterfall output.
Usage: Run interactively or import as module.
"""

def build_waterfall(steps):
    """
    steps = [
        {'entity': 'Depositor', 'action': 'Submit redemption request', 'days': 0, 'hours': None},
        {'entity': 'Tokenisation Platform', 'action': 'Process request', 'days': 1, 'hours': None},
        ...
    ]
    """
    print("\nREDEMPTION WATERFALL")
    print("=" * 60)

    total_days = 0
    for i, step in enumerate(steps, 1):
        days = step.get('days', 0)
        entity = step.get('entity', 'Unknown')
        action = step.get('action', '')
        hours = step.get('hours', None)
        source = step.get('source', 'G2 — not confirmed')
        evidence = step.get('evidence', 'G2')

        total_days += days
        time_str = f"T+{days}" if days > 0 else "T+0"
        if hours:
            time_str += f" ({hours}h)"

        print(f"Step {i}: {entity}")
        print(f"  Action: {action}")
        print(f"  Timeline: {time_str} business days")
        print(f"  Source: {source}")
        print(f"  Evidence: {evidence}")
        print()

    print(f"TOTAL: T+{total_days} business days from request to receipt")
    print("=" * 60)

    return total_days

if __name__ == '__main__':
    # Example usage
    example = [
        {'entity': 'Depositor', 'action': 'Submit redemption', 'days': 0, 'source': 'N/A', 'evidence': 'N/A'},
        {'entity': 'Protocol', 'action': 'Process withdrawal', 'days': 1, 'source': 'G2', 'evidence': 'G2'},
        {'entity': 'Custodian', 'action': 'Release assets', 'days': 2, 'source': 'G2', 'evidence': 'G2'},
    ]
    build_waterfall(example)
    print("\nNote: Replace example steps with actual confirmed counterparty data.")
    print("G2 steps require operator disclosure before evidence state = E.")
