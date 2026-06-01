# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2351?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2351
- Title: Space Exploration Research Act
- Congress: 119
- Bill type: S
- Bill number: 2351
- Origin chamber: Senate
- Introduced date: 2025-07-17
- Update date: 2026-04-18T18:26:19Z
- Update date including text: 2026-04-18T18:26:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-17: Introduced in Senate
- 2025-07-17 - IntroReferral: Introduced in Senate
- 2025-07-17 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- 2025-07-30 - Committee: Committee on Commerce, Science, and Transportation. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2026-04-13 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with an amendment in the nature of a substitute. With written report No. 119-117.
- 2026-04-13 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with an amendment in the nature of a substitute. With written report No. 119-117.
- 2026-04-13 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 369.
- Latest action: 2025-07-17: Introduced in Senate

## Actions

- 2025-07-17 - IntroReferral: Introduced in Senate
- 2025-07-17 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- 2025-07-30 - Committee: Committee on Commerce, Science, and Transportation. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2026-04-13 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with an amendment in the nature of a substitute. With written report No. 119-117.
- 2026-04-13 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with an amendment in the nature of a substitute. With written report No. 119-117.
- 2026-04-13 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 369.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-17",
    "latestAction": {
      "actionDate": "2025-07-17",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2351",
    "number": "2351",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "C001098",
        "district": "",
        "firstName": "Ted",
        "fullName": "Sen. Cruz, Ted [R-TX]",
        "lastName": "Cruz",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Space Exploration Research Act",
    "type": "S",
    "updateDate": "2026-04-18T18:26:19Z",
    "updateDateIncludingText": "2026-04-18T18:26:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-13",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 369.",
      "type": "Calendars"
    },
    {
      "actionDate": "2026-04-13",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with an amendment in the nature of a substitute. With written report No. 119-117.",
      "type": "Committee"
    },
    {
      "actionCode": "14000",
      "actionDate": "2026-04-13",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with an amendment in the nature of a substitute. With written report No. 119-117.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-07-30",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Commerce, Science, and Transportation. Ordered to be reported with an amendment in the nature of a substitute favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-07-17",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-17",
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
            "date": "2026-04-13T19:42:44Z",
            "name": "Reported By"
          },
          {
            "date": "2025-07-30T15:10:42Z",
            "name": "Markup By"
          },
          {
            "date": "2025-07-17T20:40:42Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Commerce, Science, and Transportation Committee",
      "systemCode": "sscm00",
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
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "CA"
    },
    {
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2025-07-17",
      "state": "AL"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Luj\u00e1n, Ben Ray [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "NM"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "CA"
    },
    {
      "bioguideId": "W000437",
      "firstName": "Roger",
      "fullName": "Sen. Wicker, Roger F. [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Wicker",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-07-17",
      "state": "MS"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2351is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2351\nIN THE SENATE OF THE UNITED STATES\nJuly 17, 2025 Mr. Cruz (for himself, Mr. Padilla , Mrs. Britt , Mr. Luj\u00e1n , Mr. Schiff , and Mr. Wicker ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo supplement existing lease authorities available to the Administrator of the National Aeronautics and Space Administration to support research, education, and training, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Space Exploration Research Act .\n#### 2. National Aeronautics and Space Administration supplemental lease authority\n##### (a) Supplemental lease authority\n**(1) In general**\nThe Administrator of the National Aeronautics and Space Administration (referred to in this Act as the Administrator ) may, using existing lease authorities available to the Administrator and on such terms as the Administrator considers appropriate, lease, for a term not to exceed 99 years, real property under the jurisdiction of the Administrator to 1 or more entities described in subsection (c) for the purpose of the construction and operation on such real property of 1 or more facilities the purposes of which shall be\u2014\n**(A)**\nto conduct aeronautical and space research;\n**(B)**\nto educate and train individuals for careers in the space industry;\n**(C)**\nto carry out the transfer of aeronautical and space technology between the United States public and domestic private sectors;\n**(D)**\nto conduct scientific, engineering, medical, or academic activities; and\n**(E)**\nto conduct any other space-related activity.\n**(2) Renewal**\nThe Administrator may renew a lease under this subsection for 1 or more additional periods.\n##### (b) Administrative, maintenance, and instructional support\nSubject to the availability of appropriations, the Administrator may\u2014\n**(1)**\nenter into 1 or more agreements, on such terms as the Administrator considers appropriate, with 1 or more entities described in subsection (c) to lease back real property described in subsection (a), including such real property that has been\u2014\n**(A)**\nleased to a private entity under other lease authority available to the Administrator; and\n**(B)**\nsubleased to an entity described in subsection (c);\n**(2)**\nenter into 1 or more contracts, grant agreements, cooperative agreements, or other authorized transactions with an entity described in subsection (c) with respect to such property; and\n**(3)**\nprovide administrative, maintenance, instructional, and other appropriate support, with or without reimbursement, to the 1 or more facilities described in subsection (a).\n##### (c) Entities described\nAn entity described in this subsection is\u2014\n**(1)**\nthe State in which the real property described in subsection (a) is located;\n**(2)**\na subdivision, agent, or agency of such a State;\n**(3)**\na corporation or foundation organized exclusively for education or scientific purposes that is exempt from taxation under section 501(c)(3) of the Internal Revenue Code of 1986 ( 26 U.S.C. 501(c)(3) ); and\n**(4)**\nan institution of higher education (as defined in section 102 of the Higher Education Act of 1965 ( 20 U.S.C. 1001 )).\n##### (d) Delegation\nThe Administrator may delegate the authorities under subsections (a) and (b) to subordinate officers and employees of the National Aeronautics and Space Administration, as the Administrator considers appropriate.\n##### (e) Effect of other law\nThe authority provided by this section shall apply\u2014\n**(1)**\nregardless of the existing authority used by the Administrator to lease the real property described in subsection (a); and\n**(2)**\nnotwithstanding any provision of\u2014\n**(A)**\nsection 1302 of title 40, United States Code;\n**(B)**\nsection 20145 of title 51, United States Code; or\n**(C)**\nsection 306121 of title 54, United States Code.",
      "versionDate": "2025-07-17",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s2351rs.xml",
      "text": "II\nCalendar No. 369\n119th CONGRESS\n2d Session\nS. 2351\n[Report No. 119\u2013117]\nIN THE SENATE OF THE UNITED STATES\nJuly 17, 2025 Mr. Cruz (for himself, Mr. Padilla , Mrs. Britt , Mr. Luj\u00e1n , Mr. Schiff , and Mr. Wicker ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nApril 13, 2026 Reported by Mr. Cruz , with an amendment Strike out all after the enacting clause and insert the part printed in italic\nA BILL\nTo supplement existing lease authorities available to the Administrator of the National Aeronautics and Space Administration to support research, education, and training, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Space Exploration Research Act .\n#### 2. National Aeronautics and Space Administration supplemental lease authority\n##### (a) Supplemental lease authority\n**(1) In general**\nThe Administrator of the National Aeronautics and Space Administration (referred to in this Act as the Administrator ) may, using existing lease authorities available to the Administrator and on such terms as the Administrator considers appropriate, lease, for a term not to exceed 99 years, real property under the jurisdiction of the Administrator to 1 or more entities described in subsection (c) for the purpose of the construction and operation on such real property of 1 or more facilities the purposes of which shall be\u2014\n**(A)**\nto conduct aeronautical and space research;\n**(B)**\nto educate and train individuals for careers in the space industry;\n**(C)**\nto carry out the transfer of aeronautical and space technology between the United States public and domestic private sectors;\n**(D)**\nto conduct scientific, engineering, medical, or academic activities; and\n**(E)**\nto conduct any other space-related activity.\n**(2) Renewal**\nThe Administrator may renew a lease under this subsection for 1 or more additional periods.\n##### (b) Administrative, maintenance, and instructional support\nSubject to the availability of appropriations, the Administrator may\u2014\n**(1)**\nenter into 1 or more agreements, on such terms as the Administrator considers appropriate, with 1 or more entities described in subsection (c) to lease back real property described in subsection (a), including such real property that has been\u2014\n**(A)**\nleased to a private entity under other lease authority available to the Administrator; and\n**(B)**\nsubleased to an entity described in subsection (c);\n**(2)**\nenter into 1 or more contracts, grant agreements, cooperative agreements, or other authorized transactions with an entity described in subsection (c) with respect to such property; and\n**(3)**\nprovide administrative, maintenance, instructional, and other appropriate support, with or without reimbursement, to the 1 or more facilities described in subsection (a).\n##### (c) Entities described\nAn entity described in this subsection is\u2014\n**(1)**\nthe State in which the real property described in subsection (a) is located;\n**(2)**\na subdivision, agent, or agency of such a State;\n**(3)**\na corporation or foundation organized exclusively for education or scientific purposes that is exempt from taxation under section 501(c)(3) of the Internal Revenue Code of 1986 ( 26 U.S.C. 501(c)(3) ); and\n**(4)**\nan institution of higher education (as defined in section 102 of the Higher Education Act of 1965 ( 20 U.S.C. 1001 )).\n##### (d) Delegation\nThe Administrator may delegate the authorities under subsections (a) and (b) to subordinate officers and employees of the National Aeronautics and Space Administration, as the Administrator considers appropriate.\n##### (e) Effect of other law\nThe authority provided by this section shall apply\u2014\n**(1)**\nregardless of the existing authority used by the Administrator to lease the real property described in subsection (a); and\n**(2)**\nnotwithstanding any provision of\u2014\n**(A)**\nsection 1302 of title 40, United States Code;\n**(B)**\nsection 20145 of title 51, United States Code; or\n**(C)**\nsection 306121 of title 54, United States Code.",
      "versionDate": "2026-04-13",
      "versionType": "Reported in Senate"
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
            "name": "Employment and training programs",
            "updateDate": "2025-09-09T17:38:35Z"
          },
          {
            "name": "Land transfers",
            "updateDate": "2025-09-09T17:36:28Z"
          },
          {
            "name": "Public-private cooperation",
            "updateDate": "2025-09-09T17:42:47Z"
          },
          {
            "name": "Research and development",
            "updateDate": "2025-09-09T17:38:10Z"
          },
          {
            "name": "Space flight and exploration",
            "updateDate": "2025-09-09T17:37:54Z"
          }
        ]
      },
      "policyArea": {
        "name": "Science, Technology, Communications",
        "updateDate": "2026-04-17T18:26:15Z"
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
      "date": "2025-07-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2351is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2026-04-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s2351rs.xml"
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
      "title": "Space Exploration Research Act",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2026-04-15T06:08:22Z"
    },
    {
      "title": "Space Exploration Research Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-14T11:03:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Space Exploration Research Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-25T13:53:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to supplement existing lease authorities available to the Administrator of the National Aeronautics and Space Administration to support research, education, and training, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-25T13:48:35Z"
    }
  ]
}
```
