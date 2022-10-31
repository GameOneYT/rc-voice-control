import Head from "next/head";
import Footer from "../components/Footer";
import Header from "../components/Header";

export default function HomePage() {

  return (
    <>
      <Head>
        <title>Next JS Project</title>
      </Head>
      <Header />
      <Footer />
    </>
  );
}
