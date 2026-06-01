# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7427?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7427
- Title: SAFE VISITS Act
- Congress: 119
- Bill type: HR
- Bill number: 7427
- Origin chamber: House
- Introduced date: 2026-02-09
- Update date: 2026-05-22T08:08:25Z
- Update date including text: 2026-05-22T08:08:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-09: Introduced in House
- 2026-02-09 - IntroReferral: Introduced in House
- 2026-02-09 - IntroReferral: Introduced in House
- 2026-02-09 - IntroReferral: Referred to the Committee on Homeland Security, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-02-09 - IntroReferral: Referred to the Committee on Homeland Security, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-02-10 - Committee: Referred to the Subcommittee on Counterterrorism and Intelligence.
- 2026-05-14 - Committee: Forwarded by Subcommittee to Full Committee by Voice Vote.
- 2026-05-14 - Committee: Subcommittee Consideration and Mark-up Session Held
- Latest action: 2026-02-09: Introduced in House

## Actions

- 2026-02-09 - IntroReferral: Introduced in House
- 2026-02-09 - IntroReferral: Introduced in House
- 2026-02-09 - IntroReferral: Referred to the Committee on Homeland Security, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-02-09 - IntroReferral: Referred to the Committee on Homeland Security, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-02-10 - Committee: Referred to the Subcommittee on Counterterrorism and Intelligence.
- 2026-05-14 - Committee: Forwarded by Subcommittee to Full Committee by Voice Vote.
- 2026-05-14 - Committee: Subcommittee Consideration and Mark-up Session Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-09",
    "latestAction": {
      "actionDate": "2026-02-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7427",
    "number": "7427",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "G000599",
        "district": "10",
        "firstName": "Daniel",
        "fullName": "Rep. Goldman, Daniel S. [D-NY-10]",
        "lastName": "Goldman",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "SAFE VISITS Act",
    "type": "HR",
    "updateDate": "2026-05-22T08:08:25Z",
    "updateDateIncludingText": "2026-05-22T08:08:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-14",
      "committees": {
        "item": {
          "name": "Counterterrorism, Law Enforcement, and Intelligence Subcommittee",
          "systemCode": "hshm05"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Forwarded by Subcommittee to Full Committee by Voice Vote.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-05-14",
      "committees": {
        "item": {
          "name": "Counterterrorism, Law Enforcement, and Intelligence Subcommittee",
          "systemCode": "hshm05"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Subcommittee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionDate": "2026-02-10",
      "committees": {
        "item": {
          "name": "Counterterrorism, Law Enforcement, and Intelligence Subcommittee",
          "systemCode": "hshm05"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Counterterrorism and Intelligence.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-09",
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
      "text": "Referred to the Committee on Homeland Security, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-09",
      "committees": {
        "item": {
          "name": "Homeland Security Committee",
          "systemCode": "hshm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Homeland Security, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-02-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-09",
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
          "date": "2026-02-09T17:00:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Homeland Security Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": [
              {
                "date": "2026-05-14T14:00:36Z",
                "name": "Reported by"
              },
              {
                "date": "2026-05-14T14:00:11Z",
                "name": "Markup by"
              },
              {
                "date": "2026-02-10T14:59:52Z",
                "name": "Referred to"
              }
            ]
          },
          "name": "Counterterrorism, Law Enforcement, and Intelligence Subcommittee",
          "systemCode": "hshm05"
        }
      },
      "systemCode": "hshm00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2026-02-09T17:00:10Z",
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
      "bioguideId": "T000193",
      "district": "2",
      "firstName": "Bennie",
      "fullName": "Rep. Thompson, Bennie G. [D-MS-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Thompson",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2026-02-09",
      "state": "MS"
    },
    {
      "bioguideId": "E000300",
      "district": "8",
      "firstName": "Gabe",
      "fullName": "Rep. Evans, Gabe [R-CO-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Evans",
      "party": "R",
      "sponsorshipDate": "2026-05-12",
      "state": "CO"
    },
    {
      "bioguideId": "P000621",
      "district": "9",
      "firstName": "Nellie",
      "fullName": "Rep. Pou, Nellie [D-NJ-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Pou",
      "party": "D",
      "sponsorshipDate": "2026-05-21",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7427ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7427\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 9, 2026 Mr. Goldman of New York (for himself and Mr. Thompson of Mississippi ) introduced the following bill; which was referred to the Committee on Homeland Security , and in addition to the Committee on the Judiciary , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend the Homeland Security Act of 2002 to provide threat analyses, including relating to terrorism threats, and guidance to State, local, Tribal, or territorial government officials or employees regarding visiting foreign nationals who seek access to State, local, Tribal, or territorial officials or employees, information, facilities, programs, or systems, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Securing Access from Foreign Entities Visiting Internal Sites in the States Act or the SAFE VISITS Act .\n#### 2. DHS threat analyses and guidance related to visiting foreign nationals to State, local, Tribal, and territorial governments\n##### (a) In general\nSubtitle A of title II of the Homeland Security Act of 2002 ( 6 U.S.C. 121 et seq. ) is amended by adding at the end the following new section:\n210H. Threat analyses and guidance related to visiting foreign nationals to State, local, Tribal, and territorial governments (a) In general Not later than 180 days after the date of the enactment of this section and annually thereafter, the Secretary shall submit to the Committee on Homeland Security of the House of Representatives and the Committee on Homeland Security and Governmental Affairs of the Senate a threat analysis, including relating to potential terrorism threats, reported to the Department by State, local, Tribal, or territorial government officials or employees, regarding any known visits by foreign nationals who\u2014 (1) seek to meet with such officials or employees, or (2) seek access to State, local, Tribal, or territorial government information, facilities, programs, or systems, and disseminate to State, local, Tribal, and territorial governments guidance based on such threat analysis. (b) Content of threat analysis and guidance The threat analysis, including relating to potential terrorism threats, and guidance under subsection (a) shall contain the following: (1) Descriptions of high-risk State, local, Tribal, and territorial government targets. (2) An analysis of trends related to visits by foreign nationals who seek access to State, local, Tribal, or territorial officials or employees, information, facilities, programs, or systems based on vetting request information submitted to, by, or through fusion centers (as such term is defined in section 210A) by State, local, Tribal, or territorial governments. (3) Descriptions of actions that may be taken to mitigate homeland security threats, including potential terrorism threats, and protect State, local, Tribal, and territorial officials or employees, information, facilities, programs, or systems. (c) Tailored outreach and vetting assistance (1) In general If the Secretary, based on the threat analysis under subsection (a), identifies a particular State, local, Tribal, or territorial government official or employee or information, facility, program, or system as a high-risk potential target of a visiting foreign national who seeks access to such official or employee, information, facility, program, or system, the Secretary shall carry out the following: (A) Conduct outreach to the identified State, local, Tribal, or territorial government and provide information, unclassified or classified at the lowest possible level, regarding such potential target. (B) Provide the identified State, local, Tribal, or Territorial government with assistance vetting such a foreign national. (C) Provide the identified State, local, Tribal, or Territorial government with additional guidance on specific actions that may be taken to mitigate homeland security threats, including potential terrorism threats, in connection with such visit. (2) Debriefings Not later than 30 days after an identified State, local, Tribal, or Territorial government hosts a visiting foreign national for which the Department provided assistance in accordance with paragraph (1), the Secretary shall request a debriefing from such host State, local, Tribal, or territorial government to maintain awareness of any attempt by visiting foreign nationals to obtain access to officials or employees, information, facilities, programs, or systems of such host State, local, Tribal, or Territorial government, and the techniques used by such visiting foreign nationals. (d) Report The Secretary shall annually submit to the Committee on Homeland Security of the House of Representatives and the Committee on Homeland Security and Governmental Affairs of the Senate a description of the outreach and vetting assistance by the Secretary under subsection (c) during the immediately preceding six month period. Each report under this subsection shall be submitted together with each corresponding report required under subsection (a), beginning with the second such report under such subsection. (e) Information defined In this section, the term information means data or materials collected, possessed, or prepared by a State, local, Tribal, or territorial government that is not intended for public disclosure or general use. .\n##### (b) Research and development\nThe Secretary of Homeland Security shall, to the extent practicable, coordinate with the Under Secretary for Science and Technology of the Department of Homeland Security to carry out research and development of a technology to enhance sharing of information to carry out section 210H of the Homeland Security Act of 2002, as added by subsection (a).\n##### (c) Clerical amendment\nThe table of contents in section (b) of the Homeland Security Act of 2002 is amended by inserting after the item relating to section 210G the following new item:\nSec. 210H. Threat analyses and guidance related to visiting foreign nationals to State, local, Tribal, and territorial governments. .",
      "versionDate": "2026-02-09",
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
        "updateDate": "2026-02-24T18:31:38Z"
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
      "date": "2026-02-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7427ih.xml"
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
      "title": "SAFE VISITS Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-23T13:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "SAFE VISITS Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-23T13:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Securing Access from Foreign Entities Visiting Internal Sites in the States Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-23T13:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Homeland Security Act of 2002 to provide threat analyses, including relating to terrorism threats, and guidance to State, local, Tribal, or territorial government officials or employees regarding visiting foreign nationals who seek access to State, local, Tribal, or territorial officials or employees, information, facilities, programs, or systems, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-23T13:18:25Z"
    }
  ]
}
```
