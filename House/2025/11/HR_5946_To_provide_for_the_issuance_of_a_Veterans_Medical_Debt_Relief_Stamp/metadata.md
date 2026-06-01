# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5946?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5946
- Title: Stamp Out Veterans Medical Debt Act
- Congress: 119
- Bill type: HR
- Bill number: 5946
- Origin chamber: House
- Introduced date: 2025-11-07
- Update date: 2025-12-10T09:06:19Z
- Update date including text: 2025-12-10T09:06:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-11-07: Introduced in House
- 2025-11-07 - IntroReferral: Introduced in House
- 2025-11-07 - IntroReferral: Introduced in House
- 2025-11-07 - IntroReferral: Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-11-07 - IntroReferral: Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-11-20 - Committee: Referred to the Subcommittee on Health.
- Latest action: 2025-11-07: Introduced in House

## Actions

- 2025-11-07 - IntroReferral: Introduced in House
- 2025-11-07 - IntroReferral: Introduced in House
- 2025-11-07 - IntroReferral: Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-11-07 - IntroReferral: Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-11-20 - Committee: Referred to the Subcommittee on Health.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5946",
    "number": "5946",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "F000474",
        "district": "1",
        "firstName": "Mike",
        "fullName": "Rep. Flood, Mike [R-NE-1]",
        "lastName": "Flood",
        "party": "R",
        "state": "NE"
      }
    ],
    "title": "Stamp Out Veterans Medical Debt Act",
    "type": "HR",
    "updateDate": "2025-12-10T09:06:19Z",
    "updateDateIncludingText": "2025-12-10T09:06:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-20",
      "committees": {
        "item": {
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Health.",
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
      "text": "Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-07",
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
      "text": "Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
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
          "date": "2025-11-07T19:06:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-11-20T18:34:32Z",
              "name": "Referred to"
            }
          },
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
        }
      },
      "systemCode": "hsvr00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-11-07T19:06:25Z",
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
      "bioguideId": "S001224",
      "district": "3",
      "firstName": "Keith",
      "fullName": "Rep. Self, Keith [R-TX-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Self",
      "party": "R",
      "sponsorshipDate": "2025-11-07",
      "state": "TX"
    },
    {
      "bioguideId": "S001172",
      "district": "3",
      "firstName": "Adrian",
      "fullName": "Rep. Smith, Adrian [R-NE-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Smith",
      "party": "R",
      "sponsorshipDate": "2025-11-12",
      "state": "NE"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5946ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5946\nIN THE HOUSE OF REPRESENTATIVES\nNovember 7, 2025 Mr. Flood (for himself and Mr. Self ) introduced the following bill; which was referred to the Committee on Oversight and Government Reform , and in addition to the Committee on Veterans' Affairs , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo provide for the issuance of a Veterans Medical Debt Relief Stamp.\n#### 1. Short title\nThis Act may be cited as the Stamp Out Veterans Medical Debt Act .\n#### 2. Veterans Medical Debt Relief Stamp\n##### (a) In general\nIn order to afford a convenient way for members of the public to contribute to funding to pay medical debt incurred by veterans for hospital care, medical services, and extended care services furnished by the Department of Veterans Affairs, including through the Community Care Program under section 1703 of title 38, United States Code, the United States Postal Service shall provide for the issuance and sale of a special postage stamp which shall be known as the Veterans Medical Debt Relief Stamp .\n##### (b) Terms and conditions\nThe issuance and sale of the Veterans Medical Debt Relief Stamp shall be governed by section 416 of title 39, United States Code, except that\u2014\n**(1)**\nall amounts becoming available from the sale of the stamp shall be transferred to the Department of Veterans Affairs in accordance with section 416(d) of such title; and\n**(2)**\nthe stamp\u2014\n**(A)**\nshall be issued in time for Veterans Day of each year;\n**(B)**\nshall bear such illustration, depiction, design, or other image as the United States Postal Service shall determine; and\n**(C)**\nshall not be subject to any numerical limitation under section 416(e)(1)(C) of such title.\n##### (c) Use of funds\nThe Secretary of Veterans Affairs shall disperse all amounts received by the Department of Veterans Affairs under subsection (b)(1) to the applicable Department offices (including the Veterans Health Administration, the Debt Management Center, the Financial Service Center, and the VHA Revenue Operations) for the purpose of paying down veteran medical debt incurred via unresolved copayment and coinsurance billings related to services furnished by the Department and the Community Care Program.",
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
        "updateDate": "2025-11-18T15:57:17Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5946ih.xml"
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
      "title": "Stamp Out Veterans Medical Debt Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-15T05:23:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Stamp Out Veterans Medical Debt Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-15T05:23:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide for the issuance of a Veterans Medical Debt Relief Stamp.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-15T05:18:14Z"
    }
  ]
}
```
