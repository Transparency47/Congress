# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5045?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5045
- Title: HEALTH AI Act
- Congress: 119
- Bill type: HR
- Bill number: 5045
- Origin chamber: House
- Introduced date: 2025-08-26
- Update date: 2025-09-19T17:13:00Z
- Update date including text: 2025-09-19T17:13:00Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-08-26: Introduced in House
- 2025-08-26 - IntroReferral: Introduced in House
- 2025-08-26 - IntroReferral: Introduced in House
- 2025-08-26 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-08-26: Introduced in House

## Actions

- 2025-08-26 - IntroReferral: Introduced in House
- 2025-08-26 - IntroReferral: Introduced in House
- 2025-08-26 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-08-26",
    "latestAction": {
      "actionDate": "2025-08-26",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5045",
    "number": "5045",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "L000582",
        "district": "36",
        "firstName": "Ted",
        "fullName": "Rep. Lieu, Ted [D-CA-36]",
        "lastName": "Lieu",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "HEALTH AI Act",
    "type": "HR",
    "updateDate": "2025-09-19T17:13:00Z",
    "updateDateIncludingText": "2025-09-19T17:13:00Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-08-26",
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
      "actionDate": "2025-08-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-08-26",
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
          "date": "2025-08-26T15:01:40Z",
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
      "bioguideId": "B001287",
      "district": "6",
      "firstName": "Ami",
      "fullName": "Rep. Bera, Ami [D-CA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Bera",
      "party": "D",
      "sponsorshipDate": "2025-08-26",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5045ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5045\nIN THE HOUSE OF REPRESENTATIVES\nAugust 26, 2025 Mr. Lieu (for himself and Mr. Bera ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo direct the Secretary of Health and Human Services to establish a grant program to facilitate research regarding the use of generative artificial intelligence in health care, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Healthcare Enhancement And Learning Through Harnessing Artificial Intelligence Act or the HEALTH AI Act .\n#### 2. Grants to perform research regarding the use of generative artificial intelligence in health care\n##### (a) In general\nThe Secretary of Health and Human Services shall establish a grant program to award grants to eligible entities to perform research regarding the use of generative artificial intelligence in health care.\n##### (b) Permissible research\nResearch funded pursuant to a grant under this section may include research regarding the use of generative artificial intelligence to\u2014\n**(1)**\nimprove the ability of health care practitioners to record comprehensive notes or ask medically relevant questions during an appointment with a patient;\n**(2)**\nreduce the administrative or documentation burden on clinicians;\n**(3)**\nexpedite the health insurance claims process;\n**(4)**\nimprove the efficiency and quality of customer service in the health care sector; or\n**(5)**\notherwise improve health care, as determined appropriate by the Secretary.\n##### (c) Priority\nIn awarding grants under this section, the Secretary shall give priority to eligible entities that\u2014\n**(1)**\nencourage the adoption and deployment of generative artificial intelligence across the health care sector;\n**(2)**\ninvest in workforce development of clinicians and administrators;\n**(3)**\nmitigate burnout in the health care workforce;\n**(4)**\nreduce gender, racial, and ethnic disparities in health outcomes; or\n**(5)**\nimprove the availability of patient care for members of a medically underserved population.\n##### (d) Definitions\nIn this section:\n**(1) Artificial intelligence**\nThe term artificial intelligence has the meaning given such term in section 5002 of the National Artificial Intelligence Initiative Act of 2020 ( 15 U.S.C. 9401 ).\n**(2) Eligible entity**\nThe term eligible entity means\u2014\n**(A)**\nan institution of higher education (as defined in section 101 of the Higher Education Act of 1965 ( 20 U.S.C. 1001 ));\n**(B)**\nan organization described in section 501(c)(3) of the Internal Revenue Code of 1986 ( 26 U.S.C. 501(c)(3) ) and exempt from tax under section 501(a) of such Code; and\n**(C)**\nan agency of\u2014\n**(i)**\nthe Federal Government;\n**(ii)**\na State;\n**(iii)**\na unit of local government; or\n**(iv)**\nan Indian Tribe.\n**(3) Generative artificial intelligence**\nThe term generative artificial intelligence means artificial intelligence that, in response to a prompt, uses data to produce text, media, computer code, or other content.\n**(4) Medically underserved population**\nThe term medically underserved population has the meaning given such term in section 330(b) of the Public Health Service Act ( 42 U.S.C. 254b(b) ).\n**(5) Secretary**\nThe term Secretary means the Secretary of Health and Human Services.",
      "versionDate": "2025-08-26",
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
        "name": "Health",
        "updateDate": "2025-09-19T17:13:00Z"
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
      "date": "2025-08-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5045ih.xml"
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
      "title": "HEALTH AI Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-28T02:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "HEALTH AI Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-28T02:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Healthcare Enhancement And Learning Through Harnessing Artificial Intelligence Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-28T02:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Health and Human Services to establish a grant program to facilitate research regarding the use of generative artificial intelligence in health care, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-28T02:48:18Z"
    }
  ]
}
```
