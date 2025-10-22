export default function BlogMeta({
  tag,
  date,
  readingTime,
  authorName,
  authorRole,
  authorAvatar,
}: {
  tag?: string;
  date: string;          // ISO date preferred
  readingTime?: string;  // e.g., "6 min read"
  authorName: string;
  authorRole?: string;
  authorAvatar?: string;
}) {
  const d = new Date(date);
  const nice = d.toLocaleDateString(undefined, {
    year: "numeric", month: "short", day: "numeric",
  });
  return (
    <div style={{
      display: "grid",
      gap: "8px",
      margin: "12px 0 20px",
      alignItems: "center"
    }}>
      <div style={{fontSize: 12, fontWeight: 700, color: "#0a7f58"}}>
        {tag?.toUpperCase()} {tag ? "· " : ""}{nice}{readingTime ? ` · ${readingTime}` : ""}
      </div>
      <div style={{display: "flex", alignItems: "center", gap: 10}}>
        {authorAvatar &&
          <img src={authorAvatar} alt={authorName} width={28} height={28}
               style={{borderRadius: "999px"}} />}
        <div style={{fontSize: 14}}>
          <strong>{authorName}</strong>{authorRole ? ` · ${authorRole}` : ""}
        </div>
      </div>
    </div>
  );
}
