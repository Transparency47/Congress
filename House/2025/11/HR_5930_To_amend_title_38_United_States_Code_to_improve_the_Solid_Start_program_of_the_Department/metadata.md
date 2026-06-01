# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5930?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5930
- Title: Veterans Transition Support Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 5930
- Origin chamber: House
- Introduced date: 2025-11-07
- Update date: 2026-01-08T09:06:39Z
- Update date including text: 2026-01-08T09:06:39Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-11-07: Introduced in House
- 2025-11-07 - IntroReferral: Introduced in House
- 2025-11-07 - IntroReferral: Introduced in House
- 2025-11-07 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-11-17 - Committee: Referred to the Subcommittee on Economic Opportunity.
- Latest action: 2025-11-07: Introduced in House

## Actions

- 2025-11-07 - IntroReferral: Introduced in House
- 2025-11-07 - IntroReferral: Introduced in House
- 2025-11-07 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-11-17 - Committee: Referred to the Subcommittee on Economic Opportunity.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-07",
    "latestAction": {
      "actionDate": "2025-11-07",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5930",
    "number": "5930",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "B001292",
        "district": "8",
        "firstName": "Donald",
        "fullName": "Rep. Beyer, Donald S. [D-VA-8]",
        "lastName": "Beyer",
        "party": "D",
        "state": "VA"
      }
    ],
    "title": "Veterans Transition Support Act of 2025",
    "type": "HR",
    "updateDate": "2026-01-08T09:06:39Z",
    "updateDateIncludingText": "2026-01-08T09:06:39Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-17",
      "committees": {
        "item": {
          "name": "Economic Opportunity Subcommittee",
          "systemCode": "hsvr10"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Economic Opportunity.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-07",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-11-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-07",
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
          "date": "2025-11-07T19:03:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-11-17T18:39:21Z",
              "name": "Referred to"
            }
          },
          "name": "Economic Opportunity Subcommittee",
          "systemCode": "hsvr10"
        }
      },
      "systemCode": "hsvr00",
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
      "bioguideId": "C001133",
      "district": "6",
      "firstName": "Juan",
      "fullName": "Rep. Ciscomani, Juan [R-AZ-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Ciscomani",
      "party": "R",
      "sponsorshipDate": "2025-11-07",
      "state": "AZ"
    },
    {
      "bioguideId": "M001220",
      "district": "3",
      "firstName": "Morgan",
      "fullName": "Rep. McGarvey, Morgan [D-KY-3]",
      "isOriginalCosponsor": "True",
      "lastName": "McGarvey",
      "party": "D",
      "sponsorshipDate": "2025-11-07",
      "state": "KY"
    },
    {
      "bioguideId": "S001230",
      "district": "10",
      "firstName": "Suhas",
      "fullName": "Rep. Subramanyam, Suhas [D-VA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Subramanyam",
      "party": "D",
      "sponsorshipDate": "2025-12-02",
      "state": "VA"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2026-01-07",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5930ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5930\nIN THE HOUSE OF REPRESENTATIVES\nNovember 7, 2025 Mr. Beyer (for himself, Mr. Ciscomani , and Mr. McGarvey ) introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to improve the Solid Start program of the Department of Veterans Affairs, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Veterans Transition Support Act of 2025 .\n#### 2. Outreach to members of the Armed Forces under the Solid Start program\n##### (a) In general\nSection 6320 of title 38, United States Code, is amended, in subsection (a)\u2014\n**(1)**\nin paragraph (1), by inserting members of the Armed Forces described in subsection (b) and after needs of ; and\n**(2)**\nin paragraph (2)\u2014\n**(A)**\nin the matter preceding subparagraph (A)\u2014\n**(i)**\nby inserting with the Department of Defense after coordinate efforts ; and\n**(ii)**\nby inserting such members of the Armed Forces and after to assist ;\n**(B)**\nin subparagraph (A), by inserting such members and after reach out to ; and\n**(C)**\nin subparagraph (B), by inserting such members and after to connect .\n##### (b) Activities of the Solid Start program\nSuch section is further amended, in subsection (b)(1)\u2014\n**(1)**\nin subparagraph (A), by inserting (with priority for members during the period between 120 and 210 days before separation) after separating from the Armed Forces ;\n**(2)**\nin subparagraph (D), by inserting such member's and after the needs of each ;\n**(3)**\nin subparagraph (E), by inserting such members and after prioritizing outreach to ;\n**(4)**\nin subparagraph (F), by inserting such members who are women and after providing ;\n**(5)**\nby redesignating subparagraphs (B) through (H) as subparagraphs (E) through (K), respectively; and\n**(6)**\nby inserting after subparagraph (A) the following new subparagraphs:\n(B) collecting suicide prevention policies, points of contact, and referral protocols of the Department of Defense to inform such members who are in crisis of such resources; (C) calling and speaking with each such member, regardless of separation type or characterization of service, at least one time not earlier than 210 days, and not later than 120 days, before the separation of such member from the Armed Forces\u2014 (i) to inform the member of the transitional health care available under section 1145 of title 10; and (ii) to provide to the member the contact information for\u2014 (I) the facility of the Department located closest to the member\u2019s permanent residence; and (II) a representative of an organization recognized by the Secretary under section 5902 of this title, or an agent or attorney recognized under section 5904 of this title, who may assist the member in compiling and filing the member\u2019s claim for disability compensation; (D) communicating with such members through other means (including text message or email)\u2014 (i) to schedule a call under subparagraph (C); or (ii) if calling a member under such subparagraph has not resulted in contact before exceeding the maximum number of call attempts as the Secretary may specify; .",
      "versionDate": "2025-11-07",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-11-25T18:55:47Z"
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
      "date": "2025-11-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5930ih.xml"
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
      "title": "Veterans Transition Support Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-14T06:38:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Veterans Transition Support Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-14T06:38:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 38, United States Code, to improve the Solid Start program of the Department of Veterans Affairs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-14T06:33:20Z"
    }
  ]
}
```
