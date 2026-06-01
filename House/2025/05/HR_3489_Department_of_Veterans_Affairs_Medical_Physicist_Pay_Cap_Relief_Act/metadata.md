# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3489?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3489
- Title: Department of Veterans Affairs Medical Physicist Pay Cap Relief Act
- Congress: 119
- Bill type: HR
- Bill number: 3489
- Origin chamber: House
- Introduced date: 2025-05-19
- Update date: 2026-02-26T16:33:46Z
- Update date including text: 2026-02-26T16:33:46Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-19: Introduced in House
- 2025-05-19 - IntroReferral: Introduced in House
- 2025-05-19 - IntroReferral: Introduced in House
- 2025-05-19 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-06-06 - Committee: Referred to the Subcommittee on Health.
- Latest action: 2025-05-19: Introduced in House

## Actions

- 2025-05-19 - IntroReferral: Introduced in House
- 2025-05-19 - IntroReferral: Introduced in House
- 2025-05-19 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-06-06 - Committee: Referred to the Subcommittee on Health.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-19",
    "latestAction": {
      "actionDate": "2025-05-19",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3489",
    "number": "3489",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "C001127",
        "district": "20",
        "firstName": "Sheila",
        "fullName": "Rep. Cherfilus-McCormick, Sheila [D-FL-20]",
        "lastName": "Cherfilus-McCormick",
        "party": "D",
        "state": "FL"
      }
    ],
    "title": "Department of Veterans Affairs Medical Physicist Pay Cap Relief Act",
    "type": "HR",
    "updateDate": "2026-02-26T16:33:46Z",
    "updateDateIncludingText": "2026-02-26T16:33:46Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-06",
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
      "actionDate": "2025-05-19",
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
      "actionDate": "2025-05-19",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-19",
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
          "date": "2025-05-19T16:00:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-06-06T15:44:44Z",
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
      "bioguideId": "C001133",
      "district": "6",
      "firstName": "Juan",
      "fullName": "Rep. Ciscomani, Juan [R-AZ-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Ciscomani",
      "party": "R",
      "sponsorshipDate": "2025-05-19",
      "state": "AZ"
    },
    {
      "bioguideId": "D000629",
      "district": "3",
      "firstName": "Sharice",
      "fullName": "Rep. Davids, Sharice [D-KS-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Davids",
      "party": "D",
      "sponsorshipDate": "2025-07-21",
      "state": "KS"
    },
    {
      "bioguideId": "M000317",
      "district": "11",
      "firstName": "Nicole",
      "fullName": "Rep. Malliotakis, Nicole [R-NY-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Malliotakis",
      "party": "R",
      "sponsorshipDate": "2025-07-29",
      "state": "NY"
    },
    {
      "bioguideId": "D000096",
      "district": "7",
      "firstName": "Danny",
      "fullName": "Rep. Davis, Danny K. [D-IL-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Davis",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "IL"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "IN"
    },
    {
      "bioguideId": "N000193",
      "district": "3",
      "firstName": "Zachary",
      "fullName": "Rep. Nunn, Zachary [R-IA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Nunn",
      "party": "R",
      "sponsorshipDate": "2025-09-26",
      "state": "IA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3489ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3489\nIN THE HOUSE OF REPRESENTATIVES\nMay 19, 2025 Mrs. Cherfilus-McCormick (for herself and Mr. Ciscomani ) introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to codify the requirements for appointment, qualifications, and pay for therapeutic and diagnostic medical physicists of the Department of Veterans Affairs, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Department of Veterans Affairs Medical Physicist Pay Cap Relief Act .\n#### 2. Treatment of therapeutic medical physicists of the Department of Veterans Affairs\n##### (a) Appointment\nSection 7401(1) of title 38, United States Code, is amended by inserting therapeutic medical physicists, diagnostic medical physicists, after physician assistants, .\n##### (b) Qualifications\nSection 7402(b) of such title is amended\u2014\n**(1)**\nby redesignating paragraph (14) as paragraph (16); and\n**(2)**\nby inserting after paragraph (13) the following new paragraphs:\n(14) Therapeutic medical physicist To be eligible to be appointed to a therapeutic medical physicist position, a person must\u2014 (A) have completed a post-graduate clinical training program in therapeutic medical physics satisfactory to the Secretary; and (B) be board certified in the field of therapeutic medical physics by a certifying body approved by the Secretary. (15) Diagnostic medical physicist To be eligible to be appointed to a diagnostic medical physicist position, a person must\u2014 (A) have completed a post-graduate clinical training program in diagnostic medical physics satisfactory to the Secretary; and (B) be board certified in the field of diagnostic medical physics by a certifying body approved by the Secretary. .\n##### (c) Grade\nSection 7404 of such title is amended\u2014\n**(1)**\nby inserting therapeutic medical physicist, diagnostic medical physicist, after podiatrist (dpm), ; and\n**(2)**\nby inserting after Podiatrist grade. the following:\nTherapeutic medical physicist grade. Diagnostic medical physicist grade. .\n##### (d) Personnel administration\nSection 7421(b) of such title is amended\u2014\n**(1)**\nby redesignating paragraph (9) as paragraph (11); and\n**(2)**\nby inserting, after paragraph (8), the following new paragraphs:\n(9) Therapeutic medical physicists. (10) Diagnostic medical physicists. .\n##### (e) Pay\n**(1) In general**\nSection 7431 of such title is amended\u2014\n**(A)**\nby inserting , Therapeutic Medical Physicist, Diagnostic Medical Physicist before , and Dentist Base each place it appears;\n**(B)**\nby inserting therapeutic medical physicist, diagnostic medical physicist, after podiatrist, each place it appears;\n**(C)**\nby inserting therapeutic medical physicists, diagnostic medical physicists, after podiatrists, each place it appears; and\n**(D)**\nin subsection (e)(1)(A), by inserting , therapeutic medical physicists, diagnostic medical physicists, after podiatrists .\n**(2) Administrative matters**\nSection 7433 of such title is amended by inserting therapeutic medical physicists, diagnostic medical physicists, after podiatrists, each place it appears.\n**(3) Conforming amendment**\nThe heading of subchapter III of chapter 74 of such title is amended by inserting Therapeutic Medical Physicists, Diagnostic Medical Physicists after Podiatrists, .\n**(4) Clerical amendment**\nThe table of sections at the beginning of chapter 74 of such title is amended by striking the item relating to subchapter III and inserting the following new item:\nSubchapter III\u2014Pay for Physicians, Podiatrists, Therapeutic Medical Physicists, Diagnostic Medical Physicists, and Dentists .\n##### (f) Report\nNot later than one year after the date of enactment of this Act, the Secretary of Veterans Affairs shall submit to the Committees on Veterans\u2019 Affairs of the Senate and House of Representatives a report on the amendments made by this section. Such report shall include the following:\n**(1)**\nThe effects of an increase in pay for therapeutic medical physicists and diagnostic medical physicists employed on a full-time basis within the Department of Veterans Affairs.\n**(2)**\nThe effects on therapeutic medical physicists and diagnostic medical physicists who provide care pursuant to an agreement with the Secretary.\n**(3)**\nAny change to costs to the Department.",
      "versionDate": "2025-05-19",
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
        "actionDate": "2026-02-04",
        "text": "Read twice and referred to the Committee on Veterans' Affairs."
      },
      "number": "3771",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Department of Veterans Affairs Therapeutic Medical Physicist Pay Cap Relief Act of 2026",
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
        "updateDate": "2025-06-05T18:24:07Z"
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
      "date": "2025-05-19",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3489ih.xml"
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
      "title": "Department of Veterans Affairs Medical Physicist Pay Cap Relief Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-30T12:52:35Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Department of Veterans Affairs Medical Physicist Pay Cap Relief Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-27T04:38:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 38, United States Code, to codify the requirements for appointment, qualifications, and pay for therapeutic and diagnostic medical physicists of the Department of Veterans Affairs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-27T04:33:23Z"
    }
  ]
}
```
