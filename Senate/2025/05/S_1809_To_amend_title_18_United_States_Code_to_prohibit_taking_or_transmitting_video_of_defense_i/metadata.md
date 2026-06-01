# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1809?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1809
- Title: Drone Espionage Act
- Congress: 119
- Bill type: S
- Bill number: 1809
- Origin chamber: Senate
- Introduced date: 2025-05-20
- Update date: 2026-04-13T15:35:24Z
- Update date including text: 2026-04-13T15:35:24Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-20: Introduced in Senate
- 2025-05-20 - IntroReferral: Introduced in Senate
- 2025-05-20 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- 2025-06-10 - Committee: Committee on Homeland Security and Governmental Affairs Subcommittee on Border Management, Federal Workforce, and Regulatory Affairs. Hearings held.
- 2026-02-05 - Committee: Committee on the Judiciary. Ordered to be reported without amendment favorably.
- 2026-02-09 - Committee: Committee on the Judiciary. Reported by Senator Grassley without amendment. Without written report.
- 2026-02-09 - Committee: Committee on the Judiciary. Reported by Senator Grassley without amendment. Without written report.
- 2026-02-09 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 316.
- Latest action: 2025-05-20: Introduced in Senate

## Actions

- 2025-05-20 - IntroReferral: Introduced in Senate
- 2025-05-20 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- 2025-06-10 - Committee: Committee on Homeland Security and Governmental Affairs Subcommittee on Border Management, Federal Workforce, and Regulatory Affairs. Hearings held.
- 2026-02-05 - Committee: Committee on the Judiciary. Ordered to be reported without amendment favorably.
- 2026-02-09 - Committee: Committee on the Judiciary. Reported by Senator Grassley without amendment. Without written report.
- 2026-02-09 - Committee: Committee on the Judiciary. Reported by Senator Grassley without amendment. Without written report.
- 2026-02-09 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 316.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-20",
    "latestAction": {
      "actionDate": "2025-05-20",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1809",
    "number": "1809",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "M001244",
        "district": "",
        "firstName": "Ashley",
        "fullName": "Sen. Moody, Ashley [R-FL]",
        "lastName": "Moody",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "Drone Espionage Act",
    "type": "S",
    "updateDate": "2026-04-13T15:35:24Z",
    "updateDateIncludingText": "2026-04-13T15:35:24Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-09",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 316.",
      "type": "Calendars"
    },
    {
      "actionDate": "2026-02-09",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on the Judiciary. Reported by Senator Grassley without amendment. Without written report.",
      "type": "Committee"
    },
    {
      "actionCode": "14000",
      "actionDate": "2026-02-09",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Committee on the Judiciary. Reported by Senator Grassley without amendment. Without written report.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-02-05",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on the Judiciary. Ordered to be reported without amendment favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-06-10",
      "committees": {
        "item": {
          "name": "Border Management, Federal Workforce, and Regulatory Affairs Subcommittee",
          "systemCode": "ssga22"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Homeland Security and Governmental Affairs Subcommittee on Border Management, Federal Workforce, and Regulatory Affairs. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-05-20",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-05-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
        "item": [
          {
            "date": "2026-02-09T23:38:23Z",
            "name": "Reported By"
          },
          {
            "date": "2026-02-05T15:15:00Z",
            "name": "Markup By"
          },
          {
            "date": "2025-05-20T14:59:55Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
      "type": "Standing"
    },
    {
      "chamber": "Senate",
      "name": "Homeland Security and Governmental Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-06-10T16:01:34Z",
              "name": "Hearings By (subcommittee)"
            }
          },
          "name": "Border Management, Federal Workforce, and Regulatory Affairs Subcommittee",
          "systemCode": "ssga22"
        }
      },
      "systemCode": "ssga00",
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
      "bioguideId": "C001095",
      "firstName": "Tom",
      "fullName": "Sen. Cotton, Tom [R-AR]",
      "isOriginalCosponsor": "True",
      "lastName": "Cotton",
      "party": "R",
      "sponsorshipDate": "2025-05-20",
      "state": "AR"
    },
    {
      "bioguideId": "L000577",
      "firstName": "Mike",
      "fullName": "Sen. Lee, Mike [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "party": "R",
      "sponsorshipDate": "2025-05-20",
      "state": "UT"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-05-20",
      "state": "NC"
    },
    {
      "bioguideId": "M001242",
      "firstName": "Bernie",
      "fullName": "Sen. Moreno, Bernie [R-OH]",
      "isOriginalCosponsor": "True",
      "lastName": "Moreno",
      "party": "R",
      "sponsorshipDate": "2025-05-20",
      "state": "OH"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-05-20",
      "state": "NC"
    },
    {
      "bioguideId": "S001208",
      "firstName": "Elissa",
      "fullName": "Sen. Slotkin, Elissa [D-MI]",
      "isOriginalCosponsor": "False",
      "lastName": "Slotkin",
      "party": "D",
      "sponsorshipDate": "2025-06-02",
      "state": "MI"
    },
    {
      "bioguideId": "W000437",
      "firstName": "Roger",
      "fullName": "Sen. Wicker, Roger F. [R-MS]",
      "isOriginalCosponsor": "False",
      "lastName": "Wicker",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-06-04",
      "state": "MS"
    },
    {
      "bioguideId": "C001098",
      "firstName": "Ted",
      "fullName": "Sen. Cruz, Ted [R-TX]",
      "isOriginalCosponsor": "False",
      "lastName": "Cruz",
      "party": "R",
      "sponsorshipDate": "2025-06-09",
      "state": "TX"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "False",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-06-10",
      "state": "TN"
    },
    {
      "bioguideId": "T000278",
      "firstName": "Tommy",
      "fullName": "Sen. Tuberville, Tommy [R-AL]",
      "isOriginalCosponsor": "False",
      "lastName": "Tuberville",
      "party": "R",
      "sponsorshipDate": "2025-07-14",
      "state": "AL"
    },
    {
      "bioguideId": "M001190",
      "firstName": "Markwayne",
      "fullName": "Sen. Mullin, Markwayne [R-OK]",
      "isOriginalCosponsor": "False",
      "lastName": "Mullin",
      "party": "R",
      "sponsorshipDate": "2025-07-22",
      "state": "OK"
    },
    {
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "False",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2025-07-28",
      "state": "AL"
    },
    {
      "bioguideId": "M001243",
      "firstName": "David",
      "fullName": "Sen. McCormick, David [R-PA]",
      "isOriginalCosponsor": "False",
      "lastName": "McCormick",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-11-18",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1809is.xml",
      "text": "119th CONGRESS\n1st Session\nS. 1809\nIN THE SENATE OF THE UNITED STATES\nMay 20, 2025 Mrs. Moody (for herself, Mr. Cotton , Mr. Lee , Mr. Budd , Mr. Moreno , and Mr. Tillis ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo amend title 18, United States Code, to prohibit taking or transmitting video of defense information, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Drone Espionage Act .\n#### 2. Taking or transmitting video of defense information prohibited\nSection 793 of title 18, United States Code, is amended by inserting video, after photographic negative, each place such term appears.",
      "versionDate": "2025-05-20",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s1809rs.xml",
      "text": "II\nCalendar No. 316\n119th CONGRESS\n2d Session\nS. 1809\nIN THE SENATE OF THE UNITED STATES\nMay 20, 2025 Mrs. Moody (for herself, Mr. Cotton , Mr. Lee , Mr. Budd , Mr. Moreno , Mr. Tillis , Ms. Slotkin , Mr. Wicker , Mr. Cruz , Mrs. Blackburn , Mr. Tuberville , Mr. Mullin , Mrs. Britt , and Mr. McCormick ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nFebruary 9, 2026 Reported by Mr. Grassley , without amendment\nA BILL\nTo amend title 18, United States Code, to prohibit taking or transmitting video of defense information, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Drone Espionage Act .\n#### 2. Taking or transmitting video of defense information prohibited\nSection 793 of title 18, United States Code, is amended by inserting video, after photographic negative, each place such term appears.",
      "versionDate": "2026-02-09",
      "versionType": "Reported in Senate"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-04-17",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "2939",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Drone Espionage Act",
      "type": "HR"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": {
        "item": [
          {
            "name": "Digital media",
            "updateDate": "2025-07-03T13:31:36Z"
          },
          {
            "name": "Espionage and treason",
            "updateDate": "2025-07-03T13:31:40Z"
          },
          {
            "name": "Military facilities and property",
            "updateDate": "2025-07-03T13:31:50Z"
          },
          {
            "name": "Military operations and strategy",
            "updateDate": "2025-07-03T13:31:56Z"
          }
        ]
      },
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-06-30T19:06:15Z"
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
      "date": "2025-05-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1809is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2026-02-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s1809rs.xml"
        }
      ],
      "type": "Reported in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Drone Espionage Act",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2026-02-11T06:08:21Z"
    },
    {
      "title": "Drone Espionage Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-10T12:03:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Drone Espionage Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-30T02:08:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 18, United States Code, to prohibit taking or transmitting video of defense information, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-30T02:03:25Z"
    }
  ]
}
```
