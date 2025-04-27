import React, { useEffect, useState } from 'react';
import axios from 'axios';

function Home() {
  const [suggestion, setSuggestion] = useState('');

  useEffect(() => {
    async function fetchSuggestion() {
      try {
        const response = await axios.get('http://localhost:8000/suggestions/smart/1');
        setSuggestion(response.data.suggestion);
      } catch (error) {
        console.error('Error fetching suggestion', error);
      }
    }
    fetchSuggestion();
  }, []);

  return (
    <div>
      <h2>Dashboard</h2>
      <p><strong>Smart Financial Suggestion:</strong> {suggestion}</p>
      <button onClick={() => window.location.href='/'}>Logout</button>
    </div>
  );
}

export default Home;
