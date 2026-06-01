# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7787?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7787
- Title: To amend title VII of the Public Health Service Act to strengthen the mental health workforce, and for other purposes.
- Congress: 119
- Bill type: HR
- Bill number: 7787
- Origin chamber: House
- Introduced date: 2026-03-04
- Update date: 2026-03-27T16:48:29Z
- Update date including text: 2026-03-27T16:48:29Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-04: Introduced in House
- 2026-03-04 - IntroReferral: Introduced in House
- 2026-03-04 - IntroReferral: Introduced in House
- 2026-03-04 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2026-03-04: Introduced in House

## Actions

- 2026-03-04 - IntroReferral: Introduced in House
- 2026-03-04 - IntroReferral: Introduced in House
- 2026-03-04 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-04",
    "latestAction": {
      "actionDate": "2026-03-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7787",
    "number": "7787",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "C001125",
        "district": "2",
        "firstName": "Troy",
        "fullName": "Rep. Carter, Troy A. [D-LA-2]",
        "lastName": "Carter",
        "party": "D",
        "state": "LA"
      }
    ],
    "title": "To amend title VII of the Public Health Service Act to strengthen the mental health workforce, and for other purposes.",
    "type": "HR",
    "updateDate": "2026-03-27T16:48:29Z",
    "updateDateIncludingText": "2026-03-27T16:48:29Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-04",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-03-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-04",
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
          "date": "2026-03-04T15:02:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "T000463",
      "district": "10",
      "firstName": "Michael",
      "fullName": "Rep. Turner, Michael R. [R-OH-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Turner",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2026-03-04",
      "state": "OH"
    },
    {
      "bioguideId": "M001218",
      "district": "7",
      "firstName": "Richard",
      "fullName": "Rep. McCormick, Richard [R-GA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "McCormick",
      "party": "R",
      "sponsorshipDate": "2026-03-04",
      "state": "GA"
    },
    {
      "bioguideId": "C001067",
      "district": "9",
      "firstName": "Yvette",
      "fullName": "Rep. Clarke, Yvette D. [D-NY-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Clarke",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2026-03-04",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7787ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7787\nIN THE HOUSE OF REPRESENTATIVES\nMarch 4, 2026 Mr. Carter of Louisiana (for himself, Mr. Turner of Ohio , Mr. McCormick , and Ms. Clarke of New York ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend title VII of the Public Health Service Act to strengthen the mental health workforce, and for other purposes.\n#### 1. Strengthening the mental health workforce\n##### (a) In general\nPart B of title VII of the Public Health Service Act ( 42 U.S.C. 293 et seq. ) is amended by adding at the end the following:\n742. Strengthening the mental health workforce (a) In general The Secretary shall establish and carry out a mental health provider loan deferment and forgiveness program under which an eligible individual agrees to be employed full-time as a qualified mental health provider for a period of at least 5 years (beginning on the date on which the individual is first licensed to practice as a qualified mental health provider)\u2014 (1) as a solo provider within an area that has been designated as having a shortage of mental health professionals under section 332; or (2) at an institution that serves patients who are located in an area that has been designated as having a shortage of mental health professionals under section 332. (b) Program administration Through the program established under this section, the Secretary shall enter into contracts with eligible individuals under which\u2014 (1) such eligible individuals will agree to provide mental and behavioral health care services as described in subsection (a); (2) the Secretary agrees that periodic installments of the principal of an eligible loan need not be paid, but interest shall accrue and be paid, during any period during which the borrower is employed as described in subsection (a); and (3) the Secretary, through the holder of the loan, will assume the obligation to repay the lesser of 100 percent or $200,000 of the total amount of principal and interest of an eligible loan, that are outstanding as of the day immediately preceding the first day of the first year of service (as described in subsection (a)), for an eligible individual, who\u2014 (A) has been employed as described in subsection (a) for 5 consecutive years; and (B) is not in default on a loan for which the individual seeks forgiveness. (c) Definitions In this section: (1) The term eligible individual means an individual who\u2014 (A) (i) has been accepted for enrollment, or is enrolled, as a student in a minority-serving institution eligible to receive funding under section 371 of the Higher Education Act of 1965 in a course of study or program leading to a mental or behavioral health professions degree or certificate; or (ii) is completing training hours under clinical supervision for purposes of obtaining such a degree or certificate; and (B) has accepted employment as a qualified mental health provider as described in subsection (a), to commence upon graduation. (2) The term eligible loan means\u2014 (A) any loan for education or training for mental and behavioral health care employment, including education or training relating to substance use prevention and treatment; (B) any Federal Direct Stafford Loan, Federal Direct PLUS Loan, Federal Direct Unsubsidized Stafford Loan, or Federal Direct Consolidation Loan (as such terms are used in section 455 of the Higher Education Act of 1965); (C) any Federal Perkins Loan under part E of title I of the Higher Education Act of 1965; and (D) any other Federal loan as determined appropriate by the Secretary. (3) The term qualified mental health provider means a provider of mental and behavioral health care services, including substance use prevention and treatment services, that is one of the following: (A) A physician (as defined in section 1861(r) of the Social Security Act) whose specialty is psychiatry. (B) A health service psychologist. (C) A psychiatric nurse specialist (as defined in appendix C to part 5 of subchapter A of chapter 1 of title 42, Code of Federal Regulations (or successor regulations)). (D) A marriage and family therapist (as defined in section 1861(lll)(2) of the Social Security Act). (E) A physician assistant, nurse practitioner, or clinical nurse specialist (as defined in section 1861(aa)(5) of the Social Security Act) whose specialty is mental health or psychiatry. (F) A clinical social worker (as defined in section 1861(hh)(1) of the Social Security Act). (G) A clinical psychologist (as defined by the Secretary for purposes of section 1861(ii) of the Social Security Act). (H) A mental health counselor (as defined in section 1861(lll)(4) of the Social Security Act). .",
      "versionDate": "2026-03-04",
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
        "updateDate": "2026-03-27T16:48:28Z"
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
      "date": "2026-03-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7787ih.xml"
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
      "title": "To amend title VII of the Public Health Service Act to strengthen the mental health workforce, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-22T05:33:24Z"
    },
    {
      "title": "To amend title VII of the Public Health Service Act to strengthen the mental health workforce, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-05T09:06:47Z"
    }
  ]
}
```
