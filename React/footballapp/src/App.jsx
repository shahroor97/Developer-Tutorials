// src/App.jsx
import { useEffect, useState, useMemo } from "react";
import { getSoccerLeagues } from "./services/footballApi";

function LeagueRow({ country, league, id }) {
  return (
    <tr>
      <td>{country}</td>
      <td>{league}</td>
      <td>{id}</td>
    </tr>
  );
}

export default function App() {
  const [leagues, setLeagues] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [query, setQuery] = useState("");

  useEffect(() => {
    let active = true;
    (async () => {
      setLoading(true);
      try {
        const data = await getSoccerLeagues();
        if (active) setLeagues(data);
      } catch (e) {
        if (active) setError(e?.message || "Failed to load leagues");
      } finally {
        if (active) setLoading(false);
      }
    })();
    return () => {
      active = false;
    };
  }, []);

  // Filter: case-insensitive match on country or league name
  const filtered = useMemo(() => {
    const q = query.trim().toLowerCase();
    if (!q) return leagues;
    return leagues.filter(
      (c) =>
        c?.strCountry?.toLowerCase().includes(q) ||
        c?.strLeague?.toLowerCase().includes(q)
    );
  }, [leagues, query]);

  // Set: unique countries present in filtered data
  const uniqueCountries = useMemo(() => {
    const s = new Set();
    for (const c of filtered) {
      if (c?.strCountry) s.add(c.strCountry);
    }
    return s; // Set<string>
  }, [filtered]);

  // Map: country -> count of leagues (from filtered)
  const countryCounts = useMemo(() => {
    const m = new Map();
    for (const c of filtered) {
      const key = c?.strCountry || "Unknown";
      m.set(key, (m.get(key) || 0) + 1);
    }
    return m; // Map<string, number>
  }, [filtered]);

  if (loading) return <p>Loading…</p>;
  if (error) return <p role="alert">Error: {error}</p>;

  return (
    <main className="container">
      <h1>Soccer Leagues</h1>

      <div className="controls">
        <label htmlFor="search">Search (country or league): </label>
        <input
          id="search"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="e.g. England, Spain, Premier"
          className="input"
        />
      </div>

      <p>
        Showing <strong>{filtered.length}</strong> leagues across{" "}
        <strong>{uniqueCountries.size}</strong> countries.
      </p>

      {/* Example: read from Map (country -> count) */}
      {countryCounts.size > 0 && (
        <details>
          <summary>Country counts</summary>
          <ul>
            {[...countryCounts.entries()]
              .sort((a, b) => b[1] - a[1])
              .map(([country, count]) => (
                <li key={country}>
                  {country}: {count}
                </li>
              ))}
          </ul>
        </details>
      )}

      {filtered.length === 0 ? (
        <p>No matches. Try a different search.</p>
      ) : (
        <table>
          <thead>
            <tr>
              <th>Country</th>
              <th>League</th>
              <th>ID</th>
            </tr>
          </thead>
          <tbody>
            {filtered.map((c) => (
              <LeagueRow
                key={c.idLeague}
                country={c.strCountry}
                league={c.strLeague}
                id={c.idLeague}
              />
            ))}
          </tbody>
        </table>
      )}
    </main>
  );
}
