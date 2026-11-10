"""
SIOS Labs: Semantic File System (SFS) Mock Simulation Prototype
Core Concept: Replacing strict directory strings and filenames with multi-modal embeddings 
and contextual knowledge graph vectors. An OS that understands what you mean, not just what you typed.
"""

import math
from datetime import datetime, timedelta

class MockEmbeddingEngine:
    """Simulates an on-device NPU transforming text concepts into semantic vector embeddings."""
    def __init__(self):
        # High-dimensional space representation map (Vocabulary mapping to a conceptual dense vector coordinate)
        self.concept_space = {
            "finance":      [0.90, -0.10, 0.05, 0.30],
            "money":        [0.85, -0.15, 0.00, 0.25],
            "budget":       [0.80, -0.20, 0.10, 0.40],
            "code":         [-0.10, 0.95, 0.40, -0.30],
            "programming":  [-0.15, 0.90, 0.45, -0.25],
            "software":     [-0.05, 0.85, 0.35, -0.20],
            "react":        [-0.20, 0.80, 0.70, -0.15],
            "creative":     [0.10, 0.20, -0.85, 0.60],
            "design":       [0.15, 0.10, -0.80, 0.70],
            "artwork":      [0.05, 0.05, -0.90, 0.55],
            "logo":         [0.20, 0.15, -0.75, 0.65],
            "ai":           [0.40, 0.60, 0.50, 0.50],
            "kernel":       [0.30, 0.75, 0.60, 0.10],
            "neural":       [0.50, 0.65, 0.55, 0.40]
        }

    def get_embedding(self, description: str):
        """Averages keywords found in description string to synthesize a mock dense vector embedding."""
        words = description.lower().split()
        vector = [0.0, 0.0, 0.0, 0.0]
        count = 0
        
        for word in words:
            if word in self.concept_space:
                vector = [v + self.concept_space[word][i] for i, v in enumerate(vector)]
                count += 1
                
        if count == 0:
            # Return neutral fallback vector if no vocabulary tokens match exactly
            return [0.1, 0.1, 0.1, 0.1]
            
        return [v / count for v in vector]

def cosine_similarity(v1, v2):
    """Computes basic directional semantic similarity between vectors."""
    dot_product = sum(a * b for a, b in zip(v1, v2))
    magnitude_v1 = math.sqrt(sum(a * a for a in v1))
    magnitude_v2 = math.sqrt(sum(a * a for a in v2))
    if magnitude_v1 == 0 or magnitude_v2 == 0:
        return 0.0
    return dot_product / (magnitude_v1 * magnitude_v2)

class SemanticFile:
    """Represents a metadata-driven systemic memory entity rather than a rigid physical path."""
    def __init__(self, inode_id: int, content_summary: str, embedding: list, created_days_ago: int):
        self.inode_id = inode_id
        self.content_summary = content_summary
        self.embedding = embedding
        self.timestamp = datetime.now() - timedelta(days=created_days_ago)

    def __repr__(self):
        return f"[Block Node #{self.inode_id} | Created: {self.timestamp.strftime('%Y-%m-%d')} | Data Context: '{self.content_summary}']"

class SemanticFileSystem:
    """The central SFS layer orchestrator managing local-first systemic storage vectors."""
    def __init__(self):
        self.engine = MockEmbeddingEngine()
        self.storage_pool = []
        self._seed_mock_data()

    def _seed_mock_data(self):
        # Inject standard operational file nodes representing an active ecosystem state
        data_nodes = [
            ("Q3 corporate financial spreadsheet budget calculations sheet", 2),
            ("Initial vector logo asset files for branding project artwork design suite", 14),
            ("React front-end application prototype component source code files", 5),
            ("Low-level OS microkernel scheduling routine algorithm implementation in C++", 1),
            ("Deep neural network training weights configuration file for local AI agents", 3)
        ]
        
        for idx, (summary, days_ago) in enumerate(data_nodes):
            vector = self.engine.get_embedding(summary)
            self.storage_pool.append(SemanticFile(1024 + idx, summary, vector, days_ago))

    def query(self, natural_language_prompt: str, threshold: float = 0.40):
        """Core operation: Resolves semantic query prompts without knowing specific path names."""
        print(f"\n🔍 [SFS Query Received]: \"{natural_language_prompt}\"")
        query_vector = self.engine.get_embedding(natural_language_prompt)
        
        matches = []
        for node in self.storage_pool:
            score = cosine_similarity(query_vector, node.embedding)
            matches.append((node, score))
            
        # Rank by statistical semantic match percentage scores
        matches.sort(key=lambda x: x[1], reverse=True)
        
        results = [m for m in matches if m[1] >= threshold]
        
        if not results:
            print("❌ No matching semantic nodes found above minimum correlation thresholds.")
            return
            
        for idx, (node, score) in enumerate(results, 1):
            print(f"  {idx}. Match Confidence: {score:.2%} -> {node}")

# Executable System Walkthrough Demonstration
if __name__ == "__main__":
    print("=" * 75)
    print("⚡ SIOS LABS: SEMANTIC FILE SYSTEM (SFS) KERNEL EXTENSION PROTOTYPE RUNTIME ⚡")
    print("=" * 75)
    
    sfs = SemanticFileSystem()
    
    # Test Use Case 1: Querying for financial resources via loose matching words
    sfs.query("Show me files detailing money and spending budgets from last week")
    
    # Test Use Case 2: Querying for code implementations
    sfs.query("Find programming code repositories and software apps written in react")
    
    # Test Use Case 3: Querying design assets
    sfs.query("Locate graphics creative design elements and logo art")
    
    print("\n" + "=" * 75)
    print("✨ SFS Simulation Framework Initialized Successfully. Ready for GitHub push.")
    print("=" * 75)
