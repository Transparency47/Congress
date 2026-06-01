# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/496?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/496
- Title: Veterans 2nd Amendment Restoration Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 496
- Origin chamber: House
- Introduced date: 2025-01-16
- Update date: 2026-02-12T17:32:18Z
- Update date including text: 2026-02-12T17:32:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-16: Introduced in House
- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Referred to the Committee on Veterans' Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-16 - IntroReferral: Referred to the Committee on Veterans' Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-20 - Committee: Referred to the Subcommittee on Disability Assistance and Memorial Affairs.
- Latest action: 2025-01-16: Introduced in House

## Actions

- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Referred to the Committee on Veterans' Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-16 - IntroReferral: Referred to the Committee on Veterans' Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-20 - Committee: Referred to the Subcommittee on Disability Assistance and Memorial Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-16",
    "latestAction": {
      "actionDate": "2025-01-16",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/496",
    "number": "496",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "C001132",
        "district": "2",
        "firstName": "Elijah",
        "fullName": "Rep. Crane, Elijah [R-AZ-2]",
        "lastName": "Crane",
        "party": "R",
        "state": "AZ"
      }
    ],
    "title": "Veterans 2nd Amendment Restoration Act of 2025",
    "type": "HR",
    "updateDate": "2026-02-12T17:32:18Z",
    "updateDateIncludingText": "2026-02-12T17:32:18Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-20",
      "committees": {
        "item": {
          "name": "Disability Assistance and Memorial Affairs Subcommittee",
          "systemCode": "hsvr09"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Disability Assistance and Memorial Affairs.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-16",
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
      "text": "Referred to the Committee on Veterans' Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-16",
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
      "text": "Referred to the Committee on Veterans' Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-16",
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
          "date": "2025-01-16T14:04:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-02-20T22:38:25Z",
              "name": "Referred to"
            }
          },
          "name": "Disability Assistance and Memorial Affairs Subcommittee",
          "systemCode": "hsvr09"
        }
      },
      "systemCode": "hsvr00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-01-16T14:04:15Z",
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
      "bioguideId": "L000596",
      "district": "13",
      "firstName": "Anna Paulina",
      "fullName": "Rep. Luna, Anna Paulina [R-FL-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Luna",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr496ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 496\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 16, 2025 Mr. Crane introduced the following bill; which was referred to the Committee on Veterans' Affairs , and in addition to the Committee on the Judiciary , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo direct the Secretary of Veterans Affairs to notify the Attorney General that basis for the transmission of certain information to the Department of Justice for use by the national instant criminal background check system was improper, does not apply, or no longer applies, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Veterans 2nd Amendment Restoration Act of 2025 .\n#### 2. Notification of lack of basis for the Secretary of Veterans Affairs to have transmitted certain information to the Department of Justice for use by the national instant criminal background check system\nThe Secretary of Veterans Affairs shall, within 30 days of enactment of this Act, and in accordance with section 40901(e)(1)(D) of title 34, United States Code, notify the Attorney General that the basis for the transmittal, on or after November 30, 1993, by the Secretary of Veterans Affairs, of personally identifiable information of a beneficiary, solely on the basis of a determination by the Secretary to pay benefits to a fiduciary for the use and benefit of the beneficiary under section 5502 of this title 38, United States Code, to any entity in the Department of Justice, for use by the national instant criminal background check system established under section 103 of the Brady Handgun Violence Prevention Act, was improper, does not apply, or no longer applies.\n#### 3. Determination by the Secretary of Veterans Affairs that a person is mentally incompetent is insufficient to treat such person as a mental defective for certain purposes regarding firearms or ammunition\nFor purposes of section 922 of title 18, United States Code, a person shall not be treated as having been adjudicated as a mental defective solely on the basis that the Secretary of Veterans Affairs has determined that such person\u2014\n**(1)**\nis mentally incompetent under section 3.353 of title 38, Code of Federal Regulations (or successor regulation); or\n**(2)**\nrequires a fiduciary under section 5502 of title 38, United States Code.",
      "versionDate": "2025-01-16",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Criminal justice information and records",
            "updateDate": "2025-03-10T14:16:40Z"
          },
          {
            "name": "Firearms and explosives",
            "updateDate": "2025-03-10T14:16:45Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-02-15T16:11:36Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-16",
    "originChamber": "House",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119hr496",
          "measure-number": "496",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-16",
          "originChamber": "HOUSE",
          "update-date": "2026-02-12"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr496v00",
            "update-date": "2026-02-12"
          },
          "action-date": "2025-01-16",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Veterans 2nd Amendment Restoration Act of 2025</strong></p><p>This bill provides that certain individuals are not prohibited from purchasing, selling, or possessing a firearm or ammunition solely because the Department of Veterans Affairs (VA) has determined they require a fiduciary or are mentally incompetent (i.e., unable to manage their affairs).\u00a0</p><p>Under current law, it is unlawful to sell or otherwise dispose of any firearm or ammunition to any person who has been adjudicated as mentally defective. The bill provides that a person must not be treated as having been adjudicated as mentally defective solely because the VA determined the person requires a fiduciary or is mentally incompetent per its regulations.</p><p>Within 30 days of the enactment of this bill, the VA must notify the Department of Justice (DOJ) that the VA's transmittals of certain information that was provided solely on the basis that a veteran's benefits are managed by a fiduciary were improper, do not apply, or no longer apply. This applies to VA transmittals to DOJ on or after November 30, 1993, for use by the National Instant Criminal Background Check System for firearm transferees.</p>"
        },
        "title": "Veterans 2nd Amendment Restoration Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr496.xml",
    "summary": {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Veterans 2nd Amendment Restoration Act of 2025</strong></p><p>This bill provides that certain individuals are not prohibited from purchasing, selling, or possessing a firearm or ammunition solely because the Department of Veterans Affairs (VA) has determined they require a fiduciary or are mentally incompetent (i.e., unable to manage their affairs).\u00a0</p><p>Under current law, it is unlawful to sell or otherwise dispose of any firearm or ammunition to any person who has been adjudicated as mentally defective. The bill provides that a person must not be treated as having been adjudicated as mentally defective solely because the VA determined the person requires a fiduciary or is mentally incompetent per its regulations.</p><p>Within 30 days of the enactment of this bill, the VA must notify the Department of Justice (DOJ) that the VA's transmittals of certain information that was provided solely on the basis that a veteran's benefits are managed by a fiduciary were improper, do not apply, or no longer apply. This applies to VA transmittals to DOJ on or after November 30, 1993, for use by the National Instant Criminal Background Check System for firearm transferees.</p>",
      "updateDate": "2026-02-12",
      "versionCode": "id119hr496"
    },
    "title": "Veterans 2nd Amendment Restoration Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Veterans 2nd Amendment Restoration Act of 2025</strong></p><p>This bill provides that certain individuals are not prohibited from purchasing, selling, or possessing a firearm or ammunition solely because the Department of Veterans Affairs (VA) has determined they require a fiduciary or are mentally incompetent (i.e., unable to manage their affairs).\u00a0</p><p>Under current law, it is unlawful to sell or otherwise dispose of any firearm or ammunition to any person who has been adjudicated as mentally defective. The bill provides that a person must not be treated as having been adjudicated as mentally defective solely because the VA determined the person requires a fiduciary or is mentally incompetent per its regulations.</p><p>Within 30 days of the enactment of this bill, the VA must notify the Department of Justice (DOJ) that the VA's transmittals of certain information that was provided solely on the basis that a veteran's benefits are managed by a fiduciary were improper, do not apply, or no longer apply. This applies to VA transmittals to DOJ on or after November 30, 1993, for use by the National Instant Criminal Background Check System for firearm transferees.</p>",
      "updateDate": "2026-02-12",
      "versionCode": "id119hr496"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr496ih.xml"
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
      "title": "Veterans 2nd Amendment Restoration Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-14T13:38:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Veterans 2nd Amendment Restoration Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-14T13:38:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Veterans Affairs to notify the Attorney General that basis for the transmission of certain information to the Department of Justice for use by the national instant criminal background check system was improper, does not apply, or no longer applies, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-14T13:33:25Z"
    }
  ]
}
```
