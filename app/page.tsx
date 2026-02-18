"use server";
import { redirect } from "next/navigation";
import Image from "next/image";
export async function playButton (formdata: FormData) {
  console.log(formdata)
  const username = formdata.get("username")
  redirect(`/play/${username}`)
}
export default async function Home() {
  return ( 
    <>
      <div>MTG</div> 
      <form action={playButton} >  
        <input type="text" name="username" placeholder="username" required />
        <button type="submit">Play</button>
      </form>
    </> 
  );
}