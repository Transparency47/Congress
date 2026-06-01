# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6203?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6203
- Title: United States Cadet Nurse Corps Service Recognition Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6203
- Origin chamber: House
- Introduced date: 2025-11-20
- Update date: 2026-04-10T12:11:01Z
- Update date including text: 2026-04-10T12:11:01Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-11-20: Introduced in House
- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Referred to the Committee on Veterans' Affairs, and in addition to the Committee on Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-11-20 - IntroReferral: Referred to the Committee on Veterans' Affairs, and in addition to the Committee on Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-12-09 - Committee: Referred to the Subcommittee on Disability Assistance and Memorial Affairs.
- Latest action: 2025-11-20: Introduced in House

## Actions

- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Referred to the Committee on Veterans' Affairs, and in addition to the Committee on Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-11-20 - IntroReferral: Referred to the Committee on Veterans' Affairs, and in addition to the Committee on Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-12-09 - Committee: Referred to the Subcommittee on Disability Assistance and Memorial Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-20",
    "latestAction": {
      "actionDate": "2025-11-20",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6203",
    "number": "6203",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "L000599",
        "district": "17",
        "firstName": "Michael",
        "fullName": "Rep. Lawler, Michael [R-NY-17]",
        "lastName": "Lawler",
        "party": "R",
        "state": "NY"
      }
    ],
    "title": "United States Cadet Nurse Corps Service Recognition Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-10T12:11:01Z",
    "updateDateIncludingText": "2026-04-10T12:11:01Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-09",
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
      "actionDate": "2025-11-20",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "hsas00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Veterans' Affairs, and in addition to the Committee on Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-20",
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
      "text": "Referred to the Committee on Veterans' Affairs, and in addition to the Committee on Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-11-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-20",
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
          "date": "2025-11-20T15:06:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-12-09T14:03:50Z",
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
          "date": "2025-11-20T15:06:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Armed Services Committee",
      "systemCode": "hsas00",
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
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "DC"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-11-20",
      "state": "PA"
    },
    {
      "bioguideId": "D000530",
      "district": "17",
      "firstName": "Christopher",
      "fullName": "Rep. Deluzio, Christopher R. [D-PA-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Deluzio",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "PA"
    },
    {
      "bioguideId": "H001086",
      "district": "1",
      "firstName": "Diana",
      "fullName": "Rep. Harshbarger, Diana [R-TN-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Harshbarger",
      "party": "R",
      "sponsorshipDate": "2025-12-10",
      "state": "TN"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-12-10",
      "state": "NJ"
    },
    {
      "bioguideId": "M001237",
      "district": "8",
      "firstName": "Kristen",
      "fullName": "Rep. McDonald Rivet, Kristen [D-MI-8]",
      "isOriginalCosponsor": "False",
      "lastName": "McDonald Rivet",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "MI"
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
      "sponsorshipDate": "2025-12-17",
      "state": "VA"
    },
    {
      "bioguideId": "S001196",
      "district": "21",
      "firstName": "Elise",
      "fullName": "Rep. Stefanik, Elise M. [R-NY-21]",
      "isOriginalCosponsor": "False",
      "lastName": "Stefanik",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2026-02-10",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6203ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6203\nIN THE HOUSE OF REPRESENTATIVES\nNovember 20, 2025 Mr. Lawler (for himself, Ms. Norton , Mr. Fitzpatrick , and Mr. Deluzio ) introduced the following bill; which was referred to the Committee on Veterans' Affairs , and in addition to the Committee on Armed Services , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend title 38, United States Code, to recognize and honor the service of individuals who served in the United States Cadet Nurse Corps during World War II, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the United States Cadet Nurse Corps Service Recognition Act of 2025 .\n#### 2. Recognition and honoring of service of individuals who served in United States Cadet Nurse Corps during World War II\nSection 106 of title 38, United States Code, is amended by adding at the end the following new subsection:\n(g) (1) (A) Service as a member of the United States Cadet Nurse Corps during the period beginning on July 1, 1943, and ending on December 31, 1948, of any individual who was honorably discharged therefrom pursuant to subparagraph (B) shall be considered active duty for purposes of eligibility and entitlement to headstones, markers, and other benefits under chapters 23 and 24 of this title, other than such benefits relating to the interment or inurnment of the individual in Arlington National Cemetery solely by reason of such service. (B) (i) Not later than one year after the date of the enactment of this subsection, the Secretary of Defense shall issue to each individual who served as a member of the United States Cadet Nurse Corps during the period beginning on July 1, 1943, and ending on December 31, 1948, a discharge from such service under honorable conditions if the Secretary determines that the nature and duration of the service of the individual so warrants. (ii) A discharge under clause (i) shall designate the date of discharge. The date of discharge shall be the date, as determined by the Secretary, of the termination of service of the individual concerned as described in that clause. (2) An individual who receives a discharge under paragraph (1)(B) for service as a member of the United States Cadet Nurse Corps shall be honored as a veteran but shall not be entitled by reason of such service to any benefit under a law administered by the Secretary of Veterans Affairs, except as provided in paragraph (1)(A). (3) The Secretary of Defense may design and produce a service medal, memorial plaque or gravemarker, or other commendation to honor individuals who receive a discharge under paragraph (1)(B). .",
      "versionDate": "2025-11-20",
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
        "actionDate": "2025-12-03",
        "text": "Read twice and referred to the Committee on Veterans' Affairs."
      },
      "number": "3329",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "United States Cadet Nurse Corps Service Recognition Act of 2025",
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
        "updateDate": "2025-12-09T19:38:06Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-11-20",
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
          "measure-id": "id119hr6203",
          "measure-number": "6203",
          "measure-type": "hr",
          "orig-publish-date": "2025-11-20",
          "originChamber": "HOUSE",
          "update-date": "2026-04-10"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr6203v00",
            "update-date": "2026-04-10"
          },
          "action-date": "2025-11-20",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>United States Cadet Nurse Corps Service Recognition Act of 2025</strong></p><p>This bill recognizes service as a member of the U.S. Cadet Nurse Corps between July 1, 1943, and December 31, 1948, as active duty service. The active duty designation entitles qualifying individuals to certain benefits afforded to veterans, such as burial benefits (not including interment or inurnment at Arlington National Cemetery) and honorary veteran status.</p><p>Under the bill, the Department of Defense (DOD) must issue individuals who served in the corps during the specified period a discharge from their service under honorable conditions if such a discharge is warranted based on the duration and nature of the service.</p><p>Such individuals are not entitled to Department of Veterans Affairs benefits aside from those related to burials and memorials.</p><p>The bill also authorizes DOD to produce a service medal or other commendation, memorial plaque, or grave marker to honor the individuals.</p>"
        },
        "title": "United States Cadet Nurse Corps Service Recognition Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr6203.xml",
    "summary": {
      "actionDate": "2025-11-20",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>United States Cadet Nurse Corps Service Recognition Act of 2025</strong></p><p>This bill recognizes service as a member of the U.S. Cadet Nurse Corps between July 1, 1943, and December 31, 1948, as active duty service. The active duty designation entitles qualifying individuals to certain benefits afforded to veterans, such as burial benefits (not including interment or inurnment at Arlington National Cemetery) and honorary veteran status.</p><p>Under the bill, the Department of Defense (DOD) must issue individuals who served in the corps during the specified period a discharge from their service under honorable conditions if such a discharge is warranted based on the duration and nature of the service.</p><p>Such individuals are not entitled to Department of Veterans Affairs benefits aside from those related to burials and memorials.</p><p>The bill also authorizes DOD to produce a service medal or other commendation, memorial plaque, or grave marker to honor the individuals.</p>",
      "updateDate": "2026-04-10",
      "versionCode": "id119hr6203"
    },
    "title": "United States Cadet Nurse Corps Service Recognition Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-11-20",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>United States Cadet Nurse Corps Service Recognition Act of 2025</strong></p><p>This bill recognizes service as a member of the U.S. Cadet Nurse Corps between July 1, 1943, and December 31, 1948, as active duty service. The active duty designation entitles qualifying individuals to certain benefits afforded to veterans, such as burial benefits (not including interment or inurnment at Arlington National Cemetery) and honorary veteran status.</p><p>Under the bill, the Department of Defense (DOD) must issue individuals who served in the corps during the specified period a discharge from their service under honorable conditions if such a discharge is warranted based on the duration and nature of the service.</p><p>Such individuals are not entitled to Department of Veterans Affairs benefits aside from those related to burials and memorials.</p><p>The bill also authorizes DOD to produce a service medal or other commendation, memorial plaque, or grave marker to honor the individuals.</p>",
      "updateDate": "2026-04-10",
      "versionCode": "id119hr6203"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-11-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6203ih.xml"
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
      "title": "United States Cadet Nurse Corps Service Recognition Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-09T10:23:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "United States Cadet Nurse Corps Service Recognition Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-09T10:23:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 38, United States Code, to recognize and honor the service of individuals who served in the United States Cadet Nurse Corps during World War II, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-09T10:18:23Z"
    }
  ]
}
```
