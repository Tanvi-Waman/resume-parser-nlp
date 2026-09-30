function NLPStats({ nlp }) {
  if (!nlp) {
    return null;
  }

  const tokenCount = nlp.tokens?.length || 0;

  const entityCount = nlp.entities?.length || 0;

  const nounCount =
    nlp.tokens?.filter((token) => token.pos === "NOUN").length || 0;

  const verbCount =
    nlp.tokens?.filter((token) => token.pos === "VERB").length || 0;

  const properNounCount =
    nlp.tokens?.filter((token) => token.pos === "PROPN").length || 0;

  return (
    <div className="nlp-stats">
      <div className="stat-card">
        <h3>Tokens</h3>
        <p>{tokenCount}</p>
      </div>

      <div className="stat-card">
        <h3>Entities</h3>
        <p>{entityCount}</p>
      </div>

      <div className="stat-card">
        <h3>Nouns</h3>
        <p>{nounCount}</p>
      </div>

      <div className="stat-card">
        <h3>Verbs</h3>
        <p>{verbCount}</p>
      </div>

      <div className="stat-card">
        <h3>Proper Nouns</h3>
        <p>{properNounCount}</p>
      </div>
    </div>
  );
}

export default NLPStats;
