# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2618?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2618
- Title: MORE USDA Grants Act
- Congress: 119
- Bill type: S
- Bill number: 2618
- Origin chamber: Senate
- Introduced date: 2025-07-31
- Update date: 2025-09-05T17:10:03Z
- Update date including text: 2025-09-05T17:10:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-31: Introduced in Senate
- 2025-07-31 - IntroReferral: Introduced in Senate
- 2025-07-31 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.
- Latest action: 2025-07-31: Introduced in Senate

## Actions

- 2025-07-31 - IntroReferral: Introduced in Senate
- 2025-07-31 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-31",
    "latestAction": {
      "actionDate": "2025-07-31",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2618",
    "number": "2618",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "C001113",
        "district": "",
        "firstName": "Catherine",
        "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
        "lastName": "Cortez Masto",
        "party": "D",
        "state": "NV"
      }
    ],
    "title": "MORE USDA Grants Act",
    "type": "S",
    "updateDate": "2025-09-05T17:10:03Z",
    "updateDateIncludingText": "2025-09-05T17:10:03Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-31",
      "committees": {
        "item": {
          "name": "Agriculture, Nutrition, and Forestry Committee",
          "systemCode": "ssaf00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-31",
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
          "date": "2025-07-31T19:46:48Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Agriculture, Nutrition, and Forestry Committee",
      "systemCode": "ssaf00",
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
      "bioguideId": "D000618",
      "firstName": "Steve",
      "fullName": "Sen. Daines, Steve [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Daines",
      "party": "R",
      "sponsorshipDate": "2025-07-31",
      "state": "MT"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-07-31",
      "state": "CA"
    },
    {
      "bioguideId": "C000880",
      "firstName": "Mike",
      "fullName": "Sen. Crapo, Mike [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Crapo",
      "party": "R",
      "sponsorshipDate": "2025-07-31",
      "state": "ID"
    },
    {
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-07-31",
      "state": "ID"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2618is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2618\nIN THE SENATE OF THE UNITED STATES\nJuly 31, 2025 Ms. Cortez Masto (for herself, Mr. Daines , Mr. Schiff , Mr. Crapo , and Mr. Risch ) introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo improve the process for awarding grants under certain programs of the Department of Agriculture to certain counties in which the majority of land is owned or managed by the Federal Government and to other units of local government and Tribal governments in those counties, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the More Opportunities for Rural Economies from USDA Grants Act or the MORE USDA Grants Act .\n#### 2. Definitions\nIn this Act:\n**(1) High-Density Public Land County**\nThe term High-Density Public Land County means a county (or equivalent jurisdiction) of a State or territory of the United States\u2014\n**(A)**\nthat has a population of not more than 100,000 people, according to the most recent annual estimates of population by the Bureau of the Census; and\n**(B)**\nin which more than 50 percent of the land is owned or managed by the Federal Government.\n**(2) Qualifying grant program**\nThe term qualifying grant program means\u2014\n**(A)**\nthe Rural Business Development grant program established under section 310B(c) of the Consolidated Farm and Rural Development Act ( 7 U.S.C. 1932(c) );\n**(B)**\nthe community facilities grant program established under section 306(a)(19) of the Consolidated Farm and Rural Development Act ( 7 U.S.C. 1926(a)(19) );\n**(C)**\nthe Economic Impact Initiative grant program established under section 306(a)(20)(B) of the Consolidated Farm and Rural Development Act ( 7 U.S.C. 1926(a)(20)(B) );\n**(D)**\nthe Telemedicine and Distance Learning Services grant program established under chapter 1 of subtitle D of title XXIII of the Food, Agriculture, Conservation, and Trade Act of 1990 ( 7 U.S.C. 950aaa et seq. );\n**(E)**\nthe Community Connect Grant Program established under section 604 of the Rural Electrification Act of 1936 ( 7 U.S.C. 950bb\u20133 );\n**(F)**\nthe broadband loan and grant pilot program known as the Rural eConnectivity Pilot Program or the ReConnect Program , authorized under section 779 of division A of the Consolidated Appropriations Act, 2018 ( Public Law 115\u2013141 ; 132 Stat. 399);\n**(G)**\nany discretionary grant program of the Rural Business-Cooperative Service, the Rural Housing Service, the Rural Utilities Service, or any other rural development agency of the Department of Agriculture under which grants are awarded to\u2014\n**(i)**\ncounties;\n**(ii)**\nother units of local government; or\n**(iii)**\nTribal governments; and\n**(H)**\nany other discretionary grant program of the Department of Agriculture under which grants for rural development or energy are awarded to\u2014\n**(i)**\ncounties;\n**(ii)**\nother units of local government; or\n**(iii)**\nTribal governments.\n**(3) Secretary**\nThe term Secretary means the Secretary of Agriculture.\n**(4) Tribal government**\nThe term Tribal government means the recognized governing body of any Indian or Alaska Native tribe, band, nation, pueblo, village, community, component band, or component reservation, individually identified (including parenthetically) in the list published most recently as of the date of enactment of this Act pursuant to section 104 of the Federally Recognized Indian Tribe List Act of 1994 ( 25 U.S.C. 5131 ).\n#### 3. Grants\n##### (a) Reduction in local matching requirements\nNotwithstanding any other provision of law, with respect to a High-Density Public Land County and any unit of local government or Tribal government within a High-Density Public Land County, any requirement for local matching funds under a qualifying grant program shall be reduced by 50 percent.\n##### (b) Technical assistance\nOn request of a High-Density Public Land County or any unit of local government or Tribal government within a High-Density Public Land County, the Secretary shall provide additional technical assistance to the High-Density Public Land County, unit of local government, or Tribal government before and during the annual application period for each qualifying grant program.\n##### (c) Priority\n**(1) Application approval**\nIn approving applications for a qualifying grant program, the Secretary shall give priority to an application from a High-Density Public Land County, unit of local government within a High-Density Public Land County, or Tribal government within a High-Density Public Land County that has not received support under the qualifying grant program during the 10-year period preceding the date of the application.\n**(2) Technical assistance and other support**\nIn carrying out subsections (b) and (d), the Secretary may give priority to a Tribal government within a High-Density Public Land County.\n##### (d) Other support\nThe Secretary may provide additional support, as the Secretary determines to be appropriate, for a High-Density Public Land County or a unit of local government or Tribal government within a High-Density Public Land County, including by considering and, if appropriate, offering flexibility with respect to any requirement of, or barrier to applying for or receiving assistance under, a qualifying grant program if the requirement or barrier relates to\u2014\n**(1)**\nscoring criteria relating to numerical size and impact, such as the number of jobs created or the number of people served, which disadvantage small and isolated communities;\n**(2)**\nany requirement that an applicant for a qualifying grant program partner with other institutions, such as community colleges or foundations, which may not operate in the jurisdiction of the High-Density Public Land County, unit of local government, or Tribal government seeking assistance under the qualifying grant program;\n**(3)**\nany financial or cash-on-hand requirement that a High-Density Public Land County or a unit of local government or Tribal government within a High-Density Public Land County cannot meet for reasons other than any financial constraints to which the High-Density Public Land County, unit of local government, or Tribal government is subject; or\n**(4)**\nan overly complicated or overly technical application for a qualifying grant program that deters High-Density Public Land Counties or units of local government or Tribal governments within High-Density Public Land Counties from applying for the qualifying grant program.",
      "versionDate": "2025-07-31",
      "versionType": "Introduced in Senate"
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
        "updateDate": "2025-09-05T17:10:03Z"
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
      "date": "2025-07-31",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2618is.xml"
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
      "title": "MORE USDA Grants Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-13T03:23:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "MORE USDA Grants Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-13T03:23:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "More Opportunities for Rural Economies from USDA Grants Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-13T03:23:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to improve the process for awarding grants under certain programs of the Department of Agriculture to certain counties in which the majority of land is owned or managed by the Federal Government and to other units of local government and Tribal governments in those counties, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-13T03:18:23Z"
    }
  ]
}
```
