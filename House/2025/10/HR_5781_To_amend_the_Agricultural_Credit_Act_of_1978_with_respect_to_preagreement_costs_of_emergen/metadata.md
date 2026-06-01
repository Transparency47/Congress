# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5781?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5781
- Title: MATCH Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 5781
- Origin chamber: House
- Introduced date: 2025-10-17
- Update date: 2026-05-01T21:41:23Z
- Update date including text: 2026-05-01T21:41:23Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-10-17: Introduced in House
- 2025-10-17 - IntroReferral: Introduced in House
- 2025-10-17 - IntroReferral: Introduced in House
- 2025-10-17 - IntroReferral: Referred to the House Committee on Agriculture.
- Latest action: 2025-10-17: Introduced in House

## Actions

- 2025-10-17 - IntroReferral: Introduced in House
- 2025-10-17 - IntroReferral: Introduced in House
- 2025-10-17 - IntroReferral: Referred to the House Committee on Agriculture.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-17",
    "latestAction": {
      "actionDate": "2025-10-17",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5781",
    "number": "5781",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "N000191",
        "district": "2",
        "firstName": "Joe",
        "fullName": "Rep. Neguse, Joe [D-CO-2]",
        "lastName": "Neguse",
        "party": "D",
        "state": "CO"
      }
    ],
    "title": "MATCH Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-01T21:41:23Z",
    "updateDateIncludingText": "2026-05-01T21:41:23Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-17",
      "committees": {
        "item": {
          "name": "Agriculture Committee",
          "systemCode": "hsag00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Agriculture.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-10-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-10-17",
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
          "date": "2025-10-17T18:03:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "systemCode": "hsag00",
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
      "bioguideId": "M001228",
      "district": "2",
      "firstName": "Celeste",
      "fullName": "Rep. Maloy, Celeste [R-UT-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Maloy",
      "party": "R",
      "sponsorshipDate": "2025-10-17",
      "state": "UT"
    },
    {
      "bioguideId": "G000559",
      "district": "8",
      "firstName": "John",
      "fullName": "Rep. Garamendi, John [D-CA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Garamendi",
      "party": "D",
      "sponsorshipDate": "2025-10-17",
      "state": "CA"
    },
    {
      "bioguideId": "S001221",
      "district": "3",
      "firstName": "Hillary",
      "fullName": "Rep. Scholten, Hillary J. [D-MI-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Scholten",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2026-04-30",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5781ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5781\nIN THE HOUSE OF REPRESENTATIVES\nOctober 17, 2025 Mr. Neguse (for himself, Ms. Maloy , and Mr. Garamendi ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo amend the Agricultural Credit Act of 1978 with respect to preagreement costs of emergency watershed protection measures, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Making Access To Cleanup Happen Act of 2025 or the MATCH Act of 2025 .\n#### 2. Emergency watershed program\nSection 403 of the Agricultural Credit Act of 1978 ( 16 U.S.C. 2203 ) is amended by adding at the end the following:\n(c) Preagreement costs (1) Definition of sponsor In this subsection, the term sponsor means\u2014 (A) a State or local government; and (B) an Indian Tribe (as defined in section 4 of the Indian Self-Determination and Education Assistance Act ( 25 U.S.C. 5304 )). (2) Preagreement project costs Not later than 180 days after the date of enactment of this subsection, the Secretary shall\u2014 (A) identify a list of emergency watershed protection measures the cost of which may be incurred by a sponsor prior to entering into an agreement with the Secretary under this section; and (B) develop a procedure, including appropriate deadlines, to be implemented at the State level, through which a sponsor may request, for a specified natural disaster, additional emergency watershed protection measures the cost of which may be incurred by a sponsor prior to entering into an agreement with the Secretary under this section. (3) Agreement contribution If the Secretary and a sponsor enter into an agreement under this section, the Secretary shall consider any applicable preagreement costs incurred by the sponsor for undertaking emergency watershed protection measures identified under paragraph (2) as meeting part of the contribution of the sponsor toward the cost of the project. (4) Assumption of risk A sponsor that undertakes emergency watershed protection measures prior to entering into an agreement with the Secretary under this section shall assume the risk of incurring any cost of undertaking those measures. (5) Effect Nothing in this subsection requires the Secretary to enter into an agreement with a sponsor. .",
      "versionDate": "2025-10-17",
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
        "actionDate": "2025-03-25",
        "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry."
      },
      "number": "1107",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "MATCH Act of 2025",
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
        "name": "Agriculture and Food",
        "updateDate": "2025-12-04T21:38:54Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-10-17",
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
          "measure-id": "id119hr5781",
          "measure-number": "5781",
          "measure-type": "hr",
          "orig-publish-date": "2025-10-17",
          "originChamber": "HOUSE",
          "update-date": "2026-03-24"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr5781v00",
            "update-date": "2026-03-24"
          },
          "action-date": "2025-10-17",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Making Access To Cleanup Happen Act of 2025 or the MATCH Act of 2025</strong></p><p>This bill modifies the Department of Agriculture's (USDA's) Emergency Watershed Protection (EWP) program to allow sponsors (i.e., states, local governments, and Indian tribes) to undertake certain emergency watershed protection measures prior to entering into a project agreement with\u00a0USDA and count the costs as part of the sponsor's share of the project cost once\u00a0an agreement with USDA is in place.</p><p>As background, USDA's\u00a0EWP Program offers assistance to sponsors to carry out projects that help safeguard people and property from floods, drought, fires, windstorms, and other natural disasters that impair a watershed.</p><p>This bill requires USDA to identify a list of emergency watershed protection measures that a sponsor may incur costs for prior to entering into a\u00a0project agreement with USDA under the EWP Program.\u00a0USDA must develop a procedure, to be implemented at the state level, through which these entities may request additional emergency watershed protection measures. The cost of undertaking these additional measures may be incurred by a sponsor prior to entering into an agreement with USDA.</p><p>Further, USDA must consider pre-agreement costs incurred by a sponsor for undertaking the emergency watershed protection measures as meeting part of a sponsor's contribution towards the project costs.</p>"
        },
        "title": "MATCH Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr5781.xml",
    "summary": {
      "actionDate": "2025-10-17",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Making Access To Cleanup Happen Act of 2025 or the MATCH Act of 2025</strong></p><p>This bill modifies the Department of Agriculture's (USDA's) Emergency Watershed Protection (EWP) program to allow sponsors (i.e., states, local governments, and Indian tribes) to undertake certain emergency watershed protection measures prior to entering into a project agreement with\u00a0USDA and count the costs as part of the sponsor's share of the project cost once\u00a0an agreement with USDA is in place.</p><p>As background, USDA's\u00a0EWP Program offers assistance to sponsors to carry out projects that help safeguard people and property from floods, drought, fires, windstorms, and other natural disasters that impair a watershed.</p><p>This bill requires USDA to identify a list of emergency watershed protection measures that a sponsor may incur costs for prior to entering into a\u00a0project agreement with USDA under the EWP Program.\u00a0USDA must develop a procedure, to be implemented at the state level, through which these entities may request additional emergency watershed protection measures. The cost of undertaking these additional measures may be incurred by a sponsor prior to entering into an agreement with USDA.</p><p>Further, USDA must consider pre-agreement costs incurred by a sponsor for undertaking the emergency watershed protection measures as meeting part of a sponsor's contribution towards the project costs.</p>",
      "updateDate": "2026-03-24",
      "versionCode": "id119hr5781"
    },
    "title": "MATCH Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-10-17",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Making Access To Cleanup Happen Act of 2025 or the MATCH Act of 2025</strong></p><p>This bill modifies the Department of Agriculture's (USDA's) Emergency Watershed Protection (EWP) program to allow sponsors (i.e., states, local governments, and Indian tribes) to undertake certain emergency watershed protection measures prior to entering into a project agreement with\u00a0USDA and count the costs as part of the sponsor's share of the project cost once\u00a0an agreement with USDA is in place.</p><p>As background, USDA's\u00a0EWP Program offers assistance to sponsors to carry out projects that help safeguard people and property from floods, drought, fires, windstorms, and other natural disasters that impair a watershed.</p><p>This bill requires USDA to identify a list of emergency watershed protection measures that a sponsor may incur costs for prior to entering into a\u00a0project agreement with USDA under the EWP Program.\u00a0USDA must develop a procedure, to be implemented at the state level, through which these entities may request additional emergency watershed protection measures. The cost of undertaking these additional measures may be incurred by a sponsor prior to entering into an agreement with USDA.</p><p>Further, USDA must consider pre-agreement costs incurred by a sponsor for undertaking the emergency watershed protection measures as meeting part of a sponsor's contribution towards the project costs.</p>",
      "updateDate": "2026-03-24",
      "versionCode": "id119hr5781"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-10-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5781ih.xml"
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
      "title": "MATCH Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-22T06:23:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "MATCH Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-22T06:23:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Making Access To Cleanup Happen Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-22T06:23:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Agricultural Credit Act of 1978 with respect to preagreement costs of emergency watershed protection measures, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-22T06:18:21Z"
    }
  ]
}
```
