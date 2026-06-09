import numpy as np
import cv2

class StampMatcher:
	def __init__(self, descriptor, stampPaths, ratio = 0.7,
		minMatches = 8, useHamming = True):
		self.descriptor = descriptor
		self.stampPaths = stampPaths
		self.ratio = ratio
		self.minMatches = minMatches
		self.distanceMethod = "BruteForce"

		if useHamming:
			self.distanceMethod += "-Hamming"

	def search(self, queryKps, queryDescs):
		results = {}

		for stampPath in self.stampPaths:
			cover = cv2.imread(stampPath)
			gray = cv2.cvtColor(cover, cv2.COLOR_BGR2GRAY)
			(kps, descs) = self.descriptor.describe(gray)

			score = self.match(queryKps, queryDescs, kps, descs)
			results[stampPath] = score

		if len(results) > 0:
			results = sorted([(v, k) for (k, v) in results.items() if v > 0],
				reverse = True)
		return results

	def match(self, kpsA, featuresA, kpsB, featuresB):

		# якщо дескриптори відсутні
		if featuresA is None or featuresB is None:
			return -1.0

		matcher = cv2.DescriptorMatcher_create(
			self.distanceMethod)

		rawMatches = matcher.knnMatch(
			featuresB,
			featuresA,
			2)

		matches = []

		for m in rawMatches:
			if len(m) == 2 and \
					m[0].distance < m[1].distance * self.ratio:
				matches.append(
					(m[0].trainIdx, m[0].queryIdx)
				)

		# недостатньо збігів
		if len(matches) <= self.minMatches:
			return -1.0

		ptsA = np.float32([
			kpsA[i] for (i, _) in matches
		])

		ptsB = np.float32([
			kpsB[j] for (_, j) in matches
		])

		(H, status) = cv2.findHomography(
			ptsA,
			ptsB,
			cv2.RANSAC,
			4.0
		)

		# homography не знайшлась
		if status is None:
			return -1.0

		return float(status.sum()) / status.size
