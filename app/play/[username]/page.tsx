export default async function PlayUsernamePage({
  params
}: {
  params: Promise<{ username: string }>
}) {
  const { username } = await params;
  
  return (
    <>
      <div>{username}</div>
    </>
  );
}