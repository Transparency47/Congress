# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5501?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5501
- Title: Data Improvement for Puerto Rico Recovery Act
- Congress: 119
- Bill type: HR
- Bill number: 5501
- Origin chamber: House
- Introduced date: 2025-09-18
- Update date: 2025-11-18T16:55:49Z
- Update date including text: 2025-11-18T16:55:49Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-09-18: Introduced in House
- 2025-09-18 - IntroReferral: Introduced in House
- 2025-09-18 - IntroReferral: Introduced in House
- 2025-09-18 - IntroReferral: Referred to the House Committee on Natural Resources.
- Latest action: 2025-09-18: Introduced in House

## Actions

- 2025-09-18 - IntroReferral: Introduced in House
- 2025-09-18 - IntroReferral: Introduced in House
- 2025-09-18 - IntroReferral: Referred to the House Committee on Natural Resources.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-18",
    "latestAction": {
      "actionDate": "2025-09-18",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5501",
    "number": "5501",
    "originChamber": "House",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "V000081",
        "district": "7",
        "firstName": "Nydia",
        "fullName": "Rep. Vel\u00e1zquez, Nydia M. [D-NY-7]",
        "lastName": "Vel\u00e1zquez",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "Data Improvement for Puerto Rico Recovery Act",
    "type": "HR",
    "updateDate": "2025-11-18T16:55:49Z",
    "updateDateIncludingText": "2025-11-18T16:55:49Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-18",
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
      "actionDate": "2025-09-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-18",
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
          "date": "2025-09-18T14:05:15Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5501ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5501\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 18, 2025 Ms. Vel\u00e1zquez introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo require a study on the critical data gaps experienced by Federal agencies providing grants for the recovery of Puerto Rico.\n#### 1. Short title\nThis Act may be cited as the Data Improvement for Puerto Rico Recovery Act .\n#### 2. Study required\n##### (a) In general\nNot later than 1 year after the date of the enactment of this Act, the Comptroller General shall complete and submit to the appropriate congressional committees a report containing the results of a study on the specific data needs across grant-awarding agencies. The report shall contain the following:\n**(1)**\nA list of all grants provided by grant-awarding agencies to support Puerto Rico\u2019s recovery from Hurricanes Irma, Mar\u00eda, and Fiona, the 2020 earthquakes, and the COVID\u201319 pandemic. The list shall specify the grant type, amount, and the specific disaster or emergency to which it pertains.\n**(2)**\nAn assessment of statistical products that details the stages of the grant process at which statistical products were used, including\u2014\n**(A)**\nnotice of funding opportunity;\n**(B)**\ndevelopment;\n**(C)**\napplication review;\n**(D)**\naward selection;\n**(E)**\nformulation of terms and conditions; and\n**(F)**\ntechnical assistance.\n**(3)**\nAn evaluation of the most critical data needs identified by grant-awarding agencies in managing disaster-related grants for Puerto Rico, including issues related to lack of data coverage, disparities, reporting delays, and limitations in data reliability.\n**(4)**\nA description of the extent to which the identified data gaps have impeded effective grant allocation, management, and evaluation for Puerto Rico, including any specific examples where grant execution was hindered.\n**(5)**\nWhere applicable, a list of Federal products that currently exclude Puerto Rico, but which could improve grant processes if the Puerto Rico was included. The grant-awarding agencies shall provide recommendations on integrating Puerto Rico into such Federal products to enhance grant allocation and oversight.\n##### (b) Access to prompt and complete information\nAny Federal official from whom the Comptroller General seeks information for purposes of the report required by subsection (a) shall comprehensively respond to such request for information, not later than 90 days after the receipt of that request.\n##### (c) Definitions\nIn this Act:\n**(1) Appropriate congressional committees**\nThe term appropriate congressional committees means\u2014\n**(A)**\nthe Committee on National Resources of the House of Representatives; and\n**(B)**\nthe Committee on Energy and Natural Resources of the Senate.\n**(2) Grant-awarding agencies**\nThe term grant-awarding agencies means relevant agencies what have allocated, obligated, or disbursed recovery funds for Puerto Rico.\n**(3) Relevant agencies**\nThe term relevant agencies means the following:\n**(A)**\nEnvironmental Protection Agency.\n**(B)**\nFederal Communications Commission.\n**(C)**\nFederal Emergency Management Agency.\n**(D)**\nGeneral Services Administration.\n**(E)**\nNational Science Foundation.\n**(F)**\nSmall Business Administration.\n**(G)**\nArmy Corps of Engineers.\n**(H)**\nDepartment of Agriculture.\n**(I)**\nDepartment of Commerce, including the Economic Development Administration, Minority Business Development Agency.\n**(J)**\nNational Telecommunications and Information Administration.\n**(K)**\nNational Institute of Standards and Technology.\n**(L)**\nInternational Trade Administration.\n**(M)**\nNational Oceanic and Atmospheric Administration.\n**(N)**\nDepartment of Energy.\n**(O)**\nDepartment of Health and Human Services.\n**(P)**\nDepartment of Homeland Security.\n**(Q)**\nDepartment of Housing and Urban Development.\n**(R)**\nDepartment of Justice.\n**(S)**\nDepartment of Labor.\n**(T)**\nDepartment of the Interior.\n**(U)**\nDepartment of Transportation.\n**(V)**\nDepartment of Veterans Affairs.\n**(4) Statistical products**\nThe term statistical products means Federal statistical inputs, estimates, and products used by grant-awarding agencies to develop and manage grant funding.",
      "versionDate": "2025-09-18",
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
        "name": "Science, Technology, Communications",
        "updateDate": "2025-11-18T16:55:49Z"
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
      "date": "2025-09-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5501ih.xml"
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
      "title": "Data Improvement for Puerto Rico Recovery Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-03T04:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Data Improvement for Puerto Rico Recovery Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-03T04:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require a study on the critical data gaps experienced by Federal agencies providing grants for the recovery of Puerto Rico.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-03T04:18:14Z"
    }
  ]
}
```
