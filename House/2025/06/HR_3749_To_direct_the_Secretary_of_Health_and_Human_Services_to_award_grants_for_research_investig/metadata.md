# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3749?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/3749
- Title: HER Act
- Congress: 119
- Bill type: HR
- Bill number: 3749
- Origin chamber: House
- Introduced date: 2025-06-05
- Update date: 2025-06-24T12:48:52Z
- Update date including text: 2025-06-24T12:48:52Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-05: Introduced in House
- 2025-06-05 - IntroReferral: Introduced in House
- 2025-06-05 - IntroReferral: Introduced in House
- 2025-06-05 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-06-05: Introduced in House

## Actions

- 2025-06-05 - IntroReferral: Introduced in House
- 2025-06-05 - IntroReferral: Introduced in House
- 2025-06-05 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-05",
    "latestAction": {
      "actionDate": "2025-06-05",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/3749",
    "number": "3749",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "B001313",
        "district": "11",
        "firstName": "Shontel",
        "fullName": "Rep. Brown, Shontel M. [D-OH-11]",
        "lastName": "Brown",
        "party": "D",
        "state": "OH"
      }
    ],
    "title": "HER Act",
    "type": "HR",
    "updateDate": "2025-06-24T12:48:52Z",
    "updateDateIncludingText": "2025-06-24T12:48:52Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-05",
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
      "actionDate": "2025-06-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-05",
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
          "date": "2025-06-05T14:00:15Z",
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
      "bioguideId": "M001229",
      "district": "10",
      "firstName": "LaMonica",
      "fullName": "Rep. McIver, LaMonica [D-NJ-10]",
      "isOriginalCosponsor": "True",
      "lastName": "McIver",
      "party": "D",
      "sponsorshipDate": "2025-06-05",
      "state": "NJ"
    },
    {
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2025-06-05",
      "state": "GA"
    },
    {
      "bioguideId": "P000617",
      "district": "7",
      "firstName": "Ayanna",
      "fullName": "Rep. Pressley, Ayanna [D-MA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Pressley",
      "party": "D",
      "sponsorshipDate": "2025-06-05",
      "state": "MA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3749ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3749\nIN THE HOUSE OF REPRESENTATIVES\nJune 5, 2025 Ms. Brown (for herself, Mrs. McIver , Mr. Johnson of Georgia , and Ms. Pressley ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo direct the Secretary of Health and Human Services to award grants for research, investigation, and awareness of the effect of personal care products containing endocrine-disrupting chemicals on the female reproductive system, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Health and Endocrine Research on personal care products for women Act or the HER Act .\n#### 2. Grants for research, investigation, and awareness regarding endocrine-disrupting chemicals in personal care products\n##### (a) Research grants\n**(1) In general**\nThe Secretary of Health and Human Services, acting through the Director of the National Institute of Environmental Health Sciences, shall award grants for research on the impact of personal care products containing endocrine-disrupting chemicals on the female reproductive system and related reproductive toxicity concerns.\n**(2) Reports**\nNot later than 5 years after the date of enactment of this Act, and every 5 years thereafter, the Secretary shall submit to the Congress, and make publicly available on the appropriate website of the Department of Health and Human Services, a report based on the results of the research under paragraph (1). Such report shall\u2014\n**(A)**\noutline research developments and findings related to disparities in access to safe non-endocrine-disrupting personal care products;\n**(B)**\nlist safe and harmful personal care products, as determined by the Secretary; and\n**(C)**\ninclude evidence-based or evidence-informed legislative or administrative strategies to increase the Food and Drug Administration\u2019s domain to regulate personal care product ingredients that are endocrine-disrupting chemicals that harm women\u2019s reproductive health.\n##### (b) State grants for investigation and awareness\n**(1) In general**\nThe Secretary shall award grants to States for carrying out\u2014\n**(A)**\nprograms to investigate the impact of personal care products containing endocrine-disrupting chemicals on women\u2019s reproductive health; and\n**(B)**\nprograms to develop and implement public awareness and education campaigns about the use of alternative personal care products that are less harmful to human health.\n**(2) Reports**\nNot later than 5 years after the initial awarding of grants under paragraph (1), and every 5 years thereafter, the Secretary shall submit to the Congress, and make publicly available on the appropriate website of the Department of Health and Human Services, a report summarizing the findings and results of the programs and activities funded through the grants under paragraph (1).\n##### (c) Definitions\nIn this section:\n**(1) Endocrine-disrupting chemical**\nThe term endocrine-disrupting chemical means a chemical that mimics, blocks, or interferes with the body\u2019s hormones.\n**(2) Personal care product**\nThe term personal care product means a product that\u2014\n**(A)**\nis a cosmetic (as defined in section 201 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 321 )); and\n**(B)**\nis intended to support the hygiene, grooming, or other personal care of the human body.\n**(3) Secretary**\nThe term Secretary means the Secretary of Health and Human Services.\n**(4) State**\nThe term State means\u2014\n**(A)**\neach of the several States, the District of Columbia, and the territories of the United States; and\n**(B)**\nan Indian Tribe or Tribal organization (as such terms are defined in section 4 of the Indian Self-Determination and Education Assistance Act ( 25 U.S.C. 5304 )).",
      "versionDate": "2025-06-05",
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
        "updateDate": "2025-06-24T12:48:52Z"
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
      "date": "2025-06-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3749ih.xml"
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
      "title": "HER Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-11T09:38:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "HER Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-11T09:38:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Health and Endocrine Research on personal care products for women Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-11T09:38:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Health and Human Services to award grants for research, investigation, and awareness of the effect of personal care products containing endocrine-disrupting chemicals on the female reproductive system, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-11T09:33:24Z"
    }
  ]
}
```
