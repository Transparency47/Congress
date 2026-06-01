# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1647?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1647
- Title: Tribal Climate Health Assurance Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1647
- Origin chamber: House
- Introduced date: 2025-02-27
- Update date: 2025-09-02T15:21:42Z
- Update date including text: 2025-09-02T15:21:42Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-27: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-02-27: Introduced in House

## Actions

- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-27",
    "latestAction": {
      "actionDate": "2025-02-27",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1647",
    "number": "1647",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "U000040",
        "district": "14",
        "firstName": "Lauren",
        "fullName": "Rep. Underwood, Lauren [D-IL-14]",
        "lastName": "Underwood",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "Tribal Climate Health Assurance Act of 2025",
    "type": "HR",
    "updateDate": "2025-09-02T15:21:42Z",
    "updateDateIncludingText": "2025-09-02T15:21:42Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-27",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-27",
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
          "date": "2025-02-27T14:05:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "H001068",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Huffman, Jared [D-CA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Huffman",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "CA"
    },
    {
      "bioguideId": "C001112",
      "district": "24",
      "firstName": "Salud",
      "fullName": "Rep. Carbajal, Salud O. [D-CA-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Carbajal",
      "middleName": "O.",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "CA"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "DC"
    },
    {
      "bioguideId": "K000400",
      "district": "37",
      "firstName": "Sydney",
      "fullName": "Rep. Kamlager-Dove, Sydney [D-CA-37]",
      "isOriginalCosponsor": "True",
      "lastName": "Kamlager-Dove",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "CA"
    },
    {
      "bioguideId": "A000381",
      "district": "3",
      "firstName": "Yassamin",
      "fullName": "Rep. Ansari, Yassamin [D-AZ-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Ansari",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "AZ"
    },
    {
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2025-03-03",
      "state": "GA"
    },
    {
      "bioguideId": "D000629",
      "district": "3",
      "firstName": "Sharice",
      "fullName": "Rep. Davids, Sharice [D-KS-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Davids",
      "party": "D",
      "sponsorshipDate": "2025-03-03",
      "state": "KS"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1647ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1647\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 27, 2025 Ms. Underwood (for herself, Mr. Huffman , Mr. Carbajal , Ms. Norton , Ms. Kamlager-Dove , and Ms. Ansari ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Public Health Service Act to require the Secretary of Health and Human Services, acting through the Director of the Centers for Disease Control and Prevention, to implement the Climate Ready Tribes Initiative.\n#### 1. Short title\nThis Act may be cited as the Tribal Climate Health Assurance Act of 2025 .\n#### 2. Climate Ready Tribes Initiative\nPart B of title III of the Public Health Service Act is amended by inserting after section 317V ( 42 U.S.C. 247b\u201324 ) the following new section:\n317W. Climate Ready Tribes Initiative (a) In general The Secretary, acting through the Director of the Centers for Disease Control and Prevention, in coordination with the National Indian Health Board, shall implement the Climate Ready Tribes Initiative for the following purposes: (1) Translating climate change science to inform Tribal governments, health departments, and communities. (2) Creating decision-support tools to build capacity to prepare for climate change. (3) Serving as a credible leader in planning and preparing for the public health impacts of climate change. (4) Identifying, assessing, and taking action to mitigate climate-related health threats. (5) Sharing relevant materials and resources, including information about funding and other opportunities. (b) Authorization of appropriations (1) In general To carry out this section, there is authorized to be appropriated $110,000,000 for fiscal year 2026 and each fiscal year thereafter. (2) Limitation None of the funds made available under paragraph (1) may be transferred or reprogrammed by the Secretary to carry out another program administered by the Secretary. .",
      "versionDate": "2025-02-27",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Climate change and greenhouse gases",
            "updateDate": "2025-09-02T15:21:25Z"
          },
          {
            "name": "Environmental assessment, monitoring, research",
            "updateDate": "2025-09-02T15:21:42Z"
          },
          {
            "name": "Environmental health",
            "updateDate": "2025-09-02T15:21:31Z"
          },
          {
            "name": "Health programs administration and funding",
            "updateDate": "2025-09-02T15:21:37Z"
          },
          {
            "name": "Indian social and development programs",
            "updateDate": "2025-09-02T15:21:16Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-03-21T14:49:07Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-27",
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
          "measure-id": "id119hr1647",
          "measure-number": "1647",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-27",
          "originChamber": "HOUSE",
          "update-date": "2025-08-14"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1647v00",
            "update-date": "2025-08-14"
          },
          "action-date": "2025-02-27",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Tribal Climate Health Assurance Act of 2025</strong></p><p>This bill provides statutory authority for the Centers for Disease Control and Prevention to implement the Climate Ready Tribes Initiative in coordination with the National Indian Health Board. The purposes of the initiative include translating science, creating decision-support tools, and mitigating threats relating to the health impacts of climate change on Indian tribes.\u00a0</p>"
        },
        "title": "Tribal Climate Health Assurance Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1647.xml",
    "summary": {
      "actionDate": "2025-02-27",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Tribal Climate Health Assurance Act of 2025</strong></p><p>This bill provides statutory authority for the Centers for Disease Control and Prevention to implement the Climate Ready Tribes Initiative in coordination with the National Indian Health Board. The purposes of the initiative include translating science, creating decision-support tools, and mitigating threats relating to the health impacts of climate change on Indian tribes.\u00a0</p>",
      "updateDate": "2025-08-14",
      "versionCode": "id119hr1647"
    },
    "title": "Tribal Climate Health Assurance Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-27",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Tribal Climate Health Assurance Act of 2025</strong></p><p>This bill provides statutory authority for the Centers for Disease Control and Prevention to implement the Climate Ready Tribes Initiative in coordination with the National Indian Health Board. The purposes of the initiative include translating science, creating decision-support tools, and mitigating threats relating to the health impacts of climate change on Indian tribes.\u00a0</p>",
      "updateDate": "2025-08-14",
      "versionCode": "id119hr1647"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1647ih.xml"
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
      "title": "Tribal Climate Health Assurance Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-20T09:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Tribal Climate Health Assurance Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-20T09:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Public Health Service Act to require the Secretary of Health and Human Services, acting through the Director of the Centers for Disease Control and Prevention, to implement the Climate Ready Tribes Initiative.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-20T09:18:22Z"
    }
  ]
}
```
