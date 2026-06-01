# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6899?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6899
- Title: CFTC Advisory Committee Improvement Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6899
- Origin chamber: House
- Introduced date: 2025-12-18
- Update date: 2026-05-22T08:08:31Z
- Update date including text: 2026-05-22T08:08:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-18: Introduced in House
- 2025-12-18 - IntroReferral: Introduced in House
- 2025-12-18 - IntroReferral: Introduced in House
- 2025-12-18 - IntroReferral: Referred to the House Committee on Agriculture.
- 2026-05-20 - Committee: Referred to the Subcommittee on Commodity Markets, Digital Assets, and Rural Development.
- Latest action: 2025-12-18: Introduced in House

## Actions

- 2025-12-18 - IntroReferral: Introduced in House
- 2025-12-18 - IntroReferral: Introduced in House
- 2025-12-18 - IntroReferral: Referred to the House Committee on Agriculture.
- 2026-05-20 - Committee: Referred to the Subcommittee on Commodity Markets, Digital Assets, and Rural Development.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-18",
    "latestAction": {
      "actionDate": "2025-12-18",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6899",
    "number": "6899",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "T000490",
        "district": "2",
        "firstName": "David",
        "fullName": "Rep. Taylor, David J. [R-OH-2]",
        "lastName": "Taylor",
        "party": "R",
        "state": "OH"
      }
    ],
    "title": "CFTC Advisory Committee Improvement Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-22T08:08:31Z",
    "updateDateIncludingText": "2026-05-22T08:08:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-20",
      "committees": {
        "item": {
          "name": "Commodity Markets, Digital Assets, and Rural Development Subcommittee",
          "systemCode": "hsag22"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Commodity Markets, Digital Assets, and Rural Development.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-18",
      "committees": {
        "item": {
          "name": "Agriculture Committee",
          "systemCode": "hsag00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Agriculture.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-18",
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
          "date": "2025-12-18T14:03:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-05-20T14:38:33Z",
              "name": "Referred to"
            }
          },
          "name": "Commodity Markets, Digital Assets, and Rural Development Subcommittee",
          "systemCode": "hsag22"
        }
      },
      "systemCode": "hsag00",
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
      "bioguideId": "B001313",
      "district": "11",
      "firstName": "Shontel",
      "fullName": "Rep. Brown, Shontel M. [D-OH-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Brown",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "OH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6899ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6899\nIN THE HOUSE OF REPRESENTATIVES\nDecember 18, 2025 Mr. Taylor (for himself and Ms. Brown ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo amend the Commodity Exchange Act to improve the administration of advisory committees at the Commodity Futures Trading Commission.\n#### 1. Short title\nThis Act may be cited as the CFTC Advisory Committee Improvement Act of 2025 .\n#### 2. Advisory committee changes\n##### (a) In general\nSection 2(a)(15) of the Commodity Exchange Act ( 7 U.S.C. 2(a)(15) ) is amended to read as follows:\n(15) Advisory committees (A) Establishment The Commission shall establish advisory committees to serve as vehicles for discussion and communication on matters related to the regulatory activities of the Commission. (B) Activities The activities of an advisory committee shall include the following: (i) to hold meetings at such intervals as necessary to carry out the functions of the advisory committee; and (ii) to submit to the Commission such reports and recommendations to the Commission (including minority views, if any) as the advisory committee deems appropriate. (C) Applicability of the Federal Advisory Committee Act An advisory committee established under this paragraph shall be subject to chapter 10 of title 5, United States Code. .\n##### (b) Existing advisory committees\nAn advisory committee that, as of the date of the enactment of this Act, had a charter established by the Commodity Futures Trading Commission, or that was established by section 2(a)(15) of the Commodity Exchange Act, as in effect before such date of enactment, may continue to operate in accordance with the charter or in accordance with such section, as so in effect, until the charter is renewed or September 30, 2026, whichever occurs first.",
      "versionDate": "2025-12-18",
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
        "name": "Finance and Financial Sector",
        "updateDate": "2026-01-22T16:04:57Z"
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
      "date": "2025-12-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6899ih.xml"
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
      "title": "CFTC Advisory Committee Improvement Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-21T11:08:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "CFTC Advisory Committee Improvement Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-21T11:08:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Commodity Exchange Act to improve the administration of advisory committees at the Commodity Futures Trading Commission.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-21T11:03:20Z"
    }
  ]
}
```
