def water_jug_problem(jug1_capacity, jug2_capacity, target):
    jug1_current = 0
    jug2_current = 0
    while jug1_current != target and jug2_current != target:
        print(f"({jug1_current},{jug2_current})")
        if jug2_current == jug2_capacity:
            jug2_current = 0
        elif jug1_current == 0:
            jug1_current = jug1_capacity
        else:
            pour_amount = min(jug1_current, jug2_capacity - jug2_current)
            jug1_current -= pour_amount
            jug2_current += pour_amount
    print(f"({jug1_current},{jug2_current})")
    print("Solution Found!")

# Example usage
water_jug_problem(4, 3, 2)
