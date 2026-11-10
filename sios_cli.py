"""
SIOS Labs: Command Line Interface (CLI) Parser Tool Boilerplate
Core Concept: An open-source interface framework that parses systemic natural language 
commands into discrete execution instructions for the SIOS cognitive kernel.
"""

import sys
import argparse

class SIOSCLIParser:
    """The interface layer managing ambient natural language parsing into discrete system intents."""
    def __init__(self):
        self.version = "0.1.0-stealth"

    def process_command(self, human_prompt: str):
        """Mock-tokenizes human language prompts into explicit kernel operational directives."""
        clean_prompt = human_prompt.strip().lower()
        print(f"\n🛰️ [SIOS Terminal Input]: \"{human_prompt}\"")
        print("🧠 Tokenizing system intent paths...")

        # Intent classification matrix
        if any(keyword in clean_prompt for keyword in ["find", "locate", "search", "where is"]):
            self._route_to_subsystem("Semantic File System (SFS)", "QUERY_VECTOR_NODE", clean_prompt)
        elif any(keyword in clean_prompt for keyword in ["build", "compile", "run", "deploy"]):
            self._route_to_subsystem("Autonomous Developer Mesh", "EXECUTE_SANDBOX_ENV", clean_prompt)
        elif any(keyword in clean_prompt for keyword in ["status", "resource", "cpu", "memory"]):
            self._route_to_subsystem("Cognitive Kernel Manager", "FETCH_TELEMETRY_RING", clean_prompt)
        else:
            self._route_to_subsystem("Ambient Processing Engine", "PROBABILISTIC_LLM_FALLBACK", clean_prompt)

    def _route_to_subsystem(self, subsystem: str, kernel_directive: str, payload: str):
        print(f"  └── ⚡ Routing Target : [{subsystem}]")
        print(f"  └── 🛠️ Kernel Opcode : {kernel_directive}")
        print(f"  └── 📦 Payload Context: \"{payload}\"")
        print("  └── Status         : Ready for local execution enclave loop.")

def main():
    parser = argparse.ArgumentParser(
        description="SIOS Command Line Interface (CLI) Engine - Operational Infrastructure Framework"
    )
    # Argument parser hooks
    parser.add_argument(
        "-p", "--prompt", 
        type=str, 
        help="Pass a high-level natural language instruction to the SIOS Kernel layer."
    )
    parser.add_argument(
        "-i", "--interactive", 
        action="store_true", 
        help="Spins up a persistent interactive workspace session shell."
    )

    args = parser.parse_args()
    sios_cli = SIOSCLIParser()

    print(f"⚡ SIOS Labs Command Line Interface (v{sios_cli.version}) Initialized.")

    if args.prompt:
        sios_cli.process_command(args.prompt)
    elif args.interactive or len(sys.argv) == 1:
        print("Entering interactive workspace environment shell. Type 'exit' or 'quit' to close.\n")
        while True:
            try:
                user_input = input("sios@kernel:~# ")
                if user_input.strip().lower() in ["exit", "quit"]:
                    print("Shutting down terminal channel interface workspace matrix. Goodbye.")
                    break
                if not user_input.strip():
                    continue
                sios_cli.process_command(user_input)
                print()
            except (KeyboardInterrupt, EOFError):
                print("\nExiting execution workspace frame.")
                break
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
