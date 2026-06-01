# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2792?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2792
- Title: USRC Funding Eligibility Act
- Congress: 119
- Bill type: HR
- Bill number: 2792
- Origin chamber: House
- Introduced date: 2025-04-09
- Update date: 2025-12-05T22:06:45Z
- Update date including text: 2025-12-05T22:06:45Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-04-09: Introduced in House
- 2025-04-09 - IntroReferral: Introduced in House
- 2025-04-09 - IntroReferral: Introduced in House
- 2025-04-09 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-04-09 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.
- 2025-04-09 - Committee: Referred to the Subcommittee on Highways and Transit.
- 2025-04-09 - Committee: Referred to the Subcommittee on Railroads, Pipelines, and Hazardous Materials.
- 2025-04-09 - IntroReferral: Sponsor introductory remarks on measure. (CR E303)
- Latest action: 2025-04-09: Introduced in House

## Actions

- 2025-04-09 - IntroReferral: Introduced in House
- 2025-04-09 - IntroReferral: Introduced in House
- 2025-04-09 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-04-09 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.
- 2025-04-09 - Committee: Referred to the Subcommittee on Highways and Transit.
- 2025-04-09 - Committee: Referred to the Subcommittee on Railroads, Pipelines, and Hazardous Materials.
- 2025-04-09 - IntroReferral: Sponsor introductory remarks on measure. (CR E303)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-09",
    "latestAction": {
      "actionDate": "2025-04-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2792",
    "number": "2792",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "N000147",
        "district": "",
        "firstName": "Eleanor",
        "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
        "lastName": "Norton",
        "party": "D",
        "state": "DC"
      }
    ],
    "title": "USRC Funding Eligibility Act",
    "type": "HR",
    "updateDate": "2025-12-05T22:06:45Z",
    "updateDateIncludingText": "2025-12-05T22:06:45Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-09",
      "committees": {
        "item": {
          "name": "Railroads, Pipelines, and Hazardous Materials Subcommittee",
          "systemCode": "hspw14"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Railroads, Pipelines, and Hazardous Materials.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-04-09",
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
      "actionDate": "2025-04-09",
      "committees": {
        "item": {
          "name": "Highways and Transit Subcommittee",
          "systemCode": "hspw12"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Highways and Transit.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-09",
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
      "actionDate": "2025-04-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "B00100",
      "actionDate": "2025-04-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Sponsor introductory remarks on measure. (CR E303)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-09",
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
          "date": "2025-04-09T16:00:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": [
          {
            "activities": {
              "item": {
                "date": "2025-04-09T21:11:12Z",
                "name": "Referred to"
              }
            },
            "name": "Economic Development, Public Buildings, and Emergency Management Subcommittee",
            "systemCode": "hspw13"
          },
          {
            "activities": {
              "item": {
                "date": "2025-04-09T21:11:12Z",
                "name": "Referred to"
              }
            },
            "name": "Highways and Transit Subcommittee",
            "systemCode": "hspw12"
          },
          {
            "activities": {
              "item": {
                "date": "2025-04-09T21:11:12Z",
                "name": "Referred to"
              }
            },
            "name": "Railroads, Pipelines, and Hazardous Materials Subcommittee",
            "systemCode": "hspw14"
          }
        ]
      },
      "systemCode": "hspw00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2792ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2792\nIN THE HOUSE OF REPRESENTATIVES\nApril 9, 2025 Ms. Norton introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo make the Union Station Redevelopment Corporation eligible to receive certain grants, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Union Station Redevelopment Corporation Funding Eligibility Act or the USRC Funding Eligibility Act .\n#### 2. Eligibility of Union Station Redevelopment Corporation to receive certain grants\n##### (a) Better Utilizing Investments to Leverage Development (BUILD) grants\n**(1) Eligibility**\nThe Union Station Redevelopment Corporation shall be eligible to receive grants under the program for national infrastructure investments (commonly known as the Better Utilizing Investments to Leverage Development (BUILD) grant program and formerly known as the Rebuilding American Infrastructure with Sustainability and Equity (RAISE) grant program ) carried out by the Department of Transportation.\n**(2) Federal share**\nThe Federal share of a grant under a program described in paragraph (1) to the Union Station Redevelopment Corporation shall be 100 percent.\n##### (b) National infrastructure project assistance grants\nSection 6701 of title 49, United States Code, is amended\u2014\n**(1)**\nin subsection (a)(2)\u2014\n**(A)**\nin subparagraph (G) by striking and at the end;\n**(B)**\nin subparagraph (H) by striking (G) and inserting (H) ;\n**(C)**\nby redesignating subparagraph (H) as subparagraph (I); and\n**(D)**\nby inserting after subparagraph (G) the following:\n(H) Union Station Redevelopment Corporation; and ; and\n**(2)**\nin subsection (i) by adding at the end the following:\n(4) Exception Notwithstanding paragraph (1), the total amount awarded for a project under the program awarded to the entity described in subsection (a)(2)(H) shall be 100 percent of the total eligible project costs described in subsection (h). .\n##### (c) Consolidated rail infrastructure and safety improvement grants\nSection 22907 of title 49, United States Code, is amended\u2014\n**(1)**\nin subsection (b) by adding at the end the following:\n(14) The Union Station Redevelopment Corporation. ; and\n**(2)**\nin subsection (h)(2) by inserting , except that with respect to the entity described in subsection (b)(14) the Federal share shall be 100 percent before the period.\n##### (d) Federal-State partnership for intercity passenger rail grants\nSection 24911 of title 49, United States Code, is amended\u2014\n**(1)**\nin subsection (a)(1)\u2014\n**(A)**\nin subparagraph (G) by striking or at the end;\n**(B)**\nin subparagraph (H) by striking (G) and inserting (H) ;\n**(C)**\nby redesignating subparagraph (H) as subparagraph (I); and\n**(D)**\nby inserting after subparagraph (G) the following:\n(H) the Union Station Redevelopment Corporation; or ; and\n**(2)**\nin subsection (f) by adding at the end the following:\n(4) Exception The total amount awarded for a project under the program awarded to the entity described in subsection (a)(1)(H) shall be 100 percent. .",
      "versionDate": "2025-04-09",
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
        "actionDate": "2025-04-09",
        "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation."
      },
      "number": "1373",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "USRC Funding Eligibility Act",
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
        "name": "Transportation and Public Works",
        "updateDate": "2025-05-19T16:07:20Z"
      }
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2792ih.xml"
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
      "title": "USRC Funding Eligibility Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-24T04:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "USRC Funding Eligibility Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-24T04:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Union Station Redevelopment Corporation Funding Eligibility Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-24T04:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To make the Union Station Redevelopment Corporation eligible to receive certain grants, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-24T04:48:26Z"
    }
  ]
}
```
