# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2236?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2236
- Title: Healthy Foods for Native Seniors Act
- Congress: 119
- Bill type: HR
- Bill number: 2236
- Origin chamber: House
- Introduced date: 2025-03-18
- Update date: 2026-03-16T18:19:00Z
- Update date including text: 2026-03-16T18:19:00Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-03-18: Introduced in House
- 2025-03-18 - IntroReferral: Introduced in House
- 2025-03-18 - IntroReferral: Introduced in House
- 2025-03-18 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-04-18 - Committee: Referred to the Subcommittee on Nutrition and Foreign Agriculture.
- Latest action: 2025-03-18: Introduced in House

## Actions

- 2025-03-18 - IntroReferral: Introduced in House
- 2025-03-18 - IntroReferral: Introduced in House
- 2025-03-18 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-04-18 - Committee: Referred to the Subcommittee on Nutrition and Foreign Agriculture.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-18",
    "latestAction": {
      "actionDate": "2025-03-18",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2236",
    "number": "2236",
    "originChamber": "House",
    "policyArea": {
      "name": "Native Americans"
    },
    "sponsors": [
      {
        "bioguideId": "V000136",
        "district": "2",
        "firstName": "Gabe",
        "fullName": "Rep. Vasquez, Gabe [D-NM-2]",
        "lastName": "Vasquez",
        "party": "D",
        "state": "NM"
      }
    ],
    "title": "Healthy Foods for Native Seniors Act",
    "type": "HR",
    "updateDate": "2026-03-16T18:19:00Z",
    "updateDateIncludingText": "2026-03-16T18:19:00Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-18",
      "committees": {
        "item": {
          "name": "Nutrition and Foreign Agriculture Subcommittee",
          "systemCode": "hsag03"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Nutrition and Foreign Agriculture.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-18",
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
      "actionDate": "2025-03-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-18",
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
          "date": "2025-03-18T16:03:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-04-18T21:07:00Z",
              "name": "Referred to"
            }
          },
          "name": "Nutrition and Foreign Agriculture Subcommittee",
          "systemCode": "hsag03"
        }
      },
      "systemCode": "hsag00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2236ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2236\nIN THE HOUSE OF REPRESENTATIVES\nMarch 18, 2025 Mr. Vasquez introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo direct the Secretary of Agriculture to carry out a demonstration project to allow Tribal entities to purchase agricultural commodities under the commodity supplemental food program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Healthy Foods for Native Seniors Act .\n#### 2. Commodity supplemental food program demonstration project for Tribal organizations\n##### (a) Demonstration project for Tribal organizations\n**(1) Definitions**\nIn this subsection:\n**(A) Demonstration project**\nThe term demonstration project means the demonstration project established under paragraph (2).\n**(B) Food distribution program**\nThe term food distribution program means the commodity supplemental food program under section 4 of the Agriculture and Consumer Protection Act of 1973 ( 7 U.S.C. 612c note).\n**(C) Indian reservation**\nThe term Indian reservation has the meaning given the term reservation in section 3 of the Food and Nutrition Act of 2008 ( 7 U.S.C. 2012 ).\n**(D) Indian Tribe**\nThe term Indian Tribe has the meaning given such term in section 4 of the Indian Self-Determination and Education Assistance Act ( 25 U.S.C. 5304 ).\n**(E) Secretary**\nThe term Secretary means the Secretary of Agriculture.\n**(F) Self-determination contract**\nThe term self-determination contract has the meaning given such term in section 4 of the Indian Self-Determination and Education Assistance Act ( 25 U.S.C. 5304 ) with modification as determined by the Secretary.\n**(G) Tribal entity**\nThe term Tribal entity means\u2014\n**(i)**\nan Indian reservation;\n**(ii)**\nan Indian Tribe; and\n**(iii)**\na Tribal organization.\n**(H) Tribal organization**\nThe term Tribal organization has the meaning given such term in section 3 of the Food and Nutrition Act of 2008 ( 7 U.S.C. 2012 ).\n**(2) Establishment**\nSubject to the availability of appropriations, the Secretary shall establish a demonstration project under which 1 or more Tribal entities may enter into self-determination contracts to purchase agricultural commodities under the food distribution program for the Indian reservation of that Tribal entity.\n**(3) Eligibility**\n**(A) Consultation**\nThe Secretary shall consult with Tribal entities to determine the process under which each entity may participate in the demonstration project.\n**(B) Criteria**\nThe Secretary shall select for participation in the demonstration project Tribal entities that\u2014\n**(i)**\nare successfully administering the food distribution program of the Tribal entity;\n**(ii)**\nhave the capacity to purchase agricultural commodities in accordance with paragraph (4) for the food distribution program of the Tribal entity; and\n**(iii)**\nmeet any other criteria determined by the Secretary, in consultation with the Secretary of the Interior and Tribal entities.\n**(4) Procurement of agricultural commodities**\nAny agricultural commodities purchased by a Tribal entity under the demonstration project shall\u2014\n**(A)**\nbe domestically produced;\n**(B)**\nnot result in a material increase in the amount of food in the food package of that Tribal entity compared to the amount of food that the Secretary authorized to be provided through the CSFP Guide Rate;\n**(C)**\nbe of similar or higher nutritional value as the type of agricultural commodities that would be supplanted in the existing food package for that Tribal entity or be an agricultural commodity with Tribal significance to that Tribal entity; and\n**(D)**\nmeet any other criteria determined by the Secretary.\n**(5) Report**\nNot later than 1 year after the date on which funds are appropriated under paragraph (6), and annually thereafter, the Secretary shall submit to the Committee on Agriculture of the House of Representatives and the Committee on Agriculture, Nutrition, and Forestry of the Senate a report describing the activities carried out under the demonstration project during the preceding year.\n**(6) Funding**\n**(A) Authorization of appropriations**\nThere is authorized to be appropriated to the Secretary to carry out this subsection $5,000,000, to remain available until expended.\n**(B) Appropriations in advance**\nWith respect to any funds made available under subparagraph (A), only funds appropriated in advance specifically to carry out this subsection shall be available to carry out this subsection.\n##### (b) Administration of Tribal self-Determination contracts\n**(1) Administration**\nThe Secretary shall appoint an existing office of the Department of Agriculture to administer Tribal self-determination contracts, including\u2014\n**(A)**\nawarding of FNS nutrition program self-determination contracts to selected Tribal entities; and\n**(B)**\nhiring contract officers and program staff in order to manage the selection of Tribal entities and execution of self-determination contracts.\n**(2) Staffing minimum funding**\nNotwithstanding any other provision of law, there is authorized to be appropriated to the Secretary $1,200,000 for each of fiscal years 2026 through 2029 for the payment of Department contract officers and program staff salaries and benefits.",
      "versionDate": "2025-03-18",
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
            "name": "Congressional oversight",
            "updateDate": "2026-03-16T18:18:54Z"
          },
          {
            "name": "Federal-Indian relations",
            "updateDate": "2026-03-16T18:19:00Z"
          },
          {
            "name": "Food supply, safety, and labeling",
            "updateDate": "2026-03-16T18:18:40Z"
          },
          {
            "name": "Indian social and development programs",
            "updateDate": "2026-03-16T18:18:28Z"
          },
          {
            "name": "Minority health",
            "updateDate": "2026-03-16T18:18:34Z"
          },
          {
            "name": "Nutrition and diet",
            "updateDate": "2026-03-16T18:18:45Z"
          }
        ]
      },
      "policyArea": {
        "name": "Native Americans",
        "updateDate": "2025-05-12T18:56:32Z"
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
      "date": "2025-03-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2236ih.xml"
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
      "title": "Healthy Foods for Native Seniors Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-03T13:23:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Healthy Foods for Native Seniors Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-03T13:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Agriculture to carry out a demonstration project to allow Tribal entities to purchase agricultural commodities under the commodity supplemental food program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-03T13:18:46Z"
    }
  ]
}
```
