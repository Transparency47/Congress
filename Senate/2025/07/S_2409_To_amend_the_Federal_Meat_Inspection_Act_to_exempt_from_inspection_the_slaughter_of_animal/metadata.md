# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2409?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2409
- Title: PRIME Act
- Congress: 119
- Bill type: S
- Bill number: 2409
- Origin chamber: Senate
- Introduced date: 2025-07-23
- Update date: 2026-03-03T12:03:26Z
- Update date including text: 2026-03-03T12:03:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-07-23: Introduced in Senate
- 2025-07-23 - IntroReferral: Introduced in Senate
- 2025-07-23 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.
- Latest action: 2025-07-23: Introduced in Senate

## Actions

- 2025-07-23 - IntroReferral: Introduced in Senate
- 2025-07-23 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-23",
    "latestAction": {
      "actionDate": "2025-07-23",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2409",
    "number": "2409",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "K000383",
        "district": "",
        "firstName": "Angus",
        "fullName": "Sen. King, Angus S., Jr. [I-ME]",
        "lastName": "King",
        "party": "I",
        "state": "ME"
      }
    ],
    "title": "PRIME Act",
    "type": "S",
    "updateDate": "2026-03-03T12:03:26Z",
    "updateDateIncludingText": "2026-03-03T12:03:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-23",
      "committees": {
        "item": {
          "name": "Agriculture, Nutrition, and Forestry Committee",
          "systemCode": "ssaf00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-23",
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
            "date": "2025-07-23T19:28:12Z",
            "name": "Referred To"
          },
          {
            "date": "2025-07-23T19:28:12Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Agriculture, Nutrition, and Forestry Committee",
      "systemCode": "ssaf00",
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
      "bioguideId": "P000603",
      "firstName": "Rand",
      "fullName": "Sen. Paul, Rand [R-KY]",
      "isOriginalCosponsor": "True",
      "lastName": "Paul",
      "party": "R",
      "sponsorshipDate": "2025-07-23",
      "state": "KY"
    },
    {
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-07-23",
      "state": "WY"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "OR"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "NY"
    },
    {
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2025-07-23",
      "state": "ND"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-07-23",
      "state": "TN"
    },
    {
      "bioguideId": "H001061",
      "firstName": "John",
      "fullName": "Sen. Hoeven, John [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Hoeven",
      "party": "R",
      "sponsorshipDate": "2025-07-23",
      "state": "ND"
    },
    {
      "bioguideId": "L000577",
      "firstName": "Mike",
      "fullName": "Sen. Lee, Mike [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "party": "R",
      "sponsorshipDate": "2025-07-23",
      "state": "UT"
    },
    {
      "bioguideId": "S001198",
      "firstName": "Dan",
      "fullName": "Sen. Sullivan, Dan [R-AK]",
      "isOriginalCosponsor": "False",
      "lastName": "Sullivan",
      "party": "R",
      "sponsorshipDate": "2026-03-02",
      "state": "AK"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2409is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2409\nIN THE SENATE OF THE UNITED STATES\nJuly 23, 2025 Mr. King (for himself, Mr. Paul , Ms. Lummis , Mr. Merkley , Mrs. Gillibrand , Mr. Cramer , Mrs. Blackburn , Mr. Hoeven , and Mr. Lee ) introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo amend the Federal Meat Inspection Act to exempt from inspection the slaughter of animals and the preparation of carcasses conducted at a custom slaughter facility, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Processing Revival and Intrastate Meat Exemption Act or the PRIME Act .\n#### 2. Exemption for slaughter and preparation occurring at custom slaughter facilities\nSection 23 of the Federal Meat Inspection Act ( 21 U.S.C. 623 ) is amended\u2014\n**(1)**\nby redesignating subsections (b), (c), and (d) as subsections (c), (d), and (e), respectively;\n**(2)**\nby inserting after subsection (a) the following:\n(b) Exemption for slaughter and preparation occurring at custom slaughter facilities (1) Definition of State In this subsection, the term State means any State or territory. (2) Exemption The provisions of this title requiring inspection of the slaughter of animals and the preparation of the carcasses, parts thereof, meat, and meat food products at establishments conducting those operations for commerce shall not apply to the slaughtering by any person of animals at a custom slaughter facility and the preparation at that custom slaughter facility and transportation in commerce of the carcasses, parts thereof, meat, and meat food products of those animals if\u2014 (A) the slaughtering and preparation carried out at the custom slaughter facility is carried out in accordance with the law of the State in which the custom slaughter facility is located; and (B) the animals are slaughtered and the carcasses, parts thereof, meat, and meat food products of the animals are prepared exclusively for distribution to\u2014 (i) household consumers within the State in which the custom slaughter facility is located; or (ii) restaurants, hotels, boarding houses, grocery stores, or other establishments located in the State in which the custom slaughter facility is located that\u2014 (I) are involved in the preparation of meals served directly to consumers; or (II) offer meat and meat food products for sale directly to consumers in the State. ; and\n**(3)**\nin subsection (c) (as so redesignated), in the second sentence, by striking paragraph (b) and inserting subsection .\n#### 3. No preemption of State law\nNothing in an amendment made by section 2 preempts any State law relating to\u2014\n**(1)**\nthe slaughter of animals or the preparation of carcasses, parts thereof, meat, and meat food products at a custom slaughter facility; or\n**(2)**\nthe sale of meat or meat food products.",
      "versionDate": "2025-07-23",
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
        "name": "Agriculture and Food",
        "updateDate": "2025-08-07T16:47:20Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-07-23",
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
          "measure-id": "id119s2409",
          "measure-number": "2409",
          "measure-type": "s",
          "orig-publish-date": "2025-07-23",
          "originChamber": "SENATE",
          "update-date": "2025-08-07"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s2409v00",
            "update-date": "2025-08-07"
          },
          "action-date": "2025-07-23",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><b>Processing Revival and Intrastate Meat Exemption Act or the PRIME Act</b></p> <p>This bill exempts from federal inspection requirements animals and meats that are slaughtered and prepared at custom animal slaughter facilities for distribution within the state. Under current law, a custom slaughter exemption applies if the meat is slaughtered exclusively for personal, household, guest, or employee uses. </p> <p>Specifically, the bill expands the federal inspection exemption to include the slaughter of animals or the preparation of carcasses, meat, and meat food products that are</p> <ul> <li>slaughtered and prepared at a custom slaughter facility in accordance with the laws of the state where the facility is located; and </li> <li>prepared exclusively for distribution to household consumers in the state or restaurants, hotels, boarding houses, grocery stores, or other establishments in the state that either prepare meals served directly to consumers or offer meat and food products for sale directly to consumers in the state. </li> </ul> <p>The bill does not preempt any state law concerning (1) the slaughter of animals or the preparation of carcasses, meat, and meat food products at a custom slaughter facility; or (2) the sale of meat or meat food products.</p>"
        },
        "title": "PRIME Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s2409.xml",
    "summary": {
      "actionDate": "2025-07-23",
      "actionDesc": "Introduced in Senate",
      "text": "<p><b>Processing Revival and Intrastate Meat Exemption Act or the PRIME Act</b></p> <p>This bill exempts from federal inspection requirements animals and meats that are slaughtered and prepared at custom animal slaughter facilities for distribution within the state. Under current law, a custom slaughter exemption applies if the meat is slaughtered exclusively for personal, household, guest, or employee uses. </p> <p>Specifically, the bill expands the federal inspection exemption to include the slaughter of animals or the preparation of carcasses, meat, and meat food products that are</p> <ul> <li>slaughtered and prepared at a custom slaughter facility in accordance with the laws of the state where the facility is located; and </li> <li>prepared exclusively for distribution to household consumers in the state or restaurants, hotels, boarding houses, grocery stores, or other establishments in the state that either prepare meals served directly to consumers or offer meat and food products for sale directly to consumers in the state. </li> </ul> <p>The bill does not preempt any state law concerning (1) the slaughter of animals or the preparation of carcasses, meat, and meat food products at a custom slaughter facility; or (2) the sale of meat or meat food products.</p>",
      "updateDate": "2025-08-07",
      "versionCode": "id119s2409"
    },
    "title": "PRIME Act"
  },
  "summaries": [
    {
      "actionDate": "2025-07-23",
      "actionDesc": "Introduced in Senate",
      "text": "<p><b>Processing Revival and Intrastate Meat Exemption Act or the PRIME Act</b></p> <p>This bill exempts from federal inspection requirements animals and meats that are slaughtered and prepared at custom animal slaughter facilities for distribution within the state. Under current law, a custom slaughter exemption applies if the meat is slaughtered exclusively for personal, household, guest, or employee uses. </p> <p>Specifically, the bill expands the federal inspection exemption to include the slaughter of animals or the preparation of carcasses, meat, and meat food products that are</p> <ul> <li>slaughtered and prepared at a custom slaughter facility in accordance with the laws of the state where the facility is located; and </li> <li>prepared exclusively for distribution to household consumers in the state or restaurants, hotels, boarding houses, grocery stores, or other establishments in the state that either prepare meals served directly to consumers or offer meat and food products for sale directly to consumers in the state. </li> </ul> <p>The bill does not preempt any state law concerning (1) the slaughter of animals or the preparation of carcasses, meat, and meat food products at a custom slaughter facility; or (2) the sale of meat or meat food products.</p>",
      "updateDate": "2025-08-07",
      "versionCode": "id119s2409"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-07-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2409is.xml"
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
      "title": "PRIME Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-03T12:03:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "PRIME Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-07T05:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Processing Revival and Intrastate Meat Exemption Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-07T05:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Federal Meat Inspection Act to exempt from inspection the slaughter of animals and the preparation of carcasses conducted at a custom slaughter facility, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-07T05:18:30Z"
    }
  ]
}
```
