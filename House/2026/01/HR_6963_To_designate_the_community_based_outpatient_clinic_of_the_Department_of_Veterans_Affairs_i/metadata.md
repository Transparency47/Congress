# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6963?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6963
- Title: To designate the community-based outpatient clinic of the Department of Veterans Affairs in Lafayette, Louisiana, as the "Rodney C. Hamilton Sr. VA Clinic".
- Congress: 119
- Bill type: HR
- Bill number: 6963
- Origin chamber: House
- Introduced date: 2026-01-07
- Update date: 2026-02-09T19:20:36Z
- Update date including text: 2026-02-09T19:20:36Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-01-07: Introduced in House
- 2026-01-07 - IntroReferral: Introduced in House
- 2026-01-07 - IntroReferral: Introduced in House
- 2026-01-07 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2026-01-29 - Committee: Referred to the Subcommittee on Health.
- Latest action: 2026-01-07: Introduced in House

## Actions

- 2026-01-07 - IntroReferral: Introduced in House
- 2026-01-07 - IntroReferral: Introduced in House
- 2026-01-07 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2026-01-29 - Committee: Referred to the Subcommittee on Health.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-07",
    "latestAction": {
      "actionDate": "2026-01-07",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6963",
    "number": "6963",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "H001077",
        "district": "3",
        "firstName": "Clay",
        "fullName": "Rep. Higgins, Clay [R-LA-3]",
        "lastName": "Higgins",
        "party": "R",
        "state": "LA"
      }
    ],
    "title": "To designate the community-based outpatient clinic of the Department of Veterans Affairs in Lafayette, Louisiana, as the \"Rodney C. Hamilton Sr. VA Clinic\".",
    "type": "HR",
    "updateDate": "2026-02-09T19:20:36Z",
    "updateDateIncludingText": "2026-02-09T19:20:36Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-01-29",
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
      "actionDate": "2026-01-07",
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
      "actionDate": "2026-01-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-07",
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
          "date": "2026-01-07T15:03:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-01-29T16:42:30Z",
              "name": "Referred to"
            }
          },
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
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
      "bioguideId": "J000299",
      "district": "4",
      "firstName": "Mike",
      "fullName": "Rep. Johnson, Mike [R-LA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "party": "R",
      "sponsorshipDate": "2026-01-07",
      "state": "LA"
    },
    {
      "bioguideId": "S001176",
      "district": "1",
      "firstName": "Steve",
      "fullName": "Rep. Scalise, Steve [R-LA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Scalise",
      "party": "R",
      "sponsorshipDate": "2026-01-07",
      "state": "LA"
    },
    {
      "bioguideId": "L000595",
      "district": "5",
      "firstName": "Julia",
      "fullName": "Rep. Letlow, Julia [R-LA-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Letlow",
      "party": "R",
      "sponsorshipDate": "2026-01-07",
      "state": "LA"
    },
    {
      "bioguideId": "F000110",
      "district": "6",
      "firstName": "Cleo",
      "fullName": "Rep. Fields, Cleo [D-LA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Fields",
      "party": "D",
      "sponsorshipDate": "2026-01-07",
      "state": "LA"
    },
    {
      "bioguideId": "C001125",
      "district": "2",
      "firstName": "Troy",
      "fullName": "Rep. Carter, Troy A. [D-LA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Carter",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-01-07",
      "state": "LA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr6963ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 6963\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 7, 2026 Mr. Higgins of Louisiana (for himself, Mr. Johnson of Louisiana , Mr. Scalise , Ms. Letlow , Mr. Fields , and Mr. Carter of Louisiana ) introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo designate the community-based outpatient clinic of the Department of Veterans Affairs in Lafayette, Louisiana, as the Rodney C. Hamilton Sr. VA Clinic .\n#### 1. Designation of Rodney C. Hamilton Sr. VA Clinic in Lafayette, Louisiana\n##### (a) Findings\nCongress finds that\u2014\n**(1)**\nRodney Carroll Hamilton Sr. was born in Fort Worth, Texas, on March 24, 1932, and his family moved to Lafayette, Louisiana, in the summer of 1948;\n**(2)**\nin 1949, at age seventeen, Rodney Hamilton joined the reserve components of the Marine Corps at the urging of his football coach Lou Campbell while attending Lafayette High School;\n**(3)**\nRodney Hamilton served the United States during the Korean War, was wounded in combat in September 1951, and was awarded the Purple Heart;\n**(4)**\nRodney Hamilton loved the Marine Corps and was proud of all Marines who served the United States;\n**(5)**\nRodney Hamilton was a member of the Marine Corps League, the Military Order of the Purple Heart, and the Veteran's Action Coalition of Southwest Louisiana, where he served as Founder and Chairman Emeritus;\n**(6)**\nRodney Hamilton served as a full-time elected official in the Lafayette City Government from 1968 through 1972 as a Trustee of Public Property;\n**(7)**\nRodney Hamilton made numerous contributions to help make Lafayette a better place, including leading efforts to secure and build the community-based outpatient clinic of the Department of Veterans Affairs in Lafayette, which opened in 2016;\n**(8)**\ndue to the dedication of Rodney Hamilton in realizing the community-based outpatient clinic in Lafayette, the street on which the clinic is located was named in his honor and now bears signs saying, Veterans Way, Honorary Rodney Hamilton ; and\n**(9)**\nRodney Hamilton passed away at the age of 88 on November 30, 2020.\n##### (b) Designation\nThe community-based outpatient clinic of the Department of Veterans Affairs in Lafayette, Louisiana, shall after the date of the enactment of this Act be known and designated as the Rodney C. Hamilton Sr. VA Clinic .\n##### (c) Reference\nAny reference in any law, regulation, map, document, paper, or other record of the United States to the clinic referred to in subsection (b) shall be considered to be a reference to the Rodney C. Hamilton Sr. VA Clinic.",
      "versionDate": "2026-01-07",
      "versionType": "Introduced in House"
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
        "actionDate": "2026-01-27",
        "text": "Read twice and referred to the Committee on Veterans' Affairs."
      },
      "number": "3689",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "A bill to designate the community-based outpatient clinic of the Department of Veterans Affairs in Lafayette, Louisiana, as the \"Rodney C. Hamilton Sr. VA Clinic\".",
      "type": "S"
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
        "updateDate": "2026-01-21T16:07:29Z"
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
      "date": "2026-01-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr6963ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To designate the community-based outpatient clinic of the Department of Veterans Affairs in Lafayette, Louisiana, as the \"Rodney C. Hamilton Sr. VA Clinic\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-21T11:18:31Z"
    },
    {
      "title": "To designate the community-based outpatient clinic of the Department of Veterans Affairs in Lafayette, Louisiana, as the \"Rodney C. Hamilton Sr. VA Clinic\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-08T09:06:37Z"
    }
  ]
}
```
