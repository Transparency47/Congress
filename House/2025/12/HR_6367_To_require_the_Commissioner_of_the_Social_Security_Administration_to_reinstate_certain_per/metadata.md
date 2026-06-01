# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6367?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6367
- Title: Social Security Data Transparency Act
- Congress: 119
- Bill type: HR
- Bill number: 6367
- Origin chamber: House
- Introduced date: 2025-12-02
- Update date: 2026-01-05T16:07:04Z
- Update date including text: 2026-01-05T16:07:04Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-02: Introduced in House
- 2025-12-02 - IntroReferral: Introduced in House
- 2025-12-02 - IntroReferral: Introduced in House
- 2025-12-02 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-12-02: Introduced in House

## Actions

- 2025-12-02 - IntroReferral: Introduced in House
- 2025-12-02 - IntroReferral: Introduced in House
- 2025-12-02 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-02",
    "latestAction": {
      "actionDate": "2025-12-02",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6367",
    "number": "6367",
    "originChamber": "House",
    "policyArea": {
      "name": "Social Welfare"
    },
    "sponsors": [
      {
        "bioguideId": "S001226",
        "district": "6",
        "firstName": "Andrea",
        "fullName": "Rep. Salinas, Andrea [D-OR-6]",
        "lastName": "Salinas",
        "party": "D",
        "state": "OR"
      }
    ],
    "title": "Social Security Data Transparency Act",
    "type": "HR",
    "updateDate": "2026-01-05T16:07:04Z",
    "updateDateIncludingText": "2026-01-05T16:07:04Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-02",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Ways and Means.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-02",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-02",
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
          "date": "2025-12-02T15:02:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "bioguideId": "S001225",
      "district": "17",
      "firstName": "Eric",
      "fullName": "Rep. Sorensen, Eric [D-IL-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Sorensen",
      "party": "D",
      "sponsorshipDate": "2025-12-02",
      "state": "IL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6367ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6367\nIN THE HOUSE OF REPRESENTATIVES\nDecember 2, 2025 Ms. Salinas (for herself and Mr. Sorensen ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo require the Commissioner of the Social Security Administration to reinstate certain performance statistics on a publicly accessible website of the Social Security Administration, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Social Security Data Transparency Act .\n#### 2. Reinstating transparency of SSA operations\n##### (a) In general\nNot later than 90 days after the date of enactment of this Act, and on a monthly basis thereafter, the Commissioner of the Social Security Administration shall publish on a publicly accessible website of the Social Security Administration, for the most recent month the information is available, the following information:\n**(1) First contact resolution**\nThe percentage of claimant interactions that are resolved during the first contact with the Social Security Administration.\n**(2) Customer satisfaction**\nThe percentage of claimants satisfied by each service channel (such as in-person meetings, calls using the 800 number, or any other avenue in which the Social Security Administration assists claimants) operated by the Social Security Administration.\n**(3) 800 number**\nWith respect to the 800 number of the Social Security Administration, the\u2014\n**(A)**\ntotal customers served;\n**(B)**\naverage daily call volume;\n**(C)**\naverage call wait time;\n**(D)**\naverage callback wait time;\n**(E)**\naverage speed of answer;\n**(F)**\npercentage of callers that reach a representative;\n**(G)**\naverage service time;\n**(H)**\nagent busy rate; and\n**(I)**\npercentage of calls handled by callback.\n**(4) Old age and survivors benefits**\nWith respect to claims for a benefit under title II that is not a disability benefit under section 223, information measuring the\u2014\n**(A)**\npercentage of claimants who received benefits within 2 weeks of applying;\n**(B)**\naverage time to receive a benefit payment from the date an application is submitted;\n**(C)**\nbenefits claims approved or denied;\n**(D)**\nbenefits claims pending;\n**(E)**\npercentage of benefit claim appointments scheduled within 28 days of applying; and\n**(F)**\npercentage of claims filed online.\n**(5) Disability determination**\nInformation related to disability insurance benefit claims under section 223 of the Social Security Act ( 42 U.S.C. 423 ), including\u2014\n**(A)**\nthe average processing time of such claims;\n**(B)**\nthe average time to receive a benefit payment from the date an application is submitted;\n**(C)**\nthe number of initial determinations pending;\n**(D)**\nthe number of such claims received;\n**(E)**\nthe number of claims approved or denied;\n**(F)**\nthe percentage of appointments scheduled within 28 days of the claimant applying;\n**(G)**\nthe percentage of such claims filed online; and\n**(H)**\nprocessing times and percentage of such claims processed at the initial, reconsideration, and hearings levels.\n**(6) Disability decision reconsideration**\nInformation related to the processing time for appeals of denials of a disability determination, including\u2014\n**(A)**\nthe average processing time of an appeal; and\n**(B)**\nthe number of appeals filed and the number of decisions of such appeals.\n**(7) Hearing information**\nInformation related to hearings conducted after the initial decision and reconsideration of a disability determination, including\u2014\n**(A)**\nthe average time it takes for a claimant to have a hearing;\n**(B)**\nthe number of hearings conducted\u2014\n**(i)**\nin person;\n**(ii)**\nover the phone; or\n**(iii)**\nvirtually; and\n**(C)**\nthe number of hearings pending.\n##### (b) Live tracker requirement\nWith respect to the 800 number, the Social Security Administration shall publish and maintain on a publicly accessible website of the Administration a live tracker that displays the\u2014\n**(1)**\ncall wait time;\n**(2)**\ncallback wait time;\n**(3)**\nnumber of callers on hold; and\n**(4)**\nnumber of callers waiting for a callback.\n##### (c) System outages\nNot later than 90 days after the date of enactment of this Act, and on a monthly basis thereafter, the Commissioner shall publish on a publicly accessible website of the Social Security Administration information regarding the number of system outages that result in Social Security Administration staff being unable to perform their job functions.\n##### (d) 800 number\nIn this Act, the term 800 number means the toll-free national number of the Social Security Administration, or any successor telephone number.",
      "versionDate": "2025-12-02",
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
        "name": "Social Welfare",
        "updateDate": "2026-01-05T16:07:04Z"
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
      "date": "2025-12-02",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6367ih.xml"
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
      "title": "To require the Commissioner of the Social Security Administration to reinstate certain performance statistics on a publicly accessible website of the Social Security Administration, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-19T07:58:43Z"
    },
    {
      "title": "Social Security Data Transparency Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-19T05:38:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Social Security Data Transparency Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-19T05:38:19Z"
    }
  ]
}
```
