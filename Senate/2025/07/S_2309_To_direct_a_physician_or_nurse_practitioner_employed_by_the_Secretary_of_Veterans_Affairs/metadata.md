# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2309?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2309
- Title: Veteran Burial Timeliness and Death Certificate Accountability Act
- Congress: 119
- Bill type: S
- Bill number: 2309
- Origin chamber: Senate
- Introduced date: 2025-07-16
- Update date: 2026-05-29T16:20:24Z
- Update date including text: 2026-05-29T16:20:24Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-16: Introduced in Senate
- 2025-07-16 - IntroReferral: Introduced in Senate
- 2025-07-16 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- 2025-12-10 - Committee: Committee on Veterans' Affairs. Hearings held.
- 2026-03-18 - Committee: Committee on Veterans' Affairs. Ordered to be reported with an amendment in the nature of a substitute favorably.
- Latest action: 2025-07-16: Introduced in Senate

## Actions

- 2025-07-16 - IntroReferral: Introduced in Senate
- 2025-07-16 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- 2025-12-10 - Committee: Committee on Veterans' Affairs. Hearings held.
- 2026-03-18 - Committee: Committee on Veterans' Affairs. Ordered to be reported with an amendment in the nature of a substitute favorably.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-16",
    "latestAction": {
      "actionDate": "2025-07-16",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2309",
    "number": "2309",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "B001236",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Boozman, John [R-AR]",
        "lastName": "Boozman",
        "party": "R",
        "state": "AR"
      }
    ],
    "title": "Veteran Burial Timeliness and Death Certificate Accountability Act",
    "type": "S",
    "updateDate": "2026-05-29T16:20:24Z",
    "updateDateIncludingText": "2026-05-29T16:20:24Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-18",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Veterans' Affairs. Ordered to be reported with an amendment in the nature of a substitute favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-12-10",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Veterans' Affairs. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-07-16",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-16",
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
            "date": "2026-03-18T20:00:18Z",
            "name": "Markup By"
          },
          {
            "date": "2025-12-10T21:00:22Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2025-07-16T21:39:55Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Veterans' Affairs Committee",
      "systemCode": "ssva00",
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
      "bioguideId": "H001076",
      "firstName": "Maggie",
      "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Hassan",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "NH"
    },
    {
      "bioguideId": "C001056",
      "firstName": "John",
      "fullName": "Sen. Cornyn, John [R-TX]",
      "isOriginalCosponsor": "False",
      "lastName": "Cornyn",
      "party": "R",
      "sponsorshipDate": "2025-07-28",
      "state": "TX"
    },
    {
      "bioguideId": "M001198",
      "firstName": "Roger",
      "fullName": "Sen. Marshall, Roger [R-KS]",
      "isOriginalCosponsor": "False",
      "lastName": "Marshall",
      "party": "R",
      "sponsorshipDate": "2025-09-08",
      "state": "KS"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "False",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2025-09-09",
      "state": "NE"
    },
    {
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "False",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2025-10-03",
      "state": "MT"
    },
    {
      "bioguideId": "C001095",
      "firstName": "Tom",
      "fullName": "Sen. Cotton, Tom [R-AR]",
      "isOriginalCosponsor": "False",
      "lastName": "Cotton",
      "party": "R",
      "sponsorshipDate": "2025-10-08",
      "state": "AR"
    },
    {
      "bioguideId": "L000577",
      "firstName": "Mike",
      "fullName": "Sen. Lee, Mike [R-UT]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "party": "R",
      "sponsorshipDate": "2026-05-19",
      "state": "UT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2309is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2309\nIN THE SENATE OF THE UNITED STATES\nJuly 16, 2025 Mr. Boozman (for himself and Ms. Hassan ) introduced the following bill; which was read twice and referred to the Committee on Veterans' Affairs\nA BILL\nTo direct a physician or nurse practitioner employed by the Secretary of Veterans Affairs to certify the death of a veteran not later than 48 hours after such physician or nurse practitioner learns of such death, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Veteran Burial Timeliness and Death Certificate Accountability Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nStates and counties have reported significant delays in the signing of death certificates for veterans who pass away from natural causes.\n**(2)**\nSuch delays, caused by the refusal of, or postponement by, physicians of the Department of Veterans Affairs have, in some cases, lasted as long as eight weeks.\n**(3)**\nSuch delays prevent the timely burial of deceased veterans and access to survivor benefits.\n#### 3. Timely certification of the death of a veteran\n##### (a) In general\n**(1) VA physician or nurse practitioner**\nSubject to paragraph (2), a physician or nurse practitioner employed by the Secretary of Veterans Affairs who is the primary care provider of a veteran who dies of natural causes shall certify the death of such veteran not later than 48 hours after such physician or nurse practitioner learns of such death.\n**(2) Coroner or medical examiner**\nIf a physician or nurse practitioner described in paragraph (1) cannot comply with such paragraph with respect to a death described in such paragraph, a coroner or medical examiner in the jurisdiction where such death occurred may certify such death.\n##### (b) Report\n**(1) In general**\nNot later than one year after the date of the enactment of this Act, and annually thereafter, the Secretary shall submit to the Committee on Veterans\u2019 Affairs of the Senate and the Committee on Veterans\u2019 Affairs of the House of Representatives a report regarding compliance with subsection (a).\n**(2) Elements**\nEach report required under paragraph (1) shall include, with respect to the year preceding the date of the report, the following elements:\n**(A)**\nThe percentage of cases in which a physician or nurse practitioner employed by the Secretary complied with subsection (a)(1).\n**(B)**\nThe number of cases in which such a physician or nurse practitioner could not so comply.\n**(C)**\nAn identification of the most common reasons why such a physician or nurse practitioner could not so comply.\n##### (c) Rule of construction\nNothing in this Act shall require any employee of the Department of Veterans Affairs, including a physician or nurse practitioner, to take an action not in compliance with the laws, regulations, or requirements of the appropriate jurisdiction in which the employee is licensed or practicing, or in which a death may need to be certified.",
      "versionDate": "2025-07-16",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2025-12-03",
        "text": "Referred to the Subcommittee on Health."
      },
      "number": "4398",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Veteran Burial Timeliness and Death Certificate Accountability Act",
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
            "name": "Congressional oversight",
            "updateDate": "2026-01-05T16:12:13Z"
          },
          {
            "name": "Health personnel",
            "updateDate": "2026-01-05T16:12:04Z"
          },
          {
            "name": "Veterans' medical care",
            "updateDate": "2026-01-05T16:12:08Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-07-31T22:46:49Z"
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
      "date": "2025-07-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2309is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Veteran Burial Timeliness and Death Certificate Accountability Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-20T11:03:28Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Veteran Burial Timeliness and Death Certificate Accountability Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-30T06:53:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to direct a physician or nurse practitioner employed by the Secretary of Veterans Affairs to certify the death of a veteran not later than 48 hours after such physician or nurse practitioner learns of such death, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-30T06:48:32Z"
    }
  ]
}
```
