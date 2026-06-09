from __future__ import print_function
from stampdescriptor import StampDescriptor
from stampmatcher import StampMatcher

import argparse
import glob
import csv
import cv2
import os
def main():
    ap = argparse.ArgumentParser()

    ap.add_argument("-d", "--db", required=True,
                    help="path to the stamp database")
    ap.add_argument("-c", "--stamp_dataset", required=True,
                    help="path to the stamp image dataset")
    ap.add_argument("-q", "--query", required=True,
                    help="path to the query stamp image")
    ap.add_argument("-s", "--sift", type=int, default=0,
                    help="whether or not SIFT should be used")
    args = vars(ap.parse_args())

    db = {}

    for l in csv.reader(open(args["db"])):
        db[l[0]] = l[1:]

    useSIFT = args["sift"] > 0
    useHamming = args["sift"] == 0
    ratio = 0.7
    minMatches = 40

    if useSIFT:
        minMatches = 50

    # універсальний список усіх зображень марок
    stampPaths = glob.glob(args["stamp_dataset"] + "/*.jpg")
    stampPaths += glob.glob(args["stamp_dataset"] + "/*.png")

    # створюємо descriptor
    cd = StampDescriptor(useSIFT=useSIFT)

    # matcher
    matcher = StampMatcher(
        cd,
        stampPaths,
        ratio=ratio,
        minMatches=minMatches,
        useHamming=useHamming)

    # query image
    queryImage = cv2.imread(args["query"])

    if queryImage is None:
        print("Error: query image not found!")
        return

    gray = cv2.cvtColor(queryImage, cv2.COLOR_BGR2GRAY)

    (queryKps, queryDescs) = cd.describe(gray)

    results = matcher.search(queryKps, queryDescs)

    # cv2.namedWindow("Query", cv2.WINDOW_NORMAL)
    cv2.imshow("Query", queryImage)

    if len(results) == 0:
        print("I could not find a match for that stamp!")
        cv2.waitKey(0)
    else:
        for (i, (score, stampPath)) in enumerate(results):

            filename = os.path.basename(stampPath)
            (country, stamp_name, year) = db[filename]

            print(
                "{}. {:.2f}% : {} | {} | {}".format(
                    i + 1,
                    score * 100,
                    country,
                    stamp_name,
                    year))

    # показуємо найкращий результат
    # bestMatch = results[0][1]

    # result = cv2.imread(bestMatch)
    # cv2.namedWindow("Result", cv2.WINDOW_NORMAL)
    # cv2.imshow("Result", result)

    # показуємо Top-3 результати
    topN = min(3, len(results))

    for i in range(topN):
        score, stampPath = results[i]

        result = cv2.imread(stampPath)

        windowName = (
            f"Result #{i + 1} "
            f"({score * 100:.2f}%)"
        )

        cv2.imshow(
            windowName,
            result
        )

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()