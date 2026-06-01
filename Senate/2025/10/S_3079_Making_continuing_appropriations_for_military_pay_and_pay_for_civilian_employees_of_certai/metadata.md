# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3079?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3079
- Title: Armed Forces Pay Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 3079
- Origin chamber: Senate
- Introduced date: 2025-10-30
- Update date: 2025-11-04T12:03:14Z
- Update date including text: 2025-11-04T12:03:14Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-10-30: Introduced in Senate
- 2025-10-30 - IntroReferral: Introduced in Senate
- 2025-10-30 - IntroReferral: Read twice and referred to the Committee on Appropriations.
- Latest action: 2025-10-30: Introduced in Senate

## Actions

- 2025-10-30 - IntroReferral: Introduced in Senate
- 2025-10-30 - IntroReferral: Read twice and referred to the Committee on Appropriations.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-30",
    "latestAction": {
      "actionDate": "2025-10-30",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3079",
    "number": "3079",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "C001088",
        "district": "",
        "firstName": "Christopher",
        "fullName": "Sen. Coons, Christopher A. [D-DE]",
        "lastName": "Coons",
        "party": "D",
        "state": "DE"
      }
    ],
    "title": "Armed Forces Pay Act of 2025",
    "type": "S",
    "updateDate": "2025-11-04T12:03:14Z",
    "updateDateIncludingText": "2025-11-04T12:03:14Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-10-30",
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
      "actionDate": "2025-10-30",
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
          "date": "2025-10-30T17:40:37Z",
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
      "bioguideId": "S000148",
      "firstName": "Charles",
      "fullName": "Sen. Schumer, Charles E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Schumer",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-10-30",
      "state": "NY"
    },
    {
      "bioguideId": "M001111",
      "firstName": "Patty",
      "fullName": "Sen. Murray, Patty [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Murray",
      "party": "D",
      "sponsorshipDate": "2025-10-30",
      "state": "WA"
    },
    {
      "bioguideId": "R000122",
      "firstName": "John",
      "fullName": "Sen. Reed, Jack [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Reed",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-10-30",
      "state": "RI"
    },
    {
      "bioguideId": "S001194",
      "firstName": "Brian",
      "fullName": "Sen. Schatz, Brian [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Schatz",
      "party": "D",
      "sponsorshipDate": "2025-10-30",
      "state": "HI"
    },
    {
      "bioguideId": "R000608",
      "firstName": "Jacky",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2025-10-30",
      "state": "NV"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-10-30",
      "state": "CT"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-10-30",
      "state": "NY"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-10-30",
      "state": "OR"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Luj\u00e1n, Ben Ray [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-10-30",
      "state": "NM"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2025-10-30",
      "state": "NM"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-10-30",
      "state": "VT"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-10-30",
      "state": "CA"
    },
    {
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2025-10-30",
      "state": "AZ"
    },
    {
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-10-30",
      "state": "CO"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-10-30",
      "state": "OR"
    },
    {
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2025-10-30",
      "state": "CO"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-10-30",
      "state": "NH"
    },
    {
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2025-10-30",
      "state": "RI"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-10-30",
      "state": "IL"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-10-30",
      "state": "HI"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-10-30",
      "state": "IL"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-10-30",
      "state": "MN"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2025-10-30",
      "state": "AZ"
    },
    {
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2025-10-30",
      "state": "NV"
    },
    {
      "bioguideId": "B001303",
      "firstName": "Lisa",
      "fullName": "Sen. Blunt Rochester, Lisa [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Blunt Rochester",
      "party": "D",
      "sponsorshipDate": "2025-10-30",
      "state": "DE"
    },
    {
      "bioguideId": "W000805",
      "firstName": "Mark",
      "fullName": "Sen. Warner, Mark R. [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warner",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-10-30",
      "state": "VA"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2025-11-03",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3079is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3079\nIN THE SENATE OF THE UNITED STATES\nOctober 30, 2025 Mr. Coons (for himself, Mr. Schumer , Mrs. Murray , Mr. Reed , Mr. Schatz , Ms. Rosen , Mr. Blumenthal , Mrs. Gillibrand , Mr. Wyden , Mr. Luj\u00e1n , Mr. Heinrich , Mr. Welch , Mr. Padilla , Mr. Kelly , Mr. Hickenlooper , Mr. Merkley , Mr. Bennet , Mrs. Shaheen , Mr. Whitehouse , Mr. Durbin , Ms. Hirono , Ms. Duckworth , Ms. Klobuchar , Mr. Gallego , Ms. Cortez Masto , Ms. Blunt Rochester , and Mr. Warner ) introduced the following bill; which was read twice and referred to the Committee on Appropriations\nA BILL\nMaking continuing appropriations for military pay and pay for civilian employees of certain elements of the intelligence community in the event of a Government shutdown, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Armed Forces Pay Act of 2025 .\n#### 2. Continuing appropriations for members of the Armed Forces and civilian employees of certain elements of the intelligence community\n##### (a) In general\nThere are hereby appropriated for fiscal year 2026, out of any money in the Treasury not otherwise appropriated, for any period during which interim or full-year appropriations for fiscal year 2026 are not in effect\u2014\n**(1)**\nsuch sums as are necessary to provide pay and allowances to members of the Armed Forces (as defined in section 101(a)(4) of title 10, United States Code), including members of reserve components who perform active service or inactive-duty training during such period; and\n**(2)**\nsuch sums as are necessary to provide pay and allowances to civilian employees of the Department of Defense, the Coast Guard, the Office of the Director of National Intelligence, and the Central Intelligence Agency.\n##### (b) Definitions\nIn this section, the terms active service and inactive-duty training have the meanings given those terms in section 101(d) of title 10, United States Code.\n#### 3. Termination\nAppropriations and funds made available and authority granted pursuant to this Act shall be available until whichever of the following first occurs:\n**(1)**\nThe enactment into law of an appropriation (including a continuing appropriation) for any purpose for which amounts are made available in section 2.\n**(2)**\nThe enactment into law of the applicable regular or continuing appropriations resolution or other Act without any appropriation for such purpose.\n**(3)**\nSeptember 30, 2026.\n#### 4. Treatment of appropriated funds\nFunds appropriated by this Act, or made available by the transfer of funds in this Act, for intelligence activities and intelligence-related activities are deemed to be specifically authorized by the Congress for purposes of section 504 of the National Security Act of 1947 ( 50 U.S.C. 3094 ) during fiscal year 2026 until the enactment of the Intelligence Authorization Act for Fiscal Year 2026.",
      "versionDate": "2025-10-30",
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
        "actionDate": "2025-10-28",
        "text": "Read twice and referred to the Committee on Appropriations."
      },
      "number": "3060",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Paychecks for Patriots Act of 2025",
      "type": "S"
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-11-03T15:21:01Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-10-30",
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
          "measure-id": "id119s3079",
          "measure-number": "3079",
          "measure-type": "s",
          "orig-publish-date": "2025-10-30",
          "originChamber": "SENATE",
          "update-date": "2025-11-03"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s3079v00",
            "update-date": "2025-11-03"
          },
          "action-date": "2025-10-30",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Armed Forces Pay Act of 2025</strong></p><p>This bill provides continuing appropriations to pay members of\u00a0the Armed Forces and\u00a0civilian employees of the Department of Defense (DOD) and intelligence agencies during any period in which interim or full-year appropriations for FY2026 are not in effect (i.e., a government shutdown).</p><p>Specifically, the bill provides continuing appropriations for the pay and allowances of (1) members of the Armed Forces, including reserve components, who perform active service or inactive-duty training during the period; and (2) civilian employees of DOD, the Coast Guard, the Office of the Director of National Intelligence, and the Central Intelligence Agency.</p><p>The appropriations provided by the bill are available until the earlier of (1) the enactment into law of specified appropriations legislation, or (2) September 30, 2026.\u00a0</p><p>The bill also specifies that the funds provided by this bill for intelligence or intelligence-related activities are deemed to be specifically authorized by the Congress during FY2026 until the enactment of the Intelligence Authorization Act for Fiscal Year 2026.</p>"
        },
        "title": "Armed Forces Pay Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s3079.xml",
    "summary": {
      "actionDate": "2025-10-30",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Armed Forces Pay Act of 2025</strong></p><p>This bill provides continuing appropriations to pay members of\u00a0the Armed Forces and\u00a0civilian employees of the Department of Defense (DOD) and intelligence agencies during any period in which interim or full-year appropriations for FY2026 are not in effect (i.e., a government shutdown).</p><p>Specifically, the bill provides continuing appropriations for the pay and allowances of (1) members of the Armed Forces, including reserve components, who perform active service or inactive-duty training during the period; and (2) civilian employees of DOD, the Coast Guard, the Office of the Director of National Intelligence, and the Central Intelligence Agency.</p><p>The appropriations provided by the bill are available until the earlier of (1) the enactment into law of specified appropriations legislation, or (2) September 30, 2026.\u00a0</p><p>The bill also specifies that the funds provided by this bill for intelligence or intelligence-related activities are deemed to be specifically authorized by the Congress during FY2026 until the enactment of the Intelligence Authorization Act for Fiscal Year 2026.</p>",
      "updateDate": "2025-11-03",
      "versionCode": "id119s3079"
    },
    "title": "Armed Forces Pay Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-10-30",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Armed Forces Pay Act of 2025</strong></p><p>This bill provides continuing appropriations to pay members of\u00a0the Armed Forces and\u00a0civilian employees of the Department of Defense (DOD) and intelligence agencies during any period in which interim or full-year appropriations for FY2026 are not in effect (i.e., a government shutdown).</p><p>Specifically, the bill provides continuing appropriations for the pay and allowances of (1) members of the Armed Forces, including reserve components, who perform active service or inactive-duty training during the period; and (2) civilian employees of DOD, the Coast Guard, the Office of the Director of National Intelligence, and the Central Intelligence Agency.</p><p>The appropriations provided by the bill are available until the earlier of (1) the enactment into law of specified appropriations legislation, or (2) September 30, 2026.\u00a0</p><p>The bill also specifies that the funds provided by this bill for intelligence or intelligence-related activities are deemed to be specifically authorized by the Congress during FY2026 until the enactment of the Intelligence Authorization Act for Fiscal Year 2026.</p>",
      "updateDate": "2025-11-03",
      "versionCode": "id119s3079"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-10-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3079is.xml"
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
      "title": "Armed Forces Pay Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-04T12:03:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Armed Forces Pay Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-01T03:53:13Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill making continuing appropriations for military pay and pay for civilian employees of certain elements of the intelligence community in the event of a Government shutdown, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-01T03:48:17Z"
    }
  ]
}
```
