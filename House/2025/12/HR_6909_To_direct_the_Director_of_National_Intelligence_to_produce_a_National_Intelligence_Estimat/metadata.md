# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6909?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6909
- Title: China AI Threat Assessment Act
- Congress: 119
- Bill type: HR
- Bill number: 6909
- Origin chamber: House
- Introduced date: 2025-12-18
- Update date: 2026-01-21T16:43:19Z
- Update date including text: 2026-01-21T16:43:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-18: Introduced in House
- 2025-12-18 - IntroReferral: Introduced in House
- 2025-12-18 - IntroReferral: Introduced in House
- 2025-12-18 - IntroReferral: Referred to the House Permanent Select Committee on Intelligence.
- Latest action: 2025-12-18: Introduced in House

## Actions

- 2025-12-18 - IntroReferral: Introduced in House
- 2025-12-18 - IntroReferral: Introduced in House
- 2025-12-18 - IntroReferral: Referred to the House Permanent Select Committee on Intelligence.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-18",
    "latestAction": {
      "actionDate": "2025-12-18",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6909",
    "number": "6909",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "V000138",
        "district": "7",
        "firstName": "Eugene",
        "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
        "lastName": "Vindman",
        "party": "D",
        "state": "VA"
      }
    ],
    "title": "China AI Threat Assessment Act",
    "type": "HR",
    "updateDate": "2026-01-21T16:43:19Z",
    "updateDateIncludingText": "2026-01-21T16:43:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-18",
      "committees": {
        "item": {
          "name": "Intelligence (Permanent Select) Committee",
          "systemCode": "hlig00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Permanent Select Committee on Intelligence.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-18",
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
          "date": "2025-12-18T14:09:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Intelligence (Permanent Select) Committee",
      "systemCode": "hlig00",
      "type": "Select"
    }
  ]
}
```

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "P000048",
      "district": "11",
      "firstName": "August",
      "fullName": "Rep. Pfluger, August [R-TX-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Pfluger",
      "party": "R",
      "sponsorshipDate": "2025-12-18",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6909ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6909\nIN THE HOUSE OF REPRESENTATIVES\nDecember 18, 2025 Mr. Vindman (for himself and Mr. Pfluger ) introduced the following bill; which was referred to the Permanent Select Committee on Intelligence\nA BILL\nTo direct the Director of National Intelligence to produce a National Intelligence Estimate on artificial intelligence systems developed or deployed by entities in the People\u2019s Republic of China.\n#### 1. Short title\nThis Act may be cited as the China AI Threat Assessment Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nArtificial intelligence systems developed by the People\u2019s Republic of China may embed strategic, ideological, or discriminatory biases that reflect the political or military objectives of China.\n**(2)**\nA National Intelligence Estimate is needed to evaluate the risks these systems pose to United States national security and democratic institutions.\n#### 3. National Intelligence Estimate on Chinese AI systems\n##### (a) Requirement\nNot later than 180 days after the date of enactment of this Act, the Director of National Intelligence shall submit to Congress a National Intelligence Estimate on artificial intelligence systems developed or deployed by entities in the People\u2019s Republic of China.\n##### (b) Elements\nThe National Intelligence Estimate required under subsection (a) shall include\u2014\n**(1)**\nan evaluation of whether and to what extent China-developed commercial AI systems exhibit embedded algorithmic bias, including targeting or discriminatory logic based on ethnicity, religion, political views, or nationality;\n**(2)**\nan analysis of the training data sources, model architectures, and intended use cases of such systems;\n**(3)**\nan assessment of potential use of such AI systems for foreign influence operations, surveillance, or information manipulation targeting the United States or its allies;\n**(4)**\nidentification of risks posed by the global proliferation of these systems to democratic norms, civil liberties, and military decision-making; and\n**(5)**\nrecommendations for how the intelligence community and United States allies should monitor, assess, and counter malign uses of Chinese AI technology.\n##### (c) Coordination\nIn preparing the National Intelligence Estimate under subsection (a), the Director shall coordinate with the heads of relevant elements of the intelligence community, including the Director of the National Security Agency and the Director of the Defense Intelligence Agency.\n##### (d) Artificial intelligence defined\nIn this section, the terms artificial intelligence and AI mean any system, algorithm, software, or model, including those that are commercially available, that performs tasks requiring human-like cognition, including perception, prediction, autonomous decision-making, natural language understanding, or control of physical or digital systems.",
      "versionDate": "2025-12-18",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2026-01-21T16:43:19Z"
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
      "date": "2025-12-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6909ih.xml"
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
      "title": "China AI Threat Assessment Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-21T11:08:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "China AI Threat Assessment Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-21T11:08:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Director of National Intelligence to produce a National Intelligence Estimate on artificial intelligence systems developed or deployed by entities in the People's Republic of China.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-21T11:03:19Z"
    }
  ]
}
```
