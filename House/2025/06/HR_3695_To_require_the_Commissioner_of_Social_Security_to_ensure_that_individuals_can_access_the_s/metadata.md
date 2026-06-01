# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3695?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/3695
- Title: Social Security Access Act
- Congress: 119
- Bill type: HR
- Bill number: 3695
- Origin chamber: House
- Introduced date: 2025-06-03
- Update date: 2025-06-23T14:05:34Z
- Update date including text: 2025-06-23T14:05:34Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-03: Introduced in House
- 2025-06-03 - IntroReferral: Introduced in House
- 2025-06-03 - IntroReferral: Introduced in House
- 2025-06-03 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-06-03: Introduced in House

## Actions

- 2025-06-03 - IntroReferral: Introduced in House
- 2025-06-03 - IntroReferral: Introduced in House
- 2025-06-03 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-03",
    "latestAction": {
      "actionDate": "2025-06-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/3695",
    "number": "3695",
    "originChamber": "House",
    "policyArea": {
      "name": "Social Welfare"
    },
    "sponsors": [
      {
        "bioguideId": "R000622",
        "district": "19",
        "firstName": "Josh",
        "fullName": "Rep. Riley, Josh [D-NY-19]",
        "lastName": "Riley",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "Social Security Access Act",
    "type": "HR",
    "updateDate": "2025-06-23T14:05:34Z",
    "updateDateIncludingText": "2025-06-23T14:05:34Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-03",
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
      "actionDate": "2025-06-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-03",
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
          "date": "2025-06-03T16:00:20Z",
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
      "bioguideId": "V000133",
      "district": "2",
      "firstName": "Jefferson",
      "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Drew",
      "party": "R",
      "sponsorshipDate": "2025-06-03",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3695ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3695\nIN THE HOUSE OF REPRESENTATIVES\nJune 3, 2025 Mr. Riley of New York (for himself and Mr. Van Drew ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo require the Commissioner of Social Security to ensure that individuals can access the services of the Social Security Administration through a telephone service, an internet portal, and an in-person visit.\n#### 1. Short title\nThis Act may be cited as the Social Security Access Act .\n#### 2. Social security service channel options\n##### (a) Requirement for multiple service channel options\n**(1) In general**\nUpon the date of enactment of this Act, the Commissioner of Social Security shall ensure that individuals seeking services, submitting information, or applying for benefits under titles II or XVI of the Social Security Act are provided with the option of applying for such benefits or submitting information related to receiving such services or benefits to the Social Security Administration are able to seek services, submit information, or apply for such benefits through each of the following service channel options:\n**(A) Telephone access**\nA toll-free telephone service for direct assistance with inquiries, claims, and appeals related to the receipt of such services or benefits, including the ability to speak with a representative during standard business hours.\n**(B) Online access**\nAn internet-based portal to submit and track claims for such services or benefits, make inquiries, and receive updates on such claims and inquiries.\n**(C) In-person access**\nIn-person assistance at Social Security Administration field offices.\n**(2) Telephone service requirements**\nIn providing the telephone service required by paragraph (1)(A), the Commissioner shall ensure that the telephone service\u2014\n**(A)**\nis available in English, Spanish, and such other languages to meet the needs of the populations served, as determined by the Commissioner;\n**(B)**\nis made available to individuals in all geographic areas of the United States; and\n**(C)**\nhas in place the appropriate safeguards to ensure the security and identity of individuals using such telephone service.\n**(3) Telephone access for major account changes**\nNotwithstanding any subregulatory change or guidance issued by the Commissioner of Social Security, the Commissioner shall ensure that individuals are permitted to complete the following through the telephone service described in subsection (a)(1)(A):\n**(A) Complete application for social security benefits**\nInitiate and complete applications for any benefit under title II or title XVI of the Social Security Act.\n**(B) Direct deposit changes requirement**\nRequest and verify changes to direct deposit information.\n##### (b) Reports\n**(1) Initial report**\nNot later than 1 year after the date of enactment of this Act, the Comptroller General of the United States shall submit to Congress a report on the Social Security Administration\u2019s implementation of the requirements under subsection (a), including\u2014\n**(A)**\nthe effectiveness of each service channel described in subsection (a)(1) in meeting the customer service and benefit access needs of individuals;\n**(B)**\ndifficulties or barriers encountered by individuals in accessing the telephone service described in subsection (a)(1)(A);\n**(C)**\nsecurity measures taken by the Administration to protect the personal information of individuals using such telephone service; and\n**(D)**\nrecommendations for improving the implementation of the requirements under subsection (a).\n**(2) Annual report**\nNot later than 1 year after the report described in subparagraph (A) is submitted to Congress, and annually thereafter, the Commissioner shall submit to Congress a report on\u2014\n**(A)**\nthe number of individuals assisted through each service channel;\n**(B)**\nthe number of individuals who have used the telephone service described in subsection (a)(1)(A) for applications and major account changes;\n**(C)**\nthe average wait time for an individual to be assisted through such telephone service;\n**(D)**\nthe security measures in place to protect the personal information of individuals when using such telephone service;\n**(E)**\nany reported difficulties or barriers encountered by individuals in accessing such telephone service;\n**(F)**\nplans for improving such telephone service, if necessary;\n**(G)**\nthe effectiveness of each service channel option in meeting the customer service and benefit access needs of individuals; and\n**(H)**\nany additional measures taken to improve the accessibility or delivery of services.",
      "versionDate": "2025-06-03",
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
        "updateDate": "2025-06-23T14:05:34Z"
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
      "date": "2025-06-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3695ih.xml"
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
      "title": "Social Security Access Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-09T13:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Social Security Access Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-09T13:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Commissioner of Social Security to ensure that individuals can access the services of the Social Security Administration through a telephone service, an internet portal, and an in-person visit.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-09T13:18:23Z"
    }
  ]
}
```
