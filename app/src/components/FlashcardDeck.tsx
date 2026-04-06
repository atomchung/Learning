"use client";

import { useState } from "react";
import type { Flashcard } from "@/lib/notes";

export default function FlashcardDeck({
  cards,
}: {
  cards: Flashcard[];
}) {
  const [index, setIndex] = useState(0);
  const [flipped, setFlipped] = useState(false);
  const [completed, setCompleted] = useState<Set<number>>(new Set());

  if (cards.length === 0) return null;

  const card = cards[index];
  const progress = completed.size;
  const total = cards.length;

  function next() {
    setCompleted((prev) => new Set(prev).add(index));
    setFlipped(false);
    if (index < cards.length - 1) {
      setIndex(index + 1);
    }
  }

  function prev() {
    if (index > 0) {
      setFlipped(false);
      setIndex(index - 1);
    }
  }

  function reset() {
    setIndex(0);
    setFlipped(false);
    setCompleted(new Set());
  }

  const allDone = progress === total;

  return (
    <div className="mt-6">
      <div className="flex items-center justify-between mb-3">
        <h3 className="text-base font-bold text-gray-900 dark:text-gray-100">
          閃卡複習
        </h3>
        <span className="text-xs text-gray-500">
          {progress}/{total} 完成
        </span>
      </div>

      {/* Progress bar */}
      <div className="h-1.5 w-full rounded-full bg-gray-200 dark:bg-gray-700 mb-4">
        <div
          className="h-1.5 rounded-full bg-green-500 transition-all"
          style={{ width: `${(progress / total) * 100}%` }}
        />
      </div>

      {allDone ? (
        <div className="text-center py-8">
          <p className="text-2xl mb-2">🎉</p>
          <p className="text-gray-600 dark:text-gray-400">全部複習完畢！</p>
          <button
            onClick={reset}
            className="mt-3 rounded-lg bg-blue-600 px-4 py-2 text-sm text-white hover:bg-blue-700"
          >
            再來一次
          </button>
        </div>
      ) : (
        <>
          {/* Card */}
          <button
            onClick={() => setFlipped(!flipped)}
            className="w-full min-h-[160px] rounded-2xl border-2 border-dashed border-gray-300 bg-gray-50 p-6 text-left transition-all active:scale-[0.98] dark:border-gray-600 dark:bg-gray-800/50"
          >
            <div className="text-xs font-medium uppercase tracking-wider text-gray-400 mb-2">
              {flipped ? "答案" : "問題"} ({index + 1}/{total})
            </div>
            <p className="text-base leading-relaxed text-gray-900 dark:text-gray-100">
              {flipped ? card.a : card.q}
            </p>
            {!flipped && (
              <p className="mt-4 text-xs text-gray-400">點擊翻轉查看答案</p>
            )}
          </button>

          {/* Controls */}
          <div className="mt-3 flex gap-2">
            <button
              onClick={prev}
              disabled={index === 0}
              className="flex-1 rounded-lg border border-gray-300 py-2 text-sm font-medium text-gray-700 disabled:opacity-30 dark:border-gray-600 dark:text-gray-300"
            >
              上一張
            </button>
            <button
              onClick={next}
              className="flex-1 rounded-lg bg-blue-600 py-2 text-sm font-medium text-white hover:bg-blue-700"
            >
              {index === cards.length - 1 ? "完成" : "下一張"}
            </button>
          </div>
        </>
      )}
    </div>
  );
}
