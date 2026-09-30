import NLPStats from "./NLPStats";

function NLPAnalysis({ nlp }) {
  if (!nlp) {
    return null;
  }

  return (
    <div className="nlp-analysis">
      <h2>NLP Analysis</h2>

      <NLPStats nlp={nlp} />

      {/* Named Entities */}

      <div className="nlp-section">
        <h3>Named Entities</h3>

        {nlp.entities && nlp.entities.length > 0 ? (
          <div className="entity-list">
            {nlp.entities.map((entity, index) => (
              <div className="entity-item" key={index}>
                <span className="entity-text">{entity.text}</span>

                <span className="entity-label">{entity.label}</span>
              </div>
            ))}
          </div>
        ) : (
          <p>No named entities found.</p>
        )}
      </div>

      {/* Tokens */}

      <div className="nlp-section">
        <h3>Tokens & POS Tags</h3>

        {nlp.tokens && nlp.tokens.length > 0 ? (
          <div className="token-table">
            <div className="token-header">
              <span>Token</span>
              <span>Lemma</span>
              <span>POS</span>
            </div>

            {nlp.tokens.slice(0, 100).map((token, index) => (
              <div className="token-row" key={index}>
                <span>{token.text}</span>

                <span>{token.lemma}</span>

                <span>{token.pos}</span>
              </div>
            ))}
          </div>
        ) : (
          <p>No tokens found.</p>
        )}
      </div>
    </div>
  );
}

export default NLPAnalysis;
