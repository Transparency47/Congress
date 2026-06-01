# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1393?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/1393
- Title: Wildfire Response Improvement Act
- Congress: 119
- Bill type: HR
- Bill number: 1393
- Origin chamber: House
- Introduced date: 2025-02-14
- Update date: 2025-06-24T20:18:43Z
- Update date including text: 2025-06-24T20:18:43Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-14: Introduced in House
- 2025-02-14 - IntroReferral: Introduced in House
- 2025-02-14 - IntroReferral: Introduced in House
- 2025-02-14 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-02-14 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.
- Latest action: 2025-02-14: Introduced in House

## Actions

- 2025-02-14 - IntroReferral: Introduced in House
- 2025-02-14 - IntroReferral: Introduced in House
- 2025-02-14 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-02-14 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-14",
    "latestAction": {
      "actionDate": "2025-02-14",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/1393",
    "number": "1393",
    "originChamber": "House",
    "policyArea": {
      "name": "Emergency Management"
    },
    "sponsors": [
      {
        "bioguideId": "S001211",
        "district": "4",
        "firstName": "Greg",
        "fullName": "Rep. Stanton, Greg [D-AZ-4]",
        "lastName": "Stanton",
        "party": "D",
        "state": "AZ"
      }
    ],
    "title": "Wildfire Response Improvement Act",
    "type": "HR",
    "updateDate": "2025-06-24T20:18:43Z",
    "updateDateIncludingText": "2025-06-24T20:18:43Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-14",
      "committees": {
        "item": {
          "name": "Economic Development, Public Buildings, and Emergency Management Subcommittee",
          "systemCode": "hspw13"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-14",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Transportation and Infrastructure.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-14",
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
          "date": "2025-02-14T18:31:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-02-14T22:21:22Z",
              "name": "Referred to"
            }
          },
          "name": "Economic Development, Public Buildings, and Emergency Management Subcommittee",
          "systemCode": "hspw13"
        }
      },
      "systemCode": "hspw00",
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
      "bioguideId": "L000578",
      "district": "1",
      "firstName": "Doug",
      "fullName": "Rep. LaMalfa, Doug [R-CA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "LaMalfa",
      "party": "R",
      "sponsorshipDate": "2025-02-14",
      "state": "CA"
    },
    {
      "bioguideId": "H001068",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Huffman, Jared [D-CA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Huffman",
      "party": "D",
      "sponsorshipDate": "2025-03-14",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1393ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1393\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 14, 2025 Mr. Stanton (for himself and Mr. LaMalfa ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo direct the Administrator of the Federal Emergency Management Agency to conduct a review of the criteria for evaluating the cost-effectiveness of certain mitigation projects, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Wildfire Response Improvement Act .\n#### 2. Fire management assistance program policy\nNot later than 1 year after the date of enactment of this Act, the Administrator of the Federal Emergency Management Agency shall recommend such regulations or guidance as are necessary to make eligible assessments and emergency stabilization to protect public safety, including for the fire management assistance program under section 420 of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5187 ), irrespective of the incident period for a declared fire.\n#### 3. Changes to public assistance policy guide\nNot later than 1 year after the date of enactment of this Act, the Administrator of the Federal Emergency Management Agency shall amend the Public Assistance Program and Policy Guide of the Federal Emergency Management Agency to include guidance on wildfire-specific recovery challenges, including debris removal, emergency protective measures, and the resulting toxicity of drinking water resources.\n#### 4. Mitigation cost-effectiveness\n##### (a) In general\nThe Administrator of the Federal Emergency Management Agency shall conduct a review of the criteria for evaluating the cost-effectiveness of projects intended to mitigate the impacts of wildfire under sections 203 and 404 of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5133 ; 5170c), including\u2014\n**(1)**\nthe establishment of pre-calculated benefits criterion for common defensible space mitigation projects for wildfire mitigation;\n**(2)**\nthe use of nature-based infrastructure in wildfire mitigation;\n**(3)**\nconsiderations for vegetation management for wildfire mitigation;\n**(4)**\nreducing the negative effects of wildfire smoke on public health; and\n**(5)**\nlessening the impact of wildfires on water infrastructure.\n##### (b) Updated criteria\nNot later than 1 year after the date of enactment of this Act, the Administrator shall issue such guidance as is necessary to\u2014\n**(1)**\nupdate criteria for evaluating the cost-effectiveness of mitigation projects under sections 203 and 404 of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5133 ; 5170c) based on the results of the review conducted under subsection (a); and\n**(2)**\nprioritize projects under such sections based on the criteria updated under paragraph (1).",
      "versionDate": "2025-02-14",
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
        "name": "Emergency Management",
        "updateDate": "2025-05-14T13:09:19Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-14",
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
          "measure-id": "id119hr1393",
          "measure-number": "1393",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-14",
          "originChamber": "HOUSE",
          "update-date": "2025-06-24"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1393v00",
            "update-date": "2025-06-24"
          },
          "action-date": "2025-02-14",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Wildfire Response Improvement Act</strong></p><p>This bill expands certain wildfire management assistance to beyond the time when the fire occurs and requires the Federal Emergency Management Agency (FEMA) to update various programmatic guidance relating to wildfire response and cost-effectiveness criteria for wildfire mitigation projects.</p><p>Currently, in general, government entities\u2019 costs for fighting wildfires are only eligible for assistance under the Fire Management Assistance Grant (FMAG) Program if the costs are incurred during the incident period (i.e., time during which the fire occurs). The bill requires\u00a0FEMA to modify the FMAG\u00a0Program so that assessments and emergency stabilization to protect public safety are eligible for FMAG assistance regardless of when the incident period begins or ends.</p><p>The bill also requires\u00a0FEMA to review and update its evaluation criteria for the cost-effectiveness of wildfire mitigation projects proposed under the Building Resilient Infrastructure and Communities program or Hazard Mitigation Grant Program and prioritize projects accordingly.</p><p>Additionally,\u00a0FEMA must update its policy guide for the Public Assistance program to include guidance on challenges with wildfire recovery, including the resulting toxicity of drinking water resources.</p>"
        },
        "title": "Wildfire Response Improvement Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1393.xml",
    "summary": {
      "actionDate": "2025-02-14",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Wildfire Response Improvement Act</strong></p><p>This bill expands certain wildfire management assistance to beyond the time when the fire occurs and requires the Federal Emergency Management Agency (FEMA) to update various programmatic guidance relating to wildfire response and cost-effectiveness criteria for wildfire mitigation projects.</p><p>Currently, in general, government entities\u2019 costs for fighting wildfires are only eligible for assistance under the Fire Management Assistance Grant (FMAG) Program if the costs are incurred during the incident period (i.e., time during which the fire occurs). The bill requires\u00a0FEMA to modify the FMAG\u00a0Program so that assessments and emergency stabilization to protect public safety are eligible for FMAG assistance regardless of when the incident period begins or ends.</p><p>The bill also requires\u00a0FEMA to review and update its evaluation criteria for the cost-effectiveness of wildfire mitigation projects proposed under the Building Resilient Infrastructure and Communities program or Hazard Mitigation Grant Program and prioritize projects accordingly.</p><p>Additionally,\u00a0FEMA must update its policy guide for the Public Assistance program to include guidance on challenges with wildfire recovery, including the resulting toxicity of drinking water resources.</p>",
      "updateDate": "2025-06-24",
      "versionCode": "id119hr1393"
    },
    "title": "Wildfire Response Improvement Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-14",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Wildfire Response Improvement Act</strong></p><p>This bill expands certain wildfire management assistance to beyond the time when the fire occurs and requires the Federal Emergency Management Agency (FEMA) to update various programmatic guidance relating to wildfire response and cost-effectiveness criteria for wildfire mitigation projects.</p><p>Currently, in general, government entities\u2019 costs for fighting wildfires are only eligible for assistance under the Fire Management Assistance Grant (FMAG) Program if the costs are incurred during the incident period (i.e., time during which the fire occurs). The bill requires\u00a0FEMA to modify the FMAG\u00a0Program so that assessments and emergency stabilization to protect public safety are eligible for FMAG assistance regardless of when the incident period begins or ends.</p><p>The bill also requires\u00a0FEMA to review and update its evaluation criteria for the cost-effectiveness of wildfire mitigation projects proposed under the Building Resilient Infrastructure and Communities program or Hazard Mitigation Grant Program and prioritize projects accordingly.</p><p>Additionally,\u00a0FEMA must update its policy guide for the Public Assistance program to include guidance on challenges with wildfire recovery, including the resulting toxicity of drinking water resources.</p>",
      "updateDate": "2025-06-24",
      "versionCode": "id119hr1393"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1393ih.xml"
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
      "title": "Wildfire Response Improvement Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-13T04:23:35Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Wildfire Response Improvement Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-13T04:23:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Administrator of the Federal Emergency Management Agency to conduct a review of the criteria for evaluating the cost-effectiveness of certain mitigation projects, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-13T04:19:00Z"
    }
  ]
}
```
