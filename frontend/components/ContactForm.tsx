"use client";

import React, { useState } from "react";

export default function ContactForm() {
  const [name, setName] = useState("");
  const [organization, setOrganization] = useState("");
  const [email, setEmail] = useState("");
  const [subject, setSubject] = useState("Recruitment");
  const [message, setMessage] = useState("");
  const [status, setStatus] = useState<"idle" | "sending" | "success" | "error">("idle");
  const [errorMessage, setErrorMessage] = useState("");

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setStatus("sending");
    setErrorMessage("");

    try {
      const response = await fetch("http://127.0.0.1:8000/api/networking-inquiries/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          name,
          organization,
          email,
          subject,
          message,
        }),
      });

      if (response.status === 201) {
        setStatus("success");
        setName("");
        setOrganization("");
        setEmail("");
        setSubject("Recruitment");
        setMessage("");
      } else {
        const errorData = await response.json().catch(() => ({}));
        setStatus("error");
        setErrorMessage(
          errorData.detail || 
          Object.entries(errorData)
            .map(([key, val]) => `${key}: ${Array.isArray(val) ? val.join(", ") : val}`)
            .join(" | ") ||
          "Submission failed. Please verify your input."
        );
      }
    } catch (err) {
      console.error("Connection failure:", err);
      setStatus("error");
      setErrorMessage("Network error: Failed to connect to backend server.");
    }
  };

  return (
    <section id="contact" className="space-y-8 scroll-mt-24">
      <div className="flex items-center gap-3">
        <h2 className="text-xl font-bold tracking-tight text-white uppercase">Initiate Connection</h2>
        <div className="flex-1 h-[1px] bg-slate-850" />
        <span className="text-xs text-teal-400 font-mono">04 / CONTACT</span>
      </div>

      <div className="max-w-3xl mx-auto bg-slate-950/50 border border-slate-850 rounded-3xl p-8 md:p-10 shadow-2xl relative overflow-hidden backdrop-blur">
        {/* Glow Effects */}
        <div className="absolute top-0 right-0 w-48 h-48 bg-teal-500/5 rounded-full blur-3xl pointer-events-none" />
        <div className="absolute bottom-0 left-0 w-48 h-48 bg-indigo-500/5 rounded-full blur-3xl pointer-events-none" />

        <form onSubmit={handleSubmit} className="space-y-6 relative z-10">
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            {/* Name */}
            <div className="space-y-2">
              <label htmlFor="name" className="text-xs font-semibold text-slate-400 uppercase tracking-wider">
                Full Name
              </label>
              <input
                type="text"
                id="name"
                required
                value={name}
                onChange={(e) => setName(e.target.value)}
                placeholder="e.g. John Doe"
                className="w-full px-4 py-3 rounded-xl bg-slate-900 border border-slate-800 text-white placeholder-slate-500 focus:border-teal-500 focus:ring-1 focus:ring-teal-500 outline-none transition-all text-sm"
              />
            </div>

            {/* Organization */}
            <div className="space-y-2">
              <label htmlFor="organization" className="text-xs font-semibold text-slate-400 uppercase tracking-wider">
                Organization / Company
              </label>
              <input
                type="text"
                id="organization"
                required
                value={organization}
                onChange={(e) => setOrganization(e.target.value)}
                placeholder="e.g. Acme Corp"
                className="w-full px-4 py-3 rounded-xl bg-slate-900 border border-slate-800 text-white placeholder-slate-550 focus:border-teal-500 focus:ring-1 focus:ring-teal-500 outline-none transition-all text-sm"
              />
            </div>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            {/* Email */}
            <div className="space-y-2">
              <label htmlFor="email" className="text-xs font-semibold text-slate-400 uppercase tracking-wider">
                Email Address
              </label>
              <input
                type="email"
                id="email"
                required
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                placeholder="e.g. john@example.com"
                className="w-full px-4 py-3 rounded-xl bg-slate-900 border border-slate-800 text-white placeholder-slate-500 focus:border-teal-500 focus:ring-1 focus:ring-teal-500 outline-none transition-all text-sm"
              />
            </div>

            {/* Subject */}
            <div className="space-y-2">
              <label htmlFor="subject" className="text-xs font-semibold text-slate-400 uppercase tracking-wider">
                Inquiry Subject
              </label>
              <select
                id="subject"
                value={subject}
                onChange={(e) => setSubject(e.target.value)}
                className="w-full px-4 py-3 rounded-xl bg-slate-900 border border-slate-800 text-white focus:border-teal-500 focus:ring-1 focus:ring-teal-500 outline-none transition-all text-sm"
              >
                <option value="Recruitment">Recruitment</option>
                <option value="Networking">Networking</option>
                <option value="Industry Query">Industry Query</option>
              </select>
            </div>
          </div>

          {/* Message */}
          <div className="space-y-2">
            <label htmlFor="message" className="text-xs font-semibold text-slate-400 uppercase tracking-wider">
              Message Details
            </label>
            <textarea
              id="message"
              required
              rows={5}
              value={message}
              onChange={(e) => setMessage(e.target.value)}
              placeholder="Provide context regarding your advisory or recruitment needs..."
              className="w-full px-4 py-3 rounded-xl bg-slate-900 border border-slate-800 text-white placeholder-slate-500 focus:border-teal-500 focus:ring-1 focus:ring-teal-500 outline-none transition-all text-sm resize-none"
            />
          </div>

          {/* User Feedback Banners */}
          {status === "success" && (
            <div className="p-4 rounded-xl bg-emerald-500/10 border border-emerald-500/30 text-emerald-400 text-sm flex items-center gap-3">
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={2} stroke="currentColor" className="w-5 h-5 shrink-0">
                <path strokeLinecap="round" strokeLinejoin="round" d="M9 12.75L11.25 15 15 9.75M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
              </svg>
              <span>Your inquiry has been successfully transmitted. Thank you!</span>
            </div>
          )}

          {status === "error" && (
            <div className="p-4 rounded-xl bg-rose-500/10 border border-rose-500/30 text-rose-400 text-sm flex items-center gap-3">
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={2} stroke="currentColor" className="w-5 h-5 shrink-0">
                <path strokeLinecap="round" strokeLinejoin="round" d="M12 9v3.75m9-.75a9 9 0 11-18 0 9 9 0 0118 0zm-9 3.75h.008v.008H12v-.008z" />
              </svg>
              <span>{errorMessage || "An error occurred. Please verify your inputs and try again."}</span>
            </div>
          )}

          {/* Submit Button */}
          <div>
            <button
              type="submit"
              disabled={status === "sending"}
              className="flex justify-center items-center gap-2 w-full sm:w-auto px-8 py-3 rounded-xl bg-gradient-to-r from-teal-500 to-indigo-600 hover:from-teal-400 hover:to-indigo-500 disabled:from-slate-800 disabled:to-slate-850 disabled:text-slate-500 font-semibold text-white shadow-lg shadow-teal-500/10 hover:shadow-teal-500/20 hover:scale-[1.02] active:scale-[0.98] disabled:scale-100 transition-all text-sm cursor-pointer disabled:cursor-not-allowed"
            >
              {status === "sending" ? (
                <>
                  <svg className="animate-spin -ml-1 mr-3 h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                    <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                    <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                  </svg>
                  Sending...
                </>
              ) : (
                <>
                  Send Inquiry
                  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={2.5} stroke="currentColor" className="w-4 h-4">
                    <path strokeLinecap="round" strokeLinejoin="round" d="M6 12L3.269 3.126A59.768 59.768 0 0121.485 12 59.77 59.77 0 013.27 20.876L5.999 12zm0 0h7.5" />
                  </svg>
                </>
              )}
            </button>
          </div>
        </form>
      </div>
    </section>
  );
}
