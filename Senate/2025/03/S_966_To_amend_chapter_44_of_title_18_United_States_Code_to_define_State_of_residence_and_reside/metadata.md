# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/966?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/966
- Title: Traveler's Gun Rights Act
- Congress: 119
- Bill type: S
- Bill number: 966
- Origin chamber: Senate
- Introduced date: 2025-03-11
- Update date: 2026-03-23T18:18:26Z
- Update date including text: 2026-03-23T18:18:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-03-11: Introduced in Senate
- 2025-03-11 - IntroReferral: Introduced in Senate
- 2025-03-11 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-03-11: Introduced in Senate

## Actions

- 2025-03-11 - IntroReferral: Introduced in Senate
- 2025-03-11 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-11",
    "latestAction": {
      "actionDate": "2025-03-11",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/966",
    "number": "966",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "R000605",
        "district": "",
        "firstName": "Mike",
        "fullName": "Sen. Rounds, Mike [R-SD]",
        "lastName": "Rounds",
        "party": "R",
        "state": "SD"
      }
    ],
    "title": "Traveler's Gun Rights Act",
    "type": "S",
    "updateDate": "2026-03-23T18:18:26Z",
    "updateDateIncludingText": "2026-03-23T18:18:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-11",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-11",
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
          "date": "2025-03-11T22:21:23Z",
          "name": "Referred To"
        }
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
      "bioguideId": "M001198",
      "firstName": "Roger",
      "fullName": "Sen. Marshall, Roger [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Marshall",
      "party": "R",
      "sponsorshipDate": "2025-03-11",
      "state": "KS"
    },
    {
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-03-11",
      "state": "ID"
    },
    {
      "bioguideId": "L000575",
      "firstName": "James",
      "fullName": "Sen. Lankford, James [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Lankford",
      "party": "R",
      "sponsorshipDate": "2025-03-11",
      "state": "OK"
    },
    {
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2025-03-11",
      "state": "ND"
    },
    {
      "bioguideId": "B001236",
      "firstName": "John",
      "fullName": "Sen. Boozman, John [R-AR]",
      "isOriginalCosponsor": "True",
      "lastName": "Boozman",
      "party": "R",
      "sponsorshipDate": "2025-03-11",
      "state": "AR"
    },
    {
      "bioguideId": "H001061",
      "firstName": "John",
      "fullName": "Sen. Hoeven, John [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Hoeven",
      "party": "R",
      "sponsorshipDate": "2025-03-11",
      "state": "ND"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-03-11",
      "state": "NC"
    },
    {
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2025-03-11",
      "state": "MS"
    },
    {
      "bioguideId": "C001098",
      "firstName": "Ted",
      "fullName": "Sen. Cruz, Ted [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cruz",
      "party": "R",
      "sponsorshipDate": "2025-03-11",
      "state": "TX"
    },
    {
      "bioguideId": "C000880",
      "firstName": "Mike",
      "fullName": "Sen. Crapo, Mike [R-ID]",
      "isOriginalCosponsor": "False",
      "lastName": "Crapo",
      "party": "R",
      "sponsorshipDate": "2025-03-24",
      "state": "ID"
    },
    {
      "bioguideId": "M001243",
      "firstName": "David",
      "fullName": "Sen. McCormick, David [R-PA]",
      "isOriginalCosponsor": "False",
      "lastName": "McCormick",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-11-10",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s966is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 966\nIN THE SENATE OF THE UNITED STATES\nMarch 11 (legislative day, March 10), 2025 Mr. Rounds (for himself, Mr. Marshall , Mr. Risch , Mr. Lankford , Mr. Cramer , Mr. Boozman , Mr. Hoeven , Mr. Budd , Mrs. Hyde-Smith , and Mr. Cruz ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo amend chapter 44 of title 18, United States Code, to define State of residence and resident , and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Traveler's Gun Rights Act .\n#### 2. State of residence\n##### (a) Definitions\nSection 921 of title 18, United States Code, is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nby striking (a) before As used ; and\n**(B)**\nby adding at the end the following:\n(38) (A) The term State of residence means\u2014 (i) the State in which an individual resides; (ii) in the case of an individual, or spouse of an individual, who is an active duty member of the Armed Forces\u2014 (I) the State in which the permanent duty station of the member is located; and (II) the State in which the member maintains a place of abode from which the member commutes each day to the permanent duty station of the member; or (iii) in the case of an individual who does not have a physical residence in any State, the State in which an individual maintains a private mailbox or post office box. (B) For purposes of subparagraph (A)(i)\u2014 (i) an individual resides in a State if the individual is present in the State with the intention of making a home in that State; and (ii) an individual who maintains a home in more than 1 State is a resident of each such State during the time when the individual is present in that State. (39) The term resident , with respect to a State, means an individual who satisfies clause (i), (ii), or (iii) of paragraph (38)(A) with respect to that State. ; and\n**(2)**\nby striking subsection (b).\n##### (b) National instant criminal background check system\nSection 922(t)(1)(D) of title 18, United States Code, is amended by striking transferee containing a photograph of the transferee. and inserting the following: \u201ctransferee\u2014\n(i) containing a photograph of the transferee; and (ii) containing\u2014 (I) the address of the residence of the transferee; or (II) the address for a private mailbox or post office box maintained by the transferee, if the transferee does not have a physical residence in any State. .",
      "versionDate": "2025-03-11",
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
        "actionDate": "2025-03-11",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "2060",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Traveler\u2019s Gun Rights Act",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-03-31T14:39:50Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-11",
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
          "measure-id": "id119s966",
          "measure-number": "966",
          "measure-type": "s",
          "orig-publish-date": "2025-03-11",
          "originChamber": "SENATE",
          "update-date": "2026-03-23"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s966v00",
            "update-date": "2026-03-23"
          },
          "action-date": "2025-03-11",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Traveler's Gun Rights Act</strong></p><p>This bill broadens the scope of allowable firearms transactions involving active duty servicemembers\u00a0and their spouses and individuals who do not have a residence in any state.</p><p>Currently, federal firearms laws generally prohibit a federal firearms licensee (e.g., a gun dealer) from selling or delivering a firearm to an individual whose state of residence is different than the state where the licensee's place of business is located.</p><p>This bill defines the term <em>state of residence</em> as the state in which an individual is present with an intention of making a home.</p><p>In the case of an individual who does not have a physical residence in any state, the term <em>state of residence</em> means the address of the individual's private mailbox or post office box.</p><p>In the case of a member of the Armed Forces on active duty, or his or her spouse, the term <em>state of residence</em> means (1) the state in which the member's permanent duty station is located, and (2) the state where the member maintains a place of abode from which he or she commutes to the permanent duty station.</p>"
        },
        "title": "Traveler's Gun Rights Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s966.xml",
    "summary": {
      "actionDate": "2025-03-11",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Traveler's Gun Rights Act</strong></p><p>This bill broadens the scope of allowable firearms transactions involving active duty servicemembers\u00a0and their spouses and individuals who do not have a residence in any state.</p><p>Currently, federal firearms laws generally prohibit a federal firearms licensee (e.g., a gun dealer) from selling or delivering a firearm to an individual whose state of residence is different than the state where the licensee's place of business is located.</p><p>This bill defines the term <em>state of residence</em> as the state in which an individual is present with an intention of making a home.</p><p>In the case of an individual who does not have a physical residence in any state, the term <em>state of residence</em> means the address of the individual's private mailbox or post office box.</p><p>In the case of a member of the Armed Forces on active duty, or his or her spouse, the term <em>state of residence</em> means (1) the state in which the member's permanent duty station is located, and (2) the state where the member maintains a place of abode from which he or she commutes to the permanent duty station.</p>",
      "updateDate": "2026-03-23",
      "versionCode": "id119s966"
    },
    "title": "Traveler's Gun Rights Act"
  },
  "summaries": [
    {
      "actionDate": "2025-03-11",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Traveler's Gun Rights Act</strong></p><p>This bill broadens the scope of allowable firearms transactions involving active duty servicemembers\u00a0and their spouses and individuals who do not have a residence in any state.</p><p>Currently, federal firearms laws generally prohibit a federal firearms licensee (e.g., a gun dealer) from selling or delivering a firearm to an individual whose state of residence is different than the state where the licensee's place of business is located.</p><p>This bill defines the term <em>state of residence</em> as the state in which an individual is present with an intention of making a home.</p><p>In the case of an individual who does not have a physical residence in any state, the term <em>state of residence</em> means the address of the individual's private mailbox or post office box.</p><p>In the case of a member of the Armed Forces on active duty, or his or her spouse, the term <em>state of residence</em> means (1) the state in which the member's permanent duty station is located, and (2) the state where the member maintains a place of abode from which he or she commutes to the permanent duty station.</p>",
      "updateDate": "2026-03-23",
      "versionCode": "id119s966"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s966is.xml"
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
      "title": "Traveler's Gun Rights Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-11T12:03:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Traveler's Gun Rights Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-29T02:08:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend chapter 44 of title 18, United States Code, to define \"State of residence\" and \"resident\", and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-29T02:03:18Z"
    }
  ]
}
```
