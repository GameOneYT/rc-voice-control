import Link from "next/link"
import { useRouter } from "next/router";
import Image from "next/image";
import { useEffect, useRef } from "react";

export default function Header() {
    const src = "logo.png"; // searches for file in the public folder?

    const router = useRouter();
    const navRef = useRef();
    function highlightCurrentRoute(currentRoute){
        
    }

    useEffect(e=>{
        console.log(navRef);
        highlightCurrentRoute(router);
    },[router])

    return (
        <header>
            <div className="logo">
                <Link href="/">
                    <Image
                        loader={({ src }) => src}
                        className='styles.image'
                        src={src}
                        alt='Logo'
                        width={100}
                        height={50}
                    />
                </Link>
            </div>
            <nav ref={navRef}>
                {/* giving active class to the current route */}
                <div className={("Home"+' '+`${router.pathname==='/'?'active':''}`)} > 
                    <Link href="/">Home</Link>
                </div>
                <div className={("Slideshow"+' '+`${router.pathname==='/Slideshow'?'active':''}`)}>
                    <Link href="/Slideshow">Slideshow</Link>
                </div>
                <div className={("Download"+' '+`${router.pathname==='/Download'?'active':''}`)}>
                    <Link href="/Download">Download</Link>
                </div>
                <div className={("About"+' '+`${router.pathname==='/About'?'active':''}`)}>
                    <Link href="/About">About</Link>
                </div>
            </nav>
        </header>
    )
}