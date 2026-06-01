# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8684?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8684
- Title: Transparency in Billing Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 8684
- Origin chamber: House
- Introduced date: 2026-05-07
- Update date: 2026-05-22T08:07:48Z
- Update date including text: 2026-05-22T08:07:48Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-05-07: Introduced in House
- 2026-05-07 - IntroReferral: Introduced in House
- 2026-05-07 - IntroReferral: Introduced in House
- 2026-05-07 - IntroReferral: Referred to the House Committee on Education and Workforce.
- 2026-05-21 - Committee: Committee Consideration and Mark-up Session Held
- 2026-05-21 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 34 - 0.
- Latest action: 2026-05-07: Introduced in House

## Actions

- 2026-05-07 - IntroReferral: Introduced in House
- 2026-05-07 - IntroReferral: Introduced in House
- 2026-05-07 - IntroReferral: Referred to the House Committee on Education and Workforce.
- 2026-05-21 - Committee: Committee Consideration and Mark-up Session Held
- 2026-05-21 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 34 - 0.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-07",
    "latestAction": {
      "actionDate": "2026-05-07",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8684",
    "number": "8684",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "F000450",
        "district": "5",
        "firstName": "Virginia",
        "fullName": "Rep. Foxx, Virginia [R-NC-5]",
        "lastName": "Foxx",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "Transparency in Billing Act of 2026",
    "type": "HR",
    "updateDate": "2026-05-22T08:07:48Z",
    "updateDateIncludingText": "2026-05-22T08:07:48Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-21",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 34 - 0.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-05-21",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
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
      "actionCode": "H11100",
      "actionDate": "2026-05-07",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Education and Workforce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-05-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-05-07",
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
            "date": "2026-05-21T20:09:31Z",
            "name": "Markup By"
          },
          {
            "date": "2026-05-07T13:01:40Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
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
      "bioguideId": "S000185",
      "district": "3",
      "firstName": "Robert",
      "fullName": "Rep. Scott, Robert C. \"Bobby\" [D-VA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "middleName": "C. \"Bobby\"",
      "party": "D",
      "sponsorshipDate": "2026-05-07",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8684ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8684\nIN THE HOUSE OF REPRESENTATIVES\nMay 7, 2026 Ms. Foxx (for herself and Mr. Scott of Virginia ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo amend the Employee Retirement Income Security Act of 1974 to require group health plans and health insurance issuers offering group health insurance coverage to only pay claims submitted by hospitals that have in place policies and procedures to ensure accurate billing practices, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Transparency in Billing Act of 2026 .\n#### 2. Honest billing requirements\n##### (a) In general\nSubpart B of part 7 of subtitle B of title I of the Employee Retirement Income Security Act of 1974 ( 29 U.S.C. 1185 et seq. ) is amended by adding at the end the following new section:\n727. Honest billing requirements A group health plan or health insurance issuer offering group health insurance coverage may not pay a claim for items and services furnished to an individual at an off-campus outpatient department of a provider (as defined in section 901(c)) submitted by a hospital (as defined in section 1861(e) of the Social Security Act) unless such claim submitted by such hospital includes the separate unique health identifier for the department where items and services were furnished, in accordance with section 901. .\n##### (b) Clerical amendment\nThe table of contents of the Employee Retirement Income Security Act of 1974 ( 29 U.S.C. 1001 note) is amended by adding after the item relating to section 726 the following:\nSec. 727. Honest billing requirements. .\n##### (c) Effective date\nThe amendments made by this section shall take effect with respect to plan years beginning on or after January 1, 2027.\n#### 3. Regulation of honest billing\n##### (a) In general\nSubtitle B of title I of the Employee Retirement Income Security Act of 1974 ( 29 U.S.C. 1021 et seq. ) is amended by adding at the end the following new part:\n9 Billing Requirements with Respect to Group Health Plans and Coverage 901. Honest billing requirements (a) In general A hospital may not, with respect to items and services furnished to an individual at an off-campus outpatient department of a provider, submit a claim for such items and services to a group health plan or health insurance issuer, and may not hold such individual liable for such items and services, unless\u2014 (1) such hospital obtains a separate unique health identifier established for such department pursuant to section 1173(b) of the Social Security Act; and (2) the claim for such items and services includes such separate unique health identifier for such department where such items and services were furnished. (b) Process for reporting suspected violations Not later than one year after the date of enactment of this section, the Secretary shall establish a process under which a suspected violation of this section may be reported to such Secretary. (c) Off-Campus outpatient department of a provider defined For purposes of this paragraph, the term off-campus outpatient department of a provider means a department of a provider (as defined in section 413.65 of title 42, Code of Federal Regulations, or any successor regulation) that is not located\u2014 (1) on the campus (as defined in such section) of such provider; or (2) within the distance (described in such definition of campus) from a remote location of a hospital facility (as defined in such section). .\n##### (b) Clerical amendment\nThe table of contents of the Employee Retirement Income Security Act of 1974 ( 29 U.S.C. 1001 note) is amended by inserting after the item relating to section 804 the following new item:\nPart 9\u2014Billing Requirements with Respect to Group Health Plans and Coverage Sec. 901. Honest billing requirements. .\n#### 4. Enforcement\nSection 502 of the Employee Retirement Income Security Act of 1974 ( 29 U.S.C. 1132 ) is amended\u2014\n**(1)**\nin subsection (a)(6), by striking or (9) and inserting (9), or (13) ; and\n**(2)**\nin subsection (c), by adding at the end the following new paragraph:\n(13) The Secretary may assess a civil monetary penalty against a hospital for a violation under section 901 in an amount\u2014 (A) in the case of a hospital with not more than 30 beds (as determined under section 180.90(c)(2)(ii)(D) of title 45, Code of Federal Regulations, as in effect on the date of the enactment of this paragraph), not to exceed $300 per day that the violation is ongoing, as determined by the Secretary; and (B) in the case of a hospital with more than 30 beds (as so determined), not to exceed $5,500 per each such day. .\n#### 5. Implementation\nThe Secretary of Labor shall implement the amendments made by this Act by rulemaking.",
      "versionDate": "2026-05-07",
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
        "name": "Health",
        "updateDate": "2026-05-21T19:01:04Z"
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
      "date": "2026-05-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8684ih.xml"
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
      "title": "Transparency in Billing Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-12T05:53:25Z"
    },
    {
      "title": "Transparency in Billing Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-12T05:53:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Employee Retirement Income Security Act of 1974 to require group health plans and health insurance issuers offering group health insurance coverage to only pay claims submitted by hospitals that have in place policies and procedures to ensure accurate billing practices, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-12T05:48:33Z"
    }
  ]
}
```
