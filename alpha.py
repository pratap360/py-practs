# alpha/maximizer goes to left side
# beta/minimizer goes to right side
# working of the alpha-beta runing

# initial values of aplha & beta
MAX, MIN = 1000, -1000

# return optimal value for current player
# (Initially called for the root and maximizer)


def minimax(depth, nodeIndex, maximizingPlayer, values, alpha, beta):
    # Terminating condition i.e
    # leaf node is reached
    if depth == 3:
        return values[nodeIndex]

    if maximizingPlayer:
        best = MIN

        for i in range(0, 2):
            val = minimax(depth+1, nodeIndex*2+i, False, values, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)

            # Alpha best pruning
            if beta <= alpha:
                break

        return best
    else:
        best = MAX

        for i in range(0, 2):
            val = minimax(depth+1, nodeIndex*2+i, True, values, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)

            if beta <= alpha:
                break
        return best


if __name__ == "__main__":
    values = [3, 5, 6, 9, 1, 2, 0, -1]
    print("The optimal value is :...", minimax(0, 0, True, values, MIN, MAX))
