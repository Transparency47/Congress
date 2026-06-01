# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3788?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3788
- Title: CLEAR LABELS Act
- Congress: 119
- Bill type: S
- Bill number: 3788
- Origin chamber: Senate
- Introduced date: 2026-02-05
- Update date: 2026-05-01T18:56:32Z
- Update date including text: 2026-05-01T18:56:32Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-02-05: Introduced in Senate
- 2026-02-05 - IntroReferral: Introduced in Senate
- 2026-02-05 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- 2026-03-19 - Committee: Committee on Health, Education, Labor, and Pensions. Hearings held.
- Latest action: 2026-02-05: Introduced in Senate

## Actions

- 2026-02-05 - IntroReferral: Introduced in Senate
- 2026-02-05 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- 2026-03-19 - Committee: Committee on Health, Education, Labor, and Pensions. Hearings held.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-05",
    "latestAction": {
      "actionDate": "2026-02-05",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3788",
    "number": "3788",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "S001217",
        "district": "",
        "firstName": "Rick",
        "fullName": "Sen. Scott, Rick [R-FL]",
        "lastName": "Scott",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "CLEAR LABELS Act",
    "type": "S",
    "updateDate": "2026-05-01T18:56:32Z",
    "updateDateIncludingText": "2026-05-01T18:56:32Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-19",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Health, Education, Labor, and Pensions. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-02-05",
      "committees": {
        "item": [
          {
            "name": "Banking, Housing, and Urban Affairs Committee",
            "systemCode": "ssbk00"
          },
          {
            "name": "Health, Education, Labor, and Pensions Committee",
            "systemCode": "sshr00"
          }
        ]
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-02-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
        "item": [
          {
            "date": "2026-03-19T14:01:14Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2026-02-05T18:19:56Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
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
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2026-02-05",
      "state": "NY"
    },
    {
      "bioguideId": "T000278",
      "firstName": "Tommy",
      "fullName": "Sen. Tuberville, Tommy [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Tuberville",
      "party": "R",
      "sponsorshipDate": "2026-02-05",
      "state": "AL"
    },
    {
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2026-02-05",
      "state": "AL"
    },
    {
      "bioguideId": "J000293",
      "firstName": "Ron",
      "fullName": "Sen. Johnson, Ron [R-WI]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "party": "R",
      "sponsorshipDate": "2026-02-05",
      "state": "WI"
    },
    {
      "bioguideId": "M001244",
      "firstName": "Ashley",
      "fullName": "Sen. Moody, Ashley [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Moody",
      "party": "R",
      "sponsorshipDate": "2026-02-12",
      "state": "FL"
    },
    {
      "bioguideId": "L000577",
      "firstName": "Mike",
      "fullName": "Sen. Lee, Mike [R-UT]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "party": "R",
      "sponsorshipDate": "2026-03-09",
      "state": "UT"
    },
    {
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "False",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2026-03-11",
      "state": "ND"
    },
    {
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "False",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2026-03-23",
      "state": "ID"
    },
    {
      "bioguideId": "G000386",
      "firstName": "Chuck",
      "fullName": "Sen. Grassley, Chuck [R-IA]",
      "isOriginalCosponsor": "False",
      "lastName": "Grassley",
      "party": "R",
      "sponsorshipDate": "2026-03-25",
      "state": "IA"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "False",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2026-03-25",
      "state": "NE"
    },
    {
      "bioguideId": "E000295",
      "firstName": "Joni",
      "fullName": "Sen. Ernst, Joni [R-IA]",
      "isOriginalCosponsor": "False",
      "lastName": "Ernst",
      "party": "R",
      "sponsorshipDate": "2026-04-13",
      "state": "IA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3788is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3788\nIN THE SENATE OF THE UNITED STATES\nFebruary 5, 2026 Mr. Scott of Florida (for himself, Mrs. Gillibrand , Mr. Tuberville , Mrs. Britt , and Mr. Johnson ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo amend the Federal Food, Drug, and Cosmetic Act to require drug labeling to include original manufacturer and supply chain information.\n#### 1. Short title\nThis Act may be cited as the Consumer Labeling for Enhanced API Reporting and Legitimate Accountability for Base Entity Listings Act or the CLEAR LABELS Act .\n#### 2. Require drug labeling to include original manufacturer and supply chain information\nSection 502(b) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 352(b) ) is amended\u2014\n**(1)**\nby striking containing (1) the name and place of business of the manufacturer, packer, or distributor and inserting the following: \u201ccontaining\u2014\n(A) the name, place of business, and unique facility identifier of the manufacturer, packer, or distributor or a link, barcode, QR code, or other means to access a searchable electronic portal containing such information ;\n**(2)**\nin clause (A) (as so designated), by striking (2) an accurate and inserting the following:\n(B) an accurate ;\n**(3)**\nin clause (B) (as so designated), by striking count: Provided, That under clause (2) of this paragraph reasonable variations and inserting count, provided that under this clause, reasonable variations ;\n**(4)**\nby striking (b) If in a package form and inserting the following:\n(b) (1) If it is a finished drug product in a package form ; and\n**(5)**\nby adding at the end the following:\n(2) If it is an active pharmaceutical ingredient, unless any accompanying label and certificate of analysis contains the name, place of business, and unique facility identifier of the original manufacturer. (3) (A) If it is a finished drug product, unless its labeling contains the name, place of business, and unique facility identifier of\u2014 (i) the original manufacturer of each active pharmaceutical ingredient; (ii) the original manufacturer of the finished drug product; and (iii) the packer or distributor, if any, or a link, barcode, QR code, or other means to access a searchable electronic portal containing such information. (B) In the case of a finished drug product for which there are multiple potential different manufacturers of the active pharmaceutical ingredient, the requirements of this subparagraph shall be satisfied if all such manufacturers of active pharmaceutical ingredients for the drug product are identified in the labeling or the searchable electronic portal. (4) A manufacturer, packer, or distributor required to furnish information under paragraphs (1), (2), and (3), in addition to making such information available electronically, as applicable, shall make such information available through a package insert, or in paper copy to any individual who requests such a copy. (5) For purposes of this subsection, the term original manufacturer , means the single last establishment to conduct substantial manufacturing activities prior to introduction of the active pharmaceutical ingredient or finished drug product into interstate commerce. (6) The Secretary shall issue regulations to implement subparagraphs (2) and (3) and may provide for reasonable variations in the implementation of, or an alternative placement for, the labeling requirements under such subparagraphs, including by electronic means. Such regulations shall take effect on a date determined by the Secretary and not earlier than 1 year after the date of publication of the final regulations, and shall apply with respect to drugs manufactured on or after the effective date of such regulations. .\n#### 3. Exemption from customs country of origin marking requirement\nSection 304 of the Tariff Act of 1930 ( 19 U.S.C. 1304 ) is amended by adding at the end the following:\n(m) Marking of certain finished drug products The marking requirements of subsections (a) and (b) shall not apply to articles that are finished drug products and are marked in accordance with the requirements of section 502(b)(2)(A) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 352(b)(2)(A) ). .",
      "versionDate": "2026-02-05",
      "versionType": "Introduced in Senate"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2026-04-14",
        "text": "Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "8269",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "CLEAR LABELS Act",
      "type": "HR"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": {
        "item": [
          {
            "name": "Consumer affairs",
            "updateDate": "2026-05-01T18:56:04Z"
          },
          {
            "name": "Manufacturing",
            "updateDate": "2026-05-01T18:56:27Z"
          },
          {
            "name": "Prescription drugs",
            "updateDate": "2026-05-01T18:56:10Z"
          },
          {
            "name": "Supply chain",
            "updateDate": "2026-05-01T18:56:32Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2026-02-26T15:45:24Z"
      }
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-02-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3788is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "CLEAR LABELS Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-14T11:03:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "CLEAR LABELS Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-21T04:53:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Consumer Labeling for Enhanced API Reporting and Legitimate Accountability for Base Entity Listings Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-21T04:53:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Federal Food, Drug, and Cosmetic Act to require drug labeling to include original manufacturer and supply chain information.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-21T04:48:29Z"
    }
  ]
}
```
