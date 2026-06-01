# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2428?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/2428
- Title: Wildfire Homeowner Relief Act
- Congress: 119
- Bill type: HR
- Bill number: 2428
- Origin chamber: House
- Introduced date: 2025-03-27
- Update date: 2025-07-23T14:12:24Z
- Update date including text: 2025-07-23T14:12:24Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-27: Introduced in House
- 2025-03-27 - IntroReferral: Introduced in House
- 2025-03-27 - IntroReferral: Introduced in House
- 2025-03-27 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-27 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-27 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.
- Latest action: 2025-03-27: Introduced in House

## Actions

- 2025-03-27 - IntroReferral: Introduced in House
- 2025-03-27 - IntroReferral: Introduced in House
- 2025-03-27 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-27 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-27 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-27",
    "latestAction": {
      "actionDate": "2025-03-27",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/2428",
    "number": "2428",
    "originChamber": "House",
    "policyArea": {
      "name": "Emergency Management"
    },
    "sponsors": [
      {
        "bioguideId": "F000483",
        "district": "30",
        "firstName": "Laura",
        "fullName": "Rep. Friedman, Laura [D-CA-30]",
        "lastName": "Friedman",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Wildfire Homeowner Relief Act",
    "type": "HR",
    "updateDate": "2025-07-23T14:12:24Z",
    "updateDateIncludingText": "2025-07-23T14:12:24Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-27",
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
      "actionCode": "H11100",
      "actionDate": "2025-03-27",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-27",
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
      "text": "Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-27",
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
          "date": "2025-03-27T13:02:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-03-27T21:09:54Z",
              "name": "Referred to"
            }
          },
          "name": "Economic Development, Public Buildings, and Emergency Management Subcommittee",
          "systemCode": "hspw13"
        }
      },
      "systemCode": "hspw00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-03-27T13:02:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
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
      "bioguideId": "B001285",
      "district": "26",
      "firstName": "Julia",
      "fullName": "Rep. Brownley, Julia [D-CA-26]",
      "isOriginalCosponsor": "True",
      "lastName": "Brownley",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "CA"
    },
    {
      "bioguideId": "L000582",
      "district": "36",
      "firstName": "Ted",
      "fullName": "Rep. Lieu, Ted [D-CA-36]",
      "isOriginalCosponsor": "True",
      "lastName": "Lieu",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "CA"
    },
    {
      "bioguideId": "M001225",
      "district": "15",
      "firstName": "Kevin",
      "fullName": "Rep. Mullin, Kevin [D-CA-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Mullin",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "CA"
    },
    {
      "bioguideId": "S000344",
      "district": "32",
      "firstName": "Brad",
      "fullName": "Rep. Sherman, Brad [D-CA-32]",
      "isOriginalCosponsor": "True",
      "lastName": "Sherman",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "CA"
    },
    {
      "bioguideId": "J000305",
      "district": "51",
      "firstName": "Sara",
      "fullName": "Rep. Jacobs, Sara [D-CA-51]",
      "isOriginalCosponsor": "False",
      "lastName": "Jacobs",
      "party": "D",
      "sponsorshipDate": "2025-07-21",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2428ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2428\nIN THE HOUSE OF REPRESENTATIVES\nMarch 27, 2025 Ms. Friedman (for herself, Ms. Brownley , Mr. Lieu , Mr. Mullin , and Mr. Sherman ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure , and in addition to the Committee on Financial Services , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo require the Comptroller General of the United States to conduct a study regarding a Federal buyout program available to homeowners with properties in high-risk catastrophic wildfire disaster areas, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Wildfire Homeowner Relief Act .\n#### 2. GAO study on a federal buyout program for high-risk wildfire areas\n##### (a) In general\nThe Comptroller General of the United States shall conduct a study to analyze the feasibility of using Federal grant programs to purchase property from homeowners, voluntarily selling such properties, before and after a catastrophic wildfire disaster.\n##### (b) Existing covered buyouts\nIn conducting the study under subsection (a), the Comptroller General shall compile recommendations on\u2014\n**(1)**\nhow to develop a national database on covered buyouts, existing on the date of enactment of this Act, with information on what grant program was used to purchase each respective property under such buyouts, what entity is responsible for maintaining such property, and any development on such property following the covered buyout; and\n**(2)**\nhow the Federal Emergency Management Agency and the Department of Housing and Urban Development can exchange information about any covered buyout in process as of the date of enactment of this Act.\n##### (c) New wildfire buyout program\nIn conducting the study under subsection (a) of this Act, the Comptroller General shall\u2014\n**(1)**\nanalyze how a program for the buyout of properties endangered or impacted by catastrophic wildfire disasters would compare to covered buyout programs existing on the date of enactment of this Act, including any floodplain disaster buyout programs;\n**(2)**\nprovide recommendations on which department, agency, or program should house a program for the buyout of properties endangered or impacted by catastrophic wildfire disasters; and\n**(3)**\nprovide land use recommendations for properties after a covered buyout, including\u2014\n**(A)**\nhow to ensure specific purchases and future land uses will reduce catastrophic wildfire risk, loss of life, and loss of property during catastrophic wildfires;\n**(B)**\nhow land use may be different for rural compared to urban communities and for disadvantaged compared to high-income communities;\n**(C)**\nhow to allow flexibility for communities to decide how to use the land following a covered buyout; and\n**(D)**\nwith respect to properties in high-risk areas prior to catastrophic wildfire disaster and for properties impacted after a catastrophic wildfire disaster, eligibility requirements, including\u2014\n**(i)**\nrecommendations for mapping which areas are at the highest risk for catastrophic wildfire; and\n**(ii)**\nmethodology for determining which areas would be most effective for implementing a Federal buyout program, including consideration for where the greatest benefit would be derived as a result of evacuating individuals in efforts to avoid loss of life.\n##### (d) Authority To define terms\nIn conducting the study under subsection (a), the Comptroller General shall develop definitions for the terms development , disadvantaged community , high-income community , and catastrophic wildfire .\n##### (e) Report\nNot later than 12 months after the date of enactment of this Act, the Comptroller General shall submit to Congress a report identifying findings and conclusions, including\u2014\n**(1)**\nthe results of the study conducted pursuant to subsection (a);\n**(2)**\nany recommendations made under subsection (b);\n**(3)**\nrecommendations on ways to incentivize participation in the program described in subsection (c);\n**(4)**\nanalysis of the economic impacts of the program described in subsection (c) and the cost of the program to the Federal Government; and\n**(5)**\nthe definitions developed under subsection (d).\n##### (f) Covered buyout defined\nIn this Act, a covered buyout means a purchase of property by the Federal Government from a homeowner who voluntarily sold such property because such property was recognized by the Federal Government to be in an area endangered or impacted by a catastrophic natural disaster.",
      "versionDate": "2025-03-27",
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
        "name": "Emergency Management",
        "updateDate": "2025-05-21T13:51:52Z"
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
      "date": "2025-03-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2428ih.xml"
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
      "title": "Wildfire Homeowner Relief Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-23T14:12:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Wildfire Homeowner Relief Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-04T05:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Comptroller General of the United States to conduct a study regarding a Federal buyout program available to homeowners with properties in high-risk catastrophic wildfire disaster areas, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-04T05:03:49Z"
    }
  ]
}
```
