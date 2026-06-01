# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1107?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1107
- Title: MATCH Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1107
- Origin chamber: Senate
- Introduced date: 2025-03-25
- Update date: 2026-03-24T17:19:38Z
- Update date including text: 2026-03-24T17:19:38Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-03-25: Introduced in Senate
- 2025-03-25 - IntroReferral: Introduced in Senate
- 2025-03-25 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.
- Latest action: 2025-03-25: Introduced in Senate

## Actions

- 2025-03-25 - IntroReferral: Introduced in Senate
- 2025-03-25 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-25",
    "latestAction": {
      "actionDate": "2025-03-25",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1107",
    "number": "1107",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "C001114",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Curtis, John R. [R-UT]",
        "lastName": "Curtis",
        "party": "R",
        "state": "UT"
      }
    ],
    "title": "MATCH Act of 2025",
    "type": "S",
    "updateDate": "2026-03-24T17:19:38Z",
    "updateDateIncludingText": "2026-03-24T17:19:38Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-25",
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
      "actionDate": "2025-03-25",
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
          "date": "2025-03-25T15:38:04Z",
          "name": "Referred To"
        }
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
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1107is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1107\nIN THE SENATE OF THE UNITED STATES\nMarch 25, 2025 Mr. Curtis (for himself and Mr. Bennet ) introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo amend the Agricultural Credit Act of 1978 with respect to preagreement costs of emergency watershed protection measures, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Making Access To Cleanup Happen Act of 2025 or the MATCH Act of 2025 .\n#### 2. Emergency watershed program\nSection 403 of the Agricultural Credit Act of 1978 ( 16 U.S.C. 2203 ) is amended by adding at the end the following:\n(c) Preagreement costs (1) Definition of sponsor In this subsection, the term sponsor means\u2014 (A) a State or local government; and (B) an Indian Tribe (as defined in section 4 of the Indian Self-Determination and Education Assistance Act ( 25 U.S.C. 5304 )). (2) Preagreement project costs Not later than 180 days after the date of enactment of this subsection, the Secretary shall\u2014 (A) identify a list of emergency watershed protection measures the cost of which may be incurred by a sponsor prior to entering into an agreement with the Secretary under this section; and (B) develop a procedure, including appropriate deadlines, to be implemented at the State level, through which a sponsor may request, for a specified natural disaster, additional emergency watershed protection measures the cost of which may be incurred by a sponsor prior to entering into an agreement with the Secretary under this section. (3) Agreement contribution If the Secretary and a sponsor enter into an agreement under this section, the Secretary shall consider any applicable preagreement costs incurred by the sponsor for undertaking emergency watershed protection measures identified under paragraph (2) as meeting part of the contribution of the sponsor toward the cost of the project. (4) Assumption of risk A sponsor that undertakes emergency watershed protection measures prior to entering into an agreement with the Secretary under this section shall assume the risk of incurring any cost of undertaking those measures. (5) Effect Nothing in this subsection requires the Secretary to enter into an agreement with a sponsor. .",
      "versionDate": "2025-03-25",
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
        "actionDate": "2025-10-17",
        "text": "Referred to the House Committee on Agriculture."
      },
      "number": "5781",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "MATCH Act of 2025",
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
        "name": "Agriculture and Food",
        "updateDate": "2025-05-12T19:01:50Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-25",
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
          "measure-id": "id119s1107",
          "measure-number": "1107",
          "measure-type": "s",
          "orig-publish-date": "2025-03-25",
          "originChamber": "SENATE",
          "update-date": "2026-03-24"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1107v00",
            "update-date": "2026-03-24"
          },
          "action-date": "2025-03-25",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Making Access To Cleanup Happen Act of 2025 or the MATCH Act of 2025</strong></p><p>This bill modifies the Department of Agriculture's (USDA's) Emergency Watershed Protection (EWP) program to allow sponsors (i.e., states, local governments, and Indian tribes) to undertake certain emergency watershed protection measures prior to entering into a project agreement with\u00a0USDA and count the costs as part of the sponsor's share of the project cost once\u00a0an agreement with USDA is in place.</p><p>As background, USDA's\u00a0EWP Program offers assistance to sponsors to carry out projects that help safeguard people and property from floods, drought, fires, windstorms, and other natural disasters that impair a watershed.</p><p>This bill requires USDA to identify a list of emergency watershed protection measures that a sponsor may incur costs for prior to entering into a\u00a0project agreement with USDA under the EWP Program.\u00a0USDA must develop a procedure, to be implemented at the state level, through which these entities may request additional emergency watershed protection measures. The cost of undertaking these additional measures may be incurred by a sponsor prior to entering into an agreement with USDA.</p><p>Further, USDA must consider pre-agreement costs incurred by a sponsor for undertaking the emergency watershed protection measures as meeting part of a sponsor's contribution towards the project costs.</p>"
        },
        "title": "MATCH Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1107.xml",
    "summary": {
      "actionDate": "2025-03-25",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Making Access To Cleanup Happen Act of 2025 or the MATCH Act of 2025</strong></p><p>This bill modifies the Department of Agriculture's (USDA's) Emergency Watershed Protection (EWP) program to allow sponsors (i.e., states, local governments, and Indian tribes) to undertake certain emergency watershed protection measures prior to entering into a project agreement with\u00a0USDA and count the costs as part of the sponsor's share of the project cost once\u00a0an agreement with USDA is in place.</p><p>As background, USDA's\u00a0EWP Program offers assistance to sponsors to carry out projects that help safeguard people and property from floods, drought, fires, windstorms, and other natural disasters that impair a watershed.</p><p>This bill requires USDA to identify a list of emergency watershed protection measures that a sponsor may incur costs for prior to entering into a\u00a0project agreement with USDA under the EWP Program.\u00a0USDA must develop a procedure, to be implemented at the state level, through which these entities may request additional emergency watershed protection measures. The cost of undertaking these additional measures may be incurred by a sponsor prior to entering into an agreement with USDA.</p><p>Further, USDA must consider pre-agreement costs incurred by a sponsor for undertaking the emergency watershed protection measures as meeting part of a sponsor's contribution towards the project costs.</p>",
      "updateDate": "2026-03-24",
      "versionCode": "id119s1107"
    },
    "title": "MATCH Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-03-25",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Making Access To Cleanup Happen Act of 2025 or the MATCH Act of 2025</strong></p><p>This bill modifies the Department of Agriculture's (USDA's) Emergency Watershed Protection (EWP) program to allow sponsors (i.e., states, local governments, and Indian tribes) to undertake certain emergency watershed protection measures prior to entering into a project agreement with\u00a0USDA and count the costs as part of the sponsor's share of the project cost once\u00a0an agreement with USDA is in place.</p><p>As background, USDA's\u00a0EWP Program offers assistance to sponsors to carry out projects that help safeguard people and property from floods, drought, fires, windstorms, and other natural disasters that impair a watershed.</p><p>This bill requires USDA to identify a list of emergency watershed protection measures that a sponsor may incur costs for prior to entering into a\u00a0project agreement with USDA under the EWP Program.\u00a0USDA must develop a procedure, to be implemented at the state level, through which these entities may request additional emergency watershed protection measures. The cost of undertaking these additional measures may be incurred by a sponsor prior to entering into an agreement with USDA.</p><p>Further, USDA must consider pre-agreement costs incurred by a sponsor for undertaking the emergency watershed protection measures as meeting part of a sponsor's contribution towards the project costs.</p>",
      "updateDate": "2026-03-24",
      "versionCode": "id119s1107"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1107is.xml"
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
      "title": "MATCH Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-08T02:53:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "MATCH Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-08T02:53:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Making Access To Cleanup Happen Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-08T02:53:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Agricultural Credit Act of 1978 with respect to preagreement costs of emergency watershed protection measures, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-08T02:48:22Z"
    }
  ]
}
```
