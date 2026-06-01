# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1204?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1204
- Title: Gold Star and Surviving Spouse Career Services Act
- Congress: 119
- Bill type: S
- Bill number: 1204
- Origin chamber: Senate
- Introduced date: 2025-03-31
- Update date: 2026-04-10T12:53:53Z
- Update date including text: 2026-04-10T12:53:53Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-03-31: Introduced in Senate
- 2025-03-31 - IntroReferral: Introduced in Senate
- 2025-03-31 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- 2025-12-18 - Floor: Passed Senate without amendment by Unanimous Consent. (consideration: CR S8895; text: CR S8895)
- 2025-12-18 - Floor: Passed/agreed to in Senate: Passed Senate without amendment by Unanimous Consent.
- 2025-12-18 - Discharge: Senate Committee on Veterans' Affairs discharged by Unanimous Consent.
- 2025-12-18 - Committee: Senate Committee on Veterans' Affairs discharged by Unanimous Consent.
- 2025-12-19 - Floor: Message on Senate action sent to the House.
- 2025-12-19 14:33:20 - Floor: Received in the House.
- 2025-12-19 14:40:31 - Floor: Held at the desk.
- Latest action: 2025-03-31: Introduced in Senate

## Actions

- 2025-03-31 - IntroReferral: Introduced in Senate
- 2025-03-31 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- 2025-12-18 - Floor: Passed Senate without amendment by Unanimous Consent. (consideration: CR S8895; text: CR S8895)
- 2025-12-18 - Floor: Passed/agreed to in Senate: Passed Senate without amendment by Unanimous Consent.
- 2025-12-18 - Discharge: Senate Committee on Veterans' Affairs discharged by Unanimous Consent.
- 2025-12-18 - Committee: Senate Committee on Veterans' Affairs discharged by Unanimous Consent.
- 2025-12-19 - Floor: Message on Senate action sent to the House.
- 2025-12-19 14:33:20 - Floor: Received in the House.
- 2025-12-19 14:40:31 - Floor: Held at the desk.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-31",
    "latestAction": {
      "actionDate": "2025-03-31",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1204",
    "number": "1204",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "H001076",
        "district": "",
        "firstName": "Maggie",
        "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
        "lastName": "Hassan",
        "party": "D",
        "state": "NH"
      }
    ],
    "title": "Gold Star and Surviving Spouse Career Services Act",
    "type": "S",
    "updateDate": "2026-04-10T12:53:53Z",
    "updateDateIncludingText": "2026-04-10T12:53:53Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H15000",
      "actionDate": "2025-12-19",
      "actionTime": "14:40:31",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Held at the desk.",
      "type": "Floor"
    },
    {
      "actionCode": "H14000",
      "actionDate": "2025-12-19",
      "actionTime": "14:33:20",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Received in the House.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-12-19",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Message on Senate action sent to the House.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-12-18",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Passed Senate without amendment by Unanimous Consent. (consideration: CR S8895; text: CR S8895)",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2025-12-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Passed Senate without amendment by Unanimous Consent.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-12-18",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Senate Committee on Veterans' Affairs discharged by Unanimous Consent.",
      "type": "Discharge"
    },
    {
      "actionCode": "14500",
      "actionDate": "2025-12-18",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Senate Committee on Veterans' Affairs discharged by Unanimous Consent.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-03-31",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-31",
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
            "date": "2025-12-19T00:46:06Z",
            "name": "Discharged From"
          },
          {
            "date": "2025-03-31T20:49:48Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Veterans' Affairs Committee",
      "systemCode": "ssva00",
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
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2025-03-31",
      "state": "LA"
    },
    {
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2025-03-31",
      "state": "AZ"
    },
    {
      "bioguideId": "S001227",
      "firstName": "Eric",
      "fullName": "Sen. Schmitt, Eric [R-MO]",
      "isOriginalCosponsor": "True",
      "lastName": "Schmitt",
      "middleName": "S.",
      "party": "R",
      "sponsorshipDate": "2025-03-31",
      "state": "MO"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-03-31",
      "state": "VA"
    },
    {
      "bioguideId": "C001056",
      "firstName": "John",
      "fullName": "Sen. Cornyn, John [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cornyn",
      "party": "R",
      "sponsorshipDate": "2025-03-31",
      "state": "TX"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-03-31",
      "state": "MN"
    },
    {
      "bioguideId": "L000575",
      "firstName": "James",
      "fullName": "Sen. Lankford, James [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Lankford",
      "party": "R",
      "sponsorshipDate": "2025-03-31",
      "state": "OK"
    },
    {
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-03-31",
      "state": "CO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1204is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1204\nIN THE SENATE OF THE UNITED STATES\nMarch 31, 2025 Ms. Hassan (for herself, Mr. Cassidy , Mr. Kelly , Mr. Schmitt , Mr. Kaine , Mr. Cornyn , Ms. Smith , Mr. Lankford , and Mr. Hickenlooper ) introduced the following bill; which was read twice and referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to make certain spouses eligible for services under the disabled veterans\u2019 outreach program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Gold Star and Surviving Spouse Career Services Act .\n#### 2. Eligibility of spouses for services under the disabled veterans\u2019 outreach program\nSection 4103A of title 38, United States Code, is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nin paragraph (1)\u2014\n**(i)**\nin the matter preceding subparagraph (A), by inserting and eligible persons after eligible veterans ; and\n**(ii)**\nin subparagraph (C), by inserting , and eligible persons, after Other eligible veterans ;\n**(B)**\nin paragraph (2), by inserting and eligible persons after veterans each place it appears; and\n**(C)**\nin paragraph (3)\u2014\n**(i)**\nby inserting or eligible person after veteran each place it appears; and\n**(ii)**\nby inserting or eligible person\u2019s after veteran\u2019s ;\n**(2)**\nin subsection (d)(1)\u2014\n**(A)**\nby inserting and eligible persons after eligible veterans each place it appears; and\n**(B)**\nby striking non-veteran-related ; and\n**(3)**\nby adding at the end the following new subsection:\n(e) Eligible person defined In this section, the term eligible person means\u2014 (1) any spouse described in section 4101(5) of this title; or (2) the spouse of any person who died while a member of the Armed Forces. .",
      "versionDate": "2025-03-31",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1204es.xml",
      "text": "119th CONGRESS\n1st Session\nS. 1204\nIN THE SENATE OF THE UNITED STATES\nAN ACT\nTo amend title 38, United States Code, to make certain spouses eligible for services under the disabled veterans\u2019 outreach program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Gold Star and Surviving Spouse Career Services Act .\n#### 2. Eligibility of spouses for services under the disabled veterans\u2019 outreach program\nSection 4103A of title 38, United States Code, is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nin paragraph (1)\u2014\n**(i)**\nin the matter preceding subparagraph (A), by inserting and eligible persons after eligible veterans ; and\n**(ii)**\nin subparagraph (C), by inserting , and eligible persons, after Other eligible veterans ;\n**(B)**\nin paragraph (2), by inserting and eligible persons after veterans each place it appears; and\n**(C)**\nin paragraph (3)\u2014\n**(i)**\nby inserting or eligible person after veteran each place it appears; and\n**(ii)**\nby inserting or eligible person\u2019s after veteran\u2019s ;\n**(2)**\nin subsection (d)(1)\u2014\n**(A)**\nby inserting and eligible persons after eligible veterans each place it appears; and\n**(B)**\nby striking non-veteran-related ; and\n**(3)**\nby adding at the end the following new subsection:\n(e) Eligible person defined In this section, the term eligible person means\u2014 (1) any spouse described in section 4101(5) of this title; or (2) the spouse of any person who died while a member of the Armed Forces. .",
      "versionDate": "",
      "versionType": "Engrossed in Senate"
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
        "actionDate": "2025-11-12",
        "actionTime": "12:10:52",
        "text": "Held at the desk."
      },
      "number": "2296",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "National Defense Authorization Act for Fiscal Year 2026",
      "type": "S"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-06-11",
        "text": "Subcommittee Hearings Held"
      },
      "number": "3031",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Gold Star and Surviving Spouse Career Services Act",
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
            "name": "Military personnel and dependents",
            "updateDate": "2025-06-26T16:45:42Z"
          },
          {
            "name": "Veterans' education, employment, rehabilitation",
            "updateDate": "2025-06-26T16:45:42Z"
          },
          {
            "name": "Veterans' pensions and compensation",
            "updateDate": "2025-06-26T16:45:42Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-05-12T18:06:16Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-12-18",
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
          "measure-id": "id119s1204",
          "measure-number": "1204",
          "measure-type": "s",
          "orig-publish-date": "2025-12-18",
          "originChamber": "SENATE",
          "update-date": "2026-04-10"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1204v55",
            "update-date": "2026-04-10"
          },
          "action-date": "2025-12-18",
          "action-desc": "Passed Senate",
          "summary-text": "<p><strong>Gold Star and Surviving Spouse Career Services Act</strong></p><p>This bill expands eligibility for the Disabled Veterans\u2019 Outreach Program to the spouses of certain veterans and members of the Armed Forces. Such program is administered by the Department of Labor and generally provides career and employment services to disabled veterans.</p><p>The bill expands eligibility for the program to spouses of</p><ul><li>persons who died while members of the Armed Forces;</li><li>persons who died of a service-connected disability;</li><li>members of the Armed Forces serving on active duty who, for more than 90 days, are listed as missing in action, captured by a hostile force, or forcibly detained or interned in the line of duty by a foreign government power;</li><li>persons who have a total permanent disability resulting from a service-connected disability; and</li><li>persons who died while an evaluated total disability was in existence.</li></ul>"
        },
        "title": "Gold Star and Surviving Spouse Career Services Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1204.xml",
    "summary": {
      "actionDate": "2025-12-18",
      "actionDesc": "Passed Senate",
      "text": "<p><strong>Gold Star and Surviving Spouse Career Services Act</strong></p><p>This bill expands eligibility for the Disabled Veterans\u2019 Outreach Program to the spouses of certain veterans and members of the Armed Forces. Such program is administered by the Department of Labor and generally provides career and employment services to disabled veterans.</p><p>The bill expands eligibility for the program to spouses of</p><ul><li>persons who died while members of the Armed Forces;</li><li>persons who died of a service-connected disability;</li><li>members of the Armed Forces serving on active duty who, for more than 90 days, are listed as missing in action, captured by a hostile force, or forcibly detained or interned in the line of duty by a foreign government power;</li><li>persons who have a total permanent disability resulting from a service-connected disability; and</li><li>persons who died while an evaluated total disability was in existence.</li></ul>",
      "updateDate": "2026-04-10",
      "versionCode": "id119s1204"
    },
    "title": "Gold Star and Surviving Spouse Career Services Act"
  },
  "summaries": [
    {
      "actionDate": "2025-12-18",
      "actionDesc": "Passed Senate",
      "text": "<p><strong>Gold Star and Surviving Spouse Career Services Act</strong></p><p>This bill expands eligibility for the Disabled Veterans\u2019 Outreach Program to the spouses of certain veterans and members of the Armed Forces. Such program is administered by the Department of Labor and generally provides career and employment services to disabled veterans.</p><p>The bill expands eligibility for the program to spouses of</p><ul><li>persons who died while members of the Armed Forces;</li><li>persons who died of a service-connected disability;</li><li>members of the Armed Forces serving on active duty who, for more than 90 days, are listed as missing in action, captured by a hostile force, or forcibly detained or interned in the line of duty by a foreign government power;</li><li>persons who have a total permanent disability resulting from a service-connected disability; and</li><li>persons who died while an evaluated total disability was in existence.</li></ul>",
      "updateDate": "2026-04-10",
      "versionCode": "id119s1204"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-31",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1204is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1204es.xml"
        }
      ],
      "type": "Engrossed in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Gold Star and Surviving Spouse Career Services Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-20T12:03:19Z"
    },
    {
      "billTextVersionCode": "ES",
      "billTextVersionName": "Engrossed in Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Gold Star and Surviving Spouse Career Services Act",
      "titleType": "Short Title(s) as Passed Senate",
      "titleTypeCode": "105",
      "updateDate": "2025-12-19T12:23:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Gold Star and Surviving Spouse Career Services Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-12T02:53:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 38, United States Code, to make certain spouses eligible for services under the disabled veterans' outreach program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-12T02:48:18Z"
    }
  ]
}
```
