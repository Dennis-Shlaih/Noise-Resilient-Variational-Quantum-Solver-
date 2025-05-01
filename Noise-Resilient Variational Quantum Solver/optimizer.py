from scipy.optimize import minimize
from cost_function import compute_expectation
from ansatz import create_ansatz
def optimize_vqa(cost_fn, initial_params, method='COBYLA'):
    history = []
    def callback(params):
        cost = cost_fn(params)
        history.append(cost)
        print(f"Iter {len(history)} | Cost: {cost:.4f}")

    result = minimize(cost_fn, initial_params, method=method, callback=callback)
    return result, history

if __name__ == "__main__":
    cost_fn = lambda p: -compute_expectation(p, create_ansatz)

    initial = [0.1, 0.1] 
    result, history = optimize_vqa(cost_fn, initial)

    print("\nBest Parameters:", result.x)
    print("Final Cost:", result.fun)
