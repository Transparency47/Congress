# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5734?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5734
- Title: Hiring Preference for Veterans and Americans With Disabilities Act
- Congress: 119
- Bill type: HR
- Bill number: 5734
- Origin chamber: House
- Introduced date: 2025-10-10
- Update date: 2026-04-09T19:46:42Z
- Update date including text: 2026-04-09T19:46:42Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-10-10: Introduced in House
- 2025-10-10 - IntroReferral: Introduced in House
- 2025-10-10 - IntroReferral: Introduced in House
- 2025-10-10 - IntroReferral: Referred to the House Committee on House Administration.
- Latest action: 2025-10-10: Introduced in House

## Actions

- 2025-10-10 - IntroReferral: Introduced in House
- 2025-10-10 - IntroReferral: Introduced in House
- 2025-10-10 - IntroReferral: Referred to the House Committee on House Administration.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-10",
    "latestAction": {
      "actionDate": "2025-10-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5734",
    "number": "5734",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "E000300",
        "district": "8",
        "firstName": "Gabe",
        "fullName": "Rep. Evans, Gabe [R-CO-8]",
        "lastName": "Evans",
        "party": "R",
        "state": "CO"
      }
    ],
    "title": "Hiring Preference for Veterans and Americans With Disabilities Act",
    "type": "HR",
    "updateDate": "2026-04-09T19:46:42Z",
    "updateDateIncludingText": "2026-04-09T19:46:42Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-10",
      "committees": {
        "item": {
          "name": "Committee on House Administration",
          "systemCode": "hsha00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on House Administration.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-10-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-10-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
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
          "date": "2025-10-10T16:31:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Committee on House Administration",
      "systemCode": "hsha00",
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
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-10-10",
      "state": "NC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5734ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5734\nIN THE HOUSE OF REPRESENTATIVES\nOctober 10, 2025 Mr. Evans of Colorado (for himself and Mr. Davis of North Carolina ) introduced the following bill; which was referred to the Committee on House Administration\nA BILL\nTo clarify that a State or local jurisdiction may give preference to individuals who are veterans or individuals with a disability with respect to hiring election workers to administer an election in the State or local jurisdiction, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Hiring Preference for Veterans and Americans With Disabilities Act .\n#### 2. Clarification of rules with respect to hiring of election workers\n##### (a) Preferences for veterans and individuals with disabilities\n**(1) Preferences**\nIn hiring election workers to administer an election in a State or local jurisdiction, the State or local jurisdiction may give preference to individuals who are veterans or individuals with a disability.\n**(2) Individual with a disability defined**\nIn this subsection, an individual with a disability means an individual with an impairment that substantially limits any major life activities.\n##### (b) Preference and waiver of residency requirement for spouses and dependents of absent military voters\n**(1) Preference and waivers**\nIn hiring election workers to administer an election in a State or local jurisdiction, the State or local jurisdiction\u2014\n**(A)**\nmay give preference to an individual who is a nonresident military spouse or dependent; and\n**(B)**\nmay not refuse to hire such an individual as an election worker solely on the grounds that the individual does not maintain a place of residence in the State or local jurisdiction.\n**(2) Nonresident military spouse or dependent defined**\nIn this subsection, a nonresident military spouse or dependent means an individual who is an absent uniformed services voter under section 107(1)(C) of the Uniformed and Overseas Citizen Absentee Voting Act ( 52 U.S.C. 20310(1)(C) ).",
      "versionDate": "2025-10-10",
      "versionType": "Introduced in House"
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
        "actionDate": "2025-10-09",
        "text": "Read twice and referred to the Committee on Rules and Administration."
      },
      "number": "2996",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Hiring Preference for Veterans and Americans With Disabilities Act",
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
        "name": "Government Operations and Politics",
        "updateDate": "2025-12-08T22:01:22Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-10-10",
    "originChamber": "House",
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
          "measure-id": "id119hr5734",
          "measure-number": "5734",
          "measure-type": "hr",
          "orig-publish-date": "2025-10-10",
          "originChamber": "HOUSE",
          "update-date": "2026-04-09"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr5734v00",
            "update-date": "2026-04-09"
          },
          "action-date": "2025-10-10",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Hiring Preference for Veterans and Americans With Disabilities Act</strong></p><p>This bill allows states and local jurisdictions to give a hiring preference (when hiring election workers to administer an election in the state or local jurisdiction) to veterans, individuals with a disability, and nonresident military spouses or dependents.</p><p>Further, the bill prohibits states and local jurisdictions from refusing to hire a nonresident military spouse or dependent as an election worker solely on the grounds that the individual does not maintain a place of residence in the state or local jurisdiction.</p>"
        },
        "title": "Hiring Preference for Veterans and Americans With Disabilities Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr5734.xml",
    "summary": {
      "actionDate": "2025-10-10",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Hiring Preference for Veterans and Americans With Disabilities Act</strong></p><p>This bill allows states and local jurisdictions to give a hiring preference (when hiring election workers to administer an election in the state or local jurisdiction) to veterans, individuals with a disability, and nonresident military spouses or dependents.</p><p>Further, the bill prohibits states and local jurisdictions from refusing to hire a nonresident military spouse or dependent as an election worker solely on the grounds that the individual does not maintain a place of residence in the state or local jurisdiction.</p>",
      "updateDate": "2026-04-09",
      "versionCode": "id119hr5734"
    },
    "title": "Hiring Preference for Veterans and Americans With Disabilities Act"
  },
  "summaries": [
    {
      "actionDate": "2025-10-10",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Hiring Preference for Veterans and Americans With Disabilities Act</strong></p><p>This bill allows states and local jurisdictions to give a hiring preference (when hiring election workers to administer an election in the state or local jurisdiction) to veterans, individuals with a disability, and nonresident military spouses or dependents.</p><p>Further, the bill prohibits states and local jurisdictions from refusing to hire a nonresident military spouse or dependent as an election worker solely on the grounds that the individual does not maintain a place of residence in the state or local jurisdiction.</p>",
      "updateDate": "2026-04-09",
      "versionCode": "id119hr5734"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-10-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5734ih.xml"
        }
      ],
      "type": "Introduced in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Hiring Preference for Veterans and Americans With Disabilities Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-17T11:23:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Hiring Preference for Veterans and Americans With Disabilities Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-17T11:23:13Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To clarify that a State or local jurisdiction may give preference to individuals who are veterans or individuals with a disability with respect to hiring election workers to administer an election in the State or local jurisdiction, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-17T11:18:13Z"
    }
  ]
}
```
