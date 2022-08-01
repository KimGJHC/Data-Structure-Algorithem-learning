def maxProfit(costPerCut, salePrice, lengths):
    max_profit = 0

    for sale_length in range(1, max(lengths) + 1):
        sale_price_per_rod = salePrice * sale_length
        profit = 0

        for rod_length in lengths:
            uniform_rods = rod_length // sale_length

            if uniform_rods > 0:
                extra_cut = 1 if rod_length % sale_length > 0 else 0
                total_cuts = uniform_rods - 1 + extra_cut

                costs = total_cuts * costPerCut
                revenues = uniform_rods * sale_price_per_rod

                if revenues > costs:
                    profit += revenues - costs

        if profit > max_profit:
            max_profit = profit

    return max_profit