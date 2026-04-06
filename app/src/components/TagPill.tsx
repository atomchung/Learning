import Link from "next/link";

export default function TagPill({
  tag,
  count,
  active,
}: {
  tag: string;
  count?: number;
  active?: boolean;
}) {
  return (
    <Link
      href={`/tags/${tag}`}
      className={`inline-flex items-center gap-1 rounded-full px-3 py-1 text-sm font-medium transition-colors ${
        active
          ? "bg-blue-600 text-white"
          : "bg-gray-100 text-gray-700 hover:bg-gray-200 dark:bg-gray-800 dark:text-gray-300 dark:hover:bg-gray-700"
      }`}
    >
      #{tag}
      {count !== undefined && (
        <span className="text-xs opacity-60">({count})</span>
      )}
    </Link>
  );
}
