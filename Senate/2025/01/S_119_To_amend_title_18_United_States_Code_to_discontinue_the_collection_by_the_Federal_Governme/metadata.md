# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/119?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/119
- Title: No Retaining Every Gun In a System That Restricts Your Rights Act
- Congress: 119
- Bill type: S
- Bill number: 119
- Origin chamber: Senate
- Introduced date: 2025-01-16
- Update date: 2026-04-16T11:03:24Z
- Update date including text: 2026-04-16T11:03:24Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-16: Introduced in Senate
- 2025-01-16 - IntroReferral: Introduced in Senate
- 2025-01-16 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-01-16: Introduced in Senate

## Actions

- 2025-01-16 - IntroReferral: Introduced in Senate
- 2025-01-16 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-16",
    "latestAction": {
      "actionDate": "2025-01-16",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/119",
    "number": "119",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "R000584",
        "district": "",
        "firstName": "James",
        "fullName": "Sen. Risch, James E. [R-ID]",
        "lastName": "Risch",
        "party": "R",
        "state": "ID"
      }
    ],
    "title": "No Retaining Every Gun In a System That Restricts Your Rights Act",
    "type": "S",
    "updateDate": "2026-04-16T11:03:24Z",
    "updateDateIncludingText": "2026-04-16T11:03:24Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-16",
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
      "actionDate": "2025-01-16",
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
            "date": "2025-01-16T18:22:01Z",
            "name": "Referred To"
          },
          {
            "date": "2025-01-16T18:22:01Z",
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
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "WY"
    },
    {
      "bioguideId": "D000618",
      "firstName": "Steve",
      "fullName": "Sen. Daines, Steve [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Daines",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "MT"
    },
    {
      "bioguideId": "M001198",
      "firstName": "Roger",
      "fullName": "Sen. Marshall, Roger [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Marshall",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "KS"
    },
    {
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "MT"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "NE"
    },
    {
      "bioguideId": "M001190",
      "firstName": "Markwayne",
      "fullName": "Sen. Mullin, Markwayne [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Mullin",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "OK"
    },
    {
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "MS"
    },
    {
      "bioguideId": "C000880",
      "firstName": "Mike",
      "fullName": "Sen. Crapo, Mike [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Crapo",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "ID"
    },
    {
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "False",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2026-02-11",
      "state": "LA"
    },
    {
      "bioguideId": "G000359",
      "firstName": "Lindsey",
      "fullName": "Sen. Graham, Lindsey [R-SC]",
      "isOriginalCosponsor": "False",
      "lastName": "Graham",
      "party": "R",
      "sponsorshipDate": "2026-02-11",
      "state": "SC"
    },
    {
      "bioguideId": "P000603",
      "firstName": "Rand",
      "fullName": "Sen. Paul, Rand [R-KY]",
      "isOriginalCosponsor": "False",
      "lastName": "Paul",
      "party": "R",
      "sponsorshipDate": "2026-04-15",
      "state": "KY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s119is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 119\nIN THE SENATE OF THE UNITED STATES\nJanuary 16, 2025 Mr. Risch (for himself, Ms. Lummis , Mr. Daines , Mr. Marshall , Mr. Sheehy , Mr. Ricketts , Mr. Mullin , Mrs. Hyde-Smith , and Mr. Crapo ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo amend title 18, United States Code, to discontinue the collection by the Federal Government of firearm transaction records of discontinued firearms businesses, to require the destruction of such already collected records, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the No Retaining Every Gun In a System That Restricts Your Rights Act .\n#### 2. Destruction of Bureau of Alcohol, Tobacco, Firearms, and Explosives firearm transaction records of discontinued firearms businesses\n##### (a) In general\nNot later than 90 days after the date of enactment of this Act, the Director of the Bureau of Alcohol, Tobacco, Firearms, and Explosives shall destroy each firearm transaction record delivered to the Attorney General under section 923(g)(4) of title 18, United States Code.\n##### (b) Preventing future firearm registration\nSection 923(g)(4) of title 18, United States Code, is amended by striking the second and third sentences.\n#### 3. Report to Congress\nThe Director of the Bureau of Alcohol, Tobacco, Firearms, and Explosives shall submit to Congress a written report that specifies the number of firearm transaction records destroyed under section 2(a).",
      "versionDate": "2025-01-16",
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
        "actionDate": "2025-01-20",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "563",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "No Retaining Every Gun In a System That Restricts Your Rights Act",
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
            "name": "Congressional oversight",
            "updateDate": "2025-02-19T21:25:25Z"
          },
          {
            "name": "Firearms and explosives",
            "updateDate": "2025-02-19T21:25:13Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-02-19T21:25:21Z"
          }
        ]
      },
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-02-19T13:00:44Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-16",
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
          "measure-id": "id119s119",
          "measure-number": "119",
          "measure-type": "s",
          "orig-publish-date": "2025-01-16",
          "originChamber": "SENATE",
          "update-date": "2025-04-01"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s119v00",
            "update-date": "2025-04-01"
          },
          "action-date": "2025-01-16",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>No Retaining Every Gun In a System That Restricts Your Rights Act</strong></p><p>This bill modifies the retention requirements for firearm transaction records of federal firearms licensees (FFLs) that go out of business.</p><p>Current law generally requires FFLs that go out of business to deliver their firearm transaction records to the Bureau of Alcohol, Tobacco, Firearms and Explosives (ATF).</p><p>This bill removes the requirement for FFLs that go out of business to deliver their firearm transaction records to the ATF. Further, the bill requires the ATF to destroy all out-of-business records it has collected from FFLs.</p>"
        },
        "title": "No Retaining Every Gun In a System That Restricts Your Rights Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s119.xml",
    "summary": {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>No Retaining Every Gun In a System That Restricts Your Rights Act</strong></p><p>This bill modifies the retention requirements for firearm transaction records of federal firearms licensees (FFLs) that go out of business.</p><p>Current law generally requires FFLs that go out of business to deliver their firearm transaction records to the Bureau of Alcohol, Tobacco, Firearms and Explosives (ATF).</p><p>This bill removes the requirement for FFLs that go out of business to deliver their firearm transaction records to the ATF. Further, the bill requires the ATF to destroy all out-of-business records it has collected from FFLs.</p>",
      "updateDate": "2025-04-01",
      "versionCode": "id119s119"
    },
    "title": "No Retaining Every Gun In a System That Restricts Your Rights Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>No Retaining Every Gun In a System That Restricts Your Rights Act</strong></p><p>This bill modifies the retention requirements for firearm transaction records of federal firearms licensees (FFLs) that go out of business.</p><p>Current law generally requires FFLs that go out of business to deliver their firearm transaction records to the Bureau of Alcohol, Tobacco, Firearms and Explosives (ATF).</p><p>This bill removes the requirement for FFLs that go out of business to deliver their firearm transaction records to the ATF. Further, the bill requires the ATF to destroy all out-of-business records it has collected from FFLs.</p>",
      "updateDate": "2025-04-01",
      "versionCode": "id119s119"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s119is.xml"
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
      "title": "No Retaining Every Gun In a System That Restricts Your Rights Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-16T11:03:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "No Retaining Every Gun In a System That Restricts Your Rights Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-19T03:23:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 18, United States Code, to discontinue the collection by the Federal Government of firearm transaction records of discontinued firearms businesses, to require the destruction of such already collected records, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-19T03:18:21Z"
    }
  ]
}
```
