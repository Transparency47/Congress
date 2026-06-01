# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/676?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/676
- Title: To exempt Federal actions related to energy and mineral activities on certain Federal lands from the requirements of the National Environmental Policy Act of 1969.
- Congress: 119
- Bill type: HR
- Bill number: 676
- Origin chamber: House
- Introduced date: 2025-01-23
- Update date: 2025-12-01T17:45:54Z
- Update date including text: 2025-12-01T17:45:54Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-23: Introduced in House
- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Referred to the House Committee on Natural Resources.
- Latest action: 2025-01-23: Introduced in House

## Actions

- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Referred to the House Committee on Natural Resources.

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
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/676",
    "number": "676",
    "originChamber": "House",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "H001096",
        "district": "",
        "firstName": "Harriet",
        "fullName": "Rep. Hageman, Harriet M. [R-WY-At Large]",
        "lastName": "Hageman",
        "party": "R",
        "state": "WY"
      }
    ],
    "title": "To exempt Federal actions related to energy and mineral activities on certain Federal lands from the requirements of the National Environmental Policy Act of 1969.",
    "type": "HR",
    "updateDate": "2025-12-01T17:45:54Z",
    "updateDateIncludingText": "2025-12-01T17:45:54Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-23",
      "committees": {
        "item": {
          "name": "Natural Resources Committee",
          "systemCode": "hsii00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-23",
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
          "date": "2025-01-23T15:05:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "systemCode": "hsii00",
      "type": "Standing"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr676ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 676\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 23, 2025 Ms. Hageman introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo exempt Federal actions related to energy and mineral activities on certain Federal lands from the requirements of the National Environmental Policy Act of 1969.\n#### 1. NEPA exemption for Federal actions related to energy and mineral activities on certain Federal lands\nNotwithstanding any other provision of law, the following shall not be considered a major Federal action under section 102(2)(C) of the National Environmental Policy Act of 1969 ( 42 U.S.C. 4332(2)(C) ):\n**(1)**\nIssuing, granting, or renewing a lease, easement, or right-of-way under the Mineral Leasing Act ( 30 U.S.C. 181 et seq. ) for the exploration, development, or production of oil, gas, or coal.\n**(2)**\nIssuing, granting, or renewing a permit or other authorization under the Mining Law of 1872 ( 30 U.S.C. 22 et seq. ) for the exploration, location, development, or extraction of a critical mineral on land that is open to mineral entry.",
      "versionDate": "2025-01-23",
      "versionType": "Introduced in House"
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
        "name": "Energy",
        "updateDate": "2025-02-25T14:15:36Z"
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
          "measure-id": "id119hr676",
          "measure-number": "676",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-23",
          "originChamber": "HOUSE",
          "update-date": "2025-12-01"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr676v00",
            "update-date": "2025-12-01"
          },
          "action-date": "2025-01-23",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This bill exempts certain energy and mineral actions on federal lands from the environmental review requirements under the National Environmental Policy Act of 1969 (NEPA). Specifically, the bill states that the following are not to be considered a major federal action under NEPA:</p><ul><li>issuing, granting, or renewing a lease, easement, or right-of-way under the Mineral Leasing Act\u00a0for the exploration, development, or production of oil, gas, or coal; or</li><li>issuing, granting, or renewing a permit or other authorization under the Mining Law of 1872\u00a0for the exploration, location, development, or extraction of a critical mineral on land that is open to mineral entry.</li></ul><p>By way of background,\u00a0NEPA requires agencies to identify and evaluate the impacts of major federal actions significantly affecting the quality of the human environment prior to finalizing certain decisions. Thus, if an action is not considered to be a major federal action, then it is exempt from NEPA.</p>"
        },
        "title": "To exempt Federal actions related to energy and mineral activities on certain Federal lands from the requirements of the National Environmental Policy Act of 1969."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr676.xml",
    "summary": {
      "actionDate": "2025-01-23",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill exempts certain energy and mineral actions on federal lands from the environmental review requirements under the National Environmental Policy Act of 1969 (NEPA). Specifically, the bill states that the following are not to be considered a major federal action under NEPA:</p><ul><li>issuing, granting, or renewing a lease, easement, or right-of-way under the Mineral Leasing Act\u00a0for the exploration, development, or production of oil, gas, or coal; or</li><li>issuing, granting, or renewing a permit or other authorization under the Mining Law of 1872\u00a0for the exploration, location, development, or extraction of a critical mineral on land that is open to mineral entry.</li></ul><p>By way of background,\u00a0NEPA requires agencies to identify and evaluate the impacts of major federal actions significantly affecting the quality of the human environment prior to finalizing certain decisions. Thus, if an action is not considered to be a major federal action, then it is exempt from NEPA.</p>",
      "updateDate": "2025-12-01",
      "versionCode": "id119hr676"
    },
    "title": "To exempt Federal actions related to energy and mineral activities on certain Federal lands from the requirements of the National Environmental Policy Act of 1969."
  },
  "summaries": [
    {
      "actionDate": "2025-01-23",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill exempts certain energy and mineral actions on federal lands from the environmental review requirements under the National Environmental Policy Act of 1969 (NEPA). Specifically, the bill states that the following are not to be considered a major federal action under NEPA:</p><ul><li>issuing, granting, or renewing a lease, easement, or right-of-way under the Mineral Leasing Act\u00a0for the exploration, development, or production of oil, gas, or coal; or</li><li>issuing, granting, or renewing a permit or other authorization under the Mining Law of 1872\u00a0for the exploration, location, development, or extraction of a critical mineral on land that is open to mineral entry.</li></ul><p>By way of background,\u00a0NEPA requires agencies to identify and evaluate the impacts of major federal actions significantly affecting the quality of the human environment prior to finalizing certain decisions. Thus, if an action is not considered to be a major federal action, then it is exempt from NEPA.</p>",
      "updateDate": "2025-12-01",
      "versionCode": "id119hr676"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr676ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To exempt Federal actions related to energy and mineral activities on certain Federal lands from the requirements of the National Environmental Policy Act of 1969.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-22T08:03:43Z"
    },
    {
      "title": "To exempt Federal actions related to energy and mineral activities on certain Federal lands from the requirements of the National Environmental Policy Act of 1969.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-24T09:05:59Z"
    }
  ]
}
```
