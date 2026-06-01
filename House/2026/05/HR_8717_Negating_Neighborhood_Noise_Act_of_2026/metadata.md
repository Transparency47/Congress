# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8717?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8717
- Title: Negating Neighborhood Noise Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 8717
- Origin chamber: House
- Introduced date: 2026-05-07
- Update date: 2026-05-21T19:56:36Z
- Update date including text: 2026-05-21T19:56:36Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-05-07: Introduced in House
- 2026-05-07 - IntroReferral: Introduced in House
- 2026-05-07 - IntroReferral: Introduced in House
- 2026-05-07 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- Latest action: 2026-05-07: Introduced in House

## Actions

- 2026-05-07 - IntroReferral: Introduced in House
- 2026-05-07 - IntroReferral: Introduced in House
- 2026-05-07 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-07",
    "latestAction": {
      "actionDate": "2026-05-07",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8717",
    "number": "8717",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "W000788",
        "district": "5",
        "firstName": "Nikema",
        "fullName": "Rep. Williams, Nikema [D-GA-5]",
        "lastName": "Williams",
        "party": "D",
        "state": "GA"
      }
    ],
    "title": "Negating Neighborhood Noise Act of 2026",
    "type": "HR",
    "updateDate": "2026-05-21T19:56:36Z",
    "updateDateIncludingText": "2026-05-21T19:56:36Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-07",
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
      "text": "Referred to the House Committee on Transportation and Infrastructure.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-05-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-05-07",
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
          "date": "2026-05-07T13:08:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "systemCode": "hspw00",
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
      "bioguideId": "H001047",
      "district": "4",
      "firstName": "James",
      "fullName": "Rep. Himes, James A. [D-CT-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Himes",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-05-07",
      "state": "CT"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2026-05-07",
      "state": "DC"
    },
    {
      "bioguideId": "C001117",
      "district": "6",
      "firstName": "Sean",
      "fullName": "Rep. Casten, Sean [D-IL-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Casten",
      "party": "D",
      "sponsorshipDate": "2026-05-07",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8717ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8717\nIN THE HOUSE OF REPRESENTATIVES\nMay 7, 2026 Ms. Williams of Georgia (for herself, Mr. Himes , Ms. Norton , and Mr. Casten ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo amend the National Highway System Designation Act of 1995 to permit the construction of certain noise barriers with funds from the Highway Trust Fund, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Negating Neighborhood Noise Act of 2026 .\n#### 2. Permitting use of highway trust fund for construction of certain noise barriers\nSection 339(b) of the National Highway System Designation Act of 1995 ( 23 U.S.C. 109 note) is amended to read as follows:\n(1) General rule No funds made available out of the Highway Trust Fund may be used to construct a Type II noise barrier (as defined by section 772.5 of title 23, Code of Federal Regulations) pursuant to subsections (h) and (i) of section 109 of title 23, United States Code. (2) Exceptions Paragraph (1) shall not apply to construction or preservation of a Type II noise barrier if such a barrier\u2014 (A) was not part of a project approved by the Secretary before November 28, 1995; (B) is proposed along lands that were developed or were under substantial construction before approval of the acquisition of the rights-of-ways for, or construction of, the existing highway; or (C) as determined and applied by the Secretary, separates a highway or other noise corridor from a group of structures of which the majority of such structures closest to the highway or noise corridor\u2014 (i) are residential in nature; and (ii) are at least 10 years old as of the date of the proposal of the barrier project. .\n#### 3. Eligibility for surface transportation block grant funds\nSection 133 of title 23, United States Code, is amended\u2014\n**(1)**\nin subsection (b) by adding at the end the following:\n(25) Planning, design, preservation, or construction of a Type II noise barrier (as described in section 772.5 of title 23, Code of Federal Regulations) and consistent with the requirements of section 339(b) of the National Highway System Designation Act of 1995 ( 23 U.S.C. 109 note). ; and\n**(2)**\nin subsection (c)(2) by striking and paragraph (23) and inserting , paragraph (23), and paragraph (25) .\n#### 4. Multipurpose noise barriers\n##### (a) In general\nThe Secretary of Transportation shall ensure that a noise barrier constructed or preserved under section 339(b) of the National Highway System Designation Act of 1995 ( 23 U.S.C. 109 note) or with funds made available under title 23, United States Code, may be a multipurpose noise barrier.\n##### (b) State approval\nA State, on behalf of the Secretary, may approve accommodation of a secondary beneficial use on a noise barrier within a right-of-way on a Federal-aid highway.\n##### (c) Definitions\n**(1) Multipurpose noise barrier**\nThe term multipurpose noise barrier means any noise barrier that provides a secondary beneficial use, including a barrier that hosts or accommodates renewable energy generation facilities, electrical transmission and distribution infrastructure, or broadband infrastructure and conduit.\n**(2) Secondary beneficial use**\nThe term secondary beneficial use means an environmental, economic, or social benefit in addition to highway noise mitigation.\n#### 5. Aesthetics\nA project sponsor constructing or preserving a noise barrier under section 339(b) of the National Highway System Designation Act of 1995 ( 23 U.S.C. 109 note) or with funds made available under title 23, United States Code, shall consider the aesthetics of the proposed noise barrier, consistent with the latest version of the Noise Barrier Design Handbook published by the Federal Highway Administration of the Department of Transportation.",
      "versionDate": "2026-05-07",
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
        "name": "Transportation and Public Works",
        "updateDate": "2026-05-21T19:56:35Z"
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
      "date": "2026-05-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8717ih.xml"
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
      "title": "Negating Neighborhood Noise Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-13T09:08:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Negating Neighborhood Noise Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-13T09:08:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the National Highway System Designation Act of 1995 to permit the construction of certain noise barriers with funds from the Highway Trust Fund, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-13T09:03:28Z"
    }
  ]
}
```
