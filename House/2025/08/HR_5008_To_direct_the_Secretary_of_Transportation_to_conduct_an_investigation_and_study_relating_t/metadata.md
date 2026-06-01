# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5008?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5008
- Title: Affordable Commutes Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 5008
- Origin chamber: House
- Introduced date: 2025-08-19
- Update date: 2025-10-07T08:05:39Z
- Update date including text: 2025-10-07T08:05:39Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-08-19: Introduced in House
- 2025-08-19 - IntroReferral: Introduced in House
- 2025-08-19 - IntroReferral: Introduced in House
- 2025-08-19 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-08-20 - Committee: Referred to the Subcommittee on Highways and Transit.
- Latest action: 2025-08-19: Introduced in House

## Actions

- 2025-08-19 - IntroReferral: Introduced in House
- 2025-08-19 - IntroReferral: Introduced in House
- 2025-08-19 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-08-20 - Committee: Referred to the Subcommittee on Highways and Transit.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-08-19",
    "latestAction": {
      "actionDate": "2025-08-19",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5008",
    "number": "5008",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "S001230",
        "district": "10",
        "firstName": "Suhas",
        "fullName": "Rep. Subramanyam, Suhas [D-VA-10]",
        "lastName": "Subramanyam",
        "party": "D",
        "state": "VA"
      }
    ],
    "title": "Affordable Commutes Act of 2025",
    "type": "HR",
    "updateDate": "2025-10-07T08:05:39Z",
    "updateDateIncludingText": "2025-10-07T08:05:39Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-08-20",
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
      "actionDate": "2025-08-19",
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
      "actionDate": "2025-08-19",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-08-19",
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
          "date": "2025-08-19T14:00:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-08-20T21:36:18Z",
              "name": "Referred to"
            }
          },
          "name": "Highways and Transit Subcommittee",
          "systemCode": "hspw12"
        }
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5008ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5008\nIN THE HOUSE OF REPRESENTATIVES\nAugust 19, 2025 Mr. Subramanyam introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo direct the Secretary of Transportation to conduct an investigation and study relating to purchasing certain toll roads owned by private entities and transferring ownership of such toll roads to States, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Affordable Commutes Act of 2025 .\n#### 2. Investigation of pricing practices on private toll roads\n##### (a) In general\nThe Secretary of Transportation shall conduct an investigation of the price setting of toll roads owned by private entities, including any instances of price gouging, unfair practices, or unreasonable toll price setting.\n##### (b) Referral of certain unfair practices\nIn any case in which the Secretary finds any evidence of price gouging, unfair practices, or unreasonable toll price setting pursuant to the investigation under subsection (a), the Secretary shall refer such cases to the Attorney General of the United States and the Federal Trade Commission, as applicable.\n#### 3. Study on toll roads owned by private entities\nThe Secretary shall conduct a study on the feasibility and fiscal implications of the Federal Government purchasing toll roads owned by private entities and transferring the ownership of such toll roads to the State in which such roads are located, including\u2014\n**(1)**\nwhether a change in authority of toll roads from privately-owned to State-owned facilities would benefit consumers, including in the form of lower toll costs;\n**(2)**\nthe procedural framework necessary for the Federal Government to purchase and transfer private toll roads; and\n**(3)**\nany other policies relating to tolling facilities that the Federal Government can pursue to lower costs for commuters.\n#### 4. Report to Congress\nNot later than 1 year after the date of enactment of this Act, the Secretary of Transportation shall submit to Congress a report containing\u2014\n**(1)**\nthe results of the investigation under section 2;\n**(2)**\nthe results of the study under section 3; and\n**(3)**\nany recommendations to\u2014\n**(A)**\naddress price gouging, unfair practices, or unreasonable toll price setting; and\n**(B)**\ncarry out the purchases and transfers described in section 3.",
      "versionDate": "2025-08-19",
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
        "name": "Transportation and Public Works",
        "updateDate": "2025-09-19T14:27:02Z"
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
      "date": "2025-08-19",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5008ih.xml"
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
      "title": "To direct the Secretary of Transportation to conduct an investigation and study relating to purchasing certain toll roads owned by private entities and transferring ownership of such toll roads to States, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-20T10:08:10Z"
    },
    {
      "title": "Affordable Commutes Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-20T08:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Affordable Commutes Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-20T08:23:16Z"
    }
  ]
}
```
