# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4947?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4947
- Title: No Discrimination in Farm Programs Act
- Congress: 119
- Bill type: HR
- Bill number: 4947
- Origin chamber: House
- Introduced date: 2025-08-12
- Update date: 2025-10-07T08:05:21Z
- Update date including text: 2025-10-07T08:05:21Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-08-12: Introduced in House
- 2025-08-12 - IntroReferral: Introduced in House
- 2025-08-12 - IntroReferral: Introduced in House
- 2025-08-12 - IntroReferral: Referred to the House Committee on Agriculture.
- Latest action: 2025-08-12: Introduced in House

## Actions

- 2025-08-12 - IntroReferral: Introduced in House
- 2025-08-12 - IntroReferral: Introduced in House
- 2025-08-12 - IntroReferral: Referred to the House Committee on Agriculture.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-08-12",
    "latestAction": {
      "actionDate": "2025-08-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4947",
    "number": "4947",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "A000375",
        "district": "19",
        "firstName": "Jodey",
        "fullName": "Rep. Arrington, Jodey C. [R-TX-19]",
        "lastName": "Arrington",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "No Discrimination in Farm Programs Act",
    "type": "HR",
    "updateDate": "2025-10-07T08:05:21Z",
    "updateDateIncludingText": "2025-10-07T08:05:21Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-08-12",
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
      "actionDate": "2025-08-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-08-12",
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
          "date": "2025-08-12T13:02:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "systemCode": "hsag00",
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
      "bioguideId": "P000605",
      "district": "10",
      "firstName": "Scott",
      "fullName": "Rep. Perry, Scott [R-PA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Perry",
      "party": "R",
      "sponsorshipDate": "2025-08-12",
      "state": "PA"
    },
    {
      "bioguideId": "A000379",
      "district": "4",
      "firstName": "Mark",
      "fullName": "Rep. Alford, Mark [R-MO-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Alford",
      "party": "R",
      "sponsorshipDate": "2025-08-12",
      "state": "MO"
    },
    {
      "bioguideId": "W000829",
      "district": "8",
      "firstName": "Tony",
      "fullName": "Rep. Wied, Tony [R-WI-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Wied",
      "party": "R",
      "sponsorshipDate": "2025-08-12",
      "state": "WI"
    },
    {
      "bioguideId": "R000619",
      "district": "6",
      "firstName": "Michael",
      "fullName": "Rep. Rulli, Michael A. [R-OH-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Rulli",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-08-12",
      "state": "OH"
    },
    {
      "bioguideId": "R000614",
      "district": "21",
      "firstName": "Chip",
      "fullName": "Rep. Roy, Chip [R-TX-21]",
      "isOriginalCosponsor": "False",
      "lastName": "Roy",
      "party": "R",
      "sponsorshipDate": "2025-08-26",
      "state": "TX"
    },
    {
      "bioguideId": "L000583",
      "district": "11",
      "firstName": "Barry",
      "fullName": "Rep. Loudermilk, Barry [R-GA-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Loudermilk",
      "party": "R",
      "sponsorshipDate": "2025-09-09",
      "state": "GA"
    },
    {
      "bioguideId": "H001102",
      "district": "8",
      "firstName": "Mark",
      "fullName": "Rep. Harris, Mark [R-NC-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2025-10-06",
      "state": "NC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4947ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4947\nIN THE HOUSE OF REPRESENTATIVES\nAugust 12, 2025 Mr. Arrington (for himself, Mr. Perry , Mr. Alford , Mr. Wied , and Mr. Rulli ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo prohibit the use of race-based or sex-based criteria in the administration of certain Department of Agriculture programs, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the No Discrimination in Farm Programs Act .\n#### 2. Prohibiting the use of race-based or sex-based criteria in the administration of certain Department of Agriculture programs\n##### (a) In general\nThe Secretary of Agriculture, with respect to covered programs\u2014\n**(1)**\nmay not apply race-based or sex-based criteria in the decision-making processes of the Secretary involved in administering such programs; and\n**(2)**\nshall ensure such programs are administered in a manner that upholds the principles of meritocracy, fairness, and equal opportunity for all participants.\n##### (b) Covered program defined\nIn this section, the term covered program means the following programs:\n**(1)**\nPandemic assistance programs designed to support agricultural producers impacted by the COVID\u201319 pandemic, including the Coronavirus Food Assistance Program and the Pandemic Assistance Revenue Program under part 9 of title 7, Code of Federal Regulations (or successor regulations).\n**(2)**\nThe Federal Crop Insurance program under the Federal Crop Insurance Act ( 7 U.S.C. 1501 et seq. ).\n**(3)**\nThe Wildlife Habitat Incentive Program under section 1240B(g) of the Food Security Act of 1985 ( 16 U.S.C. 3839aa\u20132(g) ).\n**(4)**\nIndemnity payment programs specified in part 760 of title 7, Code of Federal Regulations (or successor regulations).\n**(5)**\nFarm loan programs (including guaranteed farm loans and inventory property management) under the Consolidated Farm and Rural Development Act ( 7 U.S.C. 1921 et seq. ).\n**(6)**\nThe conservation reserve program established under subchapter B of chapter 1 of subtitle D of title XII of the Food Security Act of 1985 ( 16 U.S.C. 3801 et seq. ).\n**(7)**\nAgricultural management assistance provided under section 524 of the Federal Crop Insurance Act ( 7 U.S.C. 1524 ).\n**(8)**\nThe agricultural conservation easement program under subtitle H of the Food Security Act of 1985 ( 7 U.S.C. 3865 et seq. ), including wetlands reserve easements available through such program.\n**(9)**\nRural development programs under the Consolidated Farm and Rural Development Act ( 7 U.S.C. 1921 et seq. ).\n**(10)**\nLoans guarantee programs under section 306(a) of the Consolidated Farm and Rural Development Act ( 7 U.S.C. 1926(a) ), section 310B(a) of such Act ( 7 U.S.C. 1932(a) ), and section 9007 of the Farm Security and Rural Investment Act of 2002 ( 7 U.S.C. 8107 ).",
      "versionDate": "2025-08-12",
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
        "name": "Agriculture and Food",
        "updateDate": "2025-09-05T16:37:31Z"
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
      "date": "2025-08-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4947ih.xml"
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
      "title": "No Discrimination in Farm Programs Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-13T08:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "No Discrimination in Farm Programs Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-13T08:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit the use of race-based or sex-based criteria in the administration of certain Department of Agriculture programs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-13T08:18:20Z"
    }
  ]
}
```
