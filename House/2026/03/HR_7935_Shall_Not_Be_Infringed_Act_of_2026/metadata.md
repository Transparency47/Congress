# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7935?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7935
- Title: Shall Not Be Infringed Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 7935
- Origin chamber: House
- Introduced date: 2026-03-16
- Update date: 2026-04-02T19:19:30Z
- Update date including text: 2026-04-02T19:19:30Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-16: Introduced in House
- 2026-03-16 - IntroReferral: Introduced in House
- 2026-03-16 - IntroReferral: Introduced in House
- 2026-03-16 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2026-03-16: Introduced in House

## Actions

- 2026-03-16 - IntroReferral: Introduced in House
- 2026-03-16 - IntroReferral: Introduced in House
- 2026-03-16 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-16",
    "latestAction": {
      "actionDate": "2026-03-16",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7935",
    "number": "7935",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "M001239",
        "district": "5",
        "firstName": "John",
        "fullName": "Rep. McGuire, John J. [R-VA-5]",
        "lastName": "McGuire",
        "party": "R",
        "state": "VA"
      }
    ],
    "title": "Shall Not Be Infringed Act of 2026",
    "type": "HR",
    "updateDate": "2026-04-02T19:19:30Z",
    "updateDateIncludingText": "2026-04-02T19:19:30Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-16",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-03-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-16",
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
          "date": "2026-03-16T16:00:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "H001101",
      "district": "10",
      "firstName": "Pat",
      "fullName": "Rep. Harrigan, Pat [R-NC-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Harrigan",
      "party": "R",
      "sponsorshipDate": "2026-03-26",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7935ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7935\nIN THE HOUSE OF REPRESENTATIVES\nMarch 16, 2026 Mr. McGuire introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo provide for a cause of action enabling recovery of any person harmed by the limitation on ability to carry a firearm in a different jurisdiction.\n#### 1. Short title\nThis Act may be cited as the Shall Not Be Infringed Act of 2026 .\n#### 2. Gun free zone policy requirement pertaining to eligibility for Byrne-JAG funding\n##### (a) Gun free zone policy requirement\nFor each fiscal year after the expiration of the period specified in subsection (b) in which a State or unit of local government receives a grant under part E of title I of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10151 et seq. ), the State or unit of local government shall conform its laws and policies to the following:\n**(1)**\nIf the State or unit of local government has in effect any law providing for a gun free zone, then in the case of any person\u2014\n**(A)**\nwho is harmed by the use of a firearm by another,\n**(B)**\nsuch harm occurs in a gun free zone,\n**(C)**\nwho is authorized to carry a firearm in that person\u2019s State of residence, and\n**(D)**\nthe person harmed could, if allowed to carry a firearm, have averted or mitigated such harm,\nsuch person may recover, in a civil action against the State or unit of local government, compensatory damages and damages for pain and suffering.\n**(2)**\nThe term gun free zone means any geographical area where the carrying of a firearm is prohibited under Federal, State, or local law by a member of the public.\n##### (b) Compliance and ineligibility\n**(1) Compliance date**\nThe period specified in this subsection is the period beginning on the first full fiscal year after the date of enactment of this Act.\n**(2) Ineligibility for funds**\nFor any fiscal year after the expiration of the period specified in paragraph (1), a State or unit of local government that fails to comply with subsection (a), shall be subject to a reduction of not more than 99 percent of the funds that would otherwise be allocated for that fiscal year to the State or unit of local government under subpart 1 of part E of title I of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10151 et seq. ), whether characterized as the Edward Byrne Memorial State and Local Law Enforcement Assistance Programs, the Local Government Law Enforcement Block Grants Program, the Edward Byrne Memorial Justice Assistance Grant Program, or otherwise.\n##### (c) Reallocation\nAmounts not allocated under a program referred to in subsection (b)(2) to a State for failure to fully comply with subsection (a) shall be reallocated under that program to States that have not failed to comply with such subsection.\n#### 3. Gun free zone policy requirement pertaining to eligibility for COPS funding\nFor each fiscal year after the expiration of the period specified in section 2(b) in which a State or unit of local government receives a grant under part Q of title I of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10151 et seq. ), the State or unit of local government shall conform its laws and policies to the requirement in section 2(a). For any fiscal year after the expiration of the period specified in section 2(b)(1), a State or unit of local government that fails to comply with this section, shall be subject to a reduction of not more than 99 percent of the funds that would otherwise be allocated for that fiscal year to the State or unit of local government.\n#### 4. Definitions\nTerms used in this Act have the meanings given such terms in section 901 of title I of the Omnibus Crime Control and Safe Streets Act of 1968.",
      "versionDate": "2026-03-16",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2026-04-02T19:19:30Z"
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
      "date": "2026-03-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7935ih.xml"
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
      "title": "Shall Not Be Infringed Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-01T07:23:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Shall Not Be Infringed Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-01T07:23:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide for a cause of action enabling recovery of any person harmed by the limitation on ability to carry a firearm in a different jurisdiction.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-01T07:18:25Z"
    }
  ]
}
```
