/**
 * Return the percentage change difference between two values.
 *
 * @param old_value - The old value.
 * @param new_value - The new value.
 * @return number - The percentage change as a percentage to one degree accuracy.
 */
export function percentageChange(old_value: number, new_value: number) {
    const difference = new_value - old_value
    const change = (difference / old_value) * 100
    return Math.floor(change * 10) / 10;
}