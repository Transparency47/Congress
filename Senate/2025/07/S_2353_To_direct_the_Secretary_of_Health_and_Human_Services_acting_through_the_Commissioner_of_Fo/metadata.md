# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2353?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2353
- Title: Microplastics Safety Act
- Congress: 119
- Bill type: S
- Bill number: 2353
- Origin chamber: Senate
- Introduced date: 2025-07-17
- Update date: 2025-12-05T21:45:56Z
- Update date including text: 2025-12-05T21:45:56Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-17: Introduced in Senate
- 2025-07-17 - IntroReferral: Introduced in Senate
- 2025-07-17 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-07-17: Introduced in Senate

## Actions

- 2025-07-17 - IntroReferral: Introduced in Senate
- 2025-07-17 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-17",
    "latestAction": {
      "actionDate": "2025-07-17",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2353",
    "number": "2353",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "M001176",
        "district": "",
        "firstName": "Jeff",
        "fullName": "Sen. Merkley, Jeff [D-OR]",
        "lastName": "Merkley",
        "party": "D",
        "state": "OR"
      }
    ],
    "title": "Microplastics Safety Act",
    "type": "S",
    "updateDate": "2025-12-05T21:45:56Z",
    "updateDateIncludingText": "2025-12-05T21:45:56Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-17",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-17",
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
          "date": "2025-07-17T21:07:12Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
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
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-07-17",
      "state": "FL"
    },
    {
      "bioguideId": "B001303",
      "firstName": "Lisa",
      "fullName": "Sen. Blunt Rochester, Lisa [D-DE]",
      "isOriginalCosponsor": "False",
      "lastName": "Blunt Rochester",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "DE"
    },
    {
      "bioguideId": "M001244",
      "firstName": "Ashley",
      "fullName": "Sen. Moody, Ashley [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Moody",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2353is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2353\nIN THE SENATE OF THE UNITED STATES\nJuly 17, 2025 Mr. Merkley (for himself and Mr. Scott of Florida ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo direct the Secretary of Health and Human Services, acting through the Commissioner of Food and Drugs, to conduct a study, and submit to Congress a report, on the human health impacts of exposure to microplastics in food and water.\n#### 1. Short title\nThis Act may be cited as the Microplastics Safety Act .\n#### 2. FDA study and report on human health impacts of exposure to microplastics in food and water\n##### (a) Study\nThe Secretary of Health and Human Services, acting through the Commissioner of Food and Drugs (in this section referred to as the Secretary ), shall conduct a study on the human health impacts of exposure to microplastics in food and water. The study shall\u2014\n**(1)**\nidentify the major pathways of human exposure to microplastics;\n**(2)**\naddress the impact of such exposure on\u2014\n**(A)**\nchildren\u2019s health;\n**(B)**\nthe endocrine system;\n**(C)**\ncancer;\n**(D)**\nchronic illness; and\n**(E)**\nreproductive health; and\n**(3)**\naddress such other areas of importance as the Secretary determines appropriate.\n##### (b) Report\nNot later than 1 year after the date of enactment of this Act, the Secretary shall submit to Congress a report that describes\u2014\n**(1)**\nthe findings and conclusions of the study under subsection (a); and\n**(2)**\nrecommendations for legislative or administrative action to address the human health impacts of exposure to microplastics in food and water.",
      "versionDate": "2025-07-17",
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
        "actionDate": "2025-07-17",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "4486",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Microplastics Safety Act",
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
        "name": "Health",
        "updateDate": "2025-09-05T15:11:15Z"
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
      "date": "2025-07-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2353is.xml"
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
      "title": "Microplastics Safety Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-01T11:03:12Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Microplastics Safety Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-01T03:53:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to direct the Secretary of Health and Human Services, acting through the Commissioner of Food and Drugs, to conduct a study, and submit to Congress a report, on the human health impacts of exposure to microplastics in food and water.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-01T03:48:25Z"
    }
  ]
}
```
