# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1805?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1805
- Title: ARCH Act
- Congress: 119
- Bill type: HR
- Bill number: 1805
- Origin chamber: House
- Introduced date: 2025-03-03
- Update date: 2026-01-22T22:34:48Z
- Update date including text: 2026-01-22T22:34:48Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-03-03: Introduced in House
- 2025-03-03 - IntroReferral: Introduced in House
- 2025-03-03 - IntroReferral: Introduced in House
- 2025-03-03 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-03-03: Introduced in House

## Actions

- 2025-03-03 - IntroReferral: Introduced in House
- 2025-03-03 - IntroReferral: Introduced in House
- 2025-03-03 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-03",
    "latestAction": {
      "actionDate": "2025-03-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1805",
    "number": "1805",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "M001205",
        "district": "1",
        "firstName": "Carol",
        "fullName": "Rep. Miller, Carol D. [R-WV-1]",
        "lastName": "Miller",
        "party": "R",
        "state": "WV"
      }
    ],
    "title": "ARCH Act",
    "type": "HR",
    "updateDate": "2026-01-22T22:34:48Z",
    "updateDateIncludingText": "2026-01-22T22:34:48Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-03",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Ways and Means.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    }
  ]
}
```

## API Data: committees

```json
{
  "committees": [
    {
      "activities": {
        "item": {
          "date": "2025-03-03T17:04:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
      "type": "Standing"
    }
  ]
}
```

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "S001185",
      "district": "7",
      "firstName": "Terri",
      "fullName": "Rep. Sewell, Terri A. [D-AL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Sewell",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-03-03",
      "state": "AL"
    },
    {
      "bioguideId": "T000487",
      "district": "2",
      "firstName": "Jill",
      "fullName": "Rep. Tokuda, Jill N. [D-HI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Tokuda",
      "middleName": "N.",
      "party": "D",
      "sponsorshipDate": "2025-05-19",
      "state": "HI"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-11-07",
      "state": "VA"
    }
  ]
}
```

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1805ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1805\nIN THE HOUSE OF REPRESENTATIVES\nMarch 3, 2025 Mrs. Miller of West Virginia (for herself and Ms. Sewell ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend title XVIII of the Social Security Act to extend Medicare-dependent hospital and Medicare low-volume hospital payments, and to direct the Comptroller General of the United States to carry out a report on Medicare rural hospital classifications.\n#### 1. Short title\nThis Act may be cited as the Assistance for Rural Community Hospitals Act or the ARCH Act .\n#### 2. Extending Medicare-dependent hospital and Medicare low-volume hospital payments\n##### (a) MDH extension\n**(1) Extension of payment methodology**\nSection 1886(d)(5)(G) of the Social Security Act ( 42 U.S.C. 1395ww(d)(5)(G) ) is amended\u2014\n**(A)**\nin clause (i), by striking April 1, 2025 and inserting October 1, 2031 ; and\n**(B)**\nin clause (ii)(II), by striking April 1, 2025 and inserting October 1, 2031 .\n**(2) Conforming amendments**\n**(A) Extension of target amount**\nSection 1886(b)(3)(D) of the Social Security Act ( 42 U.S.C. 1395ww(b)(3)(D) ) is amended\u2014\n**(i)**\nin the matter preceding clause (i), by striking April 1, 2025 and inserting October 1, 2031 ; and\n**(ii)**\nin clause (iv), by striking fiscal year 2024 and the portion of fiscal year 2025 beginning on October 1, 2024, and ending on March 31, 2025 and inserting fiscal year 2031 .\n**(B) Permitting hospitals to decline reclassification**\nSection 13501(e)(2) of the Omnibus Budget Reconciliation Act of 1993 ( 42 U.S.C. 1395ww note) is amended by striking fiscal year 2024, or the portion of fiscal year 2025 beginning on October 1, 2024, and ending on March 31, 2025 and inserting fiscal year 2031 .\n##### (b) LVH extension\nSection 1886(d)(12) of the Social Security Act ( 42 U.S.C. 1395ww(d)(12) ) is amended\u2014\n**(1)**\nin subparagraph (C)(i)\u2014\n**(A)**\nin the matter preceding subclause (I), by striking through 2024 and the portion of fiscal year 2025 beginning on October 1, 2024, and ending on March 31, 2025 and inserting through 2031 ;\n**(B)**\nin subclause (III), by striking through 2024 and the portion of fiscal year 2025 beginning on October 1, 2024, and ending on March 31, 2025 and inserting through 2031 ; and\n**(C)**\nin subclause (IV), by striking the portion of fiscal year 2025 beginning on April 1, 2025, and ending on September 30, 2025, and fiscal year 2026 and inserting fiscal year 2032 ; and\n**(2)**\nin subparagraph (D)\u2014\n**(A)**\nin the matter preceding clause (i), by striking through 2024 or during the portion of fiscal year 2025 beginning on October 1, 2024, and ending on March 31, 2025 and inserting through 2031 ; and\n**(B)**\nin clause (ii), by striking through 2024 and the portion of fiscal year 2025 beginning on October 1, 2024, and ending on March 31, 2025 and inserting through 2031 .\n#### 3. GAO report on Medicare rural hospital classifications\nNot later than 180 days after the date of the enactment of this Act, the Comptroller General of the United States shall submit to Congress a report on Medicare rural hospital classifications that includes the following information:\n**(1)**\nThe total number of hospitals that, with respect to any of the 5 fiscal years preceding such date of enactment, had any of the following classifications:\n**(A)**\nClassification as a critical access hospital (as defined in section 1861(mm)(1) of the Social Security Act ( 42 U.S.C. 1395x(mm)(1) )).\n**(B)**\nClassification as a rural emergency hospital (as defined in section 1861(kkk)(2) of such Act ( 42 U.S.C. 1395x(kkk)(2) )).\n**(C)**\nClassification as a rural referral center (as described in section 1886(d)(5)(C) of such Act ( 42 U.S.C. 1395ww(d)(5)(C) ).\n**(D)**\nClassification as a sole community hospital (as defined in section 1886(d)(5)(D)(iii) of such Act ( 42 U.S.C. 1395ww(d)(5)(D)(iii) )).\n**(E)**\nClassification as a medicare-dependent, small rural hospital (as defined in section 1886(d)(5)(G)(iv) of such Act ( 42 U.S.C. 1395ww(d)(5)(G)(iv) )).\n**(F)**\nClassification as a low-volume hospital (as defined in section 1886(d)(12)(C)(i) of such Act ( 42 U.S.C. 1395ww(d)(12)(C)(i) )).\n**(2)**\nAn analysis of the extent to which there is overlap between the criteria for any two or more of the classifications described in paragraph (1) .\n**(3)**\nRecommendations for\u2014\n**(A)**\nsimplification with respect to such classifications and any such overlap; and\n**(B)**\nchanges with respect to the criteria for such classifications that would promote financial sustainability for rural hospitals and improve access to health care for individuals in rural areas.\n**(4)**\nThe projected effects of allowing sole community hospitals (as described in paragraph (1)(D) ) and medicare-dependent, small rural hospitals (as described in paragraph (1)(E) ) to use a cost reporting period beginning during fiscal year 2021 for the purpose of calculating adjusted payments under section 1886(d)(5) of the Social Security Act ( 42 U.S.C. 1395ww(d)(5) ).",
      "versionDate": "2025-03-03",
      "versionType": "Introduced in House"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-03-21T15:42:21Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-03",
    "originChamber": "House",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119hr1805",
          "measure-number": "1805",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-03",
          "originChamber": "HOUSE",
          "update-date": "2026-01-22"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1805v00",
            "update-date": "2026-01-22"
          },
          "action-date": "2025-03-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Assistance for Rural Community Hospitals Act or the ARCH Act</strong></p><p>This bill extends through FY2031 (1) the Medicare-Dependent Hospital Program, which provides additional payments to certain small rural hospitals that have a high proportion of Medicare patients; and (2) certain increased payment adjustments for low-volume hospitals under Medicare's inpatient prospective payment system.</p><p>It also requires the Government Accountability Office to report on the number of hospitals that received certain classifications for purposes of payment under Medicare, including low-volume hospitals and Medicare-dependent hospitals.</p>"
        },
        "title": "ARCH Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1805.xml",
    "summary": {
      "actionDate": "2025-03-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Assistance for Rural Community Hospitals Act or the ARCH Act</strong></p><p>This bill extends through FY2031 (1) the Medicare-Dependent Hospital Program, which provides additional payments to certain small rural hospitals that have a high proportion of Medicare patients; and (2) certain increased payment adjustments for low-volume hospitals under Medicare's inpatient prospective payment system.</p><p>It also requires the Government Accountability Office to report on the number of hospitals that received certain classifications for purposes of payment under Medicare, including low-volume hospitals and Medicare-dependent hospitals.</p>",
      "updateDate": "2026-01-22",
      "versionCode": "id119hr1805"
    },
    "title": "ARCH Act"
  },
  "summaries": [
    {
      "actionDate": "2025-03-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Assistance for Rural Community Hospitals Act or the ARCH Act</strong></p><p>This bill extends through FY2031 (1) the Medicare-Dependent Hospital Program, which provides additional payments to certain small rural hospitals that have a high proportion of Medicare patients; and (2) certain increased payment adjustments for low-volume hospitals under Medicare's inpatient prospective payment system.</p><p>It also requires the Government Accountability Office to report on the number of hospitals that received certain classifications for purposes of payment under Medicare, including low-volume hospitals and Medicare-dependent hospitals.</p>",
      "updateDate": "2026-01-22",
      "versionCode": "id119hr1805"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1805ih.xml"
        }
      ],
      "type": "Introduced in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "ARCH Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-20T10:23:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "ARCH Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-20T10:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Assistance for Rural Community Hospitals Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-20T10:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title XVIII of the Social Security Act to extend Medicare-dependent hospital and Medicare low-volume hospital payments, and to direct the Comptroller General of the United States to carry out a report on Medicare rural hospital classifications.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-20T10:18:36Z"
    }
  ]
}
```
