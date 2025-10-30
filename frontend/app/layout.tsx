import type React from "react";
import type { Metadata } from "next";
import { Montserrat } from "next/font/google";
import "./globals.css";

const montserrat = Montserrat({ subsets: ["latin"] });

export const metadata: Metadata = {
  title: "Query Assistant",
  description: "Shop Navigation Assistant",
  generator: "Dickson Ankamah",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className={`${montserrat.className} font-sans antialiased`}>
        {children}
      </body>
    </html>
  );
}
