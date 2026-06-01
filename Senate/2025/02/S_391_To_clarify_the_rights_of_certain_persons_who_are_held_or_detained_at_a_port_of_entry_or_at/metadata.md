# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/391?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/391
- Title: Access to Counsel Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 391
- Origin chamber: Senate
- Introduced date: 2025-02-04
- Update date: 2026-05-15T11:03:24Z
- Update date including text: 2026-05-15T11:03:24Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-04: Introduced in Senate
- 2025-02-04 - IntroReferral: Introduced in Senate
- 2025-02-04 - IntroReferral: Read twice and referred to the Committee on the Judiciary. (Sponsor introductory remarks on measure: CR S595-596)
- Latest action: 2025-02-04: Introduced in Senate

## Actions

- 2025-02-04 - IntroReferral: Introduced in Senate
- 2025-02-04 - IntroReferral: Read twice and referred to the Committee on the Judiciary. (Sponsor introductory remarks on measure: CR S595-596)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-04",
    "latestAction": {
      "actionDate": "2025-02-04",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/391",
    "number": "391",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "P000145",
        "district": "",
        "firstName": "Alex",
        "fullName": "Sen. Padilla, Alex [D-CA]",
        "lastName": "Padilla",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Access to Counsel Act of 2025",
    "type": "S",
    "updateDate": "2026-05-15T11:03:24Z",
    "updateDateIncludingText": "2026-05-15T11:03:24Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-04",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary. (Sponsor introductory remarks on measure: CR S595-596)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-04",
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
            "date": "2025-02-04T19:48:53Z",
            "name": "Referred To"
          },
          {
            "date": "2025-02-04T19:48:53Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
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
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "CT"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "NJ"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "DE"
    },
    {
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "NV"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "IL"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "IL"
    },
    {
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "CO"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "HI"
    },
    {
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "MA"
    },
    {
      "bioguideId": "M001111",
      "firstName": "Patty",
      "fullName": "Sen. Murray, Patty [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Murray",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "WA"
    },
    {
      "bioguideId": "R000608",
      "firstName": "Jacklyn",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "NV"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "CA"
    },
    {
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "MA"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "VT"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Lujan, Ben Ray [D-NM]",
      "isOriginalCosponsor": "False",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-02-11",
      "state": "NM"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2026-05-14",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s391is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 391\nIN THE SENATE OF THE UNITED STATES\nFebruary 4, 2025 Mr. Padilla (for himself, Mr. Blumenthal , Mr. Booker , Mr. Coons , Ms. Cortez Masto , Ms. Duckworth , Mr. Durbin , Mr. Hickenlooper , Ms. Hirono , Mr. Markey , Mrs. Murray , Ms. Rosen , Mr. Schiff , Ms. Warren , and Mr. Welch ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo clarify the rights of certain persons who are held or detained at a port of entry or at any facility overseen by U.S. Customs and Border Protection.\n#### 1. Short title\nThis Act may be cited as the Access to Counsel Act of 2025 .\n#### 2. Access to counsel and other assistance at ports of entry and during deferred inspection\n##### (a) Access to counsel and other assistance during inspection\nSection 235 of the Immigration and Nationality Act ( 8 U.S.C. 1225 ) is amended by adding at the end the following:\n(e) Access to counsel and other assistance during inspection at ports of entry and during deferred inspection (1) In general The Secretary of Homeland Security shall ensure that each covered individual has a meaningful opportunity to consult with counsel and an interested party during the inspection process. (2) Scope of assistance The Secretary of Homeland Security shall\u2014 (A) provide each covered individual with a meaningful opportunity to consult (including consultation by telephone) with counsel and an interested party not later than 1 hour after the secondary inspection process commences and as necessary throughout the remainder of the inspection process, including, as applicable, during deferred inspection; (B) allow counsel and an interested party to advocate on behalf of the covered individual, including by providing to the examining immigration officer information, documentation, and other evidence in support of the covered individual; and (C) to the greatest extent practicable, accommodate a request by the covered individual for counsel or an interested party to appear in person at the secondary or deferred inspection site. (3) Special rule for lawful permanent residents (A) In general Except as provided in subparagraph (B), the Secretary of Homeland Security may not accept a Form I\u2013407 Record of Abandonment of Lawful Permanent Resident Status (or a successor form) from a lawful permanent resident subject to secondary or deferred inspection without first providing such lawful permanent resident a meaningful opportunity to seek advice from counsel. (B) Exception The Secretary of Homeland Security may accept a Form I\u2013407 Record of Abandonment of Lawful Permanent Resident Status (or a successor form) from any lawful permanent resident subject to secondary or deferred inspection if such lawful permanent resident knowingly, intelligently, and voluntarily waives, in writing, the opportunity to seek advice from counsel. (4) Definitions In this section: (A) Counsel The term counsel means\u2014 (i) an attorney who is a member in good standing of the bar of any State, the District of Columbia, or a territory or a possession of the United States and is not under an order suspending, enjoining, restraining, disbarring, or otherwise restricting the attorney in the practice of law; or (ii) an individual accredited by the Attorney General, acting as a representative of an organization recognized by the Executive Office for Immigration Review, to represent a covered individual in immigration matters. (B) Covered individual The term covered individual means an individual subject to secondary or deferred inspection who is\u2014 (i) a national of the United States; (ii) an immigrant, lawfully admitted for permanent residence, who is returning from a temporary visit abroad; (iii) an alien seeking admission as an immigrant in possession of a valid unexpired immigrant visa; (iv) an alien seeking admission as a nonimmigrant in possession of a valid unexpired nonimmigrant visa; (v) a refugee; (vi) a returning asylee; or (vii) an alien who has been approved for parole under section 212(d)(5)(A), including an alien who is returning to the United States in possession of a valid advance parole document. (C) Interested party The term interested party means\u2014 (i) a relative of the covered individual; (ii) in the case of a covered individual to whom an immigrant or a nonimmigrant visa has been issued, the petitioner or sponsor thereof (including an agent of such petitioner or sponsor); or (iii) a person, organization, or entity in the United States with a bona fide connection to the covered individual. .\n##### (b) Effective date\nThe amendment made by subsection (a) shall take effect on the date that is 180 days after the date of the enactment of this Act.\n##### (c) Savings provision\nNothing in this Act, or in any amendment made by this Act, may be construed to limit a right to counsel or any right to appointed counsel under\u2014\n**(1)**\nsection 240(b)(4)(A) of the Immigration and Nationality Act ( 8 U.S.C. 1229a(b)(4)(A) );\n**(2)**\nsection 292 of such Act ( 8 U.S.C. 1362 ); or\n**(3)**\nany other provision of law, including any final court order securing such rights,\nas in effect on the day before the date of the enactment of this Act.",
      "versionDate": "2025-02-04",
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
        "actionDate": "2025-02-04",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "944",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Access to Counsel Act",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Immigration",
        "updateDate": "2025-03-10T13:42:47Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-04",
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
          "measure-id": "id119s391",
          "measure-number": "391",
          "measure-type": "s",
          "orig-publish-date": "2025-02-04",
          "originChamber": "SENATE",
          "update-date": "2025-07-10"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s391v00",
            "update-date": "2025-07-10"
          },
          "action-date": "2025-02-04",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Access to Counsel Act of 2025</strong></p><p>This bill provides various protections for covered individuals subject to secondary or deferred inspections when seeking admission into the United States. Covered individuals include U.S. nationals, lawful permanent residents, non-U.S. nationals (<em>aliens </em>under federal law) in possession of a visa, returning asylees, and refugees.</p><p>The Department of Homeland Security must ensure that a covered individual subject to secondary or deferred inspection has a meaningful opportunity to consult with counsel and certain related parties, such as a relative, within an hour of the start of the secondary inspection and as necessary during the inspection process. The counsel and related party must be allowed to advocate on behalf of the covered individual, including by providing evidence and information to the examining immigration officer.</p><p>A lawful permanent resident subject to secondary or deferred inspection may not abandon lawful permanent resident status until the individual has had a meaningful opportunity to seek advice from counsel, unless the individual voluntarily and knowingly waives in writing this opportunity to seek counsel's advice. </p>"
        },
        "title": "Access to Counsel Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s391.xml",
    "summary": {
      "actionDate": "2025-02-04",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Access to Counsel Act of 2025</strong></p><p>This bill provides various protections for covered individuals subject to secondary or deferred inspections when seeking admission into the United States. Covered individuals include U.S. nationals, lawful permanent residents, non-U.S. nationals (<em>aliens </em>under federal law) in possession of a visa, returning asylees, and refugees.</p><p>The Department of Homeland Security must ensure that a covered individual subject to secondary or deferred inspection has a meaningful opportunity to consult with counsel and certain related parties, such as a relative, within an hour of the start of the secondary inspection and as necessary during the inspection process. The counsel and related party must be allowed to advocate on behalf of the covered individual, including by providing evidence and information to the examining immigration officer.</p><p>A lawful permanent resident subject to secondary or deferred inspection may not abandon lawful permanent resident status until the individual has had a meaningful opportunity to seek advice from counsel, unless the individual voluntarily and knowingly waives in writing this opportunity to seek counsel's advice. </p>",
      "updateDate": "2025-07-10",
      "versionCode": "id119s391"
    },
    "title": "Access to Counsel Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-04",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Access to Counsel Act of 2025</strong></p><p>This bill provides various protections for covered individuals subject to secondary or deferred inspections when seeking admission into the United States. Covered individuals include U.S. nationals, lawful permanent residents, non-U.S. nationals (<em>aliens </em>under federal law) in possession of a visa, returning asylees, and refugees.</p><p>The Department of Homeland Security must ensure that a covered individual subject to secondary or deferred inspection has a meaningful opportunity to consult with counsel and certain related parties, such as a relative, within an hour of the start of the secondary inspection and as necessary during the inspection process. The counsel and related party must be allowed to advocate on behalf of the covered individual, including by providing evidence and information to the examining immigration officer.</p><p>A lawful permanent resident subject to secondary or deferred inspection may not abandon lawful permanent resident status until the individual has had a meaningful opportunity to seek advice from counsel, unless the individual voluntarily and knowingly waives in writing this opportunity to seek counsel's advice. </p>",
      "updateDate": "2025-07-10",
      "versionCode": "id119s391"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s391is.xml"
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
      "title": "Access to Counsel Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-15T11:03:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Access to Counsel Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-06T02:53:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to clarify the rights of certain persons who are held or detained at a port of entry or at any facility overseen by U.S. Customs and Border Protection.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-06T02:48:19Z"
    }
  ]
}
```
