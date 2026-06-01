# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4094?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4094
- Title: Electronic Consent Accountability Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 4094
- Origin chamber: House
- Introduced date: 2025-06-24
- Update date: 2025-10-04T08:05:43Z
- Update date including text: 2025-10-04T08:05:43Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-24: Introduced in House
- 2025-06-24 - IntroReferral: Introduced in House
- 2025-06-24 - IntroReferral: Introduced in House
- 2025-06-24 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- Latest action: 2025-06-24: Introduced in House

## Actions

- 2025-06-24 - IntroReferral: Introduced in House
- 2025-06-24 - IntroReferral: Introduced in House
- 2025-06-24 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-24",
    "latestAction": {
      "actionDate": "2025-06-24",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4094",
    "number": "4094",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
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
    "title": "Electronic Consent Accountability Act of 2025",
    "type": "HR",
    "updateDate": "2025-10-04T08:05:43Z",
    "updateDateIncludingText": "2025-10-04T08:05:43Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-24",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Oversight and Government Reform.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-06-24",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-24",
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
          "date": "2025-06-24T14:00:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Oversight and Government Reform Committee",
      "systemCode": "hsgo00",
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
      "bioguideId": "M000194",
      "district": "1",
      "firstName": "Nancy",
      "fullName": "Rep. Mace, Nancy [R-SC-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Mace",
      "party": "R",
      "sponsorshipDate": "2025-06-24",
      "state": "SC"
    },
    {
      "bioguideId": "N000193",
      "district": "3",
      "firstName": "Zachary",
      "fullName": "Rep. Nunn, Zachary [R-IA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Nunn",
      "party": "R",
      "sponsorshipDate": "2025-10-03",
      "state": "IA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4094ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4094\nIN THE HOUSE OF REPRESENTATIVES\nJune 24, 2025 Ms. Brown (for herself and Ms. Mace ) introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo direct certain Federal agencies to report to Congress on whether such agencies have implemented guidance from the Office of Management and Budget with respect to the disclosure of personal information, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Electronic Consent Accountability Act of 2025 .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nThe Government Accountability Office reports that Federal agencies need to fully implement Office of Management and Budget guidance and requirements related to the disclosure of personal information.\n**(2)**\nThe Creating Advanced Streamlined Electronic Services for Constituents Act of 2019 (CASES Act; Public Law 116\u201350 ) required the Office of Management and Budget to issue guidance to Federal agencies that requires\u2014\n**(A)**\nacceptance of electronic identity proofing and authentication;\n**(B)**\ncreation of a template for electronic consent and access forms to be posted on the websites of such agencies; and\n**(C)**\nacceptance of electronic consent from individuals after the identification of such individuals has been properly authenticated.\n**(3)**\nOn November 12, 2020, the Office of Management and Budget issued guidance in the memorandum of the Office of Management and Budget designated M\u201321\u201304 that included the required elements described in the CASES Act.\n**(4)**\nFederal agencies were instructed to implement the requirements described in such guidance by November 2021.\n#### 3. Report to Congress on implementation of guidance\n##### (a) In general\nNot later than 120 days after the date of the enactment of this Act, the head of each agency specified in subsection (b) shall submit to the Committee on Oversight and Government Reform of the House of Representatives a report that includes\u2014\n**(1)**\nwhether such head has implemented the covered responsibilities; and\n**(2)**\nif such head has not implemented the covered responsibilities\u2014\n**(A)**\na justification for why such head has not implemented such responsibilities;\n**(B)**\nthe planned timeline for such head to implement such responsibilities; and\n**(C)**\nthe steps such head is taking to implement such responsibilities.\n##### (b) Specified agencies\nThe agencies specified in this subsection are the following:\n**(1)**\nThe Department of Agriculture.\n**(2)**\nThe Department of Defense.\n**(3)**\nThe Department of Health and Human Services.\n**(4)**\nThe Department of Homeland Security.\n**(5)**\nThe Department of the Interior.\n**(6)**\nThe Department of Justice.\n**(7)**\nThe Department of Labor.\n**(8)**\nThe Department of State.\n**(9)**\nThe Department of Transportation.\n**(10)**\nThe Department of the Treasury.\n**(11)**\nThe Department of Veterans Affairs.\n**(12)**\nThe Environmental Protection Agency.\n**(13)**\nThe Equal Employment Opportunity Commission.\n**(14)**\nThe National Archives and Records Administration.\n**(15)**\nThe Office of Personnel Management.\n**(16)**\nThe Social Security Administration.\n##### (c) Covered responsibilities defined\nIn this section, the term covered responsibilities means the agency responsibilities described in the memorandum of the Office of Management and Budget designated as M\u201321\u201304, relating to Modernizing Access to and Consent for Disclosure of Records Subject to the Privacy Act , and issued November 12, 2020.",
      "versionDate": "2025-06-24",
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
        "name": "Government Operations and Politics",
        "updateDate": "2025-07-09T15:30:34Z"
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
      "date": "2025-06-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4094ih.xml"
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
      "title": "Electronic Consent Accountability Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-08T07:23:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Electronic Consent Accountability Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-08T07:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct certain Federal agencies to report to Congress on whether such agencies have implemented guidance from the Office of Management and Budget with respect to the disclosure of personal information, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-08T07:19:03Z"
    }
  ]
}
```
