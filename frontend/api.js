window.api = {
  get API_BASE_URL() {
    return window.APP_CONFIG?.API_BASE_URL || "http://localhost:8000/api";
  },

  analyzeQuestions: async function(payload) {
    try {
      const response = await fetch(`${this.API_BASE_URL}/analyze`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify(payload)
      });
      if (!response.ok) {
        throw new Error(`API returned ${response.status}`);
      }
      return await response.json();
    } catch (error) {
      console.warn("API error or unavailable, falling back to demo data:", error);
      return this.loadDemoResponse();
    }
  },

  loadDemoResponse: async function() {
    try {
      // Assuming index.html is in the same directory as demo_response.json
      const response = await fetch("demo_response.json");
      if (!response.ok) {
        throw new Error("Failed to load demo_response.json");
      }
      const data = await response.json();
      data._isDemo = true;
      return data;
    } catch (error) {
      console.error("Failed to load demo response:", error);
      return null;
    }
  }
};
