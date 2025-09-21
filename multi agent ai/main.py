from pipeline import run_pipeline

def main():
    print("🚀 Multi-Agent AI Pipeline (Ollama)")
    user_input = input("\nEnter initial project idea / requirement: ")

    # set debug=True if you want to see all intermediate steps
    results = run_pipeline(user_input, debug=True)

    print("\n=== Pipeline Results ===")
    if isinstance(results, list):  # debug=True → list of (step, output)
        for step, output in results:
            print(f"\n[{step}]\n{output}")
    else:  # debug=False → final string
        print(results)

if __name__ == "__main__":
    main()
