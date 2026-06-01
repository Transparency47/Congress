# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3395?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3395
- Title: Mammography Access for Veterans Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 3395
- Origin chamber: Senate
- Introduced date: 2025-12-09
- Update date: 2026-05-15T18:27:35Z
- Update date including text: 2026-05-15T18:27:35Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-09: Introduced in Senate
- 2025-12-09 - IntroReferral: Introduced in Senate
- 2025-12-09 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- 2026-04-29 - Committee: Committee on Veterans' Affairs. Hearings held.
- Latest action: 2025-12-09: Introduced in Senate

## Actions

- 2025-12-09 - IntroReferral: Introduced in Senate
- 2025-12-09 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- 2026-04-29 - Committee: Committee on Veterans' Affairs. Hearings held.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-09",
    "latestAction": {
      "actionDate": "2025-12-09",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3395",
    "number": "3395",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "B001277",
        "district": "",
        "firstName": "Richard",
        "fullName": "Sen. Blumenthal, Richard [D-CT]",
        "lastName": "Blumenthal",
        "party": "D",
        "state": "CT"
      }
    ],
    "title": "Mammography Access for Veterans Act of 2025",
    "type": "S",
    "updateDate": "2026-05-15T18:27:35Z",
    "updateDateIncludingText": "2026-05-15T18:27:35Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-29",
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
      "actionDate": "2025-12-09",
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
      "actionDate": "2025-12-09",
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
            "date": "2026-04-29T21:37:18Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2025-12-09T19:36:09Z",
            "name": "Referred To"
          },
          {
            "date": "2025-12-09T19:36:09Z",
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
      "bioguideId": "M000934",
      "firstName": "Jerry",
      "fullName": "Sen. Moran, Jerry [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2025-12-09",
      "state": "KS"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "HI"
    },
    {
      "bioguideId": "B001236",
      "firstName": "John",
      "fullName": "Sen. Boozman, John [R-AR]",
      "isOriginalCosponsor": "True",
      "lastName": "Boozman",
      "party": "R",
      "sponsorshipDate": "2025-12-09",
      "state": "AR"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "False",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2026-04-29",
      "state": "NM"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3395is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3395\nIN THE SENATE OF THE UNITED STATES\nDecember 9, 2025 Mr. Blumenthal (for himself, Mr. Moran , Ms. Hirono , and Mr. Boozman ) introduced the following bill; which was read twice and referred to the Committee on Veterans' Affairs\nA BILL\nTo expand the telescreening mammography pilot program of the Department of Veterans Affairs, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Mammography Access for Veterans Act of 2025 .\n#### 2. Expansion of telescreening mammography pilot program of Department of Veterans Affairs\n##### (a) In general\nSection 102 of the Making Advances in Mammography and Medical Options for Veterans Act ( Public Law 117\u2013135 ; 38 U.S.C. 7322 note) is amended\u2014\n**(1)**\nin the section heading, by striking pilot ;\n**(2)**\nby striking pilot each place it appears;\n**(3)**\nby striking subsection (b);\n**(4)**\nby redesignating subsections (c) through (e) as subsections (b) through (d), respectively; and\n**(5)**\nin subsection (d), as redesignated by paragraph (4), by striking one year after the conclusion of the program under subsection (a) and inserting May 1, 2027 .\n##### (b) Expansion of locations\nNot later than two years after the date of the enactment of this Act, the Secretary of Veterans Affairs shall ensure the Department offers at least one of the following programs in each State and Puerto Rico:\n**(1)**\nThe program under section 102 of the Making Advances in Mammography and Medical Options for Veterans Act ( Public Law 117\u2013135 ; 38 U.S.C. 7322 note), as amended by subsection (a).\n**(2)**\nA full-service mammography program within a facility of the Department.\n**(3)**\nA mobile mammography program of the Department.\n##### (c) Accessibility\nThe Secretary shall ensure that each of the programs under subsection (b) are accessible for veterans with paralysis, a spinal cord injury or disorder, or another disability, consistent with applicable accessibility requirements.\n##### (d) Rule of construction\nNothing in this section or the amendments made by this section shall prevent the Secretary of Veterans Affairs from expanding telescreening mammography services to facilities of the Department that are not\u2014\n**(1)**\nthe facilities participating in the pilot program under section 102 of the Making Advances in Mammography and Medical Options for Veterans Act ( Public Law 117\u2013135 ; 38 U.S.C. 7322 note) as of the day before the date of the enactment of this Act; or\n**(2)**\nlocated in States where the Department does not offer breast imaging services at a facility of the Department.",
      "versionDate": "2025-12-09",
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
        "actionDate": "2026-02-05",
        "text": "Referred to the House Committee on Veterans' Affairs."
      },
      "number": "7411",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Mammography Access for Veterans Act of 2025",
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
            "name": "Health care coverage and access",
            "updateDate": "2026-05-06T16:51:32Z"
          },
          {
            "name": "Health technology, devices, supplies",
            "updateDate": "2026-05-06T16:50:42Z"
          },
          {
            "name": "Telephone and wireless communication",
            "updateDate": "2026-05-06T16:50:50Z"
          },
          {
            "name": "Veterans' medical care",
            "updateDate": "2026-05-06T16:51:04Z"
          },
          {
            "name": "Women's health",
            "updateDate": "2026-05-06T16:48:57Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2026-01-06T16:48:25Z"
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
      "date": "2025-12-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3395is.xml"
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
      "title": "Mammography Access for Veterans Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-30T11:03:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Mammography Access for Veterans Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-31T03:38:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to expand the telescreening mammography pilot program of the Department of Veterans Affairs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-31T03:33:14Z"
    }
  ]
}
```
