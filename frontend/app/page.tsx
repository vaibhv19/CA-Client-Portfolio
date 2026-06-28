import React from "react";

export const dynamic = "force-dynamic";

interface ExecutiveProfile {
  id: number;
  name: string;
  designation: string;
  bio: string;
  profile_image_url?: string;
  metric1_value: string;
  metric1_label: string;
  metric2_value: string;
  metric2_label: string;
  metric3_value: string;
  metric3_label: string;
}

async function getProfile(): Promise<ExecutiveProfile | null> {
  try {
    const res = await fetch("http://127.0.0.1:8000/api/executiveprofile/", {
      cache: "no-store",
    });

    if (!res.ok) {
      // If the primary endpoint fails, fall back to the verified profile endpoint
      const fallbackRes = await fetch("http://127.0.0.1:8000/api/profile/", {
        cache: "no-store",
      });
      if (fallbackRes.ok) {
        return await fallbackRes.json();
      }
      throw new Error(`Failed to fetch executive profile. Status: ${res.status}`);
    }

    return await res.json();
  } catch (error) {
    console.error("Error fetching executive profile server-side:", error);
    return null;
  }
}

export default async function Home() {
  const profile = await getProfile();

  if (!profile) {
    return (
      <div className="min-h-screen bg-slate-900 text-slate-100 flex flex-col justify-center items-center p-6 font-sans">
        <div className="max-w-md w-full bg-slate-950/80 border border-rose-500/30 rounded-3xl p-8 text-center shadow-2xl relative overflow-hidden backdrop-blur">
          {/* Accent glow */}
          <div className="absolute -top-10 -right-10 w-24 h-24 bg-rose-500/10 rounded-full blur-xl pointer-events-none" />
          
          <div className="w-16 h-16 rounded-2xl bg-rose-500/10 text-rose-400 flex items-center justify-center mx-auto mb-6">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={2} stroke="currentColor" className="w-8 h-8">
              <path strokeLinecap="round" strokeLinejoin="round" d="M12 9v3.75m-9.303 3.376c-.866 1.5.217 3.374 1.948 3.374h14.71c1.73 0 2.813-1.874 1.948-3.374L13.949 3.378c-.866-1.5-3.032-1.5-3.898 0L2.697 16.126zM12 15.75h.007v.008H12v-.008z" />
            </svg>
          </div>
          <h2 className="text-xl font-bold text-white mb-2">Connection Failure</h2>
          <p className="text-slate-400 text-sm leading-relaxed mb-6">
            System unreachable - please ensure Django server is active
          </p>
          <div className="text-xs text-slate-500 bg-slate-900/60 p-3 rounded-xl border border-slate-800 break-all font-mono">
            GET http://127.0.0.1:8000/api/executiveprofile/
          </div>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-slate-900 text-slate-100 flex flex-col font-sans selection:bg-teal-500/30 selection:text-teal-200 relative overflow-hidden">
      {/* Top Ambient Glows */}
      <div className="absolute top-0 left-1/4 w-96 h-96 bg-teal-500/10 rounded-full blur-3xl pointer-events-none" />
      <div className="absolute top-12 right-1/4 w-96 h-96 bg-indigo-500/10 rounded-full blur-3xl pointer-events-none" />

      {/* Header Status Bar */}
      <header className="border-b border-slate-800 bg-slate-900/50 backdrop-blur-md sticky top-0 z-50">
        <div className="max-w-6xl mx-auto px-6 py-4 flex items-center justify-between">
          <div className="flex items-center gap-3">
            <div className="w-8 h-8 rounded-lg bg-gradient-to-tr from-teal-500 to-indigo-600 flex items-center justify-center font-bold text-white shadow-lg shadow-teal-500/20">
              PG
            </div>
            <div>
              <span className="font-semibold tracking-tight text-slate-100">CA Priyam Gupta</span>
              <span className="hidden sm:inline-block ml-2 px-2 py-0.5 text-[10px] font-semibold bg-slate-800 text-slate-400 rounded-full border border-slate-700">
                Executive Portfolio
              </span>
            </div>
          </div>

          <div className="flex items-center gap-2 px-3 py-1.5 rounded-full bg-slate-950 border border-slate-800 text-xs">
            <span className="relative flex h-2 w-2">
              <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-teal-400 opacity-75"></span>
              <span className="relative inline-flex rounded-full h-2 w-2 bg-teal-500"></span>
            </span>
            <span className="text-teal-400 font-medium">Server Connected</span>
          </div>
        </div>
      </header>

      {/* Main Container */}
      <main className="flex-1 max-w-6xl w-full mx-auto px-6 py-12 flex flex-col justify-center relative">
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-8 items-start">
          {/* Profile Card (Left Column) */}
          <div className="lg:col-span-1 bg-gradient-to-b from-slate-950 to-slate-900 border border-slate-800/80 rounded-3xl p-8 shadow-2xl relative overflow-hidden group">
            <div className="absolute top-0 right-0 w-32 h-32 bg-teal-500/5 rounded-full blur-2xl pointer-events-none" />
            
            <div className="flex flex-col items-center text-center">
              {/* Headshot avatar */}
              <div className="relative mb-6">
                <div className="w-28 h-28 rounded-full bg-gradient-to-tr from-teal-400 to-indigo-500 p-1 shadow-xl shadow-teal-500/10 flex items-center justify-center">
                  <div className="w-full h-full bg-slate-950 rounded-full flex items-center justify-center overflow-hidden">
                    {profile.profile_image_url ? (
                      <img
                        src={profile.profile_image_url}
                        alt={profile.name}
                        className="w-full h-full object-cover"
                      />
                    ) : (
                      <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="w-12 h-12 text-slate-400">
                        <path strokeLinecap="round" strokeLinejoin="round" d="M15.75 6a3.75 3.75 0 11-7.5 0 3.75 3.75 0 017.5 0zM4.501 20.118a7.5 7.5 0 0114.998 0A17.933 17.933 0 0112 21.75c-2.676 0-5.216-.584-7.499-1.632z" />
                      </svg>
                    )}
                  </div>
                </div>
                <div className="absolute bottom-0 right-1 w-5 h-5 bg-teal-500 border-2 border-slate-900 rounded-full flex items-center justify-center shadow-md">
                  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={3} stroke="currentColor" className="w-2.5 h-2.5 text-white">
                    <path strokeLinecap="round" strokeLinejoin="round" d="M4.5 12.75l6 6 9-13.5" />
                  </svg>
                </div>
              </div>

              <h1 className="text-2xl font-bold tracking-tight text-white">{profile.name}</h1>
              <p className="text-teal-400 font-semibold text-sm mt-1">{profile.designation}</p>

              <hr className="w-full my-6 border-slate-800" />

              <div className="w-full text-left space-y-4 text-xs">
                <div className="flex justify-between items-center py-2 border-b border-slate-850">
                  <span className="text-slate-400">Credentials</span>
                  <span className="text-slate-200 font-medium">CA (ICAI) & CS G1</span>
                </div>
                <div className="flex justify-between items-center py-2 border-b border-slate-850">
                  <span className="text-slate-400">Availability</span>
                  <span className="text-emerald-400 font-medium">Immediate Transition</span>
                </div>
                <div className="flex justify-between items-center py-2">
                  <span className="text-slate-400">Target Role</span>
                  <span className="text-slate-200 font-medium">Corporate Finance / Advisory</span>
                </div>
              </div>
            </div>

            <div className="mt-8">
              <a
                href="#contact"
                className="flex justify-center items-center gap-2 w-full py-3 px-4 rounded-xl bg-gradient-to-r from-teal-500 to-indigo-600 hover:from-teal-400 hover:to-indigo-500 font-semibold text-white shadow-lg shadow-teal-500/10 hover:shadow-teal-500/20 hover:scale-[1.02] active:scale-[0.98] transition-all text-sm"
              >
                Initiate Contact
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={2.5} stroke="currentColor" className="w-4 h-4">
                  <path strokeLinecap="round" strokeLinejoin="round" d="M13.5 4.5L21 12m0 0l-7.5 7.5M21 12H3" />
                </svg>
              </a>
            </div>
          </div>

          {/* Bio & Metrics (Right Column) */}
          <div className="lg:col-span-2 space-y-8">
            {/* Corporate Objective Card */}
            <div className="bg-slate-950/80 border border-slate-800/80 rounded-3xl p-8 shadow-2xl backdrop-blur relative overflow-hidden group">
              <div className="absolute top-0 left-0 w-32 h-32 bg-indigo-500/5 rounded-full blur-2xl pointer-events-none" />
              
              <h3 className="text-sm font-semibold tracking-wider text-slate-400 uppercase">Executive Objective</h3>
              <h2 className="text-2xl font-bold text-white mt-2 leading-relaxed">
                Bridging Regulatory Compliance & Corporate Growth
              </h2>
              <p className="text-slate-300 mt-4 text-base leading-relaxed font-light">
                {profile.bio}
              </p>
            </div>

            {/* Metrics Grid */}
            <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
              {/* Metric 1 */}
              <div className="bg-gradient-to-br from-slate-950 to-slate-900 border border-slate-800/80 rounded-2xl p-6 shadow-xl relative overflow-hidden group hover:border-slate-700/80 transition-colors">
                <div className="absolute -top-10 -right-10 w-24 h-24 bg-teal-500/5 rounded-full blur-xl pointer-events-none" />
                <div className="text-4xl font-extrabold text-white tracking-tight bg-gradient-to-r from-teal-400 to-emerald-400 bg-clip-text text-transparent">
                  {profile.metric1_value}
                </div>
                <div className="text-xs font-medium text-slate-400 mt-2 leading-tight uppercase tracking-wider">
                  {profile.metric1_label}
                </div>
              </div>

              {/* Metric 2 */}
              <div className="bg-gradient-to-br from-slate-950 to-slate-900 border border-slate-800/80 rounded-2xl p-6 shadow-xl relative overflow-hidden group hover:border-slate-700/80 transition-colors">
                <div className="absolute -top-10 -right-10 w-24 h-24 bg-indigo-500/5 rounded-full blur-xl pointer-events-none" />
                <div className="text-4xl font-extrabold text-white tracking-tight bg-gradient-to-r from-indigo-400 to-purple-400 bg-clip-text text-transparent">
                  {profile.metric2_value}
                </div>
                <div className="text-xs font-medium text-slate-400 mt-2 leading-tight uppercase tracking-wider">
                  {profile.metric2_label}
                </div>
              </div>

              {/* Metric 3 */}
              <div className="bg-gradient-to-br from-slate-950 to-slate-900 border border-slate-800/80 rounded-2xl p-6 shadow-xl relative overflow-hidden group hover:border-slate-700/80 transition-colors">
                <div className="absolute -top-10 -right-10 w-24 h-24 bg-teal-500/5 rounded-full blur-xl pointer-events-none" />
                <div className="text-4xl font-extrabold text-white tracking-tight bg-gradient-to-r from-teal-400 to-indigo-400 bg-clip-text text-transparent">
                  {profile.metric3_value}
                </div>
                <div className="text-xs font-medium text-slate-400 mt-2 leading-tight uppercase tracking-wider">
                  {profile.metric3_label}
                </div>
              </div>
            </div>
          </div>
        </div>
      </main>

      {/* Footer */}
      <footer className="border-t border-slate-900/60 bg-slate-950/80 py-8 mt-auto">
        <div className="max-w-6xl mx-auto px-6 flex flex-col md:flex-row items-center justify-between gap-4 text-xs text-slate-500">
          <div>
            &copy; 2026 CA Priyam Gupta. All rights reserved.
          </div>
          <div className="flex gap-4">
            <span className="hover:text-slate-300 transition-colors cursor-default">Financial Advisory</span>
            <span>&bull;</span>
            <span className="hover:text-slate-300 transition-colors cursor-default">Statutory & Tax Audit</span>
            <span>&bull;</span>
            <span className="hover:text-slate-300 transition-colors cursor-default">CS Professional (G1)</span>
          </div>
        </div>
      </footer>
    </div>
  );
}
