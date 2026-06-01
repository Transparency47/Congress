# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2952?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2952
- Title: $2.50 for America’s 250th Act
- Congress: 119
- Bill type: S
- Bill number: 2952
- Origin chamber: Senate
- Introduced date: 2025-09-30
- Update date: 2026-04-20T15:24:15Z
- Update date including text: 2026-04-20T15:24:15Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-09-30: Introduced in Senate
- 2025-09-30 - IntroReferral: Introduced in Senate
- 2025-09-30 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2025-09-30: Introduced in Senate

## Actions

- 2025-09-30 - IntroReferral: Introduced in Senate
- 2025-09-30 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-30",
    "latestAction": {
      "actionDate": "2025-09-30",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2952",
    "number": "2952",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "L000571",
        "district": "",
        "firstName": "Cynthia",
        "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
        "lastName": "Lummis",
        "party": "R",
        "state": "WY"
      }
    ],
    "title": "$2.50 for America\u2019s 250th Act",
    "type": "S",
    "updateDate": "2026-04-20T15:24:15Z",
    "updateDateIncludingText": "2026-04-20T15:24:15Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-30",
      "committees": {
        "item": {
          "name": "Banking, Housing, and Urban Affairs Committee",
          "systemCode": "ssbk00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-09-30",
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
            "date": "2025-09-30T19:24:59Z",
            "name": "Referred To"
          },
          {
            "date": "2025-09-30T19:24:59Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Banking, Housing, and Urban Affairs Committee",
      "systemCode": "ssbk00",
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
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "WV"
    },
    {
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "ND"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "NH"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "CA"
    },
    {
      "bioguideId": "M001153",
      "firstName": "Lisa",
      "fullName": "Sen. Murkowski, Lisa [R-AK]",
      "isOriginalCosponsor": "True",
      "lastName": "Murkowski",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "AK"
    },
    {
      "bioguideId": "S001184",
      "firstName": "Tim",
      "fullName": "Sen. Scott, Tim [R-SC]",
      "isOriginalCosponsor": "False",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-12-01",
      "state": "SC"
    },
    {
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "False",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2026-02-24",
      "state": "ME"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2952is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2952\nIN THE SENATE OF THE UNITED STATES\nSeptember 30, 2025 Ms. Lummis (for herself, Mrs. Capito , Mr. Cramer , Mrs. Shaheen , Mr. Padilla , and Ms. Murkowski ) introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo amend title 31, United States Code, to require the Secretary of the Treasury to mint and issue $2.50 numismatic coins and $2.50 circulating coins, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the $2.50 for America\u2019s 250th Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nThe signing of the Declaration of Independence was a turning point in the history of the United States and the world, and the 250th anniversary of the signing warrants national recognition.\n**(2)**\nThe 68th Congress celebrated this fact by authorizing the United States Mint to commemorate the 150th anniversary of American independence by issuing 2 coins: A half dollar and a $2.50 gold piece.\n**(3)**\nThe issuance of a $2.50 anniversary coin for the 250th anniversary serves as a historically grounded continuation of this numismatic tradition and connects Americans today with a legacy of national celebration through coinage.\n**(4)**\nThe design and distribution of this coin offer a unique and accessible opportunity for the American people to engage with and take personal ownership of their national heritage through a tangible and lasting tribute.\n**(5)**\nEvery citizen deserves the opportunity to acquire such a coin as a means to connect to the founding principles of liberty, democracy, and self-governance.\n**(6)**\nIn addition to the congressionally authorized activities already planned by the Mint, this new anniversary coin will serve not only as a lasting tribute to the founding generation and the ideals we share with them to this day, but also as a unifying and educational gesture on the occasion of the semiquincentennial.\n#### 3. Circulating $2.50 coins\n##### (a) In general\nSection 5112 of title 31, United States Code, is amended by adding at the end the following:\n(bb) Circulating $2.50 coin (1) In general The Secretary shall mint and issue a $2.50 circulating coin upon determining that minting such coin is technically feasible, economically feasible, and not cost prohibitive. (2) Requirements Each coin minted and issued under this subsection shall\u2014 (A) have features that make the denomination of the coin readily discernible from other coins; and (B) be made of an alloy prescribed by the Secretary. (3) Design (A) Obverse The obverse of each coin minted and issued under this subsection shall, during the 5-year period beginning on the date the Secretary issues any coin under this subsection, bear the image of allegorical liberty wielding the Declaration of Independence featured on the gold $2.50 Sesquicentennial Coin issued in 1926. (B) Reverse The reverse of each coin minted and issued under this subsection shall, during the 5-year period beginning on the date the Secretary issues any coin under this subsection, bear the image Independence Hall featured on the gold $2.50 Sesquicentennial Coin issued in 1926. (C) Additional inscriptions During the 5-year period beginning on the date the Secretary issues any coin under this subsection, each coin minted and issued under this subsection shall bear the inscriptions Semiquincentennial of the United States and 1776\u20132026 . (D) Subsequent designs Beginning on the date that is 5 years after the Secretary issues a coin under this subsection, and every 5 years thereafter, the Secretary may select a new design that celebrates the founding of the United States for the $2.50 coin. .\n##### (b) Sense of Congress\nIt is the sense of the Congress that the circulating coin described in subsection (bb) of section 5112 of title 31, United States Code, as added by subsection (a) of this section, should be minted and issued not later than July 4, 2026, or as soon as it is technically and economically feasible.\n#### 4. Numismatic $2.50 coins\n##### (a) In general\nSection 5112 of title 31, United States Code, as amended by section 3 of this Act, is amended by adding at the end the following:\n(cc) Numismatic $2.50 coin (1) In general The Secretary may mint and issue $2.50 numismatic coins in silver, clad, and such other alloys, including gold, as the Secretary determines in accordance with such program procedures and coin specifications, varieties, quantities, and inscriptions as the Secretary, in the Secretary\u2019s discretion, may prescribe from time to time. (2) Design (A) Obverse The obverse design of any coin minted and issued under this subsection shall, during the 2-year period beginning on the date the Secretary issues any coin under this subsection, bear the image of allegorical liberty wielding the Declaration of Independence featured on the gold $2.50 Sesquicentennial Coin issued in 1926. (B) Reverse The reverse design of any coin minted and issued under this subsection shall, during the 2-year period beginning on the date the Secretary issues any coin under this subsection, bear the image of Independence Hall featured on the gold $2.50 Sesquicentennial Coin issued in 1926. (C) Additional inscriptions During the 2-year period beginning on the date the Secretary issues any coin under this subsection, each coin minted and issued under this subsection shall bear the inscriptions Semiquincentennial of the United States and 1776\u20132026 . (D) Subsequent designs Beginning on the date that is 2 years after the date on which the Secretary issues any coin under this subsection, and every 2 years thereafter, the Secretary may select a new design that celebrates the founding of the United States for the $2.50 coin. .\n##### (b) Sense of Congress\nIt is the sense of the Congress that the numismatic coins described in subsection (cc) of section 5112 of title 31, United States Code, as added by subsection (a) of this section, should be minted and issued not later than July 4, 2026, or as soon as it is technically and economically feasible.",
      "versionDate": "2025-09-30",
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
        "actionDate": "2026-02-12",
        "text": "Received in the Senate."
      },
      "number": "5616",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "$2.50 for America\u2019s 250th Act",
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
            "name": "Currency",
            "updateDate": "2026-02-10T17:06:28Z"
          },
          {
            "name": "U.S. history",
            "updateDate": "2026-02-10T17:06:28Z"
          }
        ]
      },
      "policyArea": {
        "name": "Finance and Financial Sector",
        "updateDate": "2025-10-30T19:02:25Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-09-30",
    "originChamber": "Senate",
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
          "measure-id": "id119s2952",
          "measure-number": "2952",
          "measure-type": "s",
          "orig-publish-date": "2025-09-30",
          "originChamber": "SENATE",
          "update-date": "2026-04-20"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s2952v00",
            "update-date": "2026-04-20"
          },
          "action-date": "2025-09-30",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>$2.50 for America\u2019s 250th Act</strong></p><p>This bill requires the minting of $2.50 coins to commemorate the 250th anniversary, or the semiquincentennial, of the signing of the Declaration of Independence.</p><p>Specifically, the Department of the Treasury must mint and issue a $2.50 circulating coin upon determining that such minting is technically feasible, economically feasible, and not cost prohibitive. The design of such a coin during the first five years of its issuance must be as described by the bill, however, subsequent designs may be selected by Treasury to celebrate the founding of the United States.</p><p>Treasury may also mint and issue $2.50 numismatic coins (i.e., collectible coins) in silver, clad, and other alloys, including gold.</p>"
        },
        "title": "$2.50 for America\u2019s 250th Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s2952.xml",
    "summary": {
      "actionDate": "2025-09-30",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>$2.50 for America\u2019s 250th Act</strong></p><p>This bill requires the minting of $2.50 coins to commemorate the 250th anniversary, or the semiquincentennial, of the signing of the Declaration of Independence.</p><p>Specifically, the Department of the Treasury must mint and issue a $2.50 circulating coin upon determining that such minting is technically feasible, economically feasible, and not cost prohibitive. The design of such a coin during the first five years of its issuance must be as described by the bill, however, subsequent designs may be selected by Treasury to celebrate the founding of the United States.</p><p>Treasury may also mint and issue $2.50 numismatic coins (i.e., collectible coins) in silver, clad, and other alloys, including gold.</p>",
      "updateDate": "2026-04-20",
      "versionCode": "id119s2952"
    },
    "title": "$2.50 for America\u2019s 250th Act"
  },
  "summaries": [
    {
      "actionDate": "2025-09-30",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>$2.50 for America\u2019s 250th Act</strong></p><p>This bill requires the minting of $2.50 coins to commemorate the 250th anniversary, or the semiquincentennial, of the signing of the Declaration of Independence.</p><p>Specifically, the Department of the Treasury must mint and issue a $2.50 circulating coin upon determining that such minting is technically feasible, economically feasible, and not cost prohibitive. The design of such a coin during the first five years of its issuance must be as described by the bill, however, subsequent designs may be selected by Treasury to celebrate the founding of the United States.</p><p>Treasury may also mint and issue $2.50 numismatic coins (i.e., collectible coins) in silver, clad, and other alloys, including gold.</p>",
      "updateDate": "2026-04-20",
      "versionCode": "id119s2952"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-09-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2952is.xml"
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
      "title": "$2.50 for America\u2019s 250th Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-25T12:03:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "$2.50 for America\u2019s 250th Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-18T03:23:13Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 31, United States Code, to require the Secretary of the Treasury to mint and issue $2.50 numismatic coins and $2.50 circulating coins, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-18T03:18:17Z"
    }
  ]
}
```
