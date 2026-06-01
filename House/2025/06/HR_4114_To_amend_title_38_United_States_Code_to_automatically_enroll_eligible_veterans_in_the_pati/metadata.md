# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4114?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4114
- Title: EVEST Act
- Congress: 119
- Bill type: HR
- Bill number: 4114
- Origin chamber: House
- Introduced date: 2025-06-24
- Update date: 2026-05-21T08:08:55Z
- Update date including text: 2026-05-21T08:08:55Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-24: Introduced in House
- 2025-06-24 - IntroReferral: Introduced in House
- 2025-06-24 - IntroReferral: Introduced in House
- 2025-06-24 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-12-19 - Committee: Referred to the Subcommittee on Health.
- 2026-03-18 - Committee: Committee Hearings Held
- 2026-03-18 - Committee: Subcommittee on Health Discharged
- 2026-05-20 - Committee: Committee Hearings Held
- Latest action: 2025-06-24: Introduced in House

## Actions

- 2025-06-24 - IntroReferral: Introduced in House
- 2025-06-24 - IntroReferral: Introduced in House
- 2025-06-24 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-12-19 - Committee: Referred to the Subcommittee on Health.
- 2026-03-18 - Committee: Committee Hearings Held
- 2026-03-18 - Committee: Subcommittee on Health Discharged
- 2026-05-20 - Committee: Committee Hearings Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-24",
    "latestAction": {
      "actionDate": "2025-06-24",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4114",
    "number": "4114",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "T000472",
        "district": "39",
        "firstName": "Mark",
        "fullName": "Rep. Takano, Mark [D-CA-39]",
        "lastName": "Takano",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "EVEST Act",
    "type": "HR",
    "updateDate": "2026-05-21T08:08:55Z",
    "updateDateIncludingText": "2026-05-21T08:08:55Z"
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
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Hearings Held",
      "type": "Committee"
    },
    {
      "actionDate": "2026-03-18",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Hearings Held",
      "type": "Committee"
    },
    {
      "actionDate": "2026-03-18",
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
      "text": "Subcommittee on Health Discharged",
      "type": "Committee"
    },
    {
      "actionDate": "2025-12-19",
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
      "actionDate": "2025-06-24",
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
      "actionDate": "2025-06-24",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-24",
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
        "item": [
          {
            "date": "2026-05-20T13:27:36Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2026-03-18T16:54:21Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2025-06-24T14:03:45Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": [
              {
                "date": "2026-03-18T16:54:15Z",
                "name": "Discharged from"
              },
              {
                "date": "2025-12-19T18:59:33Z",
                "name": "Referred to"
              }
            ]
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
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2026-04-15",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4114ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4114\nIN THE HOUSE OF REPRESENTATIVES\nJune 24, 2025 Mr. Takano introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to automatically enroll eligible veterans in the patient enrollment system of Department of Veterans Affairs, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Ensuring Veterans\u2019 Smooth Transition Act or the EVEST Act .\n#### 2. Automatic enrollment of eligible veterans in patient enrollment system of Department of Veterans Affairs\n##### (a) In general\nSection 1705 of title 38, United States Code, is amended by adding at the end the following new subsection:\n(d) (1) The Secretary shall enroll each veteran described in subsection (a) in the patient enrollment system under this section not later than 60 days after receiving the information described in paragraph (2) regarding the veteran. (2) The information described in this paragraph is the information\u2014 (A) regarding a veteran that the Secretary determines is necessary to so enroll a veteran; and (B) transmitted to the Secretary under section 1142(e) of title 10. (3) Not later than 60 days after enrolling a veteran under paragraph (1), the Secretary shall provide to the veteran\u2014 (A) notice of such enrollment; (B) instructions regarding how the veteran may opt out of such enrollment; (C) instructions regarding how the veteran may elect to enroll at a later date. (4) In carrying out paragraph (3), the Secretary shall\u2014 (A) provide a notice or instructions in the form of a physical copy delivered by mail and, to the extent practical, in the form of an electronic copy delivered by electronic mail; and (B) consider using, to the extent practical, mass texting capabilities through mobile telephones. .\n##### (b) Applicability\nSubsection (d) of section 1705 of title 38, United States Code, as added by subsection (a), shall apply to a veteran\u2014\n**(1)**\nwho is discharged or separated from the Armed Forces on or after the date that is 90 days before the date of the enactment of this Act; and\n**(2)**\nwith respect to whom the Secretary receives the information described in paragraph (2) of such subsection on or after the date of the enactment of this Act.\n##### (c) Electronic certificates of eligibility\nNot later than August 1, 2026, the Secretary of Veterans Affairs shall ensure that any veteran who is eligible for automatic enrollment in the patient enrollment system under subsection (d) of section 1705 of title 38, United States Code, as added by subsection (a), is able to access\u2014\n**(1)**\nan electronic version of the veteran\u2019s certificate of eligibility for such enrollment; and\n**(2)**\nan electronic mechanism by which the veteran may opt out of such enrollment.\n##### (d) Report on automatic enrollment\n**(1) In general**\nNot later than one year after the first veteran is enrolled in the patient enrollment system of the Department of Veterans Affairs under subsection (d) of section 1705 of title 38, United States Code, as added by subsection (a), the Secretary of Veterans Affairs shall submit to the Committees on Veterans\u2019 Affairs of the Senate and House of Representatives a report on the enrollment process under such subsection. Such report shall include each of the following:\n**(A)**\nA discussion of any anticipated challenges that occurred in implementing such subsection, the strategies used to address such challenges, and the effectiveness of such strategies.\n**(B)**\nA discussion of any unanticipated challenges that occurred in implementing such subsection, the strategies used to address such challenges, and the effectiveness of such strategies.\n**(C)**\nAny additional information the Secretary determines appropriate, including information that may be useful to other Federal departments and agencies considering the implementation of similar automatic enrollment programs.\n**(2) Form of report**\nThe report required under paragraph (1) shall be submitted in unclassified form, but may include a classified annex.\n#### 3. GAO report on notice of automatic enrollment in patient enrollment system of Department of Veterans Affairs\nNot later than 180 days after the date of the enactment of this Act, the Comptroller General of the United States shall submit to the Committees on Veterans\u2019 Affairs of the Senate and House of Representatives a report containing the results of a study to determine the best methods for the Secretary of Veterans Affairs to provide notice under paragraph (3) of subsection (d) of section 1705 of title 38, United States Code, as added by section 2. In making such determination, the Comptroller General shall consider the needs of a veteran based on\u2014\n**(1)**\nage;\n**(2)**\nresidence in an urban area; and\n**(3)**\nresidence in an rural area.",
      "versionDate": "2025-06-24",
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
            "name": "Congressional oversight",
            "updateDate": "2026-04-06T20:32:03Z"
          },
          {
            "name": "Veterans' medical care",
            "updateDate": "2026-04-06T20:32:00Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-07-09T15:31:18Z"
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
      "date": "2025-06-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4114ih.xml"
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
      "title": "EVEST Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-08T09:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "EVEST Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-08T09:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Ensuring Veterans\u2019 Smooth Transition Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-08T09:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 38, United States Code, to automatically enroll eligible veterans in the patient enrollment system of Department of Veterans Affairs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-08T09:18:30Z"
    }
  ]
}
```
