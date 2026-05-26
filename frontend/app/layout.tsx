import type { Metadata } from "next";
import { Plus_Jakarta_Sans, Space_Mono } from "next/font/google";
import "./globals.css";

const uiFont = Plus_Jakarta_Sans({ subsets: ["latin"], variable: "--font-ui" });
const dataFont = Space_Mono({ weight: ["400", "700"], subsets: ["latin"], variable: "--font-data" });

export const metadata: Metadata = {
  title: "VEGA PRO | Institutional Suite",
  description: "Advanced Volatility Engineering Platform",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className={`${uiFont.variable} ${dataFont.variable} antialiased bg-bg-pure text-platinum`}>
        <div className="aurora-bg" />
        {children}
      </body>
    </html>
  );
}
