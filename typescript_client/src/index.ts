import axios, { AxiosInstance } from "axios";

export class OpenNexusClient {
  private axios: AxiosInstance;

  constructor(baseURL: string, apiKey: string) {
    this.axios = axios.create({
      baseURL,
      headers: {
        "X-API-KEY": apiKey,
        "Content-Type": "application/json",
      },
      timeout: 15000,
    });
  }

  async runBash(command: string) {
    const res = await this.axios.post("/tools/bash", { command });
    return res.data;
  }

  async webSearch(query: string) {
    const res = await this.axios.post("/tools/web_search", { query });
    return res.data;
  }

  async runPython(code: string) {
    const res = await this.axios.post("/tools/python", { code });
    return res.data;
  }
}