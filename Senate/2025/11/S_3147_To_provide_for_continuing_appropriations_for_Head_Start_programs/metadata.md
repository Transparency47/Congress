# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3147?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3147
- Title: Keep Head Start Funded Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 3147
- Origin chamber: Senate
- Introduced date: 2025-11-06
- Update date: 2025-11-19T12:03:18Z
- Update date including text: 2025-11-19T12:03:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-11-06: Introduced in Senate
- 2025-11-06 - IntroReferral: Introduced in Senate
- 2025-11-06 - IntroReferral: Read twice and referred to the Committee on Appropriations.
- Latest action: 2025-11-06: Introduced in Senate

## Actions

- 2025-11-06 - IntroReferral: Introduced in Senate
- 2025-11-06 - IntroReferral: Read twice and referred to the Committee on Appropriations.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-06",
    "latestAction": {
      "actionDate": "2025-11-06",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3147",
    "number": "3147",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "B001230",
        "district": "",
        "firstName": "Tammy",
        "fullName": "Sen. Baldwin, Tammy [D-WI]",
        "lastName": "Baldwin",
        "party": "D",
        "state": "WI"
      }
    ],
    "title": "Keep Head Start Funded Act of 2025",
    "type": "S",
    "updateDate": "2025-11-19T12:03:18Z",
    "updateDateIncludingText": "2025-11-19T12:03:18Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-06",
      "committees": {
        "item": {
          "name": "Appropriations Committee",
          "systemCode": "ssap00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Appropriations.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-11-06",
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
        "item": {
          "date": "2025-11-06T22:23:08Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Appropriations Committee",
      "systemCode": "ssap00",
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
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-11-06",
      "state": "MA"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-11-06",
      "state": "OR"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2025-11-06",
      "state": "NM"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-11-06",
      "state": "MD"
    },
    {
      "bioguideId": "R000122",
      "firstName": "John",
      "fullName": "Sen. Reed, Jack [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Reed",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-11-06",
      "state": "RI"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Luj\u00e1n, Ben Ray [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-11-06",
      "state": "NM"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-11-06",
      "state": "VT"
    },
    {
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2025-11-06",
      "state": "AZ"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2025-11-06",
      "state": "NJ"
    },
    {
      "bioguideId": "H001076",
      "firstName": "Maggie",
      "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Hassan",
      "party": "D",
      "sponsorshipDate": "2025-11-06",
      "state": "NH"
    },
    {
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2025-11-06",
      "state": "CO"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-11-06",
      "state": "CT"
    },
    {
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2025-11-06",
      "state": "GA"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-11-06",
      "state": "NH"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-11-06",
      "state": "MN"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2025-11-06",
      "state": "VT"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-11-06",
      "state": "VA"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2025-11-06",
      "state": "MD"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-11-06",
      "state": "DE"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-11-06",
      "state": "CA"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2025-11-06",
      "state": "AZ"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-11-06",
      "state": "CA"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-11-06",
      "state": "IL"
    },
    {
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2025-11-06",
      "state": "NV"
    },
    {
      "bioguideId": "M001111",
      "firstName": "Patty",
      "fullName": "Sen. Murray, Patty [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Murray",
      "party": "D",
      "sponsorshipDate": "2025-11-06",
      "state": "WA"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-11-06",
      "state": "NY"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-11-06",
      "state": "NJ"
    },
    {
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2025-11-06",
      "state": "RI"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "False",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-11-07",
      "state": "OR"
    },
    {
      "bioguideId": "P000595",
      "firstName": "Gary",
      "fullName": "Sen. Peters, Gary C. [D-MI]",
      "isOriginalCosponsor": "False",
      "lastName": "Peters",
      "party": "D",
      "sponsorshipDate": "2025-11-07",
      "state": "MI"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "False",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-11-07",
      "state": "IL"
    },
    {
      "bioguideId": "M001153",
      "firstName": "Lisa",
      "fullName": "Sen. Murkowski, Lisa [R-AK]",
      "isOriginalCosponsor": "False",
      "lastName": "Murkowski",
      "party": "R",
      "sponsorshipDate": "2025-11-07",
      "state": "AK"
    },
    {
      "bioguideId": "S001208",
      "firstName": "Elissa",
      "fullName": "Sen. Slotkin, Elissa [D-MI]",
      "isOriginalCosponsor": "False",
      "lastName": "Slotkin",
      "party": "D",
      "sponsorshipDate": "2025-11-18",
      "state": "MI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3147is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3147\nIN THE SENATE OF THE UNITED STATES\nNovember 6, 2025 Ms. Baldwin (for herself, Mr. Markey , Mr. Wyden , Mr. Heinrich , Mr. Van Hollen , Mr. Reed , Mr. Luj\u00e1n , Mr. Welch , Mr. Kelly , Mr. Kim , Ms. Hassan , Mr. Bennet , Mr. Blumenthal , Mr. Warnock , Mrs. Shaheen , Ms. Smith , Mr. Sanders , Mr. Kaine , Ms. Alsobrooks , Mr. Coons , Mr. Schiff , Mr. Gallego , Mr. Padilla , Ms. Duckworth , Ms. Cortez Masto , Mrs. Murray , Mrs. Gillibrand , Mr. Booker , and Mr. Whitehouse ) introduced the following bill; which was read twice and referred to the Committee on Appropriations\nA BILL\nTo provide for continuing appropriations for Head Start programs.\n#### 1. Short title\nThis Act may be cited as the Keep Head Start Funded Act of 2025 .\n#### 2. Continuing appropriations for Head Start\nThere are hereby appropriated for fiscal year 2026, out of any money in the Treasury not otherwise appropriated, for any period during which interim or full-year appropriations for fiscal year 2026 are not in effect, such sums as are necessary for carrying out without interruption, under the authority and conditions provided for in division A of the Full-Year Continuing Appropriations and Extensions Act, 2025 ( Public Law 119\u20134 ), all projects or activities under the Head Start Act that were conducted in fiscal year 2025, and for which appropriations were made available by the Full-Year Continuing Appropriations and Extensions Act, 2025.\n#### 3. Termination\nAppropriations and funds made available and authority granted pursuant to this Act shall be available until whichever of the following first occurs:\n**(1)**\nThe enactment into law of an appropriation (including a continuing appropriation) for any purpose for which amounts are made available in section 2.\n**(2)**\nThe enactment into law of the regular or continuing appropriations resolution or other Act for the Department of Health and Human Services without any appropriation for such purpose.\n**(3)**\nSeptember 30, 2026.\n#### 4. Charge to future appropriations\nExpenditures made pursuant to this Act shall be charged to the applicable appropriation, fund, or authorization whenever a bill in which such applicable appropriation, fund, or authorization is contained is enacted into law.\n#### 5. Effective date\nThis Act shall take effect as if enacted on September 30, 2025.",
      "versionDate": "2025-11-06",
      "versionType": "Introduced in Senate"
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
        "name": "Education",
        "updateDate": "2025-11-10T19:12:16Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-11-06",
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
          "measure-id": "id119s3147",
          "measure-number": "3147",
          "measure-type": "s",
          "orig-publish-date": "2025-11-06",
          "originChamber": "SENATE",
          "update-date": "2025-11-11"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s3147v00",
            "update-date": "2025-11-11"
          },
          "action-date": "2025-11-06",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Keep Head Start Funded Act of 2025</strong></p><p>This bill provides FY2026 continuing appropriations to carry out Head Start programs without interruption during any period in which interim or full-year appropriations for FY2026 are not in effect (i.e., a government shutdown).</p><p>The Head Start programs provide comprehensive early childhood education and development services to low-income children. The programs seek to promote school readiness through the provision of educational, health, nutritional, social, and other services.\u00a0</p><p>This bill provides FY2026 appropriations to continue projects and activities under the programs that were funded in FY2025. The appropriations are available until the earliest of</p><ul><li>the enactment into law of legislation that provides appropriations (including continuing appropriations) for Head Start,</li><li>the enactment into law of legislation that provides regular or continuing appropriations for the Department of Health and Human Services without an appropriation for Head Start, or</li><li>September 30, 2026.</li></ul><p>This bill must take effect as if it had been enacted on September 30, 2025.\u00a0</p>"
        },
        "title": "Keep Head Start Funded Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s3147.xml",
    "summary": {
      "actionDate": "2025-11-06",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Keep Head Start Funded Act of 2025</strong></p><p>This bill provides FY2026 continuing appropriations to carry out Head Start programs without interruption during any period in which interim or full-year appropriations for FY2026 are not in effect (i.e., a government shutdown).</p><p>The Head Start programs provide comprehensive early childhood education and development services to low-income children. The programs seek to promote school readiness through the provision of educational, health, nutritional, social, and other services.\u00a0</p><p>This bill provides FY2026 appropriations to continue projects and activities under the programs that were funded in FY2025. The appropriations are available until the earliest of</p><ul><li>the enactment into law of legislation that provides appropriations (including continuing appropriations) for Head Start,</li><li>the enactment into law of legislation that provides regular or continuing appropriations for the Department of Health and Human Services without an appropriation for Head Start, or</li><li>September 30, 2026.</li></ul><p>This bill must take effect as if it had been enacted on September 30, 2025.\u00a0</p>",
      "updateDate": "2025-11-11",
      "versionCode": "id119s3147"
    },
    "title": "Keep Head Start Funded Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-11-06",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Keep Head Start Funded Act of 2025</strong></p><p>This bill provides FY2026 continuing appropriations to carry out Head Start programs without interruption during any period in which interim or full-year appropriations for FY2026 are not in effect (i.e., a government shutdown).</p><p>The Head Start programs provide comprehensive early childhood education and development services to low-income children. The programs seek to promote school readiness through the provision of educational, health, nutritional, social, and other services.\u00a0</p><p>This bill provides FY2026 appropriations to continue projects and activities under the programs that were funded in FY2025. The appropriations are available until the earliest of</p><ul><li>the enactment into law of legislation that provides appropriations (including continuing appropriations) for Head Start,</li><li>the enactment into law of legislation that provides regular or continuing appropriations for the Department of Health and Human Services without an appropriation for Head Start, or</li><li>September 30, 2026.</li></ul><p>This bill must take effect as if it had been enacted on September 30, 2025.\u00a0</p>",
      "updateDate": "2025-11-11",
      "versionCode": "id119s3147"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-11-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3147is.xml"
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
      "title": "Keep Head Start Funded Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-19T12:03:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Keep Head Start Funded Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-08T05:38:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to provide for continuing appropriations for Head Start programs.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-08T05:33:25Z"
    }
  ]
}
```
