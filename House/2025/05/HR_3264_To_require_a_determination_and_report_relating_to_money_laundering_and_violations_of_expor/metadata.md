# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3264?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/3264
- Title: To require a determination and report relating to money laundering and violations of export controls and sanctions in Hong Kong.
- Congress: 119
- Bill type: HR
- Bill number: 3264
- Origin chamber: House
- Introduced date: 2025-05-07
- Update date: 2025-07-23T14:12:46Z
- Update date including text: 2025-07-23T14:12:46Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-07: Introduced in House
- 2025-05-07 - IntroReferral: Introduced in House
- 2025-05-07 - IntroReferral: Introduced in House
- 2025-05-07 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on Foreign Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-05-07 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on Foreign Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-05-07: Introduced in House

## Actions

- 2025-05-07 - IntroReferral: Introduced in House
- 2025-05-07 - IntroReferral: Introduced in House
- 2025-05-07 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on Foreign Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-05-07 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on Foreign Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-07",
    "latestAction": {
      "actionDate": "2025-05-07",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/3264",
    "number": "3264",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "W000795",
        "district": "2",
        "firstName": "Joe",
        "fullName": "Rep. Wilson, Joe [R-SC-2]",
        "lastName": "Wilson",
        "party": "R",
        "state": "SC"
      }
    ],
    "title": "To require a determination and report relating to money laundering and violations of export controls and sanctions in Hong Kong.",
    "type": "HR",
    "updateDate": "2025-07-23T14:12:46Z",
    "updateDateIncludingText": "2025-07-23T14:12:46Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-07",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Financial Services, and in addition to the Committee on Foreign Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-07",
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
      "text": "Referred to the Committee on Financial Services, and in addition to the Committee on Foreign Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-05-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-07",
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
          "date": "2025-05-07T14:00:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-05-07T14:00:20Z",
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
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2025-05-07",
      "state": "CA"
    },
    {
      "bioguideId": "S001201",
      "district": "3",
      "firstName": "Thomas",
      "fullName": "Rep. Suozzi, Thomas R. [D-NY-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Suozzi",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-06-09",
      "state": "NY"
    },
    {
      "bioguideId": "M001219",
      "district": "0",
      "firstName": "James",
      "fullName": "Del. Moylan, James C. [R-GU-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Moylan",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-07-21",
      "state": "GU"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3264ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3264\nIN THE HOUSE OF REPRESENTATIVES\nMay 7, 2025 Mr. Wilson of South Carolina (for himself and Mr. Panetta ) introduced the following bill; which was referred to the Committee on Financial Services , and in addition to the Committee on Foreign Affairs , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo require a determination and report relating to money laundering and violations of export controls and sanctions in Hong Kong.\n#### 1. Measures to address money laundering and export control and sanctions violations in Hong Kong\n##### (a) Determination with respect to money laundering\nNot later than 180 days after the date of the enactment of this Act, the Secretary of the Treasury shall submit to the appropriate congressional committees a determination, including a detailed justification, of whether reasonable grounds exist for concluding that the Hong Kong Special Administrative Region of the People\u2019s Republic of China should be designated as a jurisdiction of primary money laundering concern under section 5318A of title 31, United States Code.\n##### (b) Report on role of Hong Kong in export control and sanctions violations\n**(1) In general**\nNot later than 360 days after the date of the enactment of this Act, the Secretary of State, in coordination with the Secretary of the Treasury and the Secretary of Commerce, shall submit to the appropriate congressional committees a report assessing the ability of United States and foreign financial institutions operating in Hong Kong to identify and prevent transactions that facilitate the transfer of products, technology, and money to the Russian Federation, Iran, and other countries and entities in violation of export controls and sanctions imposed by the United States.\n**(2) Elements**\nThe report required by paragraph (1) include\u2014\n**(A)**\nan evaluation of the extent of the role of Hong Kong in facilitating the transfer of products and technologies to the Russian Federation, Iran, other countries that are adversaries of the United States, and the mainland of the People\u2019s Republic of China, in violation of export controls imposed by the United States;\n**(B)**\nan evaluation of the role of Hong Kong in facilitating trade and financial transactions that violate sanctions imposed by the United States on the Russian Federation, Iran, and other countries and entities;\n**(C)**\nan assessment of whether the National Security Law of Hong Kong has limited the ability of financial institutions to adhere to global standards for anti-money laundering and know-your-customer procedures; and\n**(D)**\na description of the level of co-operation between Hong Kong and United States authorities in enforcing export control and sanctions regimes.\n##### (c) Appropriate congressional committees defined\nIn this section, the term appropriate congressional committees means\u2014\n**(1)**\nthe Committee on Foreign Relations and the Committee on Banking, Housing, and Urban Affairs of the Senate; and\n**(2)**\nthe Committee on Foreign Affairs and the Committee on Financial Services of the House of Representatives.",
      "versionDate": "2025-05-07",
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
        "name": "International Affairs",
        "updateDate": "2025-06-10T14:35:13Z"
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
      "date": "2025-05-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3264ih.xml"
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
      "title": "To require a determination and report relating to money laundering and violations of export controls and sanctions in Hong Kong.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-23T14:12:46Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require a determination and report relating to money laundering and violations of export controls and sanctions in Hong Kong.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-15T06:12:48Z"
    }
  ]
}
```
