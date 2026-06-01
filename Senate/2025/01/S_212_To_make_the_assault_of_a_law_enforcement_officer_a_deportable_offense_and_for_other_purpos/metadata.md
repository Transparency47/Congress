# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/212?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/212
- Title: POLICE Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 212
- Origin chamber: Senate
- Introduced date: 2025-01-23
- Update date: 2025-12-06T06:48:10Z
- Update date including text: 2025-12-06T06:48:10Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-23: Introduced in Senate
- 2025-01-23 - IntroReferral: Introduced in Senate
- 2025-01-23 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-01-23: Introduced in Senate

## Actions

- 2025-01-23 - IntroReferral: Introduced in Senate
- 2025-01-23 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-23",
    "latestAction": {
      "actionDate": "2025-01-23",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/212",
    "number": "212",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "B001305",
        "district": "",
        "firstName": "Ted",
        "fullName": "Sen. Budd, Ted [R-NC]",
        "lastName": "Budd",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "POLICE Act of 2025",
    "type": "S",
    "updateDate": "2025-12-06T06:48:10Z",
    "updateDateIncludingText": "2025-12-06T06:48:10Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-23",
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
      "actionDate": "2025-01-23",
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
          "date": "2025-01-23T18:19:26Z",
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
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "NC"
    },
    {
      "bioguideId": "D000618",
      "firstName": "Steve",
      "fullName": "Sen. Daines, Steve [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Daines",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "MT"
    },
    {
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "AL"
    },
    {
      "bioguideId": "C001098",
      "firstName": "Ted",
      "fullName": "Sen. Cruz, Ted [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cruz",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "TX"
    },
    {
      "bioguideId": "S001227",
      "firstName": "Eric",
      "fullName": "Sen. Schmitt, Eric [R-MO]",
      "isOriginalCosponsor": "True",
      "lastName": "Schmitt",
      "middleName": "S.",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "MO"
    },
    {
      "bioguideId": "H000601",
      "firstName": "Bill",
      "fullName": "Sen. Hagerty, Bill [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Hagerty",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "TN"
    },
    {
      "bioguideId": "L000575",
      "firstName": "James",
      "fullName": "Sen. Lankford, James [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Lankford",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "OK"
    },
    {
      "bioguideId": "M001198",
      "firstName": "Roger",
      "fullName": "Sen. Marshall, Roger [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Marshall",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "KS"
    },
    {
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "MS"
    },
    {
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "ND"
    },
    {
      "bioguideId": "J000312",
      "firstName": "James",
      "fullName": "Sen. Justice, James C. [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Justice",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "WV"
    },
    {
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "MT"
    },
    {
      "bioguideId": "R000605",
      "firstName": "Mike",
      "fullName": "Sen. Rounds, Mike [R-SD]",
      "isOriginalCosponsor": "False",
      "lastName": "Rounds",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "SD"
    },
    {
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "False",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "LA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s212is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 212\nIN THE SENATE OF THE UNITED STATES\nJanuary 23, 2025 Mr. Budd (for himself, Mr. Tillis , Mr. Daines , Mrs. Britt , Mr. Cruz , Mr. Schmitt , Mr. Hagerty , Mr. Lankford , Mr. Marshall , Mrs. Hyde-Smith , Mr. Cramer , Mr. Justice , and Mr. Sheehy ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo make the assault of a law enforcement officer a deportable offense, and for other purposes.\n#### 1. Short titles\nThis Act may be cited as the Protect Our Law enforcement with Immigration Control and Enforcement Act of 2025 or the POLICE Act of 2025 .\n#### 2. Assault of law enforcement officer\nSection 237(a)(2) of the Immigration and Nationality Act ( 8 U.S.C. 1227(a)(2) ) is amended by adding at the end the following:\n(G) Assault of law enforcement officer (i) In general Any alien who has been convicted of, who admits having committed, or who admits committing acts which constitute the essential elements of, any offense involving assault of a law enforcement officer is deportable. (ii) Circumstances The circumstances referred to in clause (i) are that the law enforcement officer was assaulted\u2014 (I) while he or she was engaged in the performance of his or her official duties; (II) because of the performance of his or her official duties; or (III) because of his or her status as a law enforcement officer. (iii) Definitions In this subparagraph\u2014 (I) the term assault has the meaning given that term in the jurisdiction where the act occurred; and (II) the term law enforcement officer is a person authorized by law\u2014 (aa) to engage in or supervise the prevention, detection, investigation, or prosecution, or the incarceration of any person for any criminal violation of law; (bb) to apprehend, arrest, or prosecute an individual for any criminal violation of law; or (cc) to be a firefighter or other first responder. .\n#### 3. Report on aliens deported for assaulting a law enforcement officer\nThe Secretary of Homeland Security shall submit to Congress and make publicly available on the website of the Department of Homeland Security an annual report identifying the number of aliens who were deported during the previous fiscal year pursuant to section 237(a)(2)(G) of the Immigration and Nationality Act ( 8 U.S.C. 1227(a)(2)(G) ).",
      "versionDate": "2025-01-23",
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
        "actionDate": "2025-01-03",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "31",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "POLICE Act of 2025",
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
            "name": "Border security and unlawful immigration",
            "updateDate": "2025-06-04T14:17:18Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-06-04T14:17:18Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-06-04T14:17:18Z"
          },
          {
            "name": "Immigration status and procedures",
            "updateDate": "2025-06-04T14:17:18Z"
          },
          {
            "name": "Internet, web applications, social media",
            "updateDate": "2025-06-04T14:17:18Z"
          },
          {
            "name": "Law enforcement officers",
            "updateDate": "2025-06-04T14:17:18Z"
          },
          {
            "name": "Violent crime",
            "updateDate": "2025-06-04T14:17:18Z"
          }
        ]
      },
      "policyArea": {
        "name": "Immigration",
        "updateDate": "2025-03-01T13:27:22Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-23",
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
          "measure-id": "id119s212",
          "measure-number": "212",
          "measure-type": "s",
          "orig-publish-date": "2025-01-23",
          "originChamber": "SENATE",
          "update-date": "2025-04-29"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s212v00",
            "update-date": "2025-04-29"
          },
          "action-date": "2025-01-23",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Protect Our Law enforcement with Immigration Control and Enforcement Act of 2025 or the POLICE Act of 2025</strong></p><p>This bill makes assaulting a law enforcement officer, firefighter, or other first responder a deportable offense.</p><p>Specifically, the bill makes deportable any non-U.S. national (<em>alien</em> under federal law) who has been convicted of (or admits to have committed) any act that constitutes the essential elements of any offense involving assault of a law enforcement officer, firefighter, or other first responder.</p><p>The Department of Homeland Security must publish annually on its website a report on the number of individuals deported in the previous fiscal year pursuant to this bill.</p>"
        },
        "title": "POLICE Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s212.xml",
    "summary": {
      "actionDate": "2025-01-23",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Protect Our Law enforcement with Immigration Control and Enforcement Act of 2025 or the POLICE Act of 2025</strong></p><p>This bill makes assaulting a law enforcement officer, firefighter, or other first responder a deportable offense.</p><p>Specifically, the bill makes deportable any non-U.S. national (<em>alien</em> under federal law) who has been convicted of (or admits to have committed) any act that constitutes the essential elements of any offense involving assault of a law enforcement officer, firefighter, or other first responder.</p><p>The Department of Homeland Security must publish annually on its website a report on the number of individuals deported in the previous fiscal year pursuant to this bill.</p>",
      "updateDate": "2025-04-29",
      "versionCode": "id119s212"
    },
    "title": "POLICE Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-23",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Protect Our Law enforcement with Immigration Control and Enforcement Act of 2025 or the POLICE Act of 2025</strong></p><p>This bill makes assaulting a law enforcement officer, firefighter, or other first responder a deportable offense.</p><p>Specifically, the bill makes deportable any non-U.S. national (<em>alien</em> under federal law) who has been convicted of (or admits to have committed) any act that constitutes the essential elements of any offense involving assault of a law enforcement officer, firefighter, or other first responder.</p><p>The Department of Homeland Security must publish annually on its website a report on the number of individuals deported in the previous fiscal year pursuant to this bill.</p>",
      "updateDate": "2025-04-29",
      "versionCode": "id119s212"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s212is.xml"
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
      "title": "POLICE Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-25T05:08:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "POLICE Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-25T05:08:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Protect Our Law enforcement with Immigration Control and Enforcement Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-25T05:08:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to make the assault of a law enforcement officer a deportable offense, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-25T05:03:23Z"
    }
  ]
}
```
