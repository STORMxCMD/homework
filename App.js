import React from "react";

export default function Home() {
  return (
    <div className="min-h-screen bg-gray-100 flex flex-col items-center p-8">
      {/* Header */}
      <header className="text-center mb-12">
        <h1 className="text-4xl font-bold text-gray-900">Asliddin Usmonov</h1>
        <p className="text-xl text-gray-600">Junior Developer</p>
      </header>

      {/* Personal Information */}
      <section className="bg-white p-6 rounded-xl shadow-md w-full max-w-md mb-8">
        <h2 className="text-2xl font-semibold text-gray-800 mb-4">Personal Info</h2>
        <p><strong>Name:</strong> Usmonov Asliddin</p>
        <p><strong>Birthday:</strong> 30.10.2008</p>
        <p><strong>Address:</strong> Tashkent, Uzbekistan</p>
      </section>

      {/* Services Section */}
      <section className="bg-white p-6 rounded-xl shadow-md w-full max-w-2xl">
        <h2 className="text-2xl font-semibold text-gray-800 mb-6">Services</h2>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          <div className="p-4 bg-yellow-200 rounded-lg text-center">
            <h3 className="font-semibold text-lg">Programming</h3>
            <p className="text-gray-700">I have experience in web and software development.</p>
          </div>
          <div className="p-4 bg-yellow-200 rounded-lg text-center">
            <h3 className="font-semibold text-lg">Frontend & Backend</h3>
            <p className="text-gray-700">Building responsive and interactive web applications.</p>
          </div>
          <div className="p-4 bg-yellow-200 rounded-lg text-center">
            <h3 className="font-semibold text-lg">Project Development</h3>
            <p className="text-gray-700">Creating and deploying functional websites and applications.</p>
          </div>
        </div>
      </section>
    </div>
  );
}
