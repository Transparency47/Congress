# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7260?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7260
- Title: National Cemetery Administration Annual Report Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 7260
- Origin chamber: House
- Introduced date: 2026-01-27
- Update date: 2026-05-28T19:35:24Z
- Update date including text: 2026-05-28T19:35:24Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-01-27: Introduced in House
- 2026-01-27 - IntroReferral: Introduced in House
- 2026-01-27 - IntroReferral: Introduced in House
- 2026-01-27 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2026-01-30 - Committee: Referred to the Subcommittee on Disability Assistance and Memorial Affairs.
- 2026-02-03 - Committee: Subcommittee Hearings Held
- 2026-03-26 - Committee: Forwarded by Subcommittee to Full Committee (Amended) by Voice Vote.
- 2026-03-26 - Committee: Subcommittee Consideration and Mark-up Session Held
- 2026-05-14 - Committee: Committee Consideration and Mark-up Session Held
- 2026-05-14 - Committee: Ordered to be Reported (Amended) by Voice Vote.
- Latest action: 2026-01-27: Introduced in House

## Actions

- 2026-01-27 - IntroReferral: Introduced in House
- 2026-01-27 - IntroReferral: Introduced in House
- 2026-01-27 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2026-01-30 - Committee: Referred to the Subcommittee on Disability Assistance and Memorial Affairs.
- 2026-02-03 - Committee: Subcommittee Hearings Held
- 2026-03-26 - Committee: Forwarded by Subcommittee to Full Committee (Amended) by Voice Vote.
- 2026-03-26 - Committee: Subcommittee Consideration and Mark-up Session Held
- 2026-05-14 - Committee: Committee Consideration and Mark-up Session Held
- 2026-05-14 - Committee: Ordered to be Reported (Amended) by Voice Vote.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-27",
    "latestAction": {
      "actionDate": "2026-01-27",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7260",
    "number": "7260",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "M001230",
        "district": "7",
        "firstName": "Ryan",
        "fullName": "Rep. Mackenzie, Ryan [R-PA-7]",
        "lastName": "Mackenzie",
        "party": "R",
        "state": "PA"
      }
    ],
    "title": "National Cemetery Administration Annual Report Act of 2026",
    "type": "HR",
    "updateDate": "2026-05-28T19:35:24Z",
    "updateDateIncludingText": "2026-05-28T19:35:24Z"
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
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported (Amended) by Voice Vote.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-05-14",
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
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionDate": "2026-03-26",
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
      "text": "Forwarded by Subcommittee to Full Committee (Amended) by Voice Vote.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-03-26",
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
      "text": "Subcommittee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionDate": "2026-02-03",
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
      "text": "Subcommittee Hearings Held",
      "type": "Committee"
    },
    {
      "actionDate": "2026-01-30",
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
      "actionDate": "2026-01-27",
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
      "actionDate": "2026-01-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-27",
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
            "date": "2026-05-14T21:12:27Z",
            "name": "Markup By"
          },
          {
            "date": "2026-01-27T17:33:25Z",
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
                "date": "2026-03-26T15:17:00Z",
                "name": "Reported by"
              },
              {
                "date": "2026-03-26T14:28:31Z",
                "name": "Markup by"
              },
              {
                "date": "2026-02-03T15:00:14Z",
                "name": "Hearings By (subcommittee)"
              },
              {
                "date": "2026-01-30T16:40:38Z",
                "name": "Referred to"
              }
            ]
          },
          "name": "Disability Assistance and Memorial Affairs Subcommittee",
          "systemCode": "hsvr09"
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
      "bioguideId": "M001220",
      "district": "3",
      "firstName": "Morgan",
      "fullName": "Rep. McGarvey, Morgan [D-KY-3]",
      "isOriginalCosponsor": "True",
      "lastName": "McGarvey",
      "party": "D",
      "sponsorshipDate": "2026-01-27",
      "state": "KY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7260ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7260\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 27, 2026 Mr. Mackenzie (for himself and Mr. McGarvey ) introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to require the Secretary of Veterans Affairs to submit to Congress an annual report on the National Cemetery Administration, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the National Cemetery Administration Annual Report Act of 2026 .\n#### 2. Department of Veterans Affairs annual report on the National Cemetery Administration\n##### (a) In general\nChapter 24 of title 38, United States Code, is amended by adding at the end the following new section:\n2415. National Cemetery Administration annual report (a) In general Not later than one year after the date of the enactment of the National Cemetery Administration Annual Report Act of 2026, and on an annual basis thereafter, the Secretary shall submit to the Committees on Veterans\u2019 Affairs of the House of Representatives and the Senate a report on the activities of the National Cemetery Administration. (b) Elements Each report required under subsection (a) shall include, with respect to the period covered by the report\u2014 (1) the total number of interments of remains carried out by the Secretary, disaggregated by\u2014 (A) each open national cemetery under the control of the National Cemetery Administration in which remains were interred; (B) each category of eligible person described in paragraphs (1) through (10) of section 2402(a) of this title; and (C) interments of\u2014 (i) casketed remains; and (ii) cremated remains; (2) an assessment of the level of customer satisfaction achieved by the Administration; (3) a map of each\u2014 (A) national cemetery under the control of the Administration; and (B) veterans\u2019 cemetery owned by a State or county or on trust land owned by, or held in trust for, a tribal organization in receipt of a grant under section 2408 of this title; (4) a description of each open national cemetery under the control of the Administration that includes information with respect to burial options available to persons eligible for interment in such a national cemetery; (5) the number of veterans interred in a veterans\u2019 cemetery owned by a State or county or on trust land owned by, or held in trust for, a tribal organization in receipt of a grant under section 2408 of this title; (6) the number of Presidential memorial certificates, headstones, burial markers, and medallions furnished by the Administration, disaggregated by\u2014 (A) each category of eligible person described in paragraphs (1) through (10) of section 2402(a) of this title; and (B) cemetery location; (7) a summary of each major construction project and minor construction project carried out on national cemetery under the control of the Administration that was completed during such period; (8) a description of each planned major construction project and minor construction project on a national cemetery under the control of the Administration that is intended to be carried out during the first fiscal year beginning after such period; (9) the total number of interments of unclaimed remains of veterans carried out by the Secretary, disaggregated by each open national cemetery under the control of the Administration; (10) a description of each grant made during such period under\u2014 (A) section 2408 of this title; and (B) section 1 of Public Law 116\u2013107 ; (11) for each grant described in paragraph (10), a summary of\u2014 (A) the recipient of such grant; (B) the amount of such grant; and (C) the purposes for which such grant is or will be used; and (12) any other matters that the Secretary determines appropriate. (c) Form The Secretary shall make each report submitted pursuant to subsection (a) available, in digital form, on a public internet website of the Department. .\n##### (b) Clerical amendment\nThe table of sections at the beginning of such chapter is amended by inserting after the item relating to section 2414 the following new item:\n2415. National Cemetery Administration annual report .",
      "versionDate": "2026-01-27",
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
        "updateDate": "2026-02-09T19:20:03Z"
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
      "date": "2026-01-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7260ih.xml"
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
      "title": "National Cemetery Administration Annual Report Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-06T06:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "National Cemetery Administration Annual Report Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-06T06:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 38, United States Code, to require the Secretary of Veterans Affairs to submit to Congress an annual report on the National Cemetery Administration, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-06T06:18:37Z"
    }
  ]
}
```
