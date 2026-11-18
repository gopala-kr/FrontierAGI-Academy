"""positioning_2027.py — Maestro against five kinds of competing product (our scoring).

Five buyer criteria weighted by what regulated enterprises said matters (Part 4, our
weights). Each competitor category and Maestro is scored 1-5. Prints the weighted score
and the criterion where Maestro leads or trails most. Standard library only.
"""
W = {"independent verification": 0.30, "model quality": 0.20, "integration": 0.20, "price": 0.15, "deployment control": 0.15}
C = {  # category: scores in W order
    "Maestro (gate + environments)":         [5, 3, 4, 3, 5],
    "Frontier lab agent platform":           [2, 5, 4, 4, 2],
    "Hyperscaler agent runtime":             [2, 4, 5, 3, 4],
    "Evaluation-only start-up":              [4, 2, 2, 4, 3],
    "Enterprise builder (Copilot/Zapier...)":[1, 4, 5, 4, 2],
}
ks = list(W)
res = sorted(((sum(W[k] * v for k, v in zip(ks, s)), n, s) for n, s in C.items()), reverse=True)
for sc, n, s in res: print(f"{n:40} {sc:.2f}")
me = C["Maestro (gate + environments)"]; best = {k: max(s[i] for n, s in C.items() if not n.startswith("Maestro")) for i, k in enumerate(ks)}
print("leads on: " + ", ".join(k for i, k in enumerate(ks) if me[i] > best[k]) + "; trails on: " + ", ".join(k for i, k in enumerate(ks) if me[i] < best[k]))
w2 = dict(W, **{"independent verification": 0.10, "model quality": 0.40})
print("if buyers weighted model quality 40% and verification 10%: " + max(C, key=lambda n: sum(w2[k] * v for k, v in zip(ks, C[n]))))
